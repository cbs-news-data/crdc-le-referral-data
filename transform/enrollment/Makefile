GENERATED_FILES: output/enrollment.csv

.PHONY: all cleanup

all: $(GENERATED_FILES)

output/enrollment.csv: \
		src/transform_crdc_data.py \
		input/1718-crdc-sch-enrollment.csv \
		hand/variable_replace_values.yaml \
		hand/drop_cols_kwds.yaml
	python $< \
		-d hand/drop_cols_kwds.yaml \
		input/1718-crdc-sch-enrollment.csv \
		hand/variable_replace_values.yaml \
		enrollment \
		> $@		

cleanup:
	rm -f output/*