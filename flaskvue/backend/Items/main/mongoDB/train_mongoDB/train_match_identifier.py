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

class train_match_identifier():

    @classmethod
    def search_train_match_identifier_document(cls, identifier_id):
        return pyMongo.db.Train_Match_Identifier.find_one({'identifier_id': identifier_id})

    @classmethod
    def create_train_match_identifier_document(cls, identifier_id, identifier_content):
        train_match_identifier_document = {
            'identifier_id': identifier_id,
            'identifier_content': identifier_content,
        }
        return pyMongo.db.Train_Match_Identifier.insert_one(train_match_identifier_document)