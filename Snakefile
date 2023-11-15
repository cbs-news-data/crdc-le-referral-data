# Define the input files
INPUT_FILES_1314 = [
    "clean/input/1314-crdc-sch-characteristics.xlsx.csv",
    "clean/input/1314-crdc-sch-enrollment.xlsx.csv",
    "clean/input/1314-crdc-sch-referrals-arrests.xlsx.csv"
]

INPUT_FILES_1516 = ["clean/input/CRDC-2015-16-School-Data.csv.gz"]

INPUT_FILES_1718 = [
    "clean/input/1718-crdc-sch-characteristics.csv",
    "clean/input/1718-crdc-sch-enrollment.csv",
    "clean/input/1718-crdc-sch-referrals-arrests.csv"
]

OUTPUT_NOTEBOOKS = [
    "notebooks/1718_referrals_arrests/output/crdc_le_referrals_arrests_g5.ipynb",
    "notebooks/1718_referrals_arrests/output/crdc_le_referrals_arrests_g8.ipynb",
]

GRADES = [5, 8]

# Define the output file
OUTPUT_FILE_CLEANED = "clean/output/crdc-referrals-arrests-cleaned.csv"

# runs the data cleaning with the available input files
rule clean:
    input:
        src="clean/src/clean_crdc_data.py",
        const="clean/src/constants.py",
        f1=INPUT_FILES_1314,
        f2=INPUT_FILES_1516,
        f3=INPUT_FILES_1718
    output:
        cleaned=OUTPUT_FILE_CLEANED
    shell:
        "python {input.src} -f {input.f1} -f {input.f2} -f {input.f3} -o {output.cleaned}"

# Runs the notebooks with various parameters to generate the final output using papermill
rule notebooks:
    input:
        cleaned=OUTPUT_FILE_CLEANED,
        nb="notebooks/1718_referrals_arrests/crdc_le_referrals_arrests.ipynb",
    output:
        nb_g5="notebooks/1718_referrals_arrests/output/crdc_le_referrals_arrests_g5.ipynb",
        nb_g8="notebooks/1718_referrals_arrests/output/crdc_le_referrals_arrests_g8.ipynb",
    shell:
        """
        papermill {input.nb} {output.nb_g5} -p DIR notebooks/1718_referrals_arrests -p MAX_GRADE 5 -p YEAR 2017
        papermill {input.nb} {output.nb_g8} -p DIR notebooks/1718_referrals_arrests -p MAX_GRADE 8 -p YEAR 2017
        """

rule all:
    input:
        notebooks=OUTPUT_NOTEBOOKS,
        cleaned=OUTPUT_FILE_CLEANED
