import sqlite3
import os
from sqlalchemy import create_engine
from model import User_Default_Path, Base

# create database connection
basedir = os.path.abspath(os.path.dirname(__file__))
# The object created by sqlite by default can only be used by the thread that created the object
# , and sqlalchemy is multi-threaded, so we need to specify check_same_thread=False to make
#  the created object available to any thread
print(os.path.join(basedir, 'app_package.db'))
engine = create_engine('sqlite:///' + os.path.join(basedir, 'app_package.db') + '?check_same_thread=False', echo=True)

# Create File and initialize databases
Base.metadata.create_all(engine, checkfirst=True)