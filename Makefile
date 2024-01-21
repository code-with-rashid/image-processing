docker_file ?= -f docker-compose.yml -f docker-compose.local.yml
execute_flags ?=

makemigrations:
	docker compose $(docker_file) exec $(execute_flags) web python manage.py makemigrations

migrate:
	docker compose $(docker_file) exec $(execute_flags) web python manage.py migrate

createsuperuser:
	docker compose $(docker_file) exec $(execute_flags) web python manage.py createsuperuser

collectstatic:
	docker compose $(docker_file) exec $(execute_flags) web python manage.py collectstatic

shell:
	docker compose $(docker_file) exec $(execute_flags) web python manage.py shell

install:
	docker compose $(docker_file) exec $(execute_flags) web pip install $(package)

bash:
	docker compose $(docker_file) exec $(execute_flags) web bash

start:
	docker compose $(docker_file) build
	docker compose $(docker_file) up --no-start --remove-orphans
	docker compose $(docker_file) start

stop:
	docker compose $(docker_file) down

restart: stop start

dropdb:
	docker compose $(docker_file) down
	- docker volume rm image_processing_postgres_data

setup_initial_data:
	docker compose $(docker_file) run $(execute_flags) web python manage.py process_excel_images data/img.csv

redo-db: dropdb start migrate setup_initial_data

prune:
	docker system prune --force

pre-commit:
	pre-commit run --all-files

test:
	docker compose $(docker_file) run $(execute_flags) web python manage.py test --settings image_processing.settings.development --keepdb --no-input  --failfast
	docker compose $(docker_file) run $(execute_flags) web python manage.py test --settings image_processing.settings.development --keepdb --no-input  --failfast