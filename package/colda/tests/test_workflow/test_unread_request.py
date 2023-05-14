"""
tests.test_curves.py
~~~~~~~~~~~~~~~~~~~~

Test suite for the curves.py module that handles everything to do with
supply and demand curves.
"""

import pytest
from .__init__ import testing_data
from .Train_helper_function import Train_helper_function


class Test_unread_request(Train_helper_function):

    def test_unread_request(self):
        super().first_user_login()
        super().clean_db()
        super().find_assistor()

        # unread_request
        super().second_user_login()
        super().set_default_information()
        notification_category = self.get_notification()
        print('5555', notification_category)
        assert "unread_request" in notification_category.keys()
        super().train_assistor_request(notification_category)

