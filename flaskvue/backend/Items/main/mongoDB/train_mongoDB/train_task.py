import errno
import os
import re
import jwt
import uuid

from setting import Config
from flask import current_app, g
from flask_mail import Message
from datetime import datetime, timedelta
from typing import List
from abc import ABC, abstractmethod

from Items import pyMongo

class train_task():

    @classmethod
    def search_train_task_document(cls, task_id):
        return pyMongo.db.Train_Task.find_one({'task_id': task_id})

    @classmethod
    def create_train_task_document(cls, task_id, task_name, task_description, task_mode, 
                          model_name, metric_name, sponsor_id, assistor_id_list,
                          test_task_list):
        train_task_document = {
            "task_id": task_id,
            "task_name": task_name,
            "task_description": task_description,
            "task_mode": task_mode,
            "model_name": model_name,
            "metric_name": metric_name,
            "sponsor_id": sponsor_id,
            "assistor_id_list": assistor_id_list,
            "test_task_list": test_task_list,
        }
        return pyMongo.db.Train_Task.insert_one(train_task_document)
        
    @classmethod
    def update_train_task_document_test_task_list(cls, task_id, test_id):
        return pyMongo.db.Train_Task.update_one({'task_id': task_id}, {'$push':{
                   'test_task_list': test_id,
               }})