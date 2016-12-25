import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/flaskApp/docker-management")

from manage import app as application

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=8000)