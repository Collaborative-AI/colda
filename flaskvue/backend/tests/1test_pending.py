import json
from Apollo_train_helper_functions import Train_Helper_API_TestCase
from Apollo_test_helper_functions import Test_Helper_API_TestCase
from Items.models import Pending, User, Message, Notification, Matched

class Pending_API_TestCase(Train_Helper_API_TestCase, Test_Helper_API_TestCase):

    # def test_add_train_pending(self):
    #     task_id, list_content, assistor_random_id_list = self.find_assistor_two_assistors_helper()

    #     headers = self.get_token_auth_headers('unittest2', '123')
    #     data = json.dumps({'task_id': task_id})
    #     response = self.client.post('/add_train_pending/', headers=headers, data=data)
    #     self.assertEqual(response.status_code, 200)
    #     json_response = json.loads(response.get_data(as_text=True))
    #     self.assertEqual(json_response, 'add train pending successfully')

    #     queries = Pending.query.filter(Pending.pending_task_id == task_id, Pending.pending_assistor_id == 2, Pending.test_indicator == "train").all()
    #     self.assertEqual(len(queries), 1)

    #     headers = self.get_token_auth_headers('unittest', '123')
    #     data = json.dumps({'task_id': task_id})
    #     response = self.client.post('/add_train_pending/', headers=headers, data=data)
    #     self.assertEqual(response.status_code, 200)
    #     json_response = json.loads(response.get_data(as_text=True))
    #     self.assertEqual(json_response, 'add train pending successfully')

    #     queries = Pending.query.filter(Pending.pending_task_id == task_id, Pending.pending_assistor_id == 1, Pending.test_indicator == "train").all()
    #     self.assertEqual(len(queries), 1)

    #     queries = Pending.query.filter(Pending.pending_task_id == task_id, Pending.test_indicator == "train").all()
    #     self.assertEqual(len(queries), 2)

    #     return task_id

    # def test_get_all_pending(self):

    #     task_id = self.test_add_train_pending()

    #     headers = self.get_token_auth_headers('unittest', '123')
    #     response = self.client.get('/get_all_pending/', headers=headers)
    #     self.assertEqual(response.status_code, 200)
    #     json_response = json.loads(response.get_data(as_text=True))
    #     self.assertEqual(len(json_response['all_pending_items']), 1)
    #     return_pending_items = json_response['all_pending_items'][0]
    #     self.assertEqual(return_pending_items['pending_task_id'], task_id)
    #     self.assertEqual(return_pending_items['pending_task_name'], 'Cooperate with unittest2,unittest3')
    #     self.assertEqual(return_pending_items['test_indicator'], 'train')

    #     headers = self.get_token_auth_headers('unittest2', '123')
    #     response = self.client.get('/get_all_pending/', headers=headers)
    #     self.assertEqual(response.status_code, 200)
    #     json_response = json.loads(response.get_data(as_text=True))
    #     self.assertEqual(len(json_response['all_pending_items']), 1)
    #     return_pending_items = json_response['all_pending_items'][0]
    #     self.assertEqual(return_pending_items['pending_task_id'], task_id)
    #     self.assertEqual(return_pending_items['pending_task_name'], 'Cooperate with unittest')
    #     self.assertEqual(return_pending_items['test_indicator'], 'train')

        
    # def test_delete_pending(self):
        
    #     task_id = self.test_add_train_pending()
    #     test_id = None

    #     headers = self.get_token_auth_headers('unittest', '123')
    #     data = json.dumps({'task_id': task_id, 'test_id': test_id, 'test_indicator': 'train'})
    #     response = self.client.post('/delete_pending/', headers=headers, data=data)
    #     self.assertEqual(response.status_code, 200)
    #     json_response = json.loads(response.get_data(as_text=True))
    #     self.assertEqual(json_response, 'Sucessfully delete')

    #     queries = Pending.query.filter(Pending.pending_task_id == task_id, Pending.pending_assistor_id == 1, Pending.test_indicator == "train").all()
    #     self.assertEqual(len(queries), 0)

    #     headers = self.get_token_auth_headers('unittest2', '123')
    #     data = json.dumps({'task_id': task_id, 'test_id': test_id, 'test_indicator': 'train'})
    #     response = self.client.post('/delete_pending/', headers=headers, data=data)
    #     self.assertEqual(response.status_code, 200)
    #     json_response = json.loads(response.get_data(as_text=True))
    #     self.assertEqual(json_response, 'Sucessfully delete')

    #     queries = Pending.query.filter(Pending.pending_task_id == task_id, Pending.pending_assistor_id == 1, Pending.test_indicator == "train").all()
    #     self.assertEqual(len(queries), 0)


    #     queries = Pending.query.filter(Pending.pending_task_id == task_id, Pending.test_indicator == "train").all()
    #     self.assertEqual(len(queries), 0)


    def test_add_test_pending(self):
        task_id, test_id, list_content = self.find_test_assistor_two_assistors_helper()

        headers = self.get_token_auth_headers('unittest2', '123')
        data = json.dumps({'test_id': test_id})
        response = self.client.post('/add_test_pending/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response, 'add test pending successfully')

        queries = Pending.query.filter(Pending.pending_test_id == test_id, Pending.pending_assistor_id == 2, Pending.test_indicator == "test").all()
        self.assertEqual(len(queries), 1)

        headers = self.get_token_auth_headers('unittest', '123')
        data = json.dumps({'test_id': test_id})
        response = self.client.post('/add_test_pending/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response, 'add test pending successfully')

        queries = Pending.query.filter(Pending.pending_test_id == test_id, Pending.pending_assistor_id == 1, Pending.test_indicator == "test").all()
        self.assertEqual(len(queries), 1)

        queries = Pending.query.filter(Pending.pending_test_id == test_id, Pending.test_indicator == "test").all()
        self.assertEqual(len(queries), 2)

        return task_id, test_id

    def test_get_all_pending(self):

        task_id, test_id = self.test_add_test_pending()

        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/get_all_pending/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response['all_pending_items']), 1)
        return_pending_items = json_response['all_pending_items'][0]
        self.assertEqual(return_pending_items['pending_test_id'], test_id)
        self.assertEqual(return_pending_items['pending_task_name'], 'Test of ' + task_id)
        self.assertEqual(return_pending_items['test_indicator'], 'test')

        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/get_all_pending/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response['all_pending_items']), 1)
        return_pending_items = json_response['all_pending_items'][0]
        self.assertEqual(return_pending_items['pending_test_id'], test_id)
        self.assertEqual(return_pending_items['pending_task_name'], 'Test of ' + task_id)
        self.assertEqual(return_pending_items['test_indicator'], 'test')

        
    def test_delete_pending(self):
        
        task_id, test_id = self.test_add_test_pending()
        task_id = None

        headers = self.get_token_auth_headers('unittest', '123')
        data = json.dumps({'task_id': task_id, 'test_id': test_id, 'test_indicator': 'test'})
        response = self.client.post('/delete_pending/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response, 'Sucessfully delete')

        queries = Pending.query.filter(Pending.pending_test_id == test_id, Pending.pending_assistor_id == 1, Pending.test_indicator == "test").all()
        self.assertEqual(len(queries), 0)

        headers = self.get_token_auth_headers('unittest2', '123')
        data = json.dumps({'task_id': task_id, 'test_id': test_id, 'test_indicator': 'test'})
        response = self.client.post('/delete_pending/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response, 'Sucessfully delete')

        queries = Pending.query.filter(Pending.pending_test_id == test_id, Pending.pending_assistor_id == 1, Pending.test_indicator == "test").all()
        self.assertEqual(len(queries), 0)

        queries = Pending.query.filter(Pending.pending_test_id == test_id, Pending.test_indicator == "test").all()
        self.assertEqual(len(queries), 0)



