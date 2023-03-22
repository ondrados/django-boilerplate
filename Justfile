BACKEND_CONTAINER := "django-boilerplate-django-1"

# default recipe to display help information
default:
  @just --list

# Run application
run:
	docker compose -f docker-compose-local.yml up

# Run application with recreation of containers and dependencies
run-force:
	docker compose -f docker-compose-local.yml up --build

# Go inside django docker container
cli:
	docker exec -it {{BACKEND_CONTAINER}} bash

# Run shell_plus for application
shell:
	docker exec -it {{BACKEND_CONTAINER}} python manage.py shell_plus

# Create superuser
superuser:
	docker exec -it {{BACKEND_CONTAINER}} python manage.py createsuperuser

# Run fixtures for application
fixtures:
	docker exec -it {{BACKEND_CONTAINER}} sh ./load-fixtures.sh

# Create migrations for application
migrations:
	docker exec -it {{BACKEND_CONTAINER}} python manage.py makemigrations

# Run migrations for application
migrate:
	docker exec -it {{BACKEND_CONTAINER}} python manage.py migrate

lint:
    flake8

format:
    black .
