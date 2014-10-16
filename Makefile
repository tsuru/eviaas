deps:
	@pip install -r requirements.txt

run: deps
	@honcho start
