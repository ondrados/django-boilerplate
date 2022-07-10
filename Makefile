
MIN_MAKE_VERSION := 3.82

ifneq ($(MIN_MAKE_VERSION),$(firstword $(sort $(MAKE_VERSION) $(MIN_MAKE_VERSION))))
$(error GNU Make $(MIN_MAKE_VERSION) or higher required)
endif

.DEFAULT_GOAL:=help

BACKEND_CONTAINER := django-boilerplate-django-1

##@ Development
.PHONY: run run-force cli-db

run: ## Run application
	docker compose -f docker-compose-local.yml up

run-force: ## Run application with recreation of containers and dependencies
	docker compose -f docker-compose-local.yml up --build

cli-db: ## Go inside database docker app
	docker exec -it django-boilerplate-db-1 sh

##@ Django
.PHONY: cli shell test superuser fixtures migrate migrations

cli: ## Go inside django docker container
	docker exec -it $(BACKEND_CONTAINER) sh

shell: ## Run shell_plus for application
	docker exec -it $(BACKEND_CONTAINER) python manage.py shell_plus

superuser: ## Create superuser for application
	docker exec -it $(BACKEND_CONTAINER) python manage.py createsuperuser

fixtures: ## Run fixtures for application
	docker exec -it $(BACKEND_CONTAINER) sh ./load-fixtures.sh

migrations: ## Create migrations for application
	docker exec -it $(BACKEND_CONTAINER) python manage.py makemigrations

migrate: ## Run migrations for application
	docker exec -it $(BACKEND_CONTAINER) python manage.py migrate


##@ Help
.PHONY: help
help: ## Show this help usage
	@awk 'BEGIN {FS = ":.*##"; printf "Usage: make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-25s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)