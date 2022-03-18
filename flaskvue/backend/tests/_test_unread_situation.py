from Apollo_train_helper_functions import Train_Helper_API_TestCase

class Unread_Situation_API_TestCase(Train_Helper_API_TestCase):

    def test_unread_situation_two_users(self):
        task_id, assistor_username_list, user_id_list = self.find_assistor_two_assistors_helper()
        self.unread_request_two_users_helper(task_id, assistor_username_list, user_id_list)
        self.unread_match_id_two_users_helper(task_id, assistor_username_list, user_id_list)
        self.unread_situation_two_users_helper(task_id, assistor_username_list, user_id_list)