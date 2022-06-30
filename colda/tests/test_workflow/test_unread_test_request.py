"""
tests.test_curves.py
~~~~~~~~~~~~~~~~~~~~

Test suite for the curves.py module that handles everything to do with
supply and demand curves.
"""
import pytest
from colda import set_default_data_path
from colda.tests.test_workflow import testing_data

from colda.tests.test_workflow.Train_helper_function import Train_helper_function
from colda.tests.test_workflow.Test_helper_function import Test_helper_function


class Test_unread_test_request(Train_helper_function, Test_helper_function):

        def test_unread_test_request(self):
        
            super().first_user_login()
            super().clean_db()
            train_id = super().find_assistor()

            # unread_request
            super().second_user_login()
            set_default_data_path(
                default_mode=testing_data['default_mode'], 
                default_task_mode=testing_data['default_task_mode'], 
                default_model_name=testing_data['default_model_name'], 
                default_file_path=testing_data['default_file_path'],
                default_id_column=testing_data['default_id_column'], 
                default_data_column=testing_data['default_data_column']
            )
            notification_category = self.get_notification()
            print('5555', notification_category)
            assert "unread_request" in notification_category.keys()
            super().train_assistor_request(notification_category)
            
            # unread_match_identifier_assistor
            super().second_user_login()
            notification_category = self.get_notification()
            print('666', notification_category)
            assert "unread_match_identifier" in notification_category.keys()
            super().train_assistor_match_identifier(notification_category)

            # unread_match_identifier_sponsor
            super().first_user_login()
            notification_category = self.get_notification()
            print('77', notification_category)
            assert "unread_match_identifier" in notification_category.keys()
            super().train_sponsor_match_identifier(notification_category)

            # unread_sponsor_situation
            super().first_user_login()
            notification_category = self.get_notification()
            print('88', notification_category)
            assert "unread_situation" in notification_category.keys()
            super().train_sponsor_situation(notification_category)

            # unread_assistor_situation
            super().second_user_login()
            notification_category = self.get_notification()
            print('99', notification_category)
            assert "unread_situation" in notification_category.keys()
            super().train_assistor_situation(notification_category)

             # unread_sponsor_output
            super().first_user_login()
            notification_category = self.get_notification()
            print('1010', notification_category)
            assert "unread_output" in notification_category.keys()
            super().train_output(notification_category)

            super().first_user_login()
            super().find_test_assistor(train_id=train_id)

            super().second_user_login()
            notification_category = self.get_notification()
            print('1111', notification_category)
            assert "unread_test_request" in notification_category.keys()
            super()._test_assistor_request(notification_category)
