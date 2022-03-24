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

class test_match:

    @classmethod
    def search_test_match_document(cls, test_id):
        return pyMongo.db.Test_Match.find_one({'test_id': test_id})
        
    @classmethod
    def create_test_match_document(cls, test_id, task_id, total_assistor_num, sponsor_id, 
                           sponsor_random_id, identifier_id):
        test_match_document = {
            'test_id': test_id,
            'task_id': task_id,
            'total_assistor_num': total_assistor_num,
            'sponsor_information': {
                "sponsor_id": sponsor_id,
                sponsor_id: {
                    'sponsor_id_to_random_id': sponsor_random_id,
                    'identifier_id': identifier_id
                }
            },
            'sponsor_random_id_mapping':{
                sponsor_random_id: sponsor_id
            },
            'assistor_information': {},
            'assistor_random_id_mapping': {},
            'sponsor_terminate_id_dict': {},
            'assistor_terminate_id_dict': {},
        }
        return pyMongo.db.Test_Match.insert_one(test_match_document)
    
    @classmethod
    def assistor_update_test_match_document(cls, test_id, assistor_id, assistor_random_id, 
                                       identifier_id):
        base_key = 'assistor_information' + '.' + assistor_id 
        return pyMongo.db.Test_Match.update_one({'test_id': test_id}, {'$set':{
            base_key + '.assistor_id_to_random_id': assistor_random_id,
            base_key + '.identifier_id': identifier_id,
            'asssistor_random_id_mapping.' + assistor_random_id: assistor_id,
        }})

    @classmethod
    def update_user_stop_in_test_match_document(cls, test_id, user_id, role):
        if role == 'sponsor':
            return pyMongo.db.Test_Match.update_one({'test_id': test_id}, {'$set':{
                'sponsor_terminate_id_dict.' + user_id: 'terminate',
            }})
        elif role == 'assistor':
            return pyMongo.db.Test_Match.update_one({'test_id': test_id}, {'$set':{
                'assistor_terminate_id_dict.' + user_id: 'terminate',
            }})