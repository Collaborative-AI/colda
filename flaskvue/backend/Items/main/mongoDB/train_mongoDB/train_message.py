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

class train_message():

    @classmethod
    def search_train_message_document(cls, task_id):
        return pyMongo.db.Train_Message.find_one({'task_id': task_id})
        
    @classmethod
    def create_train_message_document(cls, task_id, cur_rounds_num, situation_dict):
        train_message_document = {
            'task_id': task_id,
            'cur_rounds_num': cur_rounds_num,
            'rounds_' + str(cur_rounds_num): {
                'situation_dict': situation_dict,
                'output_dict': {},
            },
        }
        return pyMongo.db.Train_Message.insert_one(train_message_document)