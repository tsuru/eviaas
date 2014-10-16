clean:
	@find . -name "*.pyc" -delete

deps:
	@pip install -r test-requirements.txt

test: clean deps
	@PYTHONPATH=. py.test -s --cov-report term-missing --cov .
	@flake8 --max-line-length 110 .

run: clean deps
	@honcho start
