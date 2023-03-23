#!/bin/sh

while ! nc -z db 3306 ; do
  echo "Waiting for the MySQL Server"
  sleep 3
done

# python manage.py wait_for_db

# Apply database migrations
echo "Apply database migrations"
# python manage.py nabshop
python manage.py migrate

python manage.py nabshopdb

# echo "Collection static"
# python manage.py collectstatic --no-input

# Start server
echo "Starting server"
# python manage.py runserver 0.0.0.0:8000

gunicorn nabshopdjango.wsgi:application --bind 0.0.0.0:8000
