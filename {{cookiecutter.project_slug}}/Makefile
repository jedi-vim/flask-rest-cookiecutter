clean:
	rm -rf dist
	rm -rf *.egg.info
	find . -type f -name *.pyc -exec rm -f {} \;

build:
	docker-compose stop
	docker-compose rm
	docker-compose build

run:
	docker-compose up

install: clean
	poetry install

lint: clean
	flake8 {{ cookiecutter.project_slug }}

test: lint
	export ENV_FOR_DYNACONF=testing; 
	pytest -v --cov-fail-under=90 --cov={{ cookiecutter.project_slug }} {{ cookiecutter.project_slug }}/tests 

test-report:
	export ENV_FOR_DYNACONF=testing; 
	pytest -v --cov-fail-under=90 --cov={{ cookiecutter.project_slug }} --cov-report=html {{ cookiecutter.project_slug }}/tests

db-init:
	poetry run initialize_db

db-migrate:
	flask db migrate -m "$(message)"

db-upgrade:
	flask db upgrade