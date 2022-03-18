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

class mongoDB():

    @classmethod
    def search_user_document(cls, user_id, username=None):
        if user_id:
            return pyMongo.db.User.find_one({'user_id': user_id})
        elif username:
            return pyMongo.db.User.find_one({'username': username})

    @classmethod
    def create_user_document(cls, user_id):
        pending_document = {
            'user_id': user_id,
            'task_dict': {}
        }
        return pyMongo.db.Pending.insert_one(pending_document)
    
    @classmethod
    def update_user_document(cls, user_id):
        pending_document = {
            'user_id': user_id,
            'task_dict': {}
        }
        return pyMongo.db.Pending.insert_one(pending_document)

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

        return pyMongo.db.Pending.update_one({'user_id': user_id}, {'$set':{'task_dict.' + id: test_indicator}})
    
    @classmethod
    def delete_pending_document_field(cls, user_id, id):
        return pyMongo.db.Pending.update_one({'user_id': user_id}, {'$unset':{'task_dict.' + id: ""}})
    
    @classmethod
    def create_stop_document(cls, task_id, cur_rounds_num, assistor_situation_don):

        pass


class train_mongoDB():

    @classmethod
    def update_notification_document(cls, user_id, notification_name, task_id, sender_random_id, role, cur_rounds_num):
        if pyMongo.db.Notification.find_one({'user_id': user_id}) == None:
            pyMongo.db.Notification.insert_one({'user_id': user_id})

        base_key = 'category' + '.' + notification_name + '.' + 'task_id_dict' + '.' + task_id 
        # print('base_key', base_key)
        return pyMongo.db.Notification.update_one({'user_id': user_id}, {'$set':{
            base_key + '.sender_random_id': sender_random_id,
            base_key + '.role': role,
            base_key + '.cur_rounds_num': cur_rounds_num,
        }})
    
    @classmethod
    def search_train_message_document(cls, task_id):
        return  pyMongo.db.Train_Message.find_one({'task_id': task_id})
        
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

    @classmethod
    def search_train_message_situation_document(cls, situation_id):
        return pyMongo.db.Train_Message_Situation.find_one({'situation_id': situation_id})

    @classmethod
    def create_train_message_situation_document(cls, situation_id, sender_id, sender_random_id, recipient_id, situation_content):
        train_message_situation_document = {
            'situation_id': situation_id,
            'sender_id': sender_id,
            'sender_random_id': sender_random_id,
            'recipient_id': recipient_id,
            'situation_content': situation_content
        }
        return pyMongo.db.Train_Message_Situation.insert_one(train_message_situation_document)
    
    @classmethod
    def search_train_message_output_document(cls, output_id):
        return pyMongo.db.Train_Message_Output.find_one({'output_id': output_id})

    @classmethod
    def create_train_message_output_document(cls, output_id, sender_id, sender_random_id, recipient_id, output_content):
        train_message_output_document = {
            'output_id': output_id,
            'sender_id': sender_id,
            'sender_random_id': sender_random_id,
            'recipient_id': recipient_id,
            'output_content': output_content
        }
        return pyMongo.db.Train_Message_Output.insert_one(train_message_output_document)

    @classmethod
    def search_train_match_document(cls, task_id):
        return pyMongo.db.Train_Match.find_one({'task_id': task_id})

    @classmethod
    def sponsor_create_train_match_document(cls, task_id, total_assistor_num, sponsor_id, 
                           sponsor_random_id, identifier_id):
        train_match_document = {
            "task_id": task_id,
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
        return pyMongo.db.Train_Match.insert_one(train_match_document)
    
    @classmethod
    def assistor_update_train_match_document(cls, task_id, assistor_id, assistor_random_id, 
                                       identifier_id):
        base_key = 'assistor_information' + '.' + assistor_id 
        return pyMongo.db.Train_Match.update_one({'task_id': task_id}, {'$set':{
            base_key + '.assistor_id_to_random_id': assistor_random_id,
            base_key + '.identifier_id': identifier_id,
            'asssistor_random_id_mapping.' + assistor_random_id: assistor_id,
        }})

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
        

class test_mongoDB():

    @classmethod
    def update_notification_document(cls, user_id, notification_name, test_id, sender_random_id, role, cur_rounds_num):
        if not isinstance(user_id, str):
            return False
        elif not isinstance(notification_name, str):
            return False
        elif test_id and not isinstance(test_id, str):
            return False
        elif not isinstance(sender_random_id, str):
            return False
        elif not isinstance(role, str):
            return False
        elif not isinstance(cur_rounds_num, int):
            return False
        
        if pyMongo.db.Notification.find_one({'user_id': user_id}) == None:
            pyMongo.db.Notification.insert_one({'user_id': user_id})

        base_key = 'category' + '.' + notification_name + '.' + 'test_id_dict' + '.' + test_id 
        return pyMongo.db.Notification.update_one({'user_id': user_id}, {'$set':{
            base_key + '.sender_random_id': sender_random_id,
            base_key + '.role': role,
            base_key + '.cur_rounds_num': cur_rounds_num,
        }})
    
    @classmethod
    def search_test_message_document(cls, test_id):
        return  pyMongo.db.Test_Message.find_one({'test_id': test_id})
        
    @classmethod
    def create_train_message_document(cls, test_id, cur_rounds_num, situation_dict):
        train_message_document = {
            'test_id': test_id,
            'cur_rounds_num': cur_rounds_num,
            'rounds_' + str(cur_rounds_num): {
                'situation_dict': situation_dict,
                'output_dict': {},
            },
        }
        return pyMongo.db.Test_Message.insert_one(train_message_document)

    @classmethod
    def search_test_message_situation_document(cls, situation_id):
        return pyMongo.db.Test_Message_Situation.find_one({'situation_id': situation_id})

    @classmethod
    def create_test_message_situation_document(cls, situation_id, sender_id, sender_random_id, recipient_id, situation_content):
        test_message_situation_document = {
            'situation_id': situation_id,
            'sender_id': sender_id,
            'sender_random_id': sender_random_id,
            'recipient_id': recipient_id,
            'situation_content': situation_content
        }
        return pyMongo.db.Test_Message_Situation.insert_one(test_message_situation_document)
    
    @classmethod
    def search_test_message_output_document(cls, output_id):
        return pyMongo.db.Test_Message_Output.find_one({'output_id': output_id})

    @classmethod
    def create_test_message_output_document(cls, output_id, sender_id, sender_random_id, recipient_id, output_content):
        test_message_output_document = {
            'output_id': output_id,
            'sender_id': sender_id,
            'sender_random_id': sender_random_id,
            'recipient_id': recipient_id,
            'output_content': output_content
        }
        return pyMongo.db.Test_Message_Output.insert_one(test_message_output_document)

    @classmethod
    def search_test_match_document(cls, test_id):
        return pyMongo.db.Test_Match.find_one({'test_id': test_id})

    @classmethod
    def sponsor_create_test_match_document(cls, test_id, task_id, total_assistor_num, sponsor_id, 
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
    def search_test_match_identifier_document(cls, identifier_id):
        return pyMongo.db.Test_Match_Identifier.find_one({'identifier_id': identifier_id})

    @classmethod
    def create_test_match_identifier_document(cls, identifier_id, identifier_content):
        test_match_identifier_document = {
            'identifier_id': identifier_id,
            'identifier_content': identifier_content,
        }
        return pyMongo.db.Test_Match_Identifier.insert_one(test_match_identifier_document)

    @classmethod
    def search_test_task_document(cls, test_id):
        return pyMongo.db.Test_Task.find_one({'test_id': test_id})

    @classmethod
    def create_test_task_document(cls, test_id, task_id, test_name, test_description, task_mode, 
                          model_name, metric_name, sponsor_id, assistor_id_list):
        test_task_document = {
            'test_id': test_id,
            "task_id": task_id,
            "test_name": test_name,
            "test_description": test_description,
            "task_mode": task_mode,
            "model_name": model_name,
            "metric_name": metric_name,
            "sponsor_id": sponsor_id,
            "assistor_id_list": assistor_id_list,
        }
        return pyMongo.db.Test_Task.insert_one(test_task_document)
        
    # @classmethod
    # def update_test_task_document_test_task_list(cls, task_id, test_id):
    #     return pyMongo.db.Train_Task.update_one({'task_id': task_id}, {'$push':{
    #                'test_task_list': test_id,
    #            }})










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
    
    


