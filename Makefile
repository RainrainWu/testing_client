PKG=app
VERSION=$(shell awk '{match($$0,"__version__ = '\''(.*)'\''",a)}END{print a[1]}' $(PKG)/__version__.py)

.PHONY: version init flake8 pylint mypy lint test coverage ci package upload clean

version:
	@echo $(VERSION)

init: clean
	pipenv --python 3.7
	pipenv install --dev

flake8:
	pipenv run flake8

pylint:
	pipenv run pylint $(PKG) --disable=missing-docstring

lint: flake8 pylint mypy

test:
	pipenv run pytest --pep8 --disable-warnings

coverage:
	pipenv run pytest --cov-report term-missing --cov-report xml --cov=$(PKG) tests

clean:
	find . -type f -name '*.py[co]' -delete
	find . -type d -name '__pycache__' -delete
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info
	rm -rf .hypothesis
	rm -rf .pytest_cache
	rm -rf .tox
	rm -f report.xml
	rm -f coverage.xml
