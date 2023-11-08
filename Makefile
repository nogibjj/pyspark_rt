install: 
	pip install --upgrade pip && \
	pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main -rw test_*.py

format:
	black *.py

lint:
	ruff check *.py

run:
#	python lib.py	
	python main.py

all: install lint format test