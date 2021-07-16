from base64 import b64encode
from datetime import datetime, timedelta
import json
import unittest
from Items import create_app, db
from Items.models import User, Message, Notification, Matched
from tests import TestConfig


class FindAPITestCase(unittest.TestCase):
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

    def test_find_recipient_no_data(self):

        # check find_recipient function with no data uploaded
        u1 = User(username='unittest', email='john@163.com')
        u1.set_password('123')
        db.session.add(u1)
        db.session.commit()

        # 附带JWT到请求头中
        headers = self.get_token_auth_headers('unittest', '123')
        
        response = self.client.post('/find_recipient/', headers=headers)
        self.assertEqual(response.status_code, 400)

        data = json.dumps({'recipient_id_list': None})
        response = self.client.post('/find_recipient/', headers=headers, data=data)
        self.assertEqual(response.status_code, 400)

    def test_find_recipient_two_recipients(self):

        # Check 1 sponsor with 2 recipients
        # Construct 2 new Matched rows
        # Check the Notification of each recipient

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

        # 附带JWT到请求头中
        headers = self.get_token_auth_headers('unittest', '123')
        list_content = [2,3]
        file = [['a','b','c'],[0,1,2],[4,5,6],[1,3,6],[]]
        data = json.dumps({'recipient_id_list': list_content, 'id_file': file})
        response = self.client.post('/find_recipient/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)

        json_response = json.loads(response.get_data(as_text=True))
        task_id = json_response['task_id']
        recipient_num = json_response['recipient_num']

        # check Matched database new rows, include sponsor to sponsor
        queries = Matched.query.filter(Matched.task_id == task_id).all()
        self.assertEqual(len(queries), recipient_num+1)
        sponsor_random_id = queries[0].sponsor_random_id
        for i in range(len(queries)):
            self.assertEqual(queries[i].sponsor_id, 1) 
            self.assertEqual(queries[i].task_id, task_id)
            self.assertEqual(queries[i].sponsor_random_id, sponsor_random_id)
            self.assertEqual(set(json.loads(queries[i].Matched_id_file)), set([0, 4, 1]))

        # check the row that sponsor to sponsor
        queries = Matched.query.filter(Matched.task_id == task_id, Matched.recipient_id_pair == 1).all()
        self.assertEqual(len(queries), 1)
        self.assertEqual(queries[0].sponsor_id, 1)
        
        # Check the Notification of user 2
        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)

        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response[-1]['name'], "unread request")
        self.assertEqual(json_response[-1]['payload'], 1)

        # User 3 cannot check the notification of user 2
        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 403)

        # Check the Notification of user 3
        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)

        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response[-1]['name'], "unread request")
        self.assertEqual(json_response[-1]['payload'], 1)

