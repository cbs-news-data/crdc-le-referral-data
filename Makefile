SHELL := /bin/bash

# TASKS := \
#     your \
#     tasks \
#     here

.PHONY: \
	  all \
	  cleanup # \
#	  $(TASKS)

all: $(TASKS)

$(TASKS): venv/bin/activate
	source $< && $(MAKE) -C $@

venv/bin/activate: requirements.txt
	if [ ! -f $@ ]; then virtualenv venv; fi
	source $@ && pip install -r $<
	touch $@
 
clean:
	for d in $(TASKS) ; do \
		cd "$(shell pwd)/$$d" && make clean  ; \
	done
