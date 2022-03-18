# -*- coding: utf-8 -*-
''' Create instance of these flask extensions '''
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_pymongo import PyMongo
# import pymongo 

import pymysql

# Flask-Cors plugin
cors = CORS()
# Flask-SQLAlchemy plugin
db = SQLAlchemy()
# # Flask-Migrate plugin
migrate = Migrate()
mail = Mail()
pyMongo = PyMongo()

