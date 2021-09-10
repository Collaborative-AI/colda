from Apollo_train_helper_functions import Train_Helper_API_TestCase

class Unread_Output_API_TestCase(Train_Helper_API_TestCase):

    def test_unread_output_two_users(self):
        task_id, list_content, assistor_random_id_list = self.find_assistor_two_assistors_helper()
        self.unread_request_two_users_helper(task_id, list_content, assistor_random_id_list)
        self.unread_match_id_two_users_helper(task_id, list_content, assistor_random_id_list)
        
        test_round = 0
        self.unread_situation_two_users_helper(task_id, list_content, assistor_random_id_list, test_round)
        self.unread_output_two_users_helper(task_id, list_content, assistor_random_id_list, test_round)
