# -*- coding: utf-8 -*-
''' Create instance of these flask extensions '''
from flask_cors import CORS
from flask_mail import Mail
from flask_pymongo import PyMongo

# Flask-Cors plugin
cors = CORS()
# # Flask-Migrate plugin
mail = Mail()
pyMongo = PyMongo()

# import pymongo
# pyMongo = pymongo()

