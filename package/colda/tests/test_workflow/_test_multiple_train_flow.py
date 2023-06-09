"""
tests.test_curves.py
~~~~~~~~~~~~~~~~~~~~

Test suite for the curves.py module that handles everything to do with
supply and demand curves.
"""
import json
from typing import Any, Dict, List
import requests
from copy import deepcopy
from . import set_default_data_path
from . import testing_data
from .Train_helper_function import Train_helper_function

import pytest

class Test_unread_request(Train_helper_function):

    def test_unread_request(self):
        
        self.first_user_login()
        self.clean_db()
        self.handleTrainRequest_helper()

        # unread_request
        self.second_user_login()
        set_default_data_path(default_mode=testing_data['default_mode'], default_task_mode=testing_data['default_task_mode'], default_model_name=testing_data['default_model_name'], default_file_path=testing_data['default_file_path'],
                            default_id_column=testing_data['default_id_column'], default_data_column=testing_data['default_data_column'])
        update_all_notifications_data = self.start_Collaboration()
        print('5555', update_all_notifications_data)
        print('fff', update_all_notifications_data['unread request'])
        assert "unread request" in update_all_notifications_data.keys()
        self.unread_request_helper(update_all_notifications_data["unread request"])
        
        # unread_match_identifier_assistor
        self.second_user_login()
        set_default_data_path(default_mode=testing_data['default_mode'], default_task_mode=testing_data['default_task_mode'], default_model_name=testing_data['default_model_name'], default_file_path=testing_data['default_file_path'],
                            default_id_column=testing_data['default_id_column'], default_data_column=testing_data['default_data_column'])
        update_all_notifications_data = self.start_Collaboration()
        assert "unread match id" in update_all_notifications_data.keys()
        self.unread_match_identifier_assistor_helper(update_all_notifications_data["unread match id"])

        # unread_match_identifier_sponsor
        self.first_user_login()
        update_all_notifications_data = self.start_Collaboration()
        assert "unread match id" in update_all_notifications_data
        self.unread_match_identifier_sponsor_helper(update_all_notifications_data["unread match id"])

        # unread_sponsor_situation
        for i in range(testing_data['max_round']):
            self.first_user_login()
            update_all_notifications_data = self.start_Collaboration()
            assert "unread situation" in update_all_notifications_data
            self.unread_situation_sponsor_helper(update_all_notifications_data["unread situation"])

            # unread_assistor_situation
            self.second_user_login()
            set_default_data_path(default_mode=testing_data['default_mode'], default_task_mode=testing_data['default_task_mode'], default_model_name=testing_data['default_model_name'], default_file_path=testing_data['default_file_path'],
                                default_id_column=testing_data['default_id_column'], default_data_column=testing_data['default_data_column'])
            update_all_notifications_data = self.start_Collaboration()
            assert "unread situation" in update_all_notifications_data
            self.unread_situation_assistor_helper(update_all_notifications_data["unread situation"])

            # unread_output
            self.first_user_login()
            update_all_notifications_data = self.start_Collaboration()
            assert "unread output" in update_all_notifications_data
            self.unread_output(update_all_notifications_data["unread output"])


