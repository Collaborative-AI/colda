from Apollo_train_helper_functions import Train_Helper_API_TestCase


class Unread_Match_ID_API_TestCase(Train_Helper_API_TestCase):

    def test_unread_match_id_two_users(self):
        self.unread_match_id_two_users_helper()