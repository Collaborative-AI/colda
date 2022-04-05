from Apollo_train_helper_functions import Train_Helper_API_TestCase
from Apollo_test_helper_functions import Test_Helper_API_TestCase

from tests.Apollo_train_helper_functions import *
from tests.Apollo_test_helper_functions import *

class Test_helper_api(Train_Helper_API_TestCase, Test_Helper_API_TestCase):

    def test_get_user_history(self):
        task_id, test_id, assistor_username_list, user_id_list = self.find_test_assistor_two_assistors_helper()

        user_id_1 = user_id_list[0]
        user_id_2 = user_id_list[1]
        user_id_3 = user_id_list[2]

        headers = self.get_token_auth_headers('unittest1', 'Xie1@456')
        response = self.client.get('/helper_api/get_user_history/' + user_id_1, headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        participated_sort_task_dict = json_response['participated_sort_task_dict']

        assert len(participated_sort_task_dict) == 2
        assert task_id in participated_sort_task_dict
        assert test_id in participated_sort_task_dict

        headers = self.get_token_auth_headers('unittest1', 'Xie1@456')
        response = self.client.get('/main_flow/create_new_test_task/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        test_id_2 = json_response['test_id']

        identifier_content = [8, 4, 3]
        data = json.dumps({
            'identifier_content': identifier_content, 
            'task_id': task_id, 
            'test_id': test_id_2,
            'task_mode': 'regression', 
            'model_name': 'LinearRegression', 
            'metric_name': 'RMSE',
            'test_name': 'unittest', 
            'test_description': 'unittest_desciption'
        })
        response = self.client.post('/main_flow/find_test_assistor/' + user_id_1, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['task_id'], task_id)
        self.assertEqual(json_response['test_id'], test_id_2)
        assistor_num = json_response['assistor_num']

        headers = self.get_token_auth_headers('unittest1', 'Xie1@456')
        response = self.client.get('/helper_api/get_user_history/' + user_id_1, headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        participated_sort_task_dict = json_response['participated_sort_task_dict']

        assert len(participated_sort_task_dict) == 3
        assert task_id in participated_sort_task_dict
        assert test_id in participated_sort_task_dict
        assert test_id_2 in participated_sort_task_dict

    def test_get_test_task_id_history(self):

        task_id, test_id, assistor_username_list, user_id_list = self.find_test_assistor_two_assistors_helper()

        user_id_1 = user_id_list[0]
        user_id_2 = user_id_list[1]
        user_id_3 = user_id_list[2]

        headers = self.get_token_auth_headers('unittest1', 'Xie1@456')
        data = json.dumps({
            'task_id': task_id, 
        })
        response = self.client.post('/helper_api/get_test_task_id_history/' + user_id_1, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        test_task_dict = json_response['test_task_dict']

        assert len(test_task_dict) == 1
        assert test_id in test_task_dict

        headers = self.get_token_auth_headers('unittest1', 'Xie1@456')
        response = self.client.get('/main_flow/create_new_test_task/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        test_id_2 = json_response['test_id']

        identifier_content = [8, 4, 3]
        data = json.dumps({
            'identifier_content': identifier_content, 
            'task_id': task_id, 
            'test_id': test_id_2,
            'task_mode': 'regression', 
            'model_name': 'LinearRegression', 
            'metric_name': 'RMSE',
            'test_name': 'unittest', 
            'test_description': 'unittest_desciption'
        })
        response = self.client.post('/main_flow/find_test_assistor/' + user_id_1, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['task_id'], task_id)
        self.assertEqual(json_response['test_id'], test_id_2)
        assistor_num = json_response['assistor_num']

        data = json.dumps({
            'task_id': task_id, 
        })
        response = self.client.post('/helper_api/get_test_task_id_history/' + user_id_1, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        test_task_dict = json_response['test_task_dict']

        assert len(test_task_dict) == 2
        assert test_id in test_task_dict
        assert test_id_2 in test_task_dict