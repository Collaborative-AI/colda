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
from .train_helper_function import Train_helper_function

import pytest

class Test_unread_request(Train_helper_function):

    def test_unread_request(self):
        self.first_user_login()
        self.handleTrainRequest_helper()

        self.second_user_login()
        self.get_Notification()

