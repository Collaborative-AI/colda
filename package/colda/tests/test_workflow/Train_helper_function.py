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

from .__init__ import testing_data
from .__init__ import coldaInstance
from .__init__ import _default_unittest_strategy

# from tests.test_workflow import _default_trainMainWorkflow
# from tests.test_workflow import _default_authentication
# from tests.test_workflow import _default_shortPolling
# from tests.test_workflow import _default_PI
# from tests.test_workflow import _default_network
from algorithm.api import (
    get_algo_log,
    get_all_algo_logs
)



class Train_helper_function:

    def clean_db(self):
        coldaInstance._default_network.get_request_chaining(
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
        coldaInstance._default_network.post_request_chaining(
            data=data,
            url_prefix='helper_api',
            url_root='create_unittest_user',
        )
        coldaInstance._default_authentication.user_login(
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
        coldaInstance._default_network.post_request_chaining(
            data=data,
            url_prefix='helper_api',
            url_root='create_unittest_user',
        )
        coldaInstance._default_authentication.user_login(
            username=testing_data['second_user_username'], 
            password=testing_data['second_user_password']
        )
        return

    def user_logout(self):
        coldaInstance._default_authentication.user_logout()
        
    def set_default_information(self):
        coldaInstance.set_default_info(
            default_mode=testing_data['default_mode'], 
            default_task_mode=testing_data['default_task_mode'], 
            default_model_name=testing_data['default_model_name'], 
            default_file_path=testing_data['default_file_path'],
            default_id_column=testing_data['default_id_column'], 
            default_data_column=testing_data['default_data_column']
        )
        return

    def get_user_id(self):
        return coldaInstance._default_PI.user_id

    def get_notification(self):
        coldaInstance._default_shortPolling.shortpolling['running'] = True
        notification = coldaInstance._default_shortPolling._ShortPolling__unittest_polling()
        print(f'notification: {notification}')
        return notification

    def find_assistor(self):
        find_assistor_res = coldaInstance._default_trainMainWorkflow.find_assistor(
            max_round=testing_data['max_round'], 
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
        coldaInstance._default_trainMainWorkflow.train_assistor_request(notification_category['unread_request']['train_id_dicts'])

    def train_sponsor_match_identifier(self, notification_category):
        coldaInstance._default_trainMainWorkflow.train_match_identifier(notification_category['unread_match_identifier']['train_id_dicts'])   
    
    def train_assistor_match_identifier(self, notification_category):
        coldaInstance._default_trainMainWorkflow.train_match_identifier(notification_category['unread_match_identifier']['train_id_dicts'])   
    
    def train_sponsor_situation(self, notification_category):
        coldaInstance._default_trainMainWorkflow.train_situation(notification_category['unread_situation']['train_id_dicts'])   
    
    def train_assistor_situation(self, notification_category):
        coldaInstance._default_trainMainWorkflow.train_situation(notification_category['unread_situation']['train_id_dicts'])   
    
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
        coldaInstance._default_trainMainWorkflow.train_output(notification_category['unread_output']['train_id_dicts'])   
        
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