SHELL := /bin/bash

TASKS := clean notebooks

.PHONY: \
	  all \
	  init \
	  cleanup \
	  $(TASKS)

all: $(TASKS)

$(TASKS): venv/bin/activate
	source $< && $(MAKE) -C $@

init: venv/bin/activate

venv/bin/activate: requirements.txt
	if [ ! -f $@ ]; then virtualenv venv; fi
	source $@ && pip install -r $<
	touch $@

cleanup:
	for d in $(TASKS) ; do \
		cd "$(shell pwd)/$$d" && make cleanup  ; \
	done