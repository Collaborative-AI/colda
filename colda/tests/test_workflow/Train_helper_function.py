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

from colda.tests.test_workflow import testing_data
from colda.tests.test_workflow import _default_trainMainWorkflow
from colda.tests.test_workflow import _default_unittest_strategy
from colda.tests.test_workflow import _default_authentication
from colda.tests.test_workflow import _default_ShortPolling
from colda.tests.test_workflow import _default_PI
from colda.tests.test_workflow import _default_Network
from colda.algorithm.api import (
    get_algo_log,
    get_all_algo_logs
)
from colda.workflow.base import BaseWorkflow
from colda.short_polling.api import ShortPolling


class Train_helper_function:

    def clean_db(self):
        _default_Network.get_request_chaining(
            url_prefix='helper_api',
            url_root='delete_unittest_db',
            url_suffix=None,
            status_code=200,
        )
        
    def first_user_login(self):
        data = {
            'username': testing_data['first_user_username'],
            'password': testing_data['first_user_password'],
            'email': testing_data['first_user_email']
        }
        _default_Network.post_request_chaining(
            data=data,
            url_prefix='helper_api',
            url_root='create_unittest_user',
        )
        _default_authentication.user_login(
            username=testing_data['first_user_username'], 
            password=testing_data['first_user_password']
        )
        return
    
    def second_user_login(self):
        data = {
            'username': testing_data['second_user_username'],
            'password': testing_data['second_user_password'],
            'email': testing_data['second_user_email']
        }
        _default_Network.post_request_chaining(
            data=data,
            url_prefix='helper_api',
            url_root='create_unittest_user',
        )
        _default_authentication.user_login(
            username=testing_data['second_user_username'], 
            password=testing_data['second_user_password']
        )
        return

    def get_user_id(self):
        return _default_PI.user_id

    def get_notification(self):
        _default_ShortPolling.shortpolling['running'] = True
        notification = _default_ShortPolling._ShortPolling__polling()
        print(f'notification: {notification}')
        return notification

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
        return find_assistor_res
        
    def train_assistor_request(self, notification_category):
        _default_trainMainWorkflow.train_assistor_request(notification_category['unread_request']['train_id_dicts'])

    def train_sponsor_match_identifier(self, notification_category):
        _default_trainMainWorkflow.train_match_identifier(notification_category['unread_match_identifier']['train_id_dicts'])   
    
    def train_assistor_match_identifier(self, notification_category):
        _default_trainMainWorkflow.train_match_identifier(notification_category['unread_match_identifier']['train_id_dicts'])   
    
    def train_sponsor_situation(self, notification_category):
        _default_trainMainWorkflow.train_situation(notification_category['unread_situation']['train_id_dicts'])   
    
    def train_assistor_situation(self, notification_category):
        _default_trainMainWorkflow.train_situation(notification_category['unread_situation']['train_id_dicts'])   
    
    def _test_algorithm_result(
        self,
        user_id: str,
        task_id: str,
        log_category: str,
        test_func,
    ):
        
        data = get_algo_log(
            user_id=user_id,
            task_id=task_id,
            log_category=log_category
        )
        print('dddddddata', data)
        assert test_func(data) == True
        return

    def train_output(
        self, 
        notification_category: dict, 
        unittest_strategy: object=None, 
        user_id: str=None, 
        train_id: str=None, 
    ) -> None:

        _default_unittest_strategy.unittest_strategy = unittest_strategy
        _default_trainMainWorkflow.train_output(notification_category['unread_output']['train_id_dicts'])   
        
        res = get_all_algo_logs()
        print('&&&', res)

        if unittest_strategy:
            log_category = 'sponsor_trained_cooperative_model_output'
            self._test_algorithm_result(
                user_id=user_id, 
                task_id=train_id, 
                log_category=log_category,
                test_func=_default_unittest_strategy.sponsor_trained_cooperative_model_output(),
            )
            
            log_category = 'assistor_trained_cooperative_model_output'
            self._test_algorithm_result(
                user_id=user_id, 
                task_id=train_id, 
                log_category=log_category,
                test_func=_default_unittest_strategy.assistor_trained_cooperative_model_output(),
            )

            log_category = 'make_result_alpha'
            self._test_algorithm_result(
                user_id=user_id, 
                task_id=train_id, 
                log_category=log_category,
                test_func=_default_unittest_strategy.alpha(),
            )  

            log_category = 'make_result'
            self._test_algorithm_result(
                user_id=user_id, 
                task_id=train_id, 
                log_category=log_category,
                test_func=_default_unittest_strategy.get_unread_test_make_result(),
            )  
        return