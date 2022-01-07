import os
from datetime import timedelta
from redis import Redis
import pymysql
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

    # sqlite
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(basedir, 'app.db')

    # mysql
    # master username
#     master_username = 'apollo'
#     password = 'Aa1234567!'
#     end_point = 'apollodatabase.cb9jianlqhw8.us-east-2.rds.amazonaws.com'
#     # database name (created by create schema in mysql workbench)
#     database_name = 'apollo_aws_mysql'
#     SQLALCHEMY_DATABASE_URI = "mysql+pymysql://%s:%s@%s/%s" % (master_username, password, end_point, database_name)
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     SQLALCHEMY_ENGINE_OPTIONS = {
#     # "poolclass": QueuePool,
#     "pool_size": 50,
# }

    # unittest
    master_username = 'apollo'
    password = 'Aa1234567!'
    end_point = 'apollodatabase.cb9jianlqhw8.us-east-2.rds.amazonaws.com'
    # database name (created by create schema in mysql workbench)
    database_name = 'apollo_aws_mysql_unittest'
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://%s:%s@%s/%s" % (master_username, password, end_point, database_name)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
    # "poolclass": QueuePool,
    "pool_size": 50,
}

<<<<<<< HEAD
    # unittest
#     master_username = 'apollo'
#     password = 'Aa1234567!'
#     end_point = 'apollodatabase.cb9jianlqhw8.us-east-2.rds.amazonaws.com'
#     # database name (created by create schema in mysql workbench)
#     database_name = 'apollo_aws_mysql_unittest'
#     SQLALCHEMY_DATABASE_URI = "mysql+pymysql://%s:%s@%s/%s" % (master_username, password, end_point, database_name)
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     SQLALCHEMY_ENGINE_OPTIONS = {
#     # "poolclass": QueuePool,
#     "pool_size": 50,
# }

=======
>>>>>>> 1c16ce9fb52a78853a026ebbaf41bb60e2b68876



    MESSAGES_PER_PAGE = 10

    # gmail for email validation
    # gmail account: apolloumn.email@gmail.com
    # gmail password: apolloumn
    # app password: wvduhthxrmktdxjb
    MAIL_SERVER ='smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'apolloumn.email@gmail.com'
    MAIL_PASSWORD = 'wvduhthxrmktdxjb'
    MAIL_USE_SSL = True
    MAIL_DEFAULT_SENDER = 'apolloumn.email@gmail.com'
    SECURITY_PASSWORD_SALT = 'zxsdfasdvasdafwe'


class ProductionConfig(Config):

    pass

class DevelopmentConfig(Config):
  
    pass
    

class TestingConfig(Config):

    pass