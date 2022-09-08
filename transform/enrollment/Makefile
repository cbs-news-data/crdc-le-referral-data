GENERATED_FILES: output/enrollment.csv

.PHONY: all cleanup

all: $(GENERATED_FILES)

output/enrollment.csv: \
		src/transform_crdc_data.py \
		input/1718-crdc-sch-enrollment.csv
	python $^ enrollment > $@

cleanup:
	rm -f output/*