"""
tests.test_curves.py
~~~~~~~~~~~~~~~~~~~~

Test suite for the curves.py module that handles everything to do with
supply and demand curves.
"""

import pytest
from .__init__ import testing_data
from .Train_helper_function import Train_helper_function


class Test_find_assistor(Train_helper_function):

    def test_find_assistor(self):
        super().first_user_login()
        super().clean_db()
        super().find_assistor()

