
test:
	@poetry run pytest .

init:
	@poetry install

load-env:
	@export $(shell cat .env | xargs)

migrate:
	@poetry run python manage.py migrate

make-migrations:
	@poetry run python manage.py makemigrations

run:
	@poetry run python manage.py runserver