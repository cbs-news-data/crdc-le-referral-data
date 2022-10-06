GENERATED_FILES: output/trends.ipynb 

all: $(GENERATED_FILES)

.PHONY: all cleanup

output/trends.ipynb: \
		trends.ipynb \
		$(wildcard input/*)
	papermill $< $@

cleanup:
	find output -type f -not -name '.gitignore' -delete