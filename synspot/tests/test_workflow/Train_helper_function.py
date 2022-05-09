"""
tests.test_curves.py
~~~~~~~~~~~~~~~~~~~~

Test suite for the curves.py module that handles everything to do with
supply and demand curves.
"""
import json
import pytest
import requests

from typing import (
    Any, 
    Dict, 
    List
)
from copy import deepcopy

from synspot.tests.test_workflow import testing_data
from synspot.tests.test_workflow import _default_trainMainWorkflow
from synspot.tests.test_workflow import _default_authorization
from synspot.tests.test_workflow import _default_getNotification
from synspot.tests.test_workflow import _default_PI
from synspot.tests.test_workflow import _default_Network


class Train_helper_function:

    def clean_db(self):
        base_url = _default_Network.base_url
        url = base_url + "/delete_all_rows/"
        try:
            delete_db_res = requests.get(url)
        except:
            print('delete_db_res wrong')
        
    def first_user_login(self):
        userLogin_res = _default_authorization.userLogin(
            username=testing_data['first_user_username'], 
            password=testing_data['first_user_password']
        )
        assert userLogin_res == True
        return
    
    def second_user_login(self):
        userLogin_res = _default_authorization.userLogin(
            username=testing_data['second_user_username'], 
            password=testing_data['second_user_password']
        )
        assert userLogin_res == True
        return

    def get_notification(self):
        return _default_getNotification.start_Collaboration()

    def find_assistor(self):
        find_assistor_res = _default_trainMainWorkflow.find_assistor(
            maxRound=testing_data['maxRound'], 
            assistors=testing_data['assistors'], 
            train_file_path=testing_data['train_file_path'],
            train_id_column=testing_data['train_id_column'], 
            train_data_column=testing_data['train_data_column'], 
            train_target_column=testing_data['train_target_column'], 
            task_mode= testing_data['task_mode'], 
            model_name=testing_data['model_name'], 
            metric_name=testing_data['metric_name'], 
            task_name=testing_data['task_name'], 
            task_description=testing_data['task_description']
        )
        assert find_assistor_res[0] == True
        return find_assistor_res[1]
        
    def train_assistor_request(self, notification_category):
        train_assistor_request = _default_trainMainWorkflow.train_assistor_request(notification_category['unread_request']['train_id_dicts'])
        assert train_assistor_request == True

    def train_sponsor_match_identifier(self, notification_category):
        train_sponsor_match_identifier = _default_trainMainWorkflow.train_match_identifier(notification_category['unread_match_identifier']['train_id_dicts'])   
        assert train_sponsor_match_identifier == True
    
    def train_assistor_match_identifier(self, notification_category):
        train_assistor_match_identifier = _default_trainMainWorkflow.train_match_identifier(notification_category['unread_match_identifier']['train_id_dicts'])   
        print('train_assistor_match_identifier', train_assistor_match_identifier)
        assert train_assistor_match_identifier == True
    
    def train_sponsor_situation(self, notification_category):
        train_sponsor_situation = _default_trainMainWorkflow.train_situation(notification_category['unread_situation']['train_id_dicts'])   
        assert train_sponsor_situation == True
    
    def train_assistor_situation(self, notification_category):
        train_assistor_situation = _default_trainMainWorkflow.train_situation(notification_category['unread_situation']['train_id_dicts'])   
        assert train_assistor_situation == True
    
    def train_output(self, notification_category):
        train_output = _default_trainMainWorkflow.train_output(notification_category['unread_output']['train_id_dicts'])   
        assert train_output == True