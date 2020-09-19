clean:
	rm -rf dist
	rm -rf *.egg.info
	find . -type f -name *.pyc -exec rm -f {} \;

docker-build:
	docker-compose stop
	docker-compose rm
	docker-compose build 

docker-run:
	docker-compose up {{ project_slug }}-api docker_db

dev-install: clean
	poetry install --dev

dev-run:
	FLASK_APP={{ project_slug }}/app.py flask run
	
dev_db-up:
	docker-compose up -d development_db

dev_db-stop:
	docker-compose stop development_db

dev_db-initialize:
	python -m {{ project_slug }}.initialize_db

test_db-up:
	docker-compose up -d test_db

test_db-stop:
	docker-compose stop test_db

lint: clean
	flake8 {{ project_slug }}
	pylint {{ project_slug }}
	isort {{ project_slug }} --check

test: lint
	ENV_FOR_DYNACONF=testing pytest
