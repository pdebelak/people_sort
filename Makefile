.PHONY: test setup

test:
	venv/bin/python -m pytest --cov=people_sort tests/

deps: requirements.txt venv
	venv/bin/pip install -r requirements.txt

venv:
	python3 -m venv venv
