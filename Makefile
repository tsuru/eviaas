clean:
	@find . -name "*.pyc" -delete

deps:
	@pip install -r test-requirements.txt

test: clean deps
	@python -m unittest discover
	@flake8 --max-line-length 110 .

run: clean deps
	@python evi/api.py
