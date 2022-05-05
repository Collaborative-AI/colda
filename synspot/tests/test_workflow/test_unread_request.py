"""
tests.test_curves.py
~~~~~~~~~~~~~~~~~~~~

Test suite for the curves.py module that handles everything to do with
supply and demand curves.
"""

import pytest
from synspot import set_default_data_path
from synspot.tests.test_workflow import testing_data
from synspot.tests.test_workflow.Train_helper_function import Train_helper_function


class Test_unread_request(Train_helper_function):

    def test_unread_request(self):
        self.first_user_login()
        self.clean_db()
        self.find_assistor()

        # unread_request
        self.second_user_login()
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
        self.train_assistor_request(notification_category)

