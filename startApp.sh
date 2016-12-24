#!/bin/sh
export ENVIRONMENT=TEST

env > /tmp/all_current_envs
pip install -r requirements.txt
python manage.py runserver &

exit 0