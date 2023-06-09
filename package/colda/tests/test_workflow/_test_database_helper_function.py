"""
tests.test_curves.py
~~~~~~~~~~~~~~~~~~~~

Test suite for the curves.py module that handles everything to do with
supply and demand curves.
"""
import json
import pytest
import requests

from copy import deepcopy
from typing import Any, Dict, List

from . import set_default_data_path, get_all_task_id_as_sponsor, get_all_test_id_as_sponsor, get_all_task_id_as_assistor, get_all_test_id_as_assistor
from . import get_all_task_id, get_all_test_id
from . import testing_data
from . import Regression_1s_1a

from .Train_helper_function import Train_helper_function
from .Test_helper_function import Test_helper_function

class Test_database_helper_function(Train_helper_function, Test_helper_function):
    def test_database_helper_function(self):
        
        self.first_user_login()
        self.clean_db()
        task_id = self.handleTrainRequest_helper()

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
        
        # self.second_user_login()
        # set_default_data_path(default_mode=testing_data['default_mode'], default_task_mode=testing_data['default_task_mode'], default_model_name=testing_data['default_model_name'], default_file_path=testing_data['default_file_path'],
        #                     default_id_column=testing_data['default_id_column'], default_data_column=testing_data['default_data_column'])
        # update_all_notifications_data = self.start_Collaboration()
        # assert "unread situation" in update_all_notifications_data
        # self.unread_situation_assistor_helper(update_all_notifications_data["unread situation"])

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

        # test stage
        self.first_user_login()
        test_id = self.handleTestRequest_helper(task_id)

        # unread_test_request
        self.second_user_login()
        set_default_data_path(default_mode=testing_data['default_mode'], default_task_mode=testing_data['default_task_mode'], default_model_name=testing_data['default_model_name'], default_file_path=testing_data['default_file_path'],
                            default_id_column=testing_data['default_id_column'], default_data_column=testing_data['default_data_column'])
        update_all_notifications_data = self.start_Collaboration()
        assert "unread test request" in update_all_notifications_data.keys()
        self.unread_test_request_helper(update_all_notifications_data["unread test request"])

        # unread_test_match_identifier_sponsor
        self.first_user_login()
        update_all_notifications_data = self.start_Collaboration()
        assert "unread test match id" in update_all_notifications_data.keys()
        self.unread_test_match_identifier_sponsor_helper(update_all_notifications_data["unread test match id"], unittest_strategy=Regression_1s_1a())

        # unread_test_match_identifier_assistor
        self.second_user_login()
        set_default_data_path(default_mode=testing_data['default_mode'], default_task_mode=testing_data['default_task_mode'], default_model_name=testing_data['default_model_name'], default_file_path=testing_data['default_file_path'],
                            default_id_column=testing_data['default_id_column'], default_data_column=testing_data['default_data_column'])
        update_all_notifications_data = self.start_Collaboration()
        assert "unread test match id" in update_all_notifications_data.keys()
        self.unread_test_match_identifier_assistor_helper(update_all_notifications_data["unread test match id"], unittest_strategy=Regression_1s_1a())

        # unread_test_output
        self.first_user_login()
        update_all_notifications_data = self.start_Collaboration()
        assert "unread test output" in update_all_notifications_data.keys()
        self.unread_test_output(update_all_notifications_data["unread test output"], unittest_strategy=Regression_1s_1a())

        self.first_user_login()
        assert get_all_task_id_as_sponsor() == [task_id]
        assert get_all_test_id_as_sponsor() == [test_id]
        assert get_all_task_id_as_assistor() == []
        assert get_all_test_id_as_assistor() == []
        assert get_all_task_id() == [task_id]
        assert get_all_test_id() == [test_id]

        self.second_user_login()
        assert get_all_task_id_as_sponsor() == []
        assert get_all_test_id_as_sponsor() == []
        assert get_all_task_id_as_assistor() == [task_id]
        assert get_all_test_id_as_assistor() == [test_id]
        assert get_all_task_id() == [task_id]
        assert get_all_test_id() == [test_id]