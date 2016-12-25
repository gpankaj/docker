from flask import Flask
from config import config_dict
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CsrfProtect

bootstrap = Bootstrap()
csrf = CsrfProtect()

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def create_app(config_name):
    app=Flask(__name__)
    app.config.from_object(config_dict[config_name])
    bootstrap.init_app(app)
    csrf.init_app(app)

    from app.blueprints.dsystem import dsystem as dsystem_blueprint
    app.register_blueprint(dsystem_blueprint)

    from app.blueprints.home import home
    app.register_blueprint(home)

    return app
