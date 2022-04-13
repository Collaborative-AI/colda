import collections
from Apollo_test_helper_functions import Test_Helper_API_TestCase

class unread_match_identifier_API_TestCase(Test_Helper_API_TestCase):

    def test_unread_match_identifier_two_users(self):
        # file_content_dict = self.init_test_user_file_content(indicator='small_data')
        file_content_dict = self.init_test_user_file_content(indicator='large_data')

        task_id, test_id, assistor_username_list, user_id_list = self.find_test_assistor_two_assistors_helper(file_content_dict=file_content_dict)
        self.unread_test_request_two_users_helper(task_id, test_id, assistor_username_list, user_id_list, file_content_dict=file_content_dict)
        self.unread_test_match_identifier_two_users_helper(task_id, test_id, assistor_username_list, user_id_list, file_content_dict=file_content_dict)
        self.unread_test_output_two_users_helper(task_id, test_id, assistor_username_list, user_id_list, file_content_dict=file_content_dict)
    