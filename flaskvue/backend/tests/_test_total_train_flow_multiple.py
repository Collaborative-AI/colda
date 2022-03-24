from Apollo_train_helper_functions import Train_Helper_API_TestCase

class Test_Total_Flow_Multiple_API_TestCase(Train_Helper_API_TestCase):

    def test_total_flow_multiple_between_two_users(self):
        # task_id, list_content, assistor_random_id_list = self.find_assistor_two_assistors_helper()
        # self.unread_request_two_users_helper(task_id, list_content, assistor_random_id_list)
        # self.unread_match_id_two_users_helper(task_id, list_content, assistor_random_id_list)
        
        # for test_round in range(1, 5):
        #     self.unread_situation_two_users_helper(task_id, list_content, assistor_random_id_list, test_round, False, False, False)
        #     self.unread_output_two_users_helper(task_id, list_content, assistor_random_id_list, test_round, False, False, False)


        task_id, assistor_username_list, user_id_list = self.find_assistor_two_assistors_helper()
        self.unread_request_two_users_helper(task_id, assistor_username_list, user_id_list)
        self.unread_match_id_two_users_helper(task_id, assistor_username_list, user_id_list)

        for test_round in range(1, 5):
            self.unread_situation_two_users_helper(task_id, assistor_username_list, user_id_list, test_rounds_num=test_round)
            self.unread_output_two_users_helper(task_id, assistor_username_list, user_id_list)
       