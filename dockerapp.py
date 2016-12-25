import sys,os
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/flaskApp/docker-management")

for env in os.environ:
    print env, os.environ[env]
    os.environ[env] = os.environ[env]
os.environ["ENVIRONMENT"] = "TEST"
os.environ["OWNER"] = "Pankaj Gupta"


from manage import app as application

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=8000)