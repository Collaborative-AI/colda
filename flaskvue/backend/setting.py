import os
from datetime import timedelta
from redis import Redis
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'), encoding='utf-8')

class Config(object):
    
    DEBUG = True
    SECRET_KEY = 'adasdaxcw!!!--xq4213'

    # When session.permanent = True, PERMANENT_SESSION_LIFETIME works.
    # session.permanent default value is False, but Redis is True
    PERMANENT_SESSION_LIFETIME = timedelta(days=31)

    # Let dict.get() write into Cookie and refresh the permenant session lifetime
    SESSION_REFRESH_EACH_REQUEST = True

    # Redis Setting
    SESSION_TYPE = 'redis'
    SESSION_KEY_PREFIX = 'Apollo_flask_backend'
    # default port is 6379
    SESSION_REDIS = Redis(host='127.0.0.1',port=6379)

    # JWT secret key
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Apollo'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MESSAGES_PER_PAGE = 10

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    pass
    

class TestingConfig(Config):
    pass