from tests.Apollo_train_helper_functions import Train_Helper_API_TestCase


class Unread_Output_API_TestCase(Train_Helper_API_TestCase):

    def test_unread_output_two_users(self):
        file_content_dict = self.init_train_user_file_content(indicator='small_data')
        train_id, assistor_username_list, user_id_list = self.find_assistor_two_assistors_helper(file_content_dict=file_content_dict)
        
        self.unread_request_two_users_helper(
            train_id, 
            assistor_username_list, 
            user_id_list, 
            file_content_dict=file_content_dict
        )
        
        self.unread_match_identifier_two_users_helper(
            train_id, 
            assistor_username_list, 
            user_id_list, 
            file_content_dict=file_content_dict
        )
        
        self.unread_situation_two_users_helper(
            train_id, 
            assistor_username_list, 
            user_id_list, 
            file_content_dict=file_content_dict
        )
        
        self.unread_output_two_users_helper(
            train_id, 
            assistor_username_list, 
            user_id_list, 
            file_content_dict=file_content_dict
        )
