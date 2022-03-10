# -*- coding: utf-8 -*-
from flask import Flask
from Items.extensions import cors, db, migrate, mail, pyMongo
from flask_mail import Mail
from Items.main import main as main_blueprint
import pymysql
# from flask_session import Session

# mail = None

def create_app(config_class=None):
    '''Factory Pattern: Create Flask app.'''
    pymysql.install_as_MySQLdb()
    app = Flask(__name__)

    # Initialization flask app
    configure_app(app, config_class)
    configure_blueprints(app)
    configure_extensions(app)

    configure_before_handlers(app)
    configure_after_handlers(app)
    configure_errorhandlers(app)
    
    return app


def configure_app(app, config_class):
    app.config.from_object(config_class)
    
    # 不检查路由中最后是否有斜杠/
    app.url_map.strict_slashes = False


def configure_blueprints(app):
    # 注册 blueprint
    # from .main import main as main_blueprint
    # print("main_blueprint", main_blueprint)
    app.register_blueprint(main_blueprint)


def configure_extensions(app):
    '''Configures the extensions.'''

    # Enable CORS
    cors.init_app(app)

    # Init Flask-SQLAlchemy
    # db.init_app(app)

    # Init Flask-Migrate
    # migrate.init_app(app, db)

    # Init email service
    mail.init_app(app)

    pyMongo.init_app(app)
    create_MongoDB_Collections()

def create_MongoDB_Collections():
    collection_list = pyMongo.db.list_collection_names()
    if 'User' not in collection_list:
        pyMongo.db.User.insert_one( { "user_id": 'placeholder' } )
        pyMongo.db.Notification.create_index([("username", 1)], unique=True)
        pyMongo.db.Notification.create_index([("email", 1)], unique=True)

    if 'Notification' not in collection_list:
        pyMongo.db.Notification.create_index([("user_id", 1)], unique=True)

    if 'Pending' not in collection_list:
        pyMongo.db.Pending.create_index([("user_id", 1)], unique=True)

    if 'Train_Message' not in collection_list:
        pyMongo.db.Train_Message.create_index([("task_id", 1)], unique=True)
    if 'Train_Message_Situation' not in collection_list:
        pyMongo.db.Train_Message_Situation.create_index([("situation_id", 1)], unique=True)
    if 'Train_Message_Output' not in collection_list:
        pyMongo.db.Train_Message_Output.create_index([("output_id", 1)], unique=True)

    if 'Test_Message' not in collection_list:
        pyMongo.db.Test_Message.create_index([("test_id", 1)], unique=True)
    if 'Test_Message_Situation' not in collection_list:
        pyMongo.db.Test_Message_Situation.create_index([("situation_id", 1)], unique=True)
    if 'Test_Message_Output' not in collection_list:
        pyMongo.db.Test_Message_Output.create_index([("output_id", 1)], unique=True)
    
    if 'Train_Match' not in collection_list:
        pyMongo.db.Train_Match.create_index([("task_id", 1)], unique=True)
    if 'Train_Match_File' not in collection_list:
        pyMongo.db.Train_Match_File.create_index([("matched_id_file_id", 1)], unique=True)
    
    if 'Test_Match' not in collection_list:
        pyMongo.db.Test_Match.create_index([("test_id", 1)], unique=True)
    if 'Test_Match_File' not in collection_list:
        pyMongo.db.Test_Match_File.create_index([("matched_id_file_id", 1)], unique=True)
    
    if 'Train_Task' not in collection_list:
        pyMongo.db.Train_Task.create_index([("task_id", 1)], unique=True)
    if 'Test_Task' not in collection_list:
        pyMongo.db.Test_Task.create_index([("test_id", 1)], unique=True)
    if 'Stop' not in collection_list:
        pyMongo.db.Stop.create_index([("stop_informed_user_id", 1)], unique=True)

def configure_before_handlers(app):
    '''Configures the before request handlers'''
    pass


def configure_after_handlers(app):
    '''Configures the after request handlers'''
    pass


def configure_errorhandlers(app):
    '''Configures the error handlers'''
    pass


