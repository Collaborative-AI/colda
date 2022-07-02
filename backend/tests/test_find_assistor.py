from tests.Apollo_train_helper_functions import Train_Helper_API_TestCase

class FindAPITestCase(Train_Helper_API_TestCase):
    def test_find_assistor_two_assistors(self):

        file_content_dict = self.init_train_user_file_content(indicator='large_data')

        self.find_assistor_two_assistors_helper(file_content_dict=file_content_dict)