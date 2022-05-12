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
from synspot.tests.test_workflow import _default_testMainWorkflow
from synspot.tests.test_workflow import _default_unittest_strategy
from synspot.tests.test_workflow import _default_authorization
from synspot.tests.test_workflow import _default_ShortPolling
from synspot.tests.test_workflow import _default_PI
from synspot.tests.test_workflow import _default_Network
from synspot.algorithm.api import AlgorithmAPI

class Test_helper_function:

    def find_test_assistor(self, train_id): 
        find_test_assistor_res = _default_testMainWorkflow.find_test_assistor(
            train_id=train_id, 
            test_file_path=testing_data['test_file_path'],
            test_id_column=testing_data['test_id_column'], 
            test_data_column=testing_data['test_data_column'], 
            test_target_column=testing_data['test_target_column'],  
            test_name=testing_data['test_name'], 
            test_description=testing_data['test_description']
        )
        print('zheli?')
        assert find_test_assistor_res[0] == True
        return find_test_assistor_res[1]
    
    def _test_assistor_request(self, notification_category):
        test_assistor_request = _default_testMainWorkflow.test_assistor_request(notification_category['unread_test_request']['test_id_dicts'])
        assert test_assistor_request == True

    def _test_algorithm_result1(self, user_id, task_id, log_category, test_func):
        data = AlgorithmAPI.get_log(
            user_id=user_id,
            task_id=task_id,
            log_category=log_category
        )
        print('dddddddata', data)
        assert test_func(data) == True
        return 

    def _test_sponsor_match_identifier(self, notification_category, unittest_strategy, user_id, test_id):
        _default_unittest_strategy.unittest_strategy = unittest_strategy
        test_sponsor_match_identifier = _default_testMainWorkflow.test_match_identifier(notification_category['unread_test_match_identifier']['test_id_dicts']) 
        log_category = 'make_test'
        self._test_algorithm_result1(
            user_id=user_id, 
            task_id=test_id, 
            log_category=log_category,
            test_func=_default_unittest_strategy.get_unread_test_sponsor_match_id_test()
        )  
        assert test_sponsor_match_identifier == True
    
    def _test_assistor_match_identifier(self, notification_category, unittest_strategy, user_id, test_id):
        _default_unittest_strategy.unittest_strategy = unittest_strategy
        test_assistor_match_identifier = _default_testMainWorkflow.test_match_identifier(notification_category['unread_test_match_identifier']['test_id_dicts'])   
        log_category = 'make_test'
        self._test_algorithm_result1(
            user_id=user_id, 
            task_id=test_id, 
            log_category=log_category,
            test_func=_default_unittest_strategy.get_unread_test_assistor_match_id_test()
        )
        assert test_assistor_match_identifier == True

    def _test_output(self, notification_category, unittest_strategy, user_id, test_id):
        _default_unittest_strategy.unittest_strategy = unittest_strategy
        test_output = _default_testMainWorkflow.test_output(notification_category['unread_test_output']['test_id_dicts']) 
        log_category = 'make_eval'
        self._test_algorithm_result1(
            user_id=user_id, 
            task_id=test_id, 
            log_category=log_category,
            test_func=_default_unittest_strategy.get_unread_test_output_test(),
        )  
        assert test_output == True