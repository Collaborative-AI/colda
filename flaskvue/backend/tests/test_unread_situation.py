from Apollo_train_helper_functions import Train_Helper_API_TestCase

class Unread_Situation_API_TestCase(Train_Helper_API_TestCase):

    def test_unread_situation_two_users(self):
        self.unread_situation_two_users_helper(0)