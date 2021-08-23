from base64 import b64encode
from datetime import datetime, timedelta
import json
import unittest
from Items import create_app, db
from Items.models import User, Message, Notification, Matched
from tests import TestConfig


class Test_Helper_Func_APITestCase(unittest.TestCase):

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
    
    def test_get_notification(self):

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

        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/ceshi/device_id=88DD/6', headers=headers)
        self.assertEqual(response.status_code, 200)
    
    # def test_delete_all_rows(self):

    #     u1 = User(username='unittest', email='john@163.com')
    #     u1.set_password('123')
    #     u2 = User(username='unittest2', email='john@163.com')
    #     u2.set_password('123')
    #     u3 = User(username='unittest3', email='john@163.com')
    #     u3.set_password('123')
    #     db.session.add(u1)
    #     db.session.add(u2)
    #     db.session.add(u3)
    #     db.session.commit()

    #     headers = self.get_token_auth_headers('unittest', '123')
    #     list_content = [2,3]
    #     data = json.dumps({'assistor_id_list': list_content})
    #     response = self.client.post('/find_assistor/', headers=headers, data=data)
    #     self.assertEqual(response.status_code, 200)

    #     headers = self.get_token_auth_headers('unittest2', '123')
    #     response = self.client.get('/delete_all_rows/', headers=headers)
    #     self.assertEqual(response.status_code, 200)

    #     queries = Matched.query.all()
    #     self.assertEqual(len(queries), 0)