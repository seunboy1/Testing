
test:
	pytest test_case/

quality_checks: setup
	isort .
	black .
	pylint --recursive=y .
	coverage run -m pytest -v
	coverage report -m

run: quality_checks test
	python main.py

setup:
	pip install -r requirements.txt
