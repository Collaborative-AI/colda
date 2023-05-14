import json
import unittest
import collections

from base64 import b64encode
from bson import ObjectId
from Items import create_app, pyMongo
from Items.utils import generate_password
from tests import TestConfig

from Items.mongoDB import mongoDB
from Items.mongoDB import train_match, train_match_identifier, train_task, train_message, train_message_situation, train_message_output

class HomePage(unittest.TestCase):

    def setUp(self):
        '''每个测试之前执行'''
        self.app = create_app(TestConfig)  # 创建Flask应用
        self.app_context = self.app.app_context()  # 激活(或推送)Flask应用上下文
        self.app_context.push()
        # db.create_all()  # 通过SQLAlchemy来使用SQLite内存数据库，db.create_all()快速创建所有的数据库表
        self.client = self.app.test_client()  # Flask内建的测试客户端，模拟浏览器行为

    def tearDown(self):
        '''每个测试之后执行'''
        # db.session.remove()
        # db.drop_all()  # 删除所有数据库表
        # self.drop_db_collections()
        self.app_context.pop()  # 退出Flask应用上下文
    
    def test_homepage(self):

        response = self.client.get('/helper_api/testing_get')
        self.assertEqual(response.status_code, 200)
        print(f'response: {response}')
        json_response = json.loads(response.get_data(as_text=True))
        print(f'ceshi: {json_response}')
        print(type(json_response))
        assert json_response == 'test successfully!'