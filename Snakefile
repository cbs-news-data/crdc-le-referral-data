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

INPUT_FILES_2021 = [
    "clean/input/2021-crdc-sch-characteristics.csv",
    "clean/input/2021-crdc-sch-enrollment.csv",
    "clean/input/2021-crdc-sch-referrals-arrests.csv"
]

GRADES = [5, 8]
YEARS = [2017, 2020]

# Define the output file
OUTPUT_FILE_CLEANED = "clean/output/crdc-referrals-arrests-cleaned.csv"

rule all:
    input:
        cleaned=OUTPUT_FILE_CLEANED,
        notebooks=expand("notebooks/crdc_referrals_arrests/output/crdc_le_referrals_arrests_g{grade}_{year}.ipynb", grade=GRADES, year=YEARS),


# runs the data cleaning with the available input files
rule clean:
    input:
        src="src/clean_crdc_data.py",
        const="src/constants.py",
        f1=INPUT_FILES_1314,
        f2=INPUT_FILES_1516,
        f3=INPUT_FILES_1718,
        f4=INPUT_FILES_2021,
    output:
        cleaned=OUTPUT_FILE_CLEANED
    shell:
        """
        python {input.src} \
            -f {input.f1} \
            -f {input.f2} \
            -f {input.f3} \
            -f {input.f4} \
            -o {output.cleaned}
        """

# Runs the notebooks with various parameters to generate the final output using papermill
rule notebooks:
    input:
        cleaned=OUTPUT_FILE_CLEANED,
        nb="notebooks/crdc_referrals_arrests/crdc_le_referrals_arrests.ipynb",
    output:
        "notebooks/crdc_referrals_arrests/output/crdc_le_referrals_arrests_g{grade}_{year}.ipynb",
    shell:
        """
        papermill {input.nb} {output} -p DIR notebooks/crdc_referrals_arrests -p MAX_GRADE {wildcards.grade} -p YEAR {wildcards.year}
        """
