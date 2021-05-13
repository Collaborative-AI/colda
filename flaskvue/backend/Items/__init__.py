from flask import Flask
from flask_session import Session
from .views import account
from .views import home


def create_app():
    app = Flask(__name__)
    app.config.from_object('setting.DevelopmentConfig')

    
    # Initialize Blueprint
    app.register_blueprint(account.account)
    app.register_blueprint(home.home)

    # Substitue session to redis
    Session(app)

    return app

