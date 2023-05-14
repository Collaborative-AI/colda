from base64 import b64encode
from datetime import datetime, timedelta
import json
import unittest
from Items import create_app, db
from Items.models import User, Message, Notification, Matched
from tests import TestConfig


class Unread_Match_ID_APITestCase(unittest.TestCase):

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
    
    def test_update_match_id_notification_one_assistor(self):
        
        # Simulate 1 assistor.
        # 1. Construct 1 Matched row in find_assistor().(find_assistor.py)
        # 2. assistors check notification (unread_request => 1)
        # 3. assistors update request notification
        # 4. assistors check updated notification (unread_request => 0)
        # 5. assistor upload ID file
        # 6. Check the Notification of sponsor and assistor
        # 7. Check update_all_notifications() (update_all_notifications.py)
        # 8. Check updated Notification

        u1 = User(username='unittest', email='john@163.com')
        u1.set_password('123')
        u2 = User(username='unittest2', email='john@163.com')
        u2.set_password('123')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()

        # 1. Construct 1 Matched row in find_assistor.
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/create_new_train_task/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        task_id = json_response['task_id']

        list_content = [2]
        file = [['a','b','c'],[8,1,2],[4,5,6],[3,3,6]]
        data = json.dumps({'assistor_id_list': list_content, 'id_file': file, 'task_id': task_id})
        response = self.client.post('/find_assistor/', headers=headers, data=data)
        json_response = json.loads(response.get_data(as_text=True))
        task_id = json_response['task_id']

        # 2. assistors check notification (unread_request => 1)
        # Check the Notification of user 2
        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response[-1]['name'], "unread request")
        self.assertEqual(json_response[-1]['payload'], 1)

        # 3. update request notification
        headers = self.get_token_auth_headers('unittest2', '123')
        data = json.dumps({'response_data': json_response})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        
        # 4. assistors check updated notification (unread_request => 0)
        # Check the Notification of user 2
        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response[-1]['name'], "unread request")
        self.assertEqual(json_response[-1]['payload'], 0)

        # 5. assistor upload ID file
        headers = self.get_token_auth_headers('unittest2', '123')
        file_content = [['a','b','c'],[0,1,2],[4,5,6],[1,3,6]]
        data = json.dumps({'task_id': task_id, 'file': file_content})
        response = self.client.post('/match_assistor_id/', headers=headers, data=data)
        query = Matched.query.filter(Matched.task_id == task_id, Matched.sponsor_id == 1, Matched.test_indicator == "train").all()
        self.assertEqual(json.loads(query[0].Matched_id_file), [4])

        # 6. Check the Notification of sponsor and assistor
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 1)
        self.assertEqual(json_response[-1]['name'], "unread match id")
        self.assertEqual(json_response[-1]['payload'], 1)

        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response2 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response2), 2)
        self.assertEqual(json_response2[-2]['name'], "unread request")
        self.assertEqual(json_response2[-2]['payload'], 0)
        self.assertEqual(json_response2[-1]['name'], "unread match id")
        self.assertEqual(json_response2[-1]['payload'], 1)

        # 7. Check update_all_notifications() (update_all_notifications.py)
        headers = self.get_token_auth_headers('unittest', '123')
        data = json.dumps({'response_data': json_response})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response["unread match id"]['check_dict'][str(task_id)], 1)

        headers = self.get_token_auth_headers('unittest2', '123')
        data = json.dumps({'response_data': json_response2})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response["unread match id"]['check_dict'][str(task_id)], 0)

        # 8. Check updated Notification
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 1)
        self.assertEqual(json_response[-1]['name'], "unread match id")
        self.assertEqual(json_response[-1]['payload'], 0)

        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 2)
        self.assertEqual(json_response[-2]['name'], "unread request")
        self.assertEqual(json_response[-2]['payload'], 0)
        self.assertEqual(json_response[-1]['name'], "unread match id")
        self.assertEqual(json_response[-1]['payload'], 0)
        

    def test_update_match_id_notification_two_assistors(self):
         # Simulate 1 assistor.
        # 1. Construct 1 Matched row in find_assistor().(find_assistor.py)
        # 2. assistors check notification (unread_request => 1)
        # 3. assistors update request notification
        # 4. assistors check updated notification (unread_request => 0)
        # 5. assistor upload ID file
        # 6. Check the Notification of sponsor and assistor
        # 7. Check update_all_notifications() (update_all_notifications.py)
        # 8. Check updated Notification

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

        # 1. Construct 1 Matched row in find_assistor.
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/create_new_train_task/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        task_id = json_response['task_id']

        list_content = [2,3]
        file = [['a','b','c'],[8,1,2],[4,5,6],[3,3,6]]
        data = json.dumps({'assistor_id_list': list_content, 'id_file': file, 'task_id': task_id})
        response = self.client.post('/find_assistor/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['task_id'], task_id)

        # 2. assistors check notification (unread_request => 1)
        # Check the Notification of user 2
        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response[-1]['name'], "unread request")
        self.assertEqual(json_response[-1]['payload'], 1)

        # Check the Notification of user 3
        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response[-1]['name'], "unread request")
        self.assertEqual(json_response[-1]['payload'], 1)

        # 3. update request notification
        headers = self.get_token_auth_headers('unittest2', '123')
        data = json.dumps({'response_data': json_response})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        
        headers = self.get_token_auth_headers('unittest3', '123')
        data = json.dumps({'response_data': json_response})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)

        # 4. assistors check updated notification (unread_request => 0)
        # Check the Notification of user 2
        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response[-1]['name'], "unread request")
        self.assertEqual(json_response[-1]['payload'], 0)

        # Check the Notification of user 3
        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response[-1]['name'], "unread request")
        self.assertEqual(json_response[-1]['payload'], 0)

        # 5. assistor upload ID file
        headers = self.get_token_auth_headers('unittest2', '123')
        file_content = [['a','b','c'],[0,1,2],[4,5,6],[1,3,6]]
        data = json.dumps({'task_id': task_id, 'file': file_content})
        response = self.client.post('/match_assistor_id/', headers=headers, data=data)
        query = Matched.query.filter(Matched.task_id == task_id, Matched.sponsor_id == 1, Matched.test_indicator == "train").all()
        self.assertEqual(json.loads(query[0].Matched_id_file), [4])

        headers = self.get_token_auth_headers('unittest3', '123')
        file_content = [['a','b','c'],[8,1,2],[4,5,6],[1,3,6]]
        data = json.dumps({'task_id': task_id, 'file': file_content})
        response = self.client.post('/match_assistor_id/', headers=headers, data=data)
        query = Matched.query.filter(Matched.task_id == task_id, Matched.assistor_id_pair == 3, Matched.test_indicator == "train").first()
        self.assertEqual(set(json.loads(query.Matched_id_file)), set([8, 4]))

        # 6. Check the Notification of sponsor and assistor
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 1)
        self.assertEqual(json_response[-1]['name'], "unread match id")
        self.assertEqual(json_response[-1]['payload'], 1)

        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response2 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response2), 2)
        self.assertEqual(json_response2[-2]['name'], "unread request")
        self.assertEqual(json_response2[-2]['payload'], 0)
        self.assertEqual(json_response2[-1]['name'], "unread match id")
        self.assertEqual(json_response2[-1]['payload'], 1)

        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response3 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response3), 2)
        self.assertEqual(json_response3[-2]['name'], "unread request")
        self.assertEqual(json_response3[-2]['payload'], 0)
        self.assertEqual(json_response3[-1]['name'], "unread match id")
        self.assertEqual(json_response3[-1]['payload'], 1)

        # 7. Check update_all_notifications() (update_all_notifications.py)
        headers = self.get_token_auth_headers('unittest', '123')
        data = json.dumps({'response_data': json_response})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response["unread match id"]['check_dict'][str(task_id)], 1)

        headers = self.get_token_auth_headers('unittest2', '123')
        data = json.dumps({'response_data': json_response2})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response["unread match id"]['check_dict'][str(task_id)], 0)

        headers = self.get_token_auth_headers('unittest3', '123')
        data = json.dumps({'response_data': json_response3})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response["unread match id"]['check_dict'][str(task_id)], 0)

        # 8. Check updated Notification
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 1)
        self.assertEqual(json_response[-1]['name'], "unread match id")
        self.assertEqual(json_response[-1]['payload'], 0)

        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 2)
        self.assertEqual(json_response[-2]['name'], "unread request")
        self.assertEqual(json_response[-2]['payload'], 0)
        self.assertEqual(json_response[-1]['name'], "unread match id")
        self.assertEqual(json_response[-1]['payload'], 0)

        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 2)
        self.assertEqual(json_response[-2]['name'], "unread request")
        self.assertEqual(json_response[-2]['payload'], 0)
        self.assertEqual(json_response[-1]['name'], "unread match id")
        self.assertEqual(json_response[-1]['payload'], 0)
            
