from Apollo_train_helper_functions import Train_Helper_API_TestCase


class Unread_Request_API_TestCase(Train_Helper_API_TestCase):

    def test_unread_request_two_users(self):
        self.unread_request_two_users_helper()
    
    