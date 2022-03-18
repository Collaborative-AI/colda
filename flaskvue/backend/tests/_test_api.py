# -*- coding: utf-8 -*-
from base64 import b64encode
from datetime import datetime, timedelta
import json
import re
import unittest
from Items import create_app, db
from Items.models import User, Matched
from tests import TestConfig


class APITestCase(unittest.TestCase):
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

    ###
    # 404等错误处理
    ###
    def test_404(self):
        # 测试请求不存在的API时
        response = self.client.get('/api/wrong/url')
        self.assertEqual(response.status_code, 404)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['error'], 'Not Found')

    ###
    # 用户认证相关测试
    ###
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
        print('sss', json_response)
        self.assertIsNotNone(json_response.get('token'))
        token = json_response['token']
        return {
            'Authorization': 'Bearer ' + token,
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    def test_get_token(self):
        # 测试用户登录，即获取JWT，需要输入正确的用户名和密码，通过Basic Auth之后发放JWT令牌
        # 首先创建一个测试用户
        u = User(username='john')
        u.set_password('123')
        db.session.add(u)
        db.session.commit()

        # 输入错误的用户密码
        headers = self.get_basic_auth_headers('john', '456')
        response = self.client.post('/tokens', headers=headers)
        self.assertEqual(response.status_code, 401)

        # 输入正确的用户密码
        headers = self.get_basic_auth_headers('john', '123')
        response = self.client.post('/tokens', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertIsNotNone(json_response.get('token'))
        self.assertTrue(re.match(r'(.+)\.(.+)\.(.+)', json_response.get('token')))

    def test_not_attach_jwt(self):
        # 测试请求头Authorization中没有附带JWT时，会返回401错误
        response = self.client.get('users/')
        self.assertEqual(response.status_code, 401)

    def test_attach_jwt(self):
        # 测试请求头Authorization中有附带JWT时，允许访问那些需要认证的API
        # 首先创建一个测试用户
        u = User(username='john', email='john@163.com')
        u.set_password('123')
        db.session.add(u)
        db.session.commit()
        # 附带JWT到请求头中
        headers = self.get_token_auth_headers('john', '123')
        response = self.client.get('/users/', headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_anonymous(self):
        # 有些API不需要认证，比如 /api/posts/
        # response = self.client.get('/api/posts/')
        # self.assertEqual(response.status_code, 200)
        pass
    ###
    # 用户API
    ###
    def get_api_headers(self):
        return {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    def test_create_user(self):
        # 测试用户注册
        # headers = self.get_api_headers()
        # # 1. 用户不传入任何必须的参数时
        # data = json.dumps({})
        # response = self.client.post('/users/', headers=headers, data=data)
        # self.assertEqual(response.status_code, 400)
        # # 2. 缺少 username 时
        # data = json.dumps({'email': 'john@163.com', 'password': '123'})
        # response = self.client.post('/users/', headers=headers, data=data)
        # self.assertEqual(response.status_code, 400)
        # # 3. 缺少 email 时
        # data = json.dumps({'username': 'john', 'password': '123'})
        # response = self.client.post('/users/', headers=headers, data=data)
        # self.assertEqual(response.status_code, 400)
        # # 4. 缺少 password 时
        # data = json.dumps({'username': 'john', 'email': 'john@163.com'})
        # response = self.client.post('/users/', headers=headers, data=data)
        # self.assertEqual(response.status_code, 400)
        # # 5. username 或者 email 已存在时
        # u = User(username='john', email='john@163.com')
        # u.set_password('123')
        # db.session.add(u)
        # db.session.commit()
        # data = json.dumps({'username': 'john', 'email': 'john@163.com', 'password': '123'})
        # response = self.client.post('/users/', headers=headers, data=data)
        # self.assertEqual(response.status_code, 400)
        # json_response = json.loads(response.get_data(as_text=True))
        # self.assertEqual(json_response['message']['username'], 'Please use a different username.')
        # self.assertEqual(json_response['message']['email'], 'Please use a different email address.')
        # # 6. 正确提供参数时
        # data = json.dumps({'username': 'david', 'email': 'david@163.com', 'password': '123'})
        # response = self.client.post('/users/', headers=headers, data=data)
        # self.assertEqual(response.status_code, 201)

        # check length verification
        headers = self.get_api_headers()
        data = json.dumps({'username': 'david', 'email': 'apolloumn.email@gmail.com', 'password': '123'})
        response = self.client.post('/users/', headers=headers, data=data)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['message']['password'], 'please create password between 8 chars and 40 chars')

        # check number verification
        data = json.dumps({'username': 'david', 'email': 'apolloumn.email@gmail.com', 'password': 'aaaaaaaaa'})
        response = self.client.post('/users/', headers=headers, data=data)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['message']['password'], 'Need at least 1 number')
        
        # check uppercase letter verification
        data = json.dumps({'username': 'david', 'email': 'apolloumn.email@gmail.com', 'password': 'aaaaaaaaa1'})
        response = self.client.post('/users/', headers=headers, data=data)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['message']['password'], 'Need at least 1 uppercase letter')

        # check lowercase letter verification
        data = json.dumps({'username': 'david', 'email': 'apolloumn.email@gmail.com', 'password': 'AAAAAAAAA1'})
        response = self.client.post('/users/', headers=headers, data=data)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['message']['password'], 'Need at least 1 lowercase letter')

        # check symbol verification
        data = json.dumps({'username': 'david', 'email': 'apolloumn.email@gmail.com', 'password': 'AAAAAAAAAa1'})
        response = self.client.post('/users/', headers=headers, data=data)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['message']['password'], 'Need at least 1 symbol')

        # check symbol verification
        # data = json.dumps({'username': 'david', 'email': 'david@163.com', 'password': '!AAAAAAAAAa1啊'})
        # response = self.client.post('/users/', headers=headers, data=data)
        # json_response = json.loads(response.get_data(as_text=True))
        # self.assertEqual(json_response['message']['password'], 'please fit in A-Za-z0-9[~!@#\$%\^&\*\(\)\+=\|\\\}\]\{\[:;<,>\?\/""]+ range')

        data = json.dumps({'username': 'david', 'email': 'apolloumn.email@gmail.com', 'password': 'Aa1234567!'})
        response = self.client.post('/users/', headers=headers, data=data)
        json_response = json.loads(response.get_data(as_text=True))
        print("22222", json_response)
        self.assertEqual(response.status_code, 201)
        
        queries = User.query.filter(User.email == 'apolloumn.email@gmail.com').all()
        self.assertEqual(len(queries), 1)
        self.assertEqual(queries[0].confirmed, 'false')

        token = json_response['token']
        headers = self.get_token_auth_headers('david', 'Aa1234567!')
        response = self.client.get('/confirm_email/'+token)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        print("33333", json_response)
        
        if json_response == 'confirmed successfully':
            queries = User.query.filter(User.email == 'apolloumn.email@gmail.com').all()
            self.assertEqual(len(queries), 1)
            self.assertEqual(queries[0].confirmed, 'true')
        
        # self.assertEqual(json_response['message']['password'], 'please fit in A-Za-z0-9[~!@#\$%\^&\*\(\)\+=\|\\\}\]\{\[:;<,>\?\/""]+ range')

        
    # def test_get_users(self):
    #     # 测试获取用户列表
    #     # 首先创建几个测试用户
    #     u1 = User(username='john', email='john@163.com')
    #     u1.set_password('123')
    #     u2 = User(username='david', email='david@163.com')
    #     u2.set_password('123')
    #     u3 = User(username='susan', email='susan@163.com')
    #     u3.set_password('123')
    #     db.session.add(u1)
    #     db.session.add(u2)
    #     db.session.add(u3)
    #     db.session.commit()

    #     # 附带JWT到请求头中
    #     headers = self.get_token_auth_headers('john', '123')
    #     response = self.client.get('/users/', headers=headers)
    #     self.assertEqual(response.status_code, 200)
    #     # 判断返回的用户集合中包含刚创建的这个用户
    #     # json_response = json.loads(response.get_data(as_text=True))
    #     # self.assertEqual(json_response['_meta']['total_items'], 3)
    #     # self.assertIsNotNone(json_response.get('items'))
    #     # self.assertEqual(json_response['items'][0]['username'], 'john')
    #     # self.assertEqual(json_response['items'][1]['username'], 'david')
    #     # self.assertEqual(json_response['items'][2]['username'], 'susan')

    # def test_get_user(self):
    #     # 测试获取一个用户
    #     # 首先创建一个测试用户
    #     headers = self.get_api_headers()
    #     data = json.dumps({'username': 'john', 'email': 'john@163.com', 'password': '123'})
    #     response = self.client.post('/users/', headers=headers, data=data)
    #     self.assertEqual(response.status_code, 201)
    #     url = response.headers.get('Location')
    #     self.assertIsNotNone(url)

    #     # 附带JWT到请求头中
    #     headers = self.get_token_auth_headers('john', '123')
    #     response = self.client.get(url, headers=headers)
    #     self.assertEqual(response.status_code, 200)
    #     # 判断返回的用户是否就是刚创建的这个用户
    #     json_response = json.loads(response.get_data(as_text=True))
    #     self.assertEqual('http://localhost' + json_response['_links']['self'], url)
    #     self.assertEqual(json_response['username'], 'john')
    #     # 请求的自己这个用户，所以响应中会包含 email 字段，不包含 is_following 字段
    #     self.assertIsNotNone(json_response['email'])
        

    