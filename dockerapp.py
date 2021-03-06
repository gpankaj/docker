import sys,os
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/flaskApp/docker-management")

for env in os.environ:
    os.environ[str(env)] = str(os.environ[env])

if os.environ.get("ENVIRONMENT", "") != "":
    os.environ["ENVIRONMENT"] = os.environ.get("ENVIRONMENT")
else:
    os.environ["ENVIRONMENT"] = "BETA"
    pass
os.environ["OWNER"] = "Pankaj Gupta"






from manage import app as application

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=8000)