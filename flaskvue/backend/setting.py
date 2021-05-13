from datetime import timedelta
from redis import Redis

class Config(object):
    DEBUG = True
    SECRET_KEY = 'adasdaxcw!!!--xq4213'

    # When session.permanent = True, PERMANENT_SESSION_LIFETIME works.
    # session.permanent default value is False, Redis is True
    PERMANENT_SESSION_LIFETIME = timedelta(days=31)

    # Let dict.get() write into Cookie and refresh the permenant session lifetime
    SESSION_REFRESH_EACH_REQUEST = True

    # Redis Setting
    SESSION_TYPE = 'redis'
    SESSION_KEY_PREFIX = 'Apollo_flask_backend'

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    # default port is 6379
    SESSION_REDIS = Redis(host='127.0.0.1',port=6379)
    

class TestingConfig(Config):
    pass