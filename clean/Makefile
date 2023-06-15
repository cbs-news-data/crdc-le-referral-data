# additional files generated: output/clean_crdc_data.log
GENERATED_FILES: output/crdc-referrals-arrests-cleaned.csv

all: $(GENERATED_FILES)

.PHONY: all cleanup

output/crdc-referrals-arrests-cleaned.csv: \
		# src/clean_crdc_data.py \
		src/dilcia.py \
		input/1314-crdc-sch-characteristics.xlsx \
		input/1314-crdc-sch-enrollment.xlsx \
		input/1314-crdc-sch-referrals-arrests.xlsx \
		input/CRDC-2015-16-School-Data.csv.gz \
		input/1718-crdc-sch-characteristics.csv \
		input/1718-crdc-sch-enrollment.csv \
		input/1718-crdc-sch-referrals-arrests.csv \
		src/constants.py
	# python src/clean_crdc_data.py \
	python src/dilcia.py \
		-f input/1314-crdc-sch-characteristics.xlsx input/1314-crdc-sch-enrollment.xlsx input/1314-crdc-sch-referrals-arrests.xlsx \
		-f input/CRDC-2015-16-School-Data.csv.gz \
		-f input/1718-crdc-sch-characteristics.csv input/1718-crdc-sch-enrollment.csv input/1718-crdc-sch-referrals-arrests.csv \
		-o output/crdc-referrals-arrests-cleaned.csv

cleanup:
	rm -f output/*