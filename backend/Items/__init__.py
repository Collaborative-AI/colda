# -*- coding: utf-8 -*-
from flask import Flask
from Items.extensions import cors, mail, pyMongo
from flask_mail import Mail

from Items.authentication import authentication_bp
from Items.main_flow import main_flow_bp
from Items.user import user_bp
from Items.helper_api import helper_api_bp



def create_app(config_class=None):
    '''Factory Pattern: Create Flask app.'''
    # pymysql.install_as_MySQLdb()
    application = Flask(__name__)

    # Initialization flask app
    configure_app(application, config_class)
    configure_blueprints(application)
    configure_extensions(application)

    configure_before_handlers(application)
    configure_after_handlers(application)
    configure_errorhandlers(application)
    
    return application


def configure_app(application, config_class):
    application.config.from_object(config_class)
    
    # 不检查路由中最后是否有斜杠/
    application.url_map.strict_slashes = False


def configure_blueprints(application):
    # 注册 blueprint
    # from .main import main as main_blueprint
    # print("main_blueprint", main_blueprint)
    application.register_blueprint(authentication_bp)
    application.register_blueprint(main_flow_bp)
    application.register_blueprint(user_bp)
    application.register_blueprint(helper_api_bp)


def configure_extensions(application):
    '''Configures the extensions.'''

    # Enable CORS
    cors.init_app(application)

    # Init Flask-SQLAlchemy
    # db.init_app(app)

    # Init Flask-Migrate
    # migrate.init_app(app, db)

    # Init email service
    mail.init_app(application)

    pyMongo.init_app(application)
    create_MongoDB_Collections()

def create_MongoDB_Collections():
    print('pyMongo', pyMongo, dir(pyMongo))
    # print('db_name', pyMongo.sample_airbnb)
    # print('db_name2', pyMongo.sample_airbnb.list_collection_names())
    # print('pymongo2', pyMongo.mysynspot_db)
    collection_list = pyMongo.db.list_collection_names()
    print('collection_list', collection_list)
    if 'User' not in collection_list:
        print('gggg')
        pyMongo.db.User.insert_one( { "user_id": 'placeholder' } )
        pyMongo.db.User.create_index([("user_id", 1)], unique=True)
        pyMongo.db.User.create_index([("username", 1)], unique=True)
        # pyMongo.db.User.create_index([("email", 1)], unique=True)

    if 'Notification' not in collection_list:
        pyMongo.db.Notification.create_index([("user_id", 1)], unique=True)

    if 'Pending' not in collection_list:
        pyMongo.db.Pending.create_index([("user_id", 1)], unique=True)

    if 'Train_Message' not in collection_list:
        pyMongo.db.Train_Message.create_index([("train_id", 1)], unique=True)
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
        pyMongo.db.Train_Match.create_index([("train_id", 1)], unique=True)
    if 'Train_Match_Identifier' not in collection_list:
        pyMongo.db.Train_Match_Identifier.create_index([("identifier_id", 1)], unique=True)

    if 'Test_Match' not in collection_list:
        pyMongo.db.Test_Match.create_index([("test_id", 1)], unique=True)
    if 'Test_Match_Identifier' not in collection_list:
        pyMongo.db.Test_Match_Identifier.create_index([("identifier_id", 1)], unique=True)
    
    if 'Train_Task' not in collection_list:
        pyMongo.db.Train_Task.create_index([("train_id", 1)], unique=True)
    if 'Test_Task' not in collection_list:
        pyMongo.db.Test_Task.create_index([("test_id", 1)], unique=True)
    if 'Stop' not in collection_list:
        pyMongo.db.Stop.create_index([("stop_informed_user_id", 1)], unique=True)

    collection_list = pyMongo.db.list_collection_names()
    print('fffff', collection_list)
    
def configure_before_handlers(application):
    '''Configures the before request handlers'''
    pass


def configure_after_handlers(application):
    '''Configures the after request handlers'''
    pass


def configure_errorhandlers(application):
    '''Configures the error handlers'''

    from werkzeug.exceptions import HTTPException
    # from app.utils.api import handle_response
    '''Configures the error handlers'''
    from flask.json import jsonify
    @application.errorhandler(Exception)
    def handle_error(e):
        print('lailelaile', e)
        code = 500
        if isinstance(e, HTTPException):
            code = e.code
        return jsonify(
            error=str(e),
            error_name=type(e).__name__
        ), code


