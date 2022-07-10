#!/bin/sh

echo "Waiting for database..."
while ! nc -z $SQL_HOST $SQL_PORT; do
  sleep 0.1
done
echo "Database available"


python manage.py migrate
python manage.py collectstatic --no-input --clear

gunicorn core.wsgi:application --bind 0.0.0.0:8000
