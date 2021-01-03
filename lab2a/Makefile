.DEFAULT_GOAL := all

all: install test run deploy

install:
	@echo "Installing pipenv and dependencies."
	pipenv --python 3.8
	pipenv shell
	pipenv install requests
	pipenv install ntplib
	pipenv install pytest

test:
	@echo "Start tests."
	pytest ./tests/tests.py >> results.txt

run:
	@echo "Run Python app."
	python app.py >> results.txt

deploy:
	@echo "Adding and Committing results.txt to git."
	git add results.txt
	git commit -m "Update results.txt"
	git push origin master