"""
tests.test_curves.py
~~~~~~~~~~~~~~~~~~~~

Test suite for the curves.py module that handles everything to do with
supply and demand curves.
"""
import json
from typing import Any, Dict, List
from copy import deepcopy

from py_pkg.Authorization import Authorization
import pytest

class TestAuthorization:
    def get_instance(self):
        Authorization_instance = Authorization()
        return Authorization_instance

    def get_testing_data(self):
        testing_data = {}
        testing_data['first_user_username'] = 'xie1'
        testing_data['first_user_password'] = 'Xie1@123'
        testing_data['second_user_username'] = 'xie2'
        testing_data['second_user_password'] = 'Xie2@123'

        return testing_data

    def test_userLogin(self):
        Authorization_instance = self.get_instance()
        testing_data = self.get_testing_data()
        
        userLogin_res = Authorization_instance.userLogin(username=testing_data['first_user_username'], password=testing_data['first_user_password'])
        assert userLogin_res == 'userLogin Successfully'