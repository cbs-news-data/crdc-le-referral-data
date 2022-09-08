GENERATED_FILES: output/arrests.csv

.PHONY: all cleanup

all: $(GENERATED_FILES)

output/arrests.csv: \
		src/split_ref_arr.py \
		input/1718-crdc-sch-referrals-arrests.csv \
		src/transform_crdc_data.py \
		hand/variable_replace_values.yaml
	python $^ --arrests | \
		python src/transform_crdc_data.py \
		hand/variable_replace_values.yaml \
		arrests \
		> $@

cleanup:
	rm -f output/*