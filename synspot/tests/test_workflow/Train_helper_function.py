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
from synspot.tests.test_workflow import _default_unittest_strategy
from synspot.tests.test_workflow import _default_authorization
from synspot.tests.test_workflow import _default_getNotification
from synspot.tests.test_workflow import _default_PI
from synspot.tests.test_workflow import _default_Network
from synspot.algorithm.api import AlgorithmAPI
from synspot.workflow.base import BaseWorkflow


class Train_helper_function:

    def clean_db(self):
        _default_Network.get_request_chaining(
            url_prefix='helper_api',
            url_root='delete_unittest_db',
            url_suffix=None,
            status_code=200,
        )
        
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

    def get_user_id(self):
        return _default_PI.user_id

    def get_notification(self):
        return _default_getNotification.start_Collaboration()

    # def set_max_round(self, num):
    #     BaseWorkflow._max_round = num
    #     return True

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
        assert train_assistor_match_identifier == True
    
    def train_sponsor_situation(self, notification_category):
        train_sponsor_situation = _default_trainMainWorkflow.train_situation(notification_category['unread_situation']['train_id_dicts'])   
        assert train_sponsor_situation == True
    
    def train_assistor_situation(self, notification_category):
        train_assistor_situation = _default_trainMainWorkflow.train_situation(notification_category['unread_situation']['train_id_dicts'])   
        assert train_assistor_situation == True
    
    def _test_algorithm_result(
        self,
        user_id: str,
        task_id: str,
        log_category: str,
        test_func,
    ):
        

        data = AlgorithmAPI.get_log(
            user_id=user_id,
            task_id=task_id,
            log_category=log_category
        )
        print('dddddddata', data)
        assert test_func(data) == True
        return

    def train_output(
        self, 
        notification_category, 
        unittest_strategy, 
        user_id, 
        train_id, 
        rounds
    ) -> None:

        _default_unittest_strategy.unittest_strategy = unittest_strategy
        train_output = _default_trainMainWorkflow.train_output(notification_category['unread_output']['train_id_dicts'])   
        
        res = AlgorithmAPI.get_all_logs()
        print('&&&', res)

        log_category = 'sponsor_trained_cooperative_model_output'
        self._test_algorithm_result(
            user_id=user_id, 
            task_id=train_id, 
            log_category=log_category,
            test_func=_default_unittest_strategy.sponsor_trained_cooperative_model_output(),
            rounds=rounds
        )
        
        log_category = 'assistor_trained_cooperative_model_output'
        self._test_algorithm_result(
            user_id=user_id, 
            task_id=train_id, 
            log_category=log_category,
            test_func=_default_unittest_strategy.assistor_trained_cooperative_model_output(),
            rounds=rounds
        )

        log_category = 'make_result_alpha'
        self._test_algorithm_result(
            user_id=user_id, 
            task_id=train_id, 
            log_category=log_category,
            test_func=_default_unittest_strategy.alpha(),
            rounds=rounds
        )  

        log_category = 'make_result'
        self._test_algorithm_result(
            user_id=user_id, 
            task_id=train_id, 
            log_category=log_category,
            test_func=_default_unittest_strategy.get_unread_test_make_result(),
            rounds=rounds
        )  

        assert train_output == True