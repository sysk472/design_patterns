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
	. .venv/$(directory)/activate; isort . --check; black . --check
	. .venv/$(directory)/activate; PYTHONPATH=. pytest .

lint:
	. .venv/$(directory)/activate; isort .; black .

clean:
	rm -rf .venv
