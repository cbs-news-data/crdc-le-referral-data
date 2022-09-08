GENERATED_FILES: output/referrals.csv

.PHONY: all cleanup

all: $(GENERATED_FILES)

output/referrals.csv: \
		src/split_ref_arr.py \
		input/1718-crdc-sch-referrals-arrests.csv \
		src/transform_crdc_data.py \
		hand/variable_replace_values.yaml
	python $^ --referrals | \
		python src/transform_crdc_data.py \
		hand/variable_replace_values.yaml \
		referrals \
		> $@

cleanup:
	rm -f output/*