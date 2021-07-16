from base64 import b64encode
from datetime import datetime, timedelta
import json
import unittest
from Items import create_app, db
from Items.models import User, Message, Notification, Matched
from tests import TestConfig


class Send_Situation_APITestCase(unittest.TestCase):

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
    
    def test_initial_round(self):

        # sponsor and 2 recipients, only sponsor would go into this function
        # 1. find_recipient() (in find_recipient.py)
        # 2. send_situation() (in send_situation.py)
        # 3. check new notification

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

        # 1. find_recipient() (in find_recipient.py)
        headers = self.get_token_auth_headers('unittest', '123')
        list_content = [2,3]
        file = [['a','b','c'],[0,1,2],[4,5,6],[1,3,6],[]]
        data = json.dumps({'recipient_id_list': list_content, 'id_file': file})
        response = self.client.post('/find_recipient/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)

        json_response = json.loads(response.get_data(as_text=True))
        task_id = json_response['task_id']

        # 2. send_situation() (in send_situation.py)
        headers = self.get_token_auth_headers('unittest', '123')
        situation_content = [[1,2,3], [4,5,6], [7,8,9]]
        data = json.dumps({'situation': situation_content, 'task_id': task_id})
        response = self.client.post('/send_situation/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)

        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['message'], 'send situation successfully!')

        queries = Message.query.filter(Message.sender_id == 1, Message.task_id == task_id).all()
        self.assertEqual(len(queries), len(list_content)+1)
        for i in range(len(queries)):
            self.assertEqual(queries[i].rounds, 0)
            self.assertEqual(queries[i].sender_id, 1)
            self.assertEqual(json.loads(queries[i].situation), [[1,2,3], [4,5,6], [7,8,9]])
        
        # 3. check new notification
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 1)
        self.assertEqual(json_response[0]['name'], "unread situation")
        self.assertEqual(json_response[0]['payload'], 1)

        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 2)
        self.assertEqual(json_response[1]['name'], "unread situation")
        self.assertEqual(json_response[1]['payload'], 1)

        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 2)
        self.assertEqual(json_response[1]['name'], "unread situation")
        self.assertEqual(json_response[1]['payload'], 1)

    def test_noninitial_round(self):

        # sponsor and 2 recipients, only sponsor would go into this function
        # 1. find_recipient() (in find_recipient.py)
        # 2. send_situation() (in send_situation.py)
        # 3. check new notification
        # 4. send_situation() again (in send_situation.py)
        # 5. Check updated Notification
        
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

        # 1. find_recipient() (in find_recipient.py)
        headers = self.get_token_auth_headers('unittest', '123')
        list_content = [2,3]
        file = [['a','b','c'],[0,1,2],[4,5,6],[1,3,6],[]]
        data = json.dumps({'recipient_id_list': list_content, 'id_file': file})
        response = self.client.post('/find_recipient/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)

        json_response = json.loads(response.get_data(as_text=True))
        task_id = json_response['task_id']

        # 2. send_situation() (in send_situation.py)
        headers = self.get_token_auth_headers('unittest', '123')
        situation_content = [[1,2,3], [4,5,6], [7,8,9]]
        data = json.dumps({'situation': situation_content, 'task_id': task_id})
        response = self.client.post('/send_situation/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)

        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['message'], 'send situation successfully!')

        queries = Message.query.filter(Message.sender_id == 1, Message.task_id == task_id).all()
        self.assertEqual(len(queries), len(list_content)+1)
        for i in range(len(queries)):
            self.assertEqual(queries[i].rounds, 0)
            self.assertEqual(queries[i].sender_id, 1)
            self.assertEqual(json.loads(queries[i].situation), [[1,2,3], [4,5,6], [7,8,9]])
        
        # 3. check new notification
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 1)
        self.assertEqual(json_response[0]['name'], "unread situation")
        self.assertEqual(json_response[0]['payload'], 1)

        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 2)
        self.assertEqual(json_response[1]['name'], "unread situation")
        self.assertEqual(json_response[1]['payload'], 1)

        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 2)
        self.assertEqual(json_response[1]['name'], "unread situation")
        self.assertEqual(json_response[1]['payload'], 1)

        # 4. send_situation() again (in send_situation.py)
        headers = self.get_token_auth_headers('unittest', '123')
        situation_content = [[3,2,1], [4,5,6], [7,8,9]]
        data = json.dumps({'situation': situation_content, 'task_id': task_id})
        response = self.client.post('/send_situation/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)

        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['message'], 'send situation successfully!')

        queries = Message.query.filter(Message.sender_id == 1, Message.task_id == task_id, Message.rounds == 1).all()
        self.assertEqual(len(queries), len(list_content)+1)
        for i in range(len(queries)):
            self.assertEqual(queries[i].rounds, 1)
            self.assertEqual(queries[i].sender_id, 1)
            self.assertEqual(json.loads(queries[i].situation), [[3,2,1], [4,5,6], [7,8,9]])

        # 5. Check updated Notification
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 1)
        self.assertEqual(json_response[0]['name'], "unread situation")
        self.assertEqual(json_response[0]['payload'], 2)

        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 2)
        self.assertEqual(json_response[1]['name'], "unread situation")
        self.assertEqual(json_response[1]['payload'], 2)

        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 2)
        self.assertEqual(json_response[1]['name'], "unread situation")
        self.assertEqual(json_response[1]['payload'], 2)







        

        






        

        

