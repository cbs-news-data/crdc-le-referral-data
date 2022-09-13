GENERATED_FILES: output/characteristics.csv

.PHONY: all cleanup

all: $(GENERATED_FILES)

output/characteristics.csv: \
		src/transform_characteristics.py \
		input/1718-crdc-sch-characteristics.csv \
		hand/states.json
	python $^ > $@

cleanup:
	rm -f output/*