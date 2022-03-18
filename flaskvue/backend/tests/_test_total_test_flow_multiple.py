from base64 import b64encode
from datetime import datetime, timedelta
import json
import unittest
from Items import create_app, db
from Items.models import User, Message, Notification, Matched
from tests import TestConfig


class Test_total_flow_APITestCase(unittest.TestCase):

    def setUp(self):
        '''每个测试之前执行'''
        self.app = create_app(TestConfig)  # 创建Flask应用
        self.app_context = self.app.app_context()  # 激活(或推送)Flask应用上下文
        self.app_context.push()
        db.create_all()  # 通过SQLAlchemy来使用SQLite内存数据库，db.create_all()快速创建所有的数据库表
        self.client = self.app.test_client()  # Flask内建的测试客户端，模拟浏览器行为

    def tearDown(self):
        '''每个测试之后执行'''
        db.session.remove()
        db.drop_all()  # 删除所有数据库表
        self.app_context.pop()  # 退出Flask应用上下文

    def get_basic_auth_headers(self, username, password):
        '''创建Basic Auth认证的headers'''
        return {
            'Authorization': 'Basic ' + b64encode(
                (username + ':' + password).encode('utf-8')).decode('utf-8'),
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    def get_token_auth_headers(self, username, password):
        '''创建JSON Web Token认证的headers'''
        headers = self.get_basic_auth_headers(username, password)
        response = self.client.post('/tokens', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertIsNotNone(json_response.get('token'))
        token = json_response['token']
        return {
            'Authorization': 'Bearer ' + token,
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    
    def test_total_flow_one_task_id_multiple_tests(self):

        # 1 sponsor and 2 assistors:

        # 1. sponsor call: find_assistor() (in finc_assistor.py)
        # 2. get task_id

        # 3. assistors check notification (unread_request => 1)
        # 4. assistors call: match_assistor_id() (in match_id.py) and upload file
        # 5. assistors check updated notification (unread_request => 0)
        # 6. sponsor call: match_sponsor_id() (in match_id.py) and upload file
        # 7. sponsor and assistors check notification (unread match id) (unread match id => 1)

        # 8. sponsor and assistors call update_match_id_notification() (in unread_match_id.py) and check updated notification (unread match id => 0)
        # 9. sponsor and assistor call: get_user_match_id() (in unread_match_id.py), get matched id file
        # 10. sponsor calls send_situation() (in send_situation.py)
        # 11. sponsor and assistors check notification (unread situation => 1)
         
        # 12. sponsor and assistors call update_situation_notification() (in unread_situation.py) and check updated notification (unread situation => 0)
        # 13. assistors call send_output() (in unread situation.py)

        # 14. sponsor check notification (unread output => 1)
        # 15. sponsor calls: update_output_notification() (in unread_output.py) and check updated notification (unread output => 0)
        # 16. sponsor calls: get_user_output() (in unread_output.py), gets output files
        # 17. sponsor calls: send_situation(), goes into new round 

        u1 = User(username='unittest', email='john@163.com')
        u1.set_password('123')
        u2 = User(username='unittest2', email='john@163.com')
        u2.set_password('123')
        u3 = User(username='unittest3', email='john@163.com')
        u3.set_password('123')
        db.session.add(u1)
        db.session.add(u2)
        db.session.add(u3)
        db.session.commit()

        # 1. sponsor call: find_assistor() (in finc_assistor.py)
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/create_new_train_task/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        # 2. get task_id
        task_id = json_response['task_id']

        list_content = [2,3]
        file = [['a','b','c'],[8,1,2],[4,5,6],[3,3,6],[12],[16],[17,19]]
        data = json.dumps({'assistor_id_list': list_content, 'id_file': file, 'task_id': task_id})
        response = self.client.post('/find_assistor/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['task_id'], task_id)

        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/create_new_test_task/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        test_id_1 = json_response['test_id']

        response = self.client.get('/create_new_test_task/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        test_id_2 = json_response['test_id']

        file = [['a','b','c'],[8,1,2],[4,5,6],[3,3,6],[12],[16],[17,19]]
        data = json.dumps({'task_id': task_id, 'id_file': file, 'test_id': test_id_1})
        response = self.client.post('/find_test_assistor/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['task_id'], task_id)
        self.assertEqual(json_response['test_id'], test_id_1)

        file = [['a','b','c'],[8],[4]]
        data = json.dumps({'task_id': task_id, 'id_file': file, 'test_id': test_id_2})
        response = self.client.post('/find_test_assistor/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['task_id'], task_id)
        self.assertEqual(json_response['test_id'], test_id_2)

        
        # 3. assistors check notification (unread_request => 1)
        # Check the Notification of user 2
        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response2 = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response2[-1]['name'], "unread test request")
        self.assertEqual(json_response2[-1]['payload'], 2)

        # User 3 cannot check the notification of user 2
        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 403)

        # Check the Notification of user 3
        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response3 = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response3[-1]['name'], "unread test request")
        self.assertEqual(json_response3[-1]['payload'], 2)

        # 4. update request notification
        headers = self.get_token_auth_headers('unittest2', '123')
        data = json.dumps({'response_data': json_response2})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)

        headers = self.get_token_auth_headers('unittest3', '123')
        data = json.dumps({'response_data': json_response3})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)

        # 5. assistors check updated notification (unread_request => 0)
        # Check the Notification of user 2
        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response[-1]['name'], "unread test request")
        self.assertEqual(json_response[-1]['payload'], 0)

        # Check the Notification of user 3
        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response[-1]['name'], "unread test request")
        self.assertEqual(json_response[-1]['payload'], 0)

        # 6. assistors call: match_assistor_id() (in match_id.py) and upload file
        # assistors upload ID file
        headers = self.get_token_auth_headers('unittest2', '123')
        file_content = [['a','b','c'],[0,1,2],[4,5,6],[1,3,6],[12],[16],[17],[18]]
        data = json.dumps({'test_id': test_id_1, 'file': file_content})
        response = self.client.post('/match_test_assistor_id/', headers=headers, data=data)

        headers = self.get_token_auth_headers('unittest3', '123')
        file_content = [['a','b','c'],[2,1,2],[3,5,6],[4,3,6],[5],[12],[18]]
        data = json.dumps({'test_id': test_id_1, 'file': file_content})
        response = self.client.post('/match_test_assistor_id/', headers=headers, data=data)

        headers = self.get_token_auth_headers('unittest2', '123')
        file_content = [['a','b','c'],[8]]
        data = json.dumps({'test_id': test_id_2, 'file': file_content})
        response = self.client.post('/match_test_assistor_id/', headers=headers, data=data)

        headers = self.get_token_auth_headers('unittest3', '123')
        file_content = [['a','b','c'],[4]]
        data = json.dumps({'test_id': test_id_2, 'file': file_content})
        response = self.client.post('/match_test_assistor_id/', headers=headers, data=data)

        # 5. assistors check updated notification (unread_request => 0)
        # Check the Notification of sponsor
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_1 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response_1), 1)
        self.assertEqual(json_response_1[-1]['name'], "unread test match id")
        self.assertEqual(json_response_1[-1]['payload'], 2)

        # Check the Notification of user 2
        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_2 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response_2), 3)
        self.assertEqual(json_response_2[-2]['name'], "unread test request")
        self.assertEqual(json_response_2[-2]['payload'], 0)
        self.assertEqual(json_response_2[-1]['name'], "unread test match id")
        self.assertEqual(json_response_2[-1]['payload'], 2)

        # Check the Notification of user 3
        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_3 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response_3), 3)
        self.assertEqual(json_response_3[-2]['name'], "unread test request")
        self.assertEqual(json_response_3[-2]['payload'], 0)
        self.assertEqual(json_response_3[-1]['name'], "unread test match id")
        self.assertEqual(json_response_3[-1]['payload'], 2)

        # 6. sponsor and assistors call update_match_id_notification() (in unread_match_id.py) and check updated notification (unread match id => 0)
        headers = self.get_token_auth_headers('unittest', '123')
        data = json.dumps({'response_data': json_response_1})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response_1 = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response_1["unread test match id"]['check_dict'][str(test_id_1)], 1)
        self.assertEqual(json_response_1["unread test match id"]['check_dict'][str(test_id_2)], 1)

        headers = self.get_token_auth_headers('unittest2', '123')
        data = json.dumps({'response_data': json_response_2})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response_2 = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response_2["unread test match id"]['check_dict'][str(test_id_1)], 0)
        self.assertEqual(json_response_2["unread test match id"]['check_dict'][str(test_id_2)], 0)

        headers = self.get_token_auth_headers('unittest3', '123')
        data = json.dumps({'response_data': json_response_3})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response_3 = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response_3["unread test match id"]['check_dict'][str(test_id_1)], 0)
        self.assertEqual(json_response_3["unread test match id"]['check_dict'][str(test_id_2)], 0)
        
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 1)
        self.assertEqual(json_response[-1]['name'], "unread test match id")
        self.assertEqual(json_response[-1]['payload'], 0)

        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 3)
        self.assertEqual(json_response[-2]['name'], "unread test request")
        self.assertEqual(json_response[-2]['payload'], 0)
        self.assertEqual(json_response[-1]['name'], "unread test match id")
        self.assertEqual(json_response[-1]['payload'], 0)

        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 3)
        self.assertEqual(json_response[-2]['name'], "unread test request")
        self.assertEqual(json_response[-2]['payload'], 0)
        self.assertEqual(json_response[-1]['name'], "unread test match id")
        self.assertEqual(json_response[-1]['payload'], 0)

        # 9. sponsor and assistor call: get_user_match_id() (in unread_match_id.py), get matched id file
        headers = self.get_token_auth_headers('unittest', '123')
        data = json.dumps({'test_id': test_id_1})
        response = self.client.post('/users/1/test_identifier_content/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertIsNotNone(json_response.get('identifier_content'))
        self.assertIsNotNone(json_response.get('assistor_random_id_pair'))
        # test match id file
        identifier_content_list = json_response['identifier_content']
        self.assertEqual(set(json.loads(identifier_content_list[0])), set([4,12,16,17]))
        self.assertEqual(set(json.loads(identifier_content_list[1])), set([3,4,12]))

        headers = self.get_token_auth_headers('unittest', '123')
        data = json.dumps({'test_id': test_id_2})
        response = self.client.post('/users/1/test_identifier_content/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertIsNotNone(json_response.get('identifier_content'))
        self.assertIsNotNone(json_response.get('assistor_random_id_pair'))
        # test match id file
        identifier_content_list = json_response['identifier_content']
        self.assertEqual(set(json.loads(identifier_content_list[0])), set([8]))
        self.assertEqual(set(json.loads(identifier_content_list[1])), set([4]))

        headers = self.get_token_auth_headers('unittest2', '123')
        data = json.dumps({'test_id': test_id_1})
        response = self.client.post('/users/2/test_identifier_content/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertIsNotNone(json_response.get('identifier_content'))
        self.assertIsNotNone(json_response.get('sponsor_random_id'))
        # test match id file
        identifier_content_list = json_response['identifier_content']
        self.assertEqual(set(json.loads(identifier_content_list[0])), set([4,12,16,17]))

        headers = self.get_token_auth_headers('unittest2', '123')
        data = json.dumps({'test_id': test_id_2})
        response = self.client.post('/users/2/test_identifier_content/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertIsNotNone(json_response.get('identifier_content'))
        self.assertIsNotNone(json_response.get('sponsor_random_id'))
        # test match id file
        identifier_content_list = json_response['identifier_content']
        self.assertEqual(set(json.loads(identifier_content_list[0])), set([8]))
        
        headers = self.get_token_auth_headers('unittest3', '123')
        data = json.dumps({'test_id': test_id_1})
        response = self.client.post('/users/3/test_identifier_content/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertIsNotNone(json_response.get('identifier_content'))
        self.assertIsNotNone(json_response.get('sponsor_random_id'))
        # test match id file
        identifier_content_list = json_response['identifier_content']
        self.assertEqual(set(json.loads(identifier_content_list[0])), set([3,4,12]))

        headers = self.get_token_auth_headers('unittest3', '123')
        data = json.dumps({'test_id': test_id_2})
        response = self.client.post('/users/3/test_identifier_content/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertIsNotNone(json_response.get('identifier_content'))
        self.assertIsNotNone(json_response.get('sponsor_random_id'))
        # test match id file
        identifier_content_list = json_response['identifier_content']
        self.assertEqual(set(json.loads(identifier_content_list[0])), set([4]))
        
        # 13. assistors call send_output() (in unread situation.py)
        headers = self.get_token_auth_headers('unittest2', '123')
        output_content = [[[3,123,6], [88,5,6], [7,99,9]],[[1,2]]]
        data = json.dumps({'output': output_content, 'test_id': test_id_1})
        response = self.client.post('/send_test_output/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['send_test_output'], "send test output successfully")
        queries = Message.query.filter(Message.assistor_id == 1, Message.test_id == test_id_1, Message.test_indicator == "test").all()
        self.assertEqual(len(queries),1)
        self.assertEqual(queries[-1].sender_id, 2)
        self.assertEqual(json.loads(queries[-1].output), [[[3,123,6], [88,5,6], [7,99,9]],[[1,2]]])

        output_content = [[[1,2]]]
        data = json.dumps({'output': output_content, 'test_id': test_id_2})
        response = self.client.post('/send_test_output/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['send_test_output'], "send test output successfully")
        queries = Message.query.filter(Message.assistor_id == 1, Message.test_id == test_id_2, Message.test_indicator == "test").all()
        self.assertEqual(len(queries),1)
        self.assertEqual(queries[-1].sender_id, 2)
        self.assertEqual(json.loads(queries[-1].output), [[[1,2]]])

        headers = self.get_token_auth_headers('unittest3', '123')
        output_content = [[6,123,6], [88,5,6], [7,87.6,9]]
        data = json.dumps({'output': output_content, 'test_id': test_id_1})
        response = self.client.post('/send_test_output/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['send_test_output'], "send test output successfully")
        queries = Message.query.filter(Message.assistor_id == 1, Message.test_id == test_id_1, Message.test_indicator == "test").all()
        self.assertEqual(len(queries), 2)
        self.assertEqual(queries[-1].sender_id, 3)
        self.assertEqual(json.loads(queries[-1].output), [[6,123,6], [88,5,6], [7,87.6,9]])

        output_content = [[7,87.6,9]]
        data = json.dumps({'output': output_content, 'test_id': test_id_2})
        response = self.client.post('/send_test_output/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['send_test_output'], "send test output successfully")
        queries = Message.query.filter(Message.assistor_id == 1, Message.test_id == test_id_2, Message.test_indicator == "test").all()
        self.assertEqual(len(queries), 2)
        self.assertEqual(queries[-1].sender_id, 3)
        self.assertEqual(json.loads(queries[-1].output), [[7,87.6,9]])

        # 14. sponsor check notification (unread output => 1)
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 2)
        self.assertEqual(json_response[-1]['name'], "unread test output")
        self.assertEqual(json_response[-1]['payload'], 4)

        # 15. sponsor calls: update_output_notification() (in unread_output.py) and check updated notification (unread output => 0)
        data = json.dumps({'response_data': json_response})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        # check rounds
        self.assertEqual(json_response["unread test output"]['check_dict'][str(test_id_1)], 1)
        self.assertEqual(json_response["unread test output"]['check_dict'][str(test_id_2)], 1)

        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 2)
        self.assertEqual(json_response[-1]['name'], "unread test output")
        self.assertEqual(json_response[-1]['payload'], 0)

        # 16. sponsor calls: get_user_output() (in unread_output.py), gets output files
        data = json.dumps({'test_id': test_id_1})
        response = self.client.post('/test_output/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json.loads(json_response['output'][0]), [[[3,123,6], [88,5,6], [7,99,9]],[[1,2]]])
        self.assertEqual(json.loads(json_response['output'][1]), [[6,123,6], [88,5,6], [7,87.6,9]])

        data = json.dumps({'test_id': test_id_2})
        response = self.client.post('/test_output/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json.loads(json_response['output'][0]), [[[1,2]]])
        self.assertEqual(json.loads(json_response['output'][1]), [[7,87.6,9]])
