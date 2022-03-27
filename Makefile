ifeq "$(OS)" "Windows_NT"
directory := Scripts
else
directory := bin
endif

.PHONY: tests

install:
	python -m venv .venv
	. .venv/$(directory)/activate; pip install -r requirements.txt

tests:
	. .venv/$(directory)/activate; PYTHONPATH=. pytest .

clean:
	rm -rf .venv
