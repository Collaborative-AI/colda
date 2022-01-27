"""
tests.test_curves.py
~~~~~~~~~~~~~~~~~~~~

Test suite for the curves.py module that handles everything to do with
supply and demand curves.
"""
import json
from typing import Any, Dict, List
from copy import deepcopy
from .train_helper_function import Train_helper_function
import pytest

class Test_handleTrainRequest(Train_helper_function):

    def test_handleTrainRequest(self):
        self.first_user_login()
        self.handleTrainRequest_helper()