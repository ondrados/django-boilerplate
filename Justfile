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
	docker compose -f docker-compose-local.yml exec -it django sh

# Run shell_plus for application
shell:
	docker compose -f docker-compose-local.yml exec -it django python manage.py shell_plus

# Create superuser
superuser:
	docker compose -f docker-compose-local.yml exec -it django python manage.py createsuperuser

# Run fixtures for application
fixtures:
	docker compose -f docker-compose-local.yml exec -it django sh ./load-fixtures.sh

# Create migrations for application
migrations:
	docker compose -f docker-compose-local.yml exec -it django python manage.py makemigrations

# Run migrations for application
migrate:
	docker compose -f docker-compose-local.yml exec -it django python manage.py migrate

lint:
    flake8

format:
    black .
