clean:
	@find . -name "*.pyc" -delete

deps:
	@pip install -r requirements.txt

run: deps
	@honcho start
