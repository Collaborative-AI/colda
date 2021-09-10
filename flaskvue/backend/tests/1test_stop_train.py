from Apollo_train_helper_functions import Train_Helper_API_TestCase

class Stop_Train_API_TestCase(Train_Helper_API_TestCase):

    def test_stop_situation_train_two_users(self):
        self.stop_situation_train_two_users_helper(0)

        