#!/bin/sh
export ENVIRONMENT=PRODUCTION

env > /tmp/all_current_envs

if [ "$DEPLOYMENT_GROUP_NAME" == "Staging" ]
then
    sed -i -e 's/Listen 80/Listen 9090/g' /etc/httpd/conf/httpd.conf
fi