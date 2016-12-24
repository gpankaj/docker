#!/bin/sh
export ENVIRONMENT=TEST
rm -rf /tmp/all_current_envs
env > /tmp/all_current_envs
sudo pip install -r requirements.txt
python manage.py runserver &
exit 0