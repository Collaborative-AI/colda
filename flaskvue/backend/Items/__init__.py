from flask import Flask
from Items.extensions import cors, db, migrate
from Items.main import main as main_blueprint
# from flask_session import Session


def create_app(config_class=None):
    '''Factory Pattern: Create Flask app.'''
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
    app.register_blueprint(main_blueprint)


def configure_extensions(app):
    '''Configures the extensions.'''
    # Enable CORS
    cors.init_app(app)
    # Init Flask-SQLAlchemy
    db.init_app(app)
    # Init Flask-Migrate
    migrate.init_app(app, db)


def configure_before_handlers(app):
    '''Configures the before request handlers'''
    pass


def configure_after_handlers(app):
    '''Configures the after request handlers'''
    pass


def configure_errorhandlers(app):
    '''Configures the error handlers'''
    pass


