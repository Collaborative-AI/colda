import errno
import os
import re
import jwt
import uuid

from config import Config
from flask import current_app, g
from flask_mail import Message
from datetime import datetime, timedelta
from typing import List
from abc import ABC, abstractmethod

from Items import pyMongo

from pymongo.errors import (
    BulkWriteError,
    DocumentTooLarge
)


class train_match():
    
    @classmethod
    def search_train_match_document(cls, train_id):
        return pyMongo.db.Train_Match.find_one({'train_id': train_id})

    @classmethod
    def create_train_match_document(
        cls, 
        train_id, 
        total_assistor_num, 
        sponsor_id, 
        sponsor_random_id, 
        identifier_id
    ):
    
        train_match_document = {
            "train_id": train_id,
            'total_assistor_num': total_assistor_num,
            "sponsor_information": {
                "sponsor_id": sponsor_id,
                sponsor_id: {
                    "sponsor_id_to_random_id": sponsor_random_id,
                    'identifier_id': identifier_id
                }
            },
            "sponsor_random_id_mapping":{
                sponsor_random_id: sponsor_id
            },
            "assistor_information": {},
            "assistor_random_id_mapping": {},
            'sponsor_terminate_id_dict': {},
            'assistor_terminate_id_dict': {},
        }

        # print('zhezhezhezhe')
        # try:
        #     pyMongo.db.Train_Match.insert_one(train_match_document)
        # except DocumentTooLarge as err:
        #     raise DocumentTooLarge('cuolege')

        return pyMongo.db.Train_Match.insert_one(train_match_document)
    
    @classmethod
    def assistor_update_train_match_document(cls, train_id, assistor_id, assistor_random_id, 
                                       identifier_id):

        base_key = f'assistor_information.{assistor_id}'
        return pyMongo.db.Train_Match.update_one({'train_id': train_id}, {'$set':{
            f'{base_key}.assistor_id_to_random_id': assistor_random_id,
            f'{base_key}.identifier_id': identifier_id,
            f'assistor_random_id_mapping.{assistor_random_id}': assistor_id,
        }})

    @classmethod
    def update_user_stop_in_train_match_document(cls, train_id, user_id, role):
        if role == 'sponsor':
            return pyMongo.db.Train_Match.update_one({'train_id': train_id}, {'$set':{
                f'sponsor_terminate_id_dict.{user_id}': 'terminate'
            }})
        elif role == 'assistor':
            return pyMongo.db.Train_Match.update_one({'train_id': train_id}, {'$set':{
                f'assistor_terminate_id_dict.{user_id}': 'terminate'
            }})

