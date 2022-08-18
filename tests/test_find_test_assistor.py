from tests.Apollo_test_helper_functions import Test_Helper_API_TestCase


class Find_Test_API_TestCase(Test_Helper_API_TestCase):
    
    def test_find_test_assistor_two_assistors(self):

        file_content_dict = self.init_test_user_file_content(indicator='small_data')
        self.find_test_assistor_two_assistors_helper(file_content_dict=file_content_dict)

    

    
