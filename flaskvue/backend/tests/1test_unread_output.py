from base64 import b64encode
from datetime import datetime, timedelta
import json
import unittest
from Items import create_app, db
from Items.models import User, Message, Notification, Matched
from tests import TestConfig


class Unread_Output_APITestCase(unittest.TestCase):

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
    
    def test_update_output_notification(self):

        # sponsor and 2 recipients, only sponsor would go into update_output_notification()
        # 1. find_recipient() (in find_recipient.py)
        # 2. send_situation() (in send_situation.py)
        # 3. send_output() (in unread_situation.py) only recipient can send
        # 4. check new notification
        # 5. update_output_notification() (in unread_output.py)
        # 6. check notification

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
        data = json.dumps({'recipient_id_list': list_content})
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

        # 3. send_output() (in unread_situation.py) only recipient can send
        headers = self.get_token_auth_headers('unittest2', '123')
        output_content = [[3,123,6], [88,5,6], [7,99,9]]
        data = json.dumps({'output': output_content, 'rounds': 0, 'task_id': task_id})
        response = self.client.post('/send_output/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['send_output'], "send output successfully")
        queries = Message.query.filter(Message.recipient_id == 1, Message.task_id == task_id, Message.rounds == 0).all()
        self.assertEqual(len(queries), 2)
        self.assertEqual(queries[1].sender_id, 2)
        self.assertEqual(json.loads(queries[1].output), [[3,123,6], [88,5,6], [7,99,9]])

        # should not have unread output now
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 1)
        self.assertEqual(json_response[0]['name'], "unread situation")
        self.assertEqual(json_response[0]['payload'], 1)

        headers = self.get_token_auth_headers('unittest3', '123')
        output_content = [[6,123,6], [88,5,6], [7,87.6,9]]
        data = json.dumps({'output': output_content, 'rounds': 0, 'task_id': task_id})
        response = self.client.post('/send_output/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['send_output'], "send output successfully")
        queries = Message.query.filter(Message.recipient_id == 1, Message.task_id == task_id, Message.rounds == 0).all()
        self.assertEqual(len(queries), 3)
        self.assertEqual(queries[2].sender_id, 3)
        self.assertEqual(json.loads(queries[2].output), [[6,123,6], [88,5,6], [7,87.6,9]])

        # 4. check new notification
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 2)
        self.assertEqual(json_response[0]['name'], "unread situation")
        self.assertEqual(json_response[0]['payload'], 1)
        self.assertEqual(json_response[1]['name'], "unread output")
        self.assertEqual(json_response[1]['payload'], 2)

        # 5. update_output_notification() (in unread_output.py)
        data = json.dumps({'task_id_list': json_response[-1]['task_id_list']})
        response = self.client.post('/update_output_notification/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response[str(task_id)], 0)

        # 6. check notification
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 2)
        self.assertEqual(json_response[0]['name'], "unread situation")
        self.assertEqual(json_response[0]['payload'], 1)
        self.assertEqual(json_response[1]['name'], "unread output")
        self.assertEqual(json_response[1]['payload'], 0)

    def test_get_user_output(self):

        # sponsor and 2 recipients, only sponsor would go into update_output_notification()
        # 1. find_recipient() (in find_recipient.py)
        # 2. send_situation() (in send_situation.py)
        # 3. send_output() (in unread_situation.py) only recipient can send
        # 4. check new notification
        # 5. update_output_notification() (in unread_output.py)
        # 6. check notification

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
        data = json.dumps({'recipient_id_list': list_content})
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

        # 3. send_output() (in unread_situation.py) only recipient can send
        headers = self.get_token_auth_headers('unittest2', '123')
        output_content = [[3,123,6], [88,5,6], [7,99,9]]
        data = json.dumps({'output': output_content, 'rounds': 0, 'task_id': task_id})
        response = self.client.post('/send_output/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['send_output'], "send output successfully")
        queries = Message.query.filter(Message.recipient_id == 1, Message.task_id == task_id, Message.rounds == 0).all()
        self.assertEqual(len(queries), 2)
        self.assertEqual(queries[1].sender_id, 2)
        self.assertEqual(json.loads(queries[1].output), [[3,123,6], [88,5,6], [7,99,9]])

        # should not have unread output now
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 1)
        self.assertEqual(json_response[0]['name'], "unread situation")
        self.assertEqual(json_response[0]['payload'], 1)

        headers = self.get_token_auth_headers('unittest3', '123')
        output_content = [[6,123,6], [88,5,6], [7,87.6,9]]
        data = json.dumps({'output': output_content, 'rounds': 0, 'task_id': task_id})
        response = self.client.post('/send_output/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['send_output'], "send output successfully")
        queries = Message.query.filter(Message.recipient_id == 1, Message.task_id == task_id, Message.rounds == 0).all()
        self.assertEqual(len(queries), 3)
        self.assertEqual(queries[2].sender_id, 3)
        self.assertEqual(json.loads(queries[2].output), [[6,123,6], [88,5,6], [7,87.6,9]])

        # 4. check new notification
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 2)
        self.assertEqual(json_response[0]['name'], "unread situation")
        self.assertEqual(json_response[0]['payload'], 1)
        self.assertEqual(json_response[1]['name'], "unread output")
        self.assertEqual(json_response[1]['payload'], 2)

        # 5. update_output_notification() (in unread_output.py)
        data = json.dumps({'task_id_list': json_response[-1]['task_id_list']})
        response = self.client.post('/update_output_notification/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response[str(task_id)], 0)

        # 6. check notification
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 2)
        self.assertEqual(json_response[0]['name'], "unread situation")
        self.assertEqual(json_response[0]['payload'], 1)
        self.assertEqual(json_response[1]['name'], "unread output")
        self.assertEqual(json_response[1]['payload'], 0)

        # get_user_output()
        data = json.dumps({'task_id_list': json_response[-1]['task_id_list']})
        data = json.dumps({'task_id': task_id, 'rounds': 0})
        response = self.client.post('/users/1/output/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json.loads(json_response['output'][0]), [[3,123,6], [88,5,6], [7,99,9]])
        self.assertEqual(json.loads(json_response['output'][1]), [[6,123,6], [88,5,6], [7,87.6,9]])

        # only call this function with id that is sponsor
        headers = self.get_token_auth_headers('unittest2', '123')
        data = json.dumps({'task_id': task_id, 'rounds': 0})
        response = self.client.post('/users/2/output/', headers=headers, data=data)
        self.assertEqual(response.status_code, 403)

        # only call this function with id that is sponsor, check if the caller and the id is the same
        headers = self.get_token_auth_headers('unittest2', '123')
        data = json.dumps({'task_id': task_id, 'rounds': 0})
        response = self.client.post('/users/1/output/', headers=headers, data=data)
        self.assertEqual(response.status_code, 403)

        

        
