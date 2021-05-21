from flask import Flask
from flask_session import Session
from flask_socketio import SocketIO
from flask_cors import CORS

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

    # CORS(app, resources={r'/*': {'origins': '*'}})
    # socketio.init_app(app)
    
    CORS(app, supports_credentials=True) # HTTP/HTTPS 跨域
    # socketio = SocketIO(app, cors_allowed_origins="*") # websocket 跨域
    socketio.init_app(app=app,cors_allowed_origins="*")

    return app

