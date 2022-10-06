GENERATED_FILES: output/crdc_le_referrals_arrests.ipynb 

all: $(GENERATED_FILES)

.PHONY: all cleanup

output/crdc_le_referrals_arrests.ipynb: \
		crdc_le_referrals_arrests.ipynb \
		$(wildcard input/*)
	papermill $< $@

cleanup:
	find output -type f -not -name '.gitignore' -delete