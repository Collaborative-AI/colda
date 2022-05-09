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
from . import _default_testRequest
from . import _default_authorization
from . import _default_getNotification
from . import _default_PI
from . import _default_Network

from . import unittest_strategy_interface
_default_unittest_strategy_interface = unittest_strategy_interface()

import pytest

class Test_helper_function:

    def handleTestRequest_helper(self, task_id): 
        handleTestRequest_res = _default_testRequest.handleTestRequest(task_id=task_id, test_file_path=testing_data['test_file_path'],
                             test_id_column=testing_data['test_id_column'], test_data_column=testing_data['test_data_column'], test_target_column=testing_data['test_target_column'],  
                             test_name=testing_data['test_name'], test_description=testing_data['test_description'])
        print('zheli?')
        assert handleTestRequest_res[0] == 'handleTestRequest successfully'
        return handleTestRequest_res[1]
    
    def unread_test_request_helper(self, unread_test_request_notification):
        unread_test_request_res = _default_testRequest.unread_test_request(unread_test_request_notification)
        assert unread_test_request_res == 'unread_test_request done'

    def unread_test_match_identifier_sponsor_helper(self, unread_test_match_identifier_notification, unittest_strategy):
        _default_unittest_strategy_interface.unittest_strategy = unittest_strategy
        unread_test_match_identifier_sponsor_res = _default_testRequest.unread_test_match_identifier(unread_test_match_identifier_notification, _default_unittest_strategy_interface.get_unread_test_sponsor_match_id_test())   
        assert unread_test_match_identifier_sponsor_res == 'unread_test_match_identifier done'
    
    def unread_test_match_identifier_assistor_helper(self, unread_test_match_identifier_notification, unittest_strategy):
        _default_unittest_strategy_interface.unittest_strategy = unittest_strategy
        unread_test_match_identifier_assistor_res = _default_testRequest.unread_test_match_identifier(unread_test_match_identifier_notification, _default_unittest_strategy_interface.get_unread_test_assistor_match_id_test())   
        print('unread_test_match_identifier_assistor_res', unread_test_match_identifier_assistor_res)
        assert unread_test_match_identifier_assistor_res == 'unread_test_match_identifier done'
    
    def unread_test_output(self, unread_test_output_notification, unittest_strategy):
        _default_unittest_strategy_interface.unittest_strategy = unittest_strategy
        unread_test_output_res = _default_testRequest.unread_test_output(unread_test_output_notification, _default_unittest_strategy_interface.get_unread_test_output_test())   
        assert unread_test_output_res == 'unread_test_output done'