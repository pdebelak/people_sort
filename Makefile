.PHONY: test deps server

test:
	venv/bin/python -m pytest --cov=people_sort tests/

server:
	FLASK_APP=people_sort.api venv/bin/python -m flask run

deps: requirements.txt venv
	venv/bin/pip install -r requirements.txt

venv:
	python3 -m venv venv
