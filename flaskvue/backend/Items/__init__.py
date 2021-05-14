from flask import Flask
from flask_session import Session
from flask_socketio import SocketIO

socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    app.config.from_object('setting.DevelopmentConfig')
    # app.debug = True
    # app.config['SECRET_KEY'] = 'gjr39dkjn344_!67#'

    # Initialize Blueprint
    # from .main import account
    # from .main import home
    # app.register_blueprint(account.account)
    # app.register_blueprint(home.home)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    # Substitue session to redis
    Session(app)

    socketio.init_app(app)
    return app

