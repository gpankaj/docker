#!/bin/sh
export ENVIRONMENT=TEST
sudo rm -rf /tmp/all_current_envs
env > /tmp/all_current_envs

sudo /usr/bin/pip install -r requirements.txt
python manage.py runserver &
exit 0