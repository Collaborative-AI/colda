"""
tests.test_curves.py
~~~~~~~~~~~~~~~~~~~~

Test suite for the curves.py module that handles everything to do with
supply and demand curves.
"""
import json
import requests
from typing import Any, Dict, List
from copy import deepcopy
from . import testing_data
from . import _default_trainRequest
from . import _default_authorization
from . import _default_get_notification
from . import _default_PersonalInformation
from . import _default_Network

import pytest

class Train_helper_function:

    def clean_db(self):
        base_url = _default_Network.get_base_url()
        url = base_url + "/delete_all_rows/"
        try:
            delete_db_res = requests.get(url)
        except RuntimeError:
            print('delete_db_res wrong')
        

    def first_user_login(self):
        userLogin_res = _default_authorization.userLogin(username=testing_data['first_user_username'], password=testing_data['first_user_password'])
        assert userLogin_res == 'userLogin Successfully'
        return
    
    def second_user_login(self):
        userLogin_res = _default_authorization.userLogin(username=testing_data['second_user_username'], password=testing_data['second_user_password'])
        assert userLogin_res == 'userLogin Successfully'
        return

    def get_Notification(self):
        return _default_get_notification.getNotification()

    def handleTrainRequest_helper(self):
        
        handleTrainRequest_res = _default_trainRequest.handleTrainRequest(maxRound=testing_data['maxRound'], assistors=testing_data['assistors'], train_file_path=testing_data['train_file_path'],
                             train_id_column=testing_data['train_id_column'], train_data_column=testing_data['train_data_column'], train_target_column=testing_data['train_target_column'], 
                             task_mode= testing_data['task_mode'], model_name=testing_data['model_name'], metric_name=testing_data['metric_name'], 
                             task_name=testing_data['task_name'], task_description=testing_data['task_description'])
        assert handleTrainRequest_res == 'handleTrainRequest successfully'
    
    def unread_request_helper(self, unread_request_notification):
        unread_request_res = _default_trainRequest.unread_request(unread_request_notification)
        assert unread_request_res == 'unread_request successfully'

    def unread_match_id_sponsor_helper(self, unread_match_id_notification):
        unread_match_id_sponsor_res = _default_trainRequest.unread_match_id(unread_match_id_notification)   
        assert unread_match_id_sponsor_res == 'unread match id done'
    
    def unread_match_id_assistor_helper(self, unread_match_id_notification):
        unread_match_id_assistor_res = _default_trainRequest.unread_match_id(unread_match_id_notification)   
        print('unread_match_id_assistor_res', unread_match_id_assistor_res)
        assert unread_match_id_assistor_res == 'unread match id done'
    
    def unread_situation_sponsor_helper(self, unread_situation_notification):
        unread_situation_sponsor_res = _default_trainRequest.unread_situation(unread_situation_notification)   
        assert unread_situation_sponsor_res == 'unread situation done'
    
    def unread_situation_assistor_helper(self, unread_situation_notification):
        unread_situation_assistor_res = _default_trainRequest.unread_situation(unread_situation_notification)   
        assert unread_situation_assistor_res == 'unread situation done'
    
    def unread_output(self, unread_output_notification):
        unread_output_res = _default_trainRequest.unread_output(unread_output_notification)   
        assert unread_output_res == 'unread output done'