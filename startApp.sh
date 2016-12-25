#!/bin/sh

sudo rm -rf /tmp/all_current_envs
env > /tmp/all_current_envs
sudo cp -f /var/www/flaskApp/docker-management/FlaskApp-QA.conf /etc/apache2/sites-available/FlaskApp.conf
sudo rm /etc/apache2/sites-enabled/*
sudo sudo a2ensite FlaskApp
sudo /etc/init.d/apache2 reload

sudo /usr/bin/pip install -r requirements.txt

exit 0