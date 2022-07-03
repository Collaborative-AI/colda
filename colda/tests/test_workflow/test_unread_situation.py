"""
tests.test_curves.py
~~~~~~~~~~~~~~~~~~~~

Test suite for the curves.py module that handles everything to do with
supply and demand curves.
"""
import pytest
from colda.tests.test_workflow import testing_data
from colda.tests.test_workflow.Train_helper_function import Train_helper_function


class Test_unread_situation(Train_helper_function):

    def test_unread_situation(self):
        
        self.first_user_login()
        self.clean_db()
        self.find_assistor()

        # unread_request
        self.second_user_login()
        super().set_default_information()
        notification_category = self.get_notification()
        print('5555', notification_category)
        assert "unread_request" in notification_category.keys()
        self.train_assistor_request(notification_category)
        
        # unread_match_identifier_assistor
        self.second_user_login()
        notification_category = self.get_notification()
        print('666', notification_category)
        assert "unread_match_identifier" in notification_category.keys()
        self.train_assistor_match_identifier(notification_category)

        # unread_match_identifier_sponsor
        self.first_user_login()
        notification_category = self.get_notification()
        print('77', notification_category)
        assert "unread_match_identifier" in notification_category.keys()
        self.train_sponsor_match_identifier(notification_category)

        # unread_sponsor_situation
        self.first_user_login()
        notification_category = self.get_notification()
        print('88', notification_category)
        assert "unread_situation" in notification_category.keys()
        self.train_sponsor_situation(notification_category)

        # unread_assistor_situation
        self.second_user_login()
        notification_category = self.get_notification()
        print('99', notification_category)
        assert "unread_situation" in notification_category.keys()
        self.train_assistor_situation(notification_category)