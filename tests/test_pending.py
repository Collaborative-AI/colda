import json

from flask_pymongo import PyMongo
from tests.Apollo_train_helper_functions import Train_Helper_API_TestCase
from tests.Apollo_test_helper_functions import Test_Helper_API_TestCase

from tests.Apollo_train_helper_functions import *
from tests.Apollo_test_helper_functions import *

class Pending_API_TestCase(Train_Helper_API_TestCase, Test_Helper_API_TestCase):

    def test_add_train_pending(self):

        file_content_dict = self.init_test_user_file_content(indicator='small_data')
        train_id, assistor_username_list, user_id_list = self.find_assistor_two_assistors_helper(file_content_dict=file_content_dict)

        user_id_1 = user_id_list[0]
        user_id_2 = user_id_list[1]
        user_id_3 = user_id_list[2]

        headers = self.get_token_auth_headers('unittest2', 'Xie1@456')
        data = json.dumps({
            'train_id': train_id
        })
        response = self.client.post('/main_flow/add_train_pending/' + user_id_2, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['message'], 'add train pending successfully')

        pending_document = mongoDB.search_pending_document(user_id=user_id_2)
        assert train_id in pending_document['task_dict']

        headers = self.get_token_auth_headers('unittest3', 'Xie1@456')
        data = json.dumps({
            'train_id': train_id
        })
        response = self.client.post('/main_flow/add_train_pending/' + user_id_3, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['message'], 'add train pending successfully')

        pending_document = mongoDB.search_pending_document(user_id=user_id_3)
        assert train_id in pending_document['task_dict']

        return train_id, user_id_list

    def test_add_test_pending(self):
        
        file_content_dict = self.init_test_user_file_content(indicator='small_data')
        train_id, test_id, assistor_username_list, user_id_list = self.find_test_assistor_two_assistors_helper(file_content_dict=file_content_dict)

        user_id_1 = user_id_list[0]
        user_id_2 = user_id_list[1]
        user_id_3 = user_id_list[2]

        headers = self.get_token_auth_headers('unittest2', 'Xie1@456')
        data = json.dumps({
            'test_id': test_id
        })
        response = self.client.post('/main_flow/add_test_pending/' + user_id_2, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['message'], 'add test pending successfully')

        pending_document = mongoDB.search_pending_document(user_id=user_id_2)
        assert test_id in pending_document['task_dict']

        headers = self.get_token_auth_headers('unittest3', 'Xie1@456')
        data = json.dumps({
            'test_id': test_id
        })
        response = self.client.post('/main_flow/add_test_pending/' + user_id_3, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['message'], 'add test pending successfully')

        pending_document = mongoDB.search_pending_document(user_id=user_id_3)
        assert test_id in pending_document['task_dict']

        return train_id, test_id, user_id_list

    def test_get_all_pending(self):

        file_content_dict = self.init_test_user_file_content(indicator='small_data')
        train_id, assistor_username_list, user_id_list = self.find_assistor_two_assistors_helper(file_content_dict=file_content_dict)
        pyMongo.db.Notification.delete_many({})
        train_id, test_id, assistor_username_list, user_id_list = self.find_test_assistor_two_assistors_helper(file_content_dict=file_content_dict)
        
        user_id_1 = user_id_list[0]
        user_id_2 = user_id_list[1]
        user_id_3 = user_id_list[2]

        headers = self.get_token_auth_headers('unittest2', 'Xie1@456')
        data = json.dumps({
            'train_id': train_id
        })
        response = self.client.post('/main_flow/add_train_pending/' + user_id_2, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['message'], 'add train pending successfully')

        headers = self.get_token_auth_headers('unittest3', 'Xie1@456')
        data = json.dumps({
            'train_id': train_id
        })
        response = self.client.post('/main_flow/add_train_pending/' + user_id_3, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['message'], 'add train pending successfully')

        # test_id = 'test_task_remporary_id'
        headers = self.get_token_auth_headers('unittest2', 'Xie1@456')
        data = json.dumps({
            'test_id': test_id
        })
        response = self.client.post('/main_flow/add_test_pending/' + user_id_2, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['message'], 'add test pending successfully')

        headers = self.get_token_auth_headers('unittest3', 'Xie1@456')
        data = json.dumps({
            'test_id': test_id
        })
        response = self.client.post('/main_flow/add_test_pending/' + user_id_3, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['message'], 'add test pending successfully')

        # task_id, test_id = self.task_id, self.test_id
        headers = self.get_token_auth_headers('unittest2', 'Xie1@456')
        response = self.client.get('/main_flow/get_all_pending/' + user_id_2, headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response['all_pending_items']), 2)
        assert train_id in json_response['all_pending_items']
        assert test_id in json_response['all_pending_items']

        headers = self.get_token_auth_headers('unittest3', 'Xie1@456')
        response = self.client.get('/main_flow/get_all_pending/' + user_id_3, headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response['all_pending_items']), 2)
        assert train_id in json_response['all_pending_items']
        assert test_id in json_response['all_pending_items']

    def test_delete_pending(self):
        
        file_content_dict = self.init_test_user_file_content(indicator='small_data')
        train_id, assistor_username_list, user_id_list = self.find_assistor_two_assistors_helper(file_content_dict=file_content_dict)
        pyMongo.db.Notification.delete_many({})
        train_id, test_id, assistor_username_list, user_id_list = self.find_test_assistor_two_assistors_helper(file_content_dict=file_content_dict)
        
        user_id_1 = user_id_list[0]
        user_id_2 = user_id_list[1]
        user_id_3 = user_id_list[2]

        headers = self.get_token_auth_headers('unittest2', 'Xie1@456')
        data = json.dumps({
            'train_id': train_id
        })
        response = self.client.post('/main_flow/add_train_pending/' + user_id_2, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['message'], 'add train pending successfully')

        headers = self.get_token_auth_headers('unittest3', 'Xie1@456')
        data = json.dumps({
            'train_id': train_id
        })
        response = self.client.post('/main_flow/add_train_pending/' + user_id_3, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['message'], 'add train pending successfully')

        # test_id = 'test_task_remporary_id'
        headers = self.get_token_auth_headers('unittest2', 'Xie1@456')
        data = json.dumps({
            'test_id': test_id
        })
        response = self.client.post('/main_flow/add_test_pending/' + user_id_2, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['message'], 'add test pending successfully')

        headers = self.get_token_auth_headers('unittest3', 'Xie1@456')
        data = json.dumps({
            'test_id': test_id
        })
        response = self.client.post('/main_flow/add_test_pending/' + user_id_3, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['message'], 'add test pending successfully')

        user_id_1 = user_id_list[0]
        user_id_2 = user_id_list[1]
        user_id_3 = user_id_list[2]

        # delete train task
        headers = self.get_token_auth_headers('unittest2', 'Xie1@456')
        data = json.dumps({
            'train_id': train_id, 
            'test_id': test_id, 
            'test_indicator': 'train'
        })
        response = self.client.post('/main_flow/delete_pending/' + user_id_2, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['message'], 'delete successfully')

        pending_document = mongoDB.search_pending_document(user_id=user_id_2)
        assert train_id not in pending_document['task_dict']
        assert test_id in pending_document['task_dict']

        # delete test task
        data = json.dumps({
            'train_id': train_id, 
            'test_id': test_id, 
            'test_indicator': 'test'
        })
        response = self.client.post('/main_flow/delete_pending/' + user_id_2, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['message'], 'delete successfully')

        pending_document = mongoDB.search_pending_document(user_id=user_id_2)
        assert train_id not in pending_document['task_dict']
        assert test_id not in pending_document['task_dict']

        # delete train task
        headers = self.get_token_auth_headers('unittest3', 'Xie1@456')
        data = json.dumps({
            'train_id': train_id, 
            'test_id': test_id, 
            'test_indicator': 'train'
        })
        response = self.client.post('/main_flow/delete_pending/' + user_id_3, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['message'], 'delete successfully')

        pending_document = mongoDB.search_pending_document(user_id=user_id_3)
        assert train_id not in pending_document['task_dict']
        assert test_id in pending_document['task_dict']

        # delete test task
        data = json.dumps({
            'train_id': train_id, 
            'test_id': test_id, 
            'test_indicator': 'test'
        })
        response = self.client.post('/main_flow/delete_pending/' + user_id_3, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['message'], 'delete successfully')

        pending_document = mongoDB.search_pending_document(user_id=user_id_3)
        assert train_id not in pending_document['task_dict']
        assert test_id not in pending_document['task_dict']