import os
basedir = os.path.abspath(os.path.dirname(__file__))
import sys
sys.path.append(basedir)

import sqlite3
import os
from sqlalchemy import create_engine
from model import *

# create database connection
basedir = os.path.abspath(os.path.dirname(__file__))
# The object created by sqlite by default can only be used by the thread that created the object
# , and sqlalchemy is multi-threaded, so we need to specify check_same_thread=False to make
#  the created object available to any thread
print(os.path.join(basedir, 'app_package.db'))
engine = create_engine('sqlite:///' + os.path.join(basedir, 'app_package.db') + '?check_same_thread=False', echo=True)

# Create File and initialize databases
Base.metadata.create_all(engine, checkfirst=True)

from sqlalchemy.orm import sessionmaker
# engine是2.2中创建的连接
Session = sessionmaker(bind=engine)

def assign_value_to_user_default_path_instance(instance, user_id, test_indicator, task_id, training_file_path, id_column, data_column, target_column, task_name, task_description):

    if test_indicator == "train":
        instance.user_id = user_id
        instance.test_indicator = test_indicator
        instance.task_id = task_id
        instance.training_file_path = training_file_path
        instance.id_column = id_column
        instance.data_column = data_column
        instance.target_column = target_column
        instance.task_name = task_name
        instance.task_description = task_description

    elif test_indicator == "test":


    return instance


def assign_value_to_user_chosen_path_instance():

    return


def assign_value_to_user_pending_page_instance():
    return