.PHONY: all init check test coverage html pdf clean clean-all

all:
	@echo 'init             install development requirements'
	@echo 'check            run static code checkers'
	@echo 'test             run unit tests'
	@echo 'coverage         generate HTML coverage report'
	@echo 'html             build HTML documentation'
	@echo 'pdf              build PDF documentation (requires LaTeX)'
	@echo 'clean            cleanup source tree'
	@echo 'clean-all        also removes tox and eggs'

init:
	@pip install -q -r dev-requirements.txt

test: check
	@python -m pytest --cov=flask_signin --cov=tests --cov-branch

coverage: check
	@python -m pytest --cov=flask_signin --cov=tests --cov-branch \
		--cov-report html

check:
	@python setup.py check --restructuredtext --strict && \
		([ $$? -eq 0 ] && echo "README.rst ok") || \
		echo "Invalid markup in README.rst!"
	@python -m pylint --rcfile=.pylintrc flask_signin
	@python -m pycodestyle flask_signin tests
	@python -m pydocstyle flask_signin

html:
	@$(MAKE) -C docs html

pdf:
	@$(MAKE) -C docs latexpdf

clean:
	@rm -f flask_signin/*.pyc
	@rm -f tests/*.pyc
	@rm -f .coverage
	@rm -rf htmlcov
	@rm -rf __pycache__ flask_sigin/__pycache__ tests/__pycache__
	@rm -rf *.egg-info

clean-all: clean
	@rm -rf .tox
	@rm -rf .eggs
	@$(MAKE) -C docs clean
