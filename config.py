import os

class Config():
    SECRET_KEY=os.environ.get('SECRET_KEY')

class DevelopmentConfig(Config):
    DEBUG=True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'top s3cr3t'

class TestConfig(Config):
    TESTING=True

class ProductionConfig(Config):
    pass

config_dict = {
    'development' : DevelopmentConfig,
    'test' : TestConfig,
    'production': ProductionConfig,
    'default' : DevelopmentConfig
}