from tests.Apollo_test_helper_functions import Test_Helper_API_TestCase


class Unread_Test_Request_API_TestCase(Test_Helper_API_TestCase):

    def test_unread_test_request_two_users(self):
        file_content_dict = self.init_test_user_file_content(indicator='small_data')
        train_id, test_id, assistor_username_list, user_id_list = self.find_test_assistor_two_assistors_helper(file_content_dict=file_content_dict)

        self.unread_test_request_two_users_helper(
            train_id, 
            test_id, 
            assistor_username_list, 
            user_id_list,
            file_content_dict=file_content_dict
        )
    
    