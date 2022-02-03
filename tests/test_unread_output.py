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
from .Test_helper_function import Test_helper_function

import pytest

class Test_unread_test_match_id(Train_helper_function, Test_helper_function):

    def test_unread_test_match_id(self):
        
        self.first_user_login()
        self.clean_db()
        task_id = self.handleTrainRequest_helper()

        # unread_request
        self.second_user_login()
        set_default_data_path(default_mode=testing_data['default_mode'], default_task_mode=testing_data['default_task_mode'], default_model_name=testing_data['default_model_name'], default_file_path=testing_data['default_file_path'],
                            default_id_column=testing_data['default_id_column'], default_data_column=testing_data['default_data_column'])
        update_all_notifications_data = self.get_Notification()
        print('5555', update_all_notifications_data)
        print('fff', update_all_notifications_data['unread request'])
        assert "unread request" in update_all_notifications_data.keys()
        self.unread_request_helper(update_all_notifications_data["unread request"])
        
        # unread_match_id_assistor
        self.second_user_login()
        set_default_data_path(default_mode=testing_data['default_mode'], default_task_mode=testing_data['default_task_mode'], default_model_name=testing_data['default_model_name'], default_file_path=testing_data['default_file_path'],
                            default_id_column=testing_data['default_id_column'], default_data_column=testing_data['default_data_column'])
        update_all_notifications_data = self.get_Notification()
        assert "unread match id" in update_all_notifications_data.keys()
        self.unread_match_id_assistor_helper(update_all_notifications_data["unread match id"])

        # unread_match_id_sponsor
        self.first_user_login()
        update_all_notifications_data = self.get_Notification()
        assert "unread match id" in update_all_notifications_data
        self.unread_match_id_sponsor_helper(update_all_notifications_data["unread match id"])

        # unread_sponsor_situation
        for i in range(1):
            self.first_user_login()
            update_all_notifications_data = self.get_Notification()
            assert "unread situation" in update_all_notifications_data
            self.unread_situation_sponsor_helper(update_all_notifications_data["unread situation"])

            # unread_assistor_situation
            self.second_user_login()
            set_default_data_path(default_mode=testing_data['default_mode'], default_task_mode=testing_data['default_task_mode'], default_model_name=testing_data['default_model_name'], default_file_path=testing_data['default_file_path'],
                                default_id_column=testing_data['default_id_column'], default_data_column=testing_data['default_data_column'])
            update_all_notifications_data = self.get_Notification()
            assert "unread situation" in update_all_notifications_data
            self.unread_situation_assistor_helper(update_all_notifications_data["unread situation"])

            # unread_output
            self.first_user_login()
            update_all_notifications_data = self.get_Notification()
            assert "unread output" in update_all_notifications_data
            self.unread_output(update_all_notifications_data["unread output"])

        # test stage
        self.first_user_login()
        self.handleTestRequest_helper(task_id)

        # unread_test_request
        self.second_user_login()
        set_default_data_path(default_mode=testing_data['default_mode'], default_task_mode=testing_data['default_task_mode'], default_model_name=testing_data['default_model_name'], default_file_path=testing_data['default_file_path'],
                            default_id_column=testing_data['default_id_column'], default_data_column=testing_data['default_data_column'])
        update_all_notifications_data = self.get_Notification()
        assert "unread test request" in update_all_notifications_data.keys()
        self.unread_test_request_helper(update_all_notifications_data["unread test request"])

        # unread_test_match_id_sponsor
        self.first_user_login()
        update_all_notifications_data = self.get_Notification()
        assert "unread test match id" in update_all_notifications_data.keys()
        self.unread_test_match_id_sponsor_helper(update_all_notifications_data["unread test match id"])

        # unread_test_match_id_assistor
        self.second_user_login()
        set_default_data_path(default_mode=testing_data['default_mode'], default_task_mode=testing_data['default_task_mode'], default_model_name=testing_data['default_model_name'], default_file_path=testing_data['default_file_path'],
                            default_id_column=testing_data['default_id_column'], default_data_column=testing_data['default_data_column'])
        update_all_notifications_data = self.get_Notification()
        assert "unread test match id" in update_all_notifications_data.keys()
        self.unread_test_match_id_assistor_helper(update_all_notifications_data["unread test match id"])

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
from .Test_helper_function import Test_helper_function

import pytest

class Test_unread_test_output(Train_helper_function, Test_helper_function):

    def test_unread_test_output(self):
        
        self.first_user_login()
        self.clean_db()
        task_id = self.handleTrainRequest_helper()

        # unread_request
        self.second_user_login()
        set_default_data_path(default_mode=testing_data['default_mode'], default_task_mode=testing_data['default_task_mode'], default_model_name=testing_data['default_model_name'], default_file_path=testing_data['default_file_path'],
                            default_id_column=testing_data['default_id_column'], default_data_column=testing_data['default_data_column'])
        update_all_notifications_data = self.get_Notification()
        print('5555', update_all_notifications_data)
        print('fff', update_all_notifications_data['unread request'])
        assert "unread request" in update_all_notifications_data.keys()
        self.unread_request_helper(update_all_notifications_data["unread request"])
        
        # unread_match_id_assistor
        self.second_user_login()
        set_default_data_path(default_mode=testing_data['default_mode'], default_task_mode=testing_data['default_task_mode'], default_model_name=testing_data['default_model_name'], default_file_path=testing_data['default_file_path'],
                            default_id_column=testing_data['default_id_column'], default_data_column=testing_data['default_data_column'])
        update_all_notifications_data = self.get_Notification()
        assert "unread match id" in update_all_notifications_data.keys()
        self.unread_match_id_assistor_helper(update_all_notifications_data["unread match id"])

        # unread_match_id_sponsor
        self.first_user_login()
        update_all_notifications_data = self.get_Notification()
        assert "unread match id" in update_all_notifications_data
        self.unread_match_id_sponsor_helper(update_all_notifications_data["unread match id"])
        
        for i in range(1):
            # unread_sponsor_situation
            self.first_user_login()
            update_all_notifications_data = self.get_Notification()
            assert "unread situation" in update_all_notifications_data
            self.unread_situation_sponsor_helper(update_all_notifications_data["unread situation"])

            # unread_assistor_situation
            self.second_user_login()
            set_default_data_path(default_mode=testing_data['default_mode'], default_task_mode=testing_data['default_task_mode'], default_model_name=testing_data['default_model_name'], default_file_path=testing_data['default_file_path'],
                                default_id_column=testing_data['default_id_column'], default_data_column=testing_data['default_data_column'])
            update_all_notifications_data = self.get_Notification()
            assert "unread situation" in update_all_notifications_data
            self.unread_situation_assistor_helper(update_all_notifications_data["unread situation"])

            # unread_output
            self.first_user_login()
            update_all_notifications_data = self.get_Notification()
            assert "unread output" in update_all_notifications_data
            self.unread_output(update_all_notifications_data["unread output"])

        # test stage
        self.first_user_login()
        self.handleTestRequest_helper(task_id)

        # unread_test_request
        self.second_user_login()
        set_default_data_path(default_mode=testing_data['default_mode'], default_task_mode=testing_data['default_task_mode'], default_model_name=testing_data['default_model_name'], default_file_path=testing_data['default_file_path'],
                            default_id_column=testing_data['default_id_column'], default_data_column=testing_data['default_data_column'])
        update_all_notifications_data = self.get_Notification()
        assert "unread test request" in update_all_notifications_data.keys()
        self.unread_test_request_helper(update_all_notifications_data["unread test request"])

        # unread_test_match_id_sponsor
        self.first_user_login()
        update_all_notifications_data = self.get_Notification()
        assert "unread test match id" in update_all_notifications_data.keys()
        self.unread_test_match_id_sponsor_helper(update_all_notifications_data["unread test match id"])

        # unread_test_match_id_assistor
        self.second_user_login()
        set_default_data_path(default_mode=testing_data['default_mode'], default_task_mode=testing_data['default_task_mode'], default_model_name=testing_data['default_model_name'], default_file_path=testing_data['default_file_path'],
                            default_id_column=testing_data['default_id_column'], default_data_column=testing_data['default_data_column'])
        update_all_notifications_data = self.get_Notification()
        assert "unread test match id" in update_all_notifications_data.keys()
        self.unread_test_match_id_assistor_helper(update_all_notifications_data["unread test match id"])

        # unread_test_output
        self.first_user_login()
        update_all_notifications_data = self.get_Notification()
        assert "unread test output" in update_all_notifications_data.keys()
        self.unread_test_output(update_all_notifications_data["unread test output"])