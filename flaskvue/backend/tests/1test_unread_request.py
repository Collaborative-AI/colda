from base64 import b64encode
from datetime import datetime, timedelta
import json
import unittest
from Items import create_app, db
from Items.models import User, Message, Notification, Matched
from tests import TestConfig


class Unread_Request_APITestCase(unittest.TestCase):
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

    def test_unread_request_one_user(self):

        # Simulate 1 recipient.
        # 1. Construct 1 Matched row in find_recipient().
        # 2. Check recipient Notification
        # 3. update request notification
        # 4. check update notification
        # 5. Recipient uploads the ID file
        # 6. Check Updated Notification

        u1 = User(username='unittest', email='john@163.com')
        u1.set_password('123')
        u2 = User(username='unittest2', email='john@163.com')
        u2.set_password('123')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()

        # 1. 附带JWT到请求头中, Construct 1 Matched row in find_recipient first.
        headers = self.get_token_auth_headers('unittest', '123')
        list_content = [2]
        file = [['a','b','c'],[0,1,2],[4,5,6],[1,3,6],[]]
        data = json.dumps({'recipient_id_list': list_content, 'id_file': file})
        response = self.client.post('/find_recipient/', headers=headers, data=data)
        json_response = json.loads(response.get_data(as_text=True))
        task_id = json_response['task_id']

        # 2. Check the Notification of user 2
        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response[-1]['name'], "unread request")
        self.assertEqual(json_response[-1]['payload'], 1)
        
        # 3. update request notification
        data = json.dumps({'response_data': json_response})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))

        # 4. check update notification
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response[-1]['name'], "unread request")
        self.assertEqual(json_response[-1]['payload'], 0)

        # 5. Recipient uploads the ID file
        headers = self.get_token_auth_headers('unittest2', '123')
        file_content = [['a','b','c'],[0,1,2],[4,5,6],[3,3,6],[]]
        data = json.dumps({'task_id': task_id, 'file': file_content})
        response = self.client.post('/match_recipient_id/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        stored = json_response['stored']
        task_id_response = json_response['task_id']
        self.assertEqual(stored, "recipient match id stored")
        self.assertEqual(task_id, task_id_response)

        # 6. Check Updated Notification
        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response[-2]['name'], "unread request")
        self.assertEqual(json_response[-2]['payload'], 0)
        self.assertEqual(json_response[-1]['name'], "unread match id")
        self.assertEqual(json_response[-1]['payload'], 1)

        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response[-1]['name'], "unread match id")
        self.assertEqual(json_response[-1]['payload'], 1)

    def test_unread_request_two_users(self):

        # Simulate 2 recipients.
        # 1. Construct 2 Matched row in find_recipient().
        # 2. Check recipient Notification
        # 3. update request notification
        # 4. check update notification
        # 5. Recipient uploads the ID file
        # 6. Check Updated Notification

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

        # 1. 附带JWT到请求头中, Construct 1 Matched row in find_recipient first.
        headers = self.get_token_auth_headers('unittest', '123')
        list_content = [2,3]
        file = [['a','b','c'],[0,1,2],[4,5,6],[1,3,6],[]]
        data = json.dumps({'recipient_id_list': list_content, 'id_file': file})
        response = self.client.post('/find_recipient/', headers=headers, data=data)
        json_response = json.loads(response.get_data(as_text=True))
        task_id = json_response['task_id']
        query = Matched.query.filter(Matched.task_id == task_id, Matched.recipient_id_pair == 2, Matched.test_indicator == "train").all()
        self.assertEqual(set(json.loads(query[0].Matched_id_file)), set([0,1,4]))
        query = Matched.query.filter(Matched.task_id == task_id, Matched.recipient_id_pair == 3, Matched.test_indicator == "train").all()
        self.assertEqual(set(json.loads(query[0].Matched_id_file)), set([0,1,4]))

        # 2. Check the Notification of user 2
        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response2 = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response2[-1]['name'], "unread request")
        self.assertEqual(json_response2[-1]['payload'], 1)

         # 2. Check the Notification of user 3
        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response3 = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response3[-1]['name'], "unread request")
        self.assertEqual(json_response3[-1]['payload'], 1)
        
        # 3. update request notification
        headers = self.get_token_auth_headers('unittest2', '123')
        data = json.dumps({'response_data': json_response2})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)

        headers = self.get_token_auth_headers('unittest3', '123')
        data = json.dumps({'response_data': json_response3})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)

        # 4. check update notification
        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response[-1]['name'], "unread request")
        self.assertEqual(json_response[-1]['payload'], 0)

        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response[-1]['name'], "unread request")
        self.assertEqual(json_response[-1]['payload'], 0)

        # 5. Recipient uploads the ID file
        headers = self.get_token_auth_headers('unittest2', '123')
        file_content = [['a','b','c'],[0,1,2],[4,5,6],[3,3,6],[]]
        data = json.dumps({'task_id': task_id, 'file': file_content})
        response = self.client.post('/match_recipient_id/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        stored = json_response['stored']
        task_id_response = json_response['task_id']
        self.assertEqual(stored, "recipient match id stored")
        self.assertEqual(task_id, task_id_response)
        # test matched id file
        query = Matched.query.filter(Matched.task_id == task_id, Matched.recipient_id_pair == 2, Matched.test_indicator == "train").all()
        self.assertEqual(set(json.loads(query[0].Matched_id_file)), set([0,4]))

        # should not exist notification yet
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 0)
        
        headers = self.get_token_auth_headers('unittest3', '123')
        file_content = [['a','b','c'],[0,1,2],[5,5,6],[3,3,6],[]]
        data = json.dumps({'task_id': task_id, 'file': file_content})
        response = self.client.post('/match_recipient_id/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        stored = json_response['stored']
        task_id_response = json_response['task_id']
        self.assertEqual(stored, "recipient match id stored")
        self.assertEqual(task_id, task_id_response)
        # test matched id file
        query = Matched.query.filter(Matched.task_id == task_id, Matched.recipient_id_pair == 3, Matched.test_indicator == "train").all()
        self.assertEqual(set(json.loads(query[0].Matched_id_file)), set([0]))

        # 6. Check Updated Notification
        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response[-2]['name'], "unread request")
        self.assertEqual(json_response[-2]['payload'], 0)
        self.assertEqual(json_response[-1]['name'], "unread match id")
        self.assertEqual(json_response[-1]['payload'], 1)

        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response[-2]['name'], "unread request")
        self.assertEqual(json_response[-2]['payload'], 0)
        self.assertEqual(json_response[-1]['name'], "unread match id")
        self.assertEqual(json_response[-1]['payload'], 1)

        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response[-1]['name'], "unread match id")
        self.assertEqual(json_response[-1]['payload'], 1)

    
    