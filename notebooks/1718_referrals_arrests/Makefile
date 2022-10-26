GENERATED_FILES: output/crdc_le_referrals_arrests_g5.ipynb output/crdc_le_referrals_arrests_g8.ipynb 

all: $(GENERATED_FILES)

.PHONY: all cleanup

output/crdc_le_referrals_arrests_g5.ipynb: \
		crdc_le_referrals_arrests.ipynb \
		$(wildcard input/*)
	papermill $< -p MAX_GRADE 5 $@

output/crdc_le_referrals_arrests_g8.ipynb: \
		crdc_le_referrals_arrests.ipynb \
		$(wildcard input/*)
	papermill $< -p MAX_GRADE 8 $@

cleanup:
	find output -type f -not -name '.gitignore' -delete