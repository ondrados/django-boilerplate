#!/bin/sh

echo "Waiting for database..."
SQL_HOST=$(echo $DATABASE_URL | cut -d@ -f2 | cut -d: -f1)
SQL_PORT=$(echo $DATABASE_URL | cut -d@ -f2 | cut -d: -f2 | cut -d/ -f1)
while ! nc -z $SQL_HOST $SQL_PORT; do
  sleep 0.1
done
echo "Database available"


python manage.py migrate
python manage.py collectstatic --no-input --clear

gunicorn app.wsgi:application --bind 0.0.0.0:8000
