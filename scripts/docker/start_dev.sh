#!/usr/bin/env bash

echo -e "\e[34m >>> Migrating changes \e[97m"
python manage.py migrate
echo -e "\e[32m >>> migration completed \e[97m"

echo -e "\e[34m >>> Collecting Static files \e[97m"
python manage.py collectstatic --noinput
echo -e "\e[32m >>> Static files collect completed \e[97m"

uvicorn djangoapp.asgi:application --host 0.0.0.0 --port 8000 --reload --reload-dir /djangoapp
