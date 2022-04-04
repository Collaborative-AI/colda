import json
import unittest

from base64 import b64encode
from datetime import datetime, timedelta
from bson import ObjectId
from Items import create_app, pyMongo
from Items.utils import generate_password
from tests import TestConfig

from Items.mongoDB import mongoDB
from Items.mongoDB import train_match, train_match_identifier, train_task, train_message, train_message_situation, train_message_output

class user_API_TestCase(unittest.TestCase):

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
        self.drop_db_collections()
        self.app_context.pop()  # 退出Flask应用上下文

    def drop_db_collections(self):
        pyMongo.db.User.drop()
        pyMongo.db.Notification.drop()
        pyMongo.db.Pending.drop()
        pyMongo.db.Train_Message.drop()
        pyMongo.db.Train_Message_Situation.drop()
        pyMongo.db.Train_Message_Output.drop()
        pyMongo.db.Test_Message.drop()
        pyMongo.db.Test_Message_Situation.drop()
        pyMongo.db.Test_Message_Output.drop()
        pyMongo.db.Train_Match.drop()
        pyMongo.db.Train_Match_Identifier.drop()
        pyMongo.db.Test_Match.drop()
        pyMongo.db.Test_Match_Identifier.drop()
        pyMongo.db.Train_Task.drop()
        pyMongo.db.Test_Task.drop()
        pyMongo.db.Stop.drop()

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
        response = self.client.post('/auth/tokens', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertIsNotNone(json_response.get('token'))
        token = json_response['token']
        return {
            'Authorization': 'Bearer ' + token,
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    
    def test_create_user(self):
        pass

    

        