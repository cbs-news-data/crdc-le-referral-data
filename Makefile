SHELL := /bin/bash

TASKS := clean notebooks

.PHONY: \
	  all \
	  init \
	  cleanup \
	  $(TASKS)

all: $(TASKS)

$(TASKS): .venv/bin/activate
	source $< && $(MAKE) -C $@ -j 4

init: .venv/bin/activate

.venv/bin/activate: pyproject.toml
	poetry install --no-root

cleanup:
	for d in $(TASKS) ; do \
		cd "$(shell pwd)/$$d" && make cleanup  ; \
	done