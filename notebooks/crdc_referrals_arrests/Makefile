GENERATED_FILES: output/crdc_referrals_arrests.html

.PHONY: all cleanup

all: $(GENERATED_FILES)

output/crdc_referrals_arrests.html: \
		crdc_referrals_arrests.ipynb \
		input/arrests.csv \
		input/characteristics.csv \
		input/enrollment.csv \
		input/referrals.csv \
		src/transform_crdc_data.py
	jupyter nbconvert --execute --to html $< --stdout > $@

cleanup:
	rm -f output/*
