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

from test_mongoDB import test_match
from test_mongoDB import test_match_identifier
from test_mongoDB import test_message
from test_mongoDB import test_message_output
from test_mongoDB import test_task

from train_mongoDB import train_match
from train_mongoDB import train_match_identifier
from train_mongoDB import train_message
from train_mongoDB import train_message_situation
from train_mongoDB import train_message_output
from train_mongoDB import train_task

class mongoDB():

    @classmethod
    def update_notification_document(cls, user_id, notification_name, id, sender_random_id, role, cur_rounds_num, test_indicator):
        if not isinstance(user_id, str):
            return False
        elif not isinstance(notification_name, str):
            return False
        elif id and not isinstance(id, str):
            return False
        elif not isinstance(sender_random_id, str):
            return False
        elif not isinstance(role, str):
            return False
        elif not isinstance(cur_rounds_num, int):
            return False
        elif not isinstance(test_indicator, str):
            return False
        
        if pyMongo.db.Notification.find_one({'user_id': user_id}) == None:
            pyMongo.db.Notification.insert_one({'user_id': user_id})

        if test_indicator == 'train':
            base_key = 'category' + '.' + notification_name + '.' + 'train_id_dict' + '.' + id 
        elif test_indicator == 'test':
            base_key = 'category' + '.' + notification_name + '.' + 'test_id_dict' + '.' + id 

        return pyMongo.db.Notification.update_one({'user_id': user_id}, {'$set':{
            base_key + '.sender_random_id': sender_random_id,
            base_key + '.role': role,
            base_key + '.cur_rounds_num': cur_rounds_num,
        }})
        
    @classmethod
    def search_user_document(cls, user_id, username, email, key_indicator):
        if key_indicator == 'user_id':
            return pyMongo.db.User.find_one({'user_id': user_id})
        elif key_indicator == 'username':
            return pyMongo.db.User.find_one({'username': username})
        elif key_indicator == 'email':
            return pyMongo.db.User.find_one({'email': email})


    @classmethod
    def create_user_document(cls, user_id):
        pending_document = {
            'user_id': user_id,
            'task_dict': {}
        }
        return pyMongo.db.Pending.insert_one(pending_document)
    
    @classmethod
    def update_user_document(cls, user_id):
        pass

    @classmethod
    def search_pending_document(cls, user_id):
        return pyMongo.db.Pending.find_one({'user_id': user_id})
    
    @classmethod
    def create_pending_document(cls, user_id):
        pending_document = {
            'user_id': user_id,
            'task_dict': {}
        }
        return pyMongo.db.Pending.insert_one(pending_document)

    @classmethod
    def update_pending_document(cls, user_id, id, test_indicator):
        if cls.search_pending_document(user_id) == None:
            cls.create_pending_document(user_id)

        return pyMongo.db.Pending.update_one({'user_id': user_id}, {'$set':{
            'task_dict.' + id: test_indicator
        }})
    
    @classmethod
    def delete_pending_document_field(cls, user_id, id):
        return pyMongo.db.Pending.update_one({'user_id': user_id}, {'$unset':{
            'task_dict.' + id: ""
        }})
    
    @classmethod
    def create_stop_document(cls, task_id, cur_rounds_num, assistor_situation_don):
        pass

    
    




    # class Strategy(ABC):
#     """
#     The Strategy interface declares operations common to all supported versions
#     of some algorithm.

#     The Context uses this interface to call the algorithm defined by Concrete
#     Strategies.
#     """

#     @classmethod
#     @abstractmethod
#     def add_notification_document(cls):
#         pass
      
#     @classmethod
#     @abstractmethod
#     def create_pending_document(cls):
#         pass
    
#     @classmethod
#     @abstractmethod
#     def create_stop_document(cls):
#         pass
    
#     @classmethod
#     @abstractmethod
#     def add_message_document(cls):
#         pass
    
#     @classmethod
#     @abstractmethod
#     def add_message_situation_document(cls):
#         pass
    
#     @classmethod
#     @abstractmethod
#     def add_message_output_document(cls):
#         pass
    
#     @classmethod
#     @abstractmethod
#     def add_match_document(cls):
#         pass

#     @classmethod
#     @abstractmethod
#     def add_match_file_document(cls):
#         pass
    
#     @classmethod
#     @abstractmethod
#     def add_task_document(cls):
#         pass




# class mongoDB_strategy_interface():
#     """
#     The Context defines the interface of interest to clients.
#     """

#     def __init__(self) -> None:
#         self._mongoDB_strategy = None

#     @property
#     def mongoDB_strategy(self) -> Strategy:
#         """
#         The Context maintains a reference to one of the Strategy objects. The
#         Context does not know the concrete class of a strategy. It should work
#         with all strategies via the Strategy interface.
#         """

#         return self._mongoDB_strategy

#     @mongoDB_strategy.setter
#     def mongoDB_strategy(self, mongoDB_strategy: Strategy) -> None:
#         """
#         Usually, the Context allows replacing a Strategy object at runtime.
#         """

#         self._mongoDB_strategy = mongoDB_strategy

#     def add_user(self):
#         return

#     def add_notification_document(self, user_id, notification_name, task_id, test_id, 
#                                   sender_random_id, role, cur_rounds_num):
#         if not isinstance(user_id, str):
#             return False
#         elif not isinstance(notification_name, str):
#             return False
#         elif task_id and not isinstance(task_id, str):
#             return False
#         elif test_id and not isinstance(test_id, str):
#             return False
#         elif not isinstance(sender_random_id, str):
#             return False
#         elif not isinstance(role, str):
#             return False
#         elif not isinstance(cur_rounds_num, int):
#             return False
#         # cant send to task_id and test_id together
#         elif task_id and test_id:
#             return False
        
#         return self._mongoDB_strategy.add_notification_document(user_id, notification_name, task_id, test_id, 
#                                                                 sender_random_id, role, cur_rounds_num)
    
#     def create_pending_document(self):
#         pass
    
#     def create_stop_document(self):
#         pass
    
#     def add_message_document(self):
#         pass

#     def add_message_situation_document(self):
#         pass
    
#     def add_message_output_document(self):
#         pass
    
#     def add_match_file_document(self, user_id, notification_name, task_id, test_id, 
#                                 sender_random_id, role, cur_rounds_num):

#         return self._mongoDB_strategy.add_match_file_document(user_id, notification_name, task_id, test_id, 
#                                                               sender_random_id, role, cur_rounds_num)
        
  
#     def add_task_document(self, user_id, notification_name, task_id, test_id, 
#                                 sender_random_id, role, cur_rounds_num):
                              
#         return self._mongoDB_strategy.add_match_file_document(user_id, notification_name, task_id, test_id, 
#                                                               sender_random_id, role, cur_rounds_num)
    
    


