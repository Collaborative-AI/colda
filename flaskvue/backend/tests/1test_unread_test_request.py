from Apollo_test_helper_functions import Test_Helper_API_TestCase


class Unread_Test_Request_API_TestCase(Test_Helper_API_TestCase):

    def test_unread_test_request_two_users(self):
        test_id, list_content = self.test_find_test_assistor_two_assistors_helper()
        self.unread_test_request_two_users_helper(test_id, list_content)
    
    