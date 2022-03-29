import json
import unittest

from base64 import b64encode
from datetime import datetime, timedelta
from bson import ObjectId
from Items import create_app, pyMongo
from tests import TestConfig
from Items.utils import generate_password

from Items.mongoDB import mongoDB
from Items.mongoDB import train_match, train_match_identifier, train_task, train_message, train_message_situation, train_message_output
from Items.mongoDB import test_match, test_match_identifier, test_task, test_message, test_message_output

class Test_Helper_API_TestCase(unittest.TestCase):
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
    
    
    def find_test_assistor_two_assistors_helper(self):

        # Check 1 sponsor with 2 assistors
        # Construct 2 new Matched rows
        # Check the Notification of each assistor

        newObjectId = ObjectId()
        user_id_1 = str(newObjectId)
        password_hash = generate_password('Xie1@456')
        new_user_document = {
            '_id': newObjectId,
            'user_id': user_id_1,
            'username': 'unittest1',
            'name': None,
            'authority_level': 'user',
            'email': 'john1@163.com',
            'password_hash': password_hash,
            'confirm_email': True
        }
        user_document = mongoDB.search_user_document(user_id=None, username='unittest1', 
                                        email=None, key_indicator='username')
        if user_document == None:
            mongoDB.create_user_document(user_document=new_user_document)
        else:
            user_id_1 = user_document['user_id']

        newObjectId = ObjectId()
        user_id_2 = str(newObjectId)
        password_hash = generate_password('Xie1@456')
        new_user_document = {
            '_id': newObjectId,
            'user_id': user_id_2,
            'username': 'unittest2',
            'name': None,
            'authority_level': 'user',
            'email': 'john2@163.com',
            'password_hash': password_hash,
            'confirm_email': True
        }
        user_document = mongoDB.search_user_document(user_id=None, username='unittest2', 
                                        email=None, key_indicator='username')
        if user_document == None:
            mongoDB.create_user_document(user_document=new_user_document)
        else:
            user_id_2 = user_document['user_id']

        newObjectId = ObjectId()
        user_id_3 = str(newObjectId)
        password_hash = generate_password('Xie1@456')
        new_user_document = {
            '_id': newObjectId,
            'user_id': user_id_3,
            'username': 'unittest3',
            'name': None,
            'authority_level': 'user',
            'email': 'john3@163.com',
            'password_hash': password_hash,
            'confirm_email': True
        }
        user_document = mongoDB.search_user_document(user_id=None, username='unittest3', 
                                        email=None, key_indicator='username')
        if user_document == None:
            mongoDB.create_user_document(user_document=new_user_document)
        else:
            user_id_3 = user_document['user_id']

        print('test_user_id_1', user_id_1)
        print('test_user_id_2', user_id_2)
        print('test_user_id_3', user_id_3)

        # 附带JWT到请求头中
        headers = self.get_token_auth_headers('unittest1', 'Xie1@456')
        response = self.client.get('/main_flow/create_new_train_task/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        task_id = json_response['task_id']

        assistor_username_list = ['unittest2', 'unittest3']
        identifier_content = [0, 4, 1]
        data = json.dumps({
            'assistor_username_list': assistor_username_list, 
            'identifier_content': identifier_content, 
            'task_id': task_id, 
            'task_mode': 'regression', 
            'model_name': 'LinearRegression', 
            'metric_name': 'RMSE',
            'task_name': 'unittest', 
            'task_description': 'unittest_desciption'
        })
        response = self.client.post('/main_flow/find_assistor/' + user_id_1, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['task_id'], task_id)
        assistor_num = json_response['assistor_num']

        # check Train_Match database new rows, include sponsor to sponsor
        train_match_document = train_match.search_train_match_document(task_id=task_id)
        total_assistor_num = train_match_document['total_assistor_num']
        sponsor_id = train_match_document['sponsor_information']['sponsor_id']
        sponsor_information = train_match_document['sponsor_information']
        assistor_information = train_match_document['assistor_information']
        sponsor_terminate_id_dict = train_match_document['sponsor_terminate_id_dict']
        assistor_terminate_id_dict = train_match_document['assistor_terminate_id_dict']
        sponsor_random_id_mapping = train_match_document['sponsor_random_id_mapping']
        asssistor_random_id_mapping = train_match_document['assistor_random_id_mapping']
        sponsor_random_id = sponsor_information[sponsor_id]['sponsor_id_to_random_id']
        sponsor_identifier_id = sponsor_information[sponsor_id]['identifier_id']

        self.assertEqual(train_match_document['task_id'], task_id)
        self.assertEqual(total_assistor_num, assistor_num)
        self.assertEqual(sponsor_id, user_id_1)
        self.assertEqual(sponsor_random_id_mapping[sponsor_random_id], sponsor_id)
        self.assertEqual(len(assistor_information), 0)
        self.assertEqual(len(asssistor_random_id_mapping), 0)
        self.assertEqual(len(sponsor_terminate_id_dict), 0)
        self.assertEqual(len(assistor_terminate_id_dict), 0)

        train_task_document = train_task.search_train_task_document(task_id=task_id)
        task_name = train_task_document['task_name']
        task_description = train_task_document['task_description']
        task_mode = train_task_document['task_mode']
        model_name = train_task_document['model_name']
        metric_name = train_task_document['metric_name']
        assistor_id_list = train_task_document['assistor_id_list']
        test_task_list = train_task_document['test_task_list']

        self.assertEqual(train_task_document['task_id'], task_id)
        self.assertEqual(task_name, 'unittest')
        self.assertEqual(task_description, 'unittest_desciption')
        self.assertEqual(task_mode, 'regression')
        self.assertEqual(model_name, 'LinearRegression')
        self.assertEqual(metric_name, 'RMSE')
        self.assertEqual(train_task_document['sponsor_id'], sponsor_id)
        self.assertEqual(assistor_id_list, [user_id_2, user_id_3])
        self.assertEqual(len(test_task_list), 0)

        # 5. assistor uploads the ID file
        headers = self.get_token_auth_headers('unittest2', 'Xie1@456')
        identifier_content = [0, 4, 1, 12, 16, 17, 18]
        data = json.dumps({
            'task_id': task_id, 
            'identifier_content': identifier_content
        })
        response = self.client.post('/main_flow/match_identifier_content/' + user_id_2, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        stored = json_response['stored']
        task_id_response = json_response['task_id']
        self.assertEqual(stored, "assistor match id stored")
        self.assertEqual(task_id, task_id_response)

        headers = self.get_token_auth_headers('unittest3', 'Xie1@456')
        identifier_content = [2, 3, 4, 5, 12, 18]
        data = json.dumps({
            'task_id': task_id, 
            'identifier_content': identifier_content
        })
        response = self.client.post('/main_flow/match_identifier_content/' + user_id_3, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        stored = json_response['stored']
        task_id_response = json_response['task_id']
        self.assertEqual(stored, "assistor match id stored")
        self.assertEqual(task_id, task_id_response)

        # should not exist notification yet for sponsor
        headers = self.get_token_auth_headers('unittest1', 'Xie1@456')
        response = self.client.get('/main_flow/get_notifications/' + user_id_1, headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response['notification_result']['category']), 1)

        # Check the Notification of user 2
        headers = self.get_token_auth_headers('unittest2', 'Xie1@456')
        response = self.client.get('/main_flow/get_notifications/' + user_id_2, headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_2 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response_2['notification_result']['category']), 2)
        self.assertEqual(len(json_response_2['notification_result']['category']['unread_request']['task_id_dict']), 1)
        assert task_id in json_response_2['notification_result']['category']['unread_request']['task_id_dict']

        # User 3 cannot check the notification of user 2
        headers = self.get_token_auth_headers('unittest3', 'Xie1@456')
        response = self.client.get('/main_flow/get_notifications/' + user_id_2, headers=headers)
        self.assertEqual(response.status_code, 403)

        # Check the Notification of user 3
        headers = self.get_token_auth_headers('unittest3', 'Xie1@456')
        response = self.client.get('/main_flow/get_notifications/' + user_id_3, headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_3 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response_3['notification_result']['category']), 2)
        self.assertEqual(len(json_response_3['notification_result']['category']['unread_request']['task_id_dict']), 1)
        assert task_id in json_response_3['notification_result']['category']['unread_request']['task_id_dict']

        # create test id
        headers = self.get_token_auth_headers('unittest1', 'Xie1@456')
        response = self.client.get('/main_flow/create_new_test_task/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        test_id = json_response['test_id']

        identifier_content = [8, 4, 3]
        data = json.dumps({
            'identifier_content': identifier_content, 
            'task_id': task_id, 
            'test_id': test_id,
            'task_mode': 'regression', 
            'model_name': 'LinearRegression', 
            'metric_name': 'RMSE',
            'test_name': 'unittest', 
            'test_description': 'unittest_desciption'
        })
        response = self.client.post('/main_flow/find_test_assistor/' + user_id_1, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['task_id'], task_id)
        self.assertEqual(json_response['test_id'], test_id)
        assistor_num = json_response['assistor_num']

        # check Test_Match database new rows, include sponsor to sponsor
        test_match_document = test_match.search_test_match_document(test_id=test_id)
        total_assistor_num = test_match_document['total_assistor_num']
        sponsor_id = test_match_document['sponsor_information']['sponsor_id']
        sponsor_information = test_match_document['sponsor_information']
        assistor_information = test_match_document['assistor_information']
        sponsor_terminate_id_dict = test_match_document['sponsor_terminate_id_dict']
        assistor_terminate_id_dict = test_match_document['assistor_terminate_id_dict']
        sponsor_random_id_mapping = test_match_document['sponsor_random_id_mapping']
        asssistor_random_id_mapping = test_match_document['assistor_random_id_mapping']
        sponsor_random_id = sponsor_information[sponsor_id]['sponsor_id_to_random_id']
        sponsor_identifier_id = sponsor_information[sponsor_id]['identifier_id']

        self.assertEqual(test_match_document['task_id'], task_id)
        self.assertEqual(test_match_document['test_id'], test_id)
        self.assertEqual(total_assistor_num, assistor_num)
        self.assertEqual(sponsor_id, user_id_1)
        self.assertEqual(sponsor_random_id_mapping[sponsor_random_id], sponsor_id)
        self.assertEqual(len(assistor_information), 0)
        self.assertEqual(len(asssistor_random_id_mapping), 0)
        self.assertEqual(len(sponsor_terminate_id_dict), 0)
        self.assertEqual(len(assistor_terminate_id_dict), 0)
        
        train_task_document = train_task.search_train_task_document(task_id=task_id)
        test_task_list = train_task_document['test_task_list']
        self.assertEqual(len(test_task_list), 1)
        self.assertEqual(test_task_list[0], test_id)

        test_task_document = test_task.search_test_task_document(test_id=test_id)
        test_name = test_task_document['test_name']
        test_description = test_task_document['test_description']
        task_mode = test_task_document['task_mode']
        model_name = test_task_document['model_name']
        metric_name = test_task_document['metric_name']
        assistor_id_list = test_task_document['assistor_id_list']

        self.assertEqual(train_task_document['task_id'], task_id)
        self.assertEqual(test_name, 'unittest')
        self.assertEqual(test_description, 'unittest_desciption')
        self.assertEqual(task_mode, 'regression')
        self.assertEqual(model_name, 'LinearRegression')
        self.assertEqual(metric_name, 'RMSE')
        self.assertEqual(train_task_document['sponsor_id'], sponsor_id)
        self.assertEqual(assistor_id_list, [user_id_2, user_id_3])

        assistor_username_list = ['unittest2', 'unittest3']
        user_id_list = [user_id_1, user_id_2, user_id_3]
        return task_id, test_id, assistor_username_list, user_id_list

    def unread_test_request_two_users_helper(self, task_id, test_id, assistor_username_list, user_id_list):
        
        user_id_1 = user_id_list[0]
        user_id_2 = user_id_list[1]
        user_id_3 = user_id_list[2]

        # Check the Notification of user 1
        headers = self.get_token_auth_headers('unittest1', 'Xie1@456')
        response = self.client.get('/main_flow/get_notifications/' + user_id_1, headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_1 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response_1['notification_result']['category']), 0)

        # Check the Notification of user 2
        headers = self.get_token_auth_headers('unittest2', 'Xie1@456')
        response = self.client.get('/main_flow/get_notifications/' + user_id_2, headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_2 = json.loads(response.get_data(as_text=True))
        print('json_response_2', json_response_2)
        self.assertEqual(len(json_response_2['notification_result']['category']), 1)
        self.assertEqual(len(json_response_2['notification_result']['category']['unread_test_request']['test_id_dict']), 1)
        assert test_id in json_response_2['notification_result']['category']['unread_test_request']['test_id_dict']

        # User 3 cannot check the notification of user 2
        headers = self.get_token_auth_headers('unittest3', 'Xie1@456')
        response = self.client.get('/main_flow/get_notifications/' + user_id_2, headers=headers)
        self.assertEqual(response.status_code, 403)

        # Check the Notification of user 3
        headers = self.get_token_auth_headers('unittest3', 'Xie1@456')
        response = self.client.get('/main_flow/get_notifications/' + user_id_3, headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_3 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response_3['notification_result']['category']), 1)
        self.assertEqual(len(json_response_3['notification_result']['category']['unread_test_request']['test_id_dict']), 1)
        assert test_id in json_response_3['notification_result']['category']['unread_test_request']['test_id_dict']

        # 5. assistor upload ID file
        headers = self.get_token_auth_headers('unittest2', 'Xie1@456')
        identifier_content = [0, 4, 1]
        data = json.dumps({
            'task_id': task_id, 
            'test_id': test_id,
            'identifier_content': identifier_content
        })
        response = self.client.post('/main_flow/match_test_identifier_content/' + user_id_2, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        stored = json_response['stored']
        test_id_response = json_response['test_id']
        self.assertEqual(stored, "assistor test match id stored")
        self.assertEqual(test_id, test_id_response)

        # test test_match_document
        test_match_document = test_match.search_test_match_document(test_id=test_id)
        assistor_information = test_match_document['assistor_information']
        assert user_id_2 in assistor_information
        identifier_id = assistor_information[user_id_2]['identifier_id']

        test_match_identifier_document = test_match_identifier.search_test_match_identifier_document(identifier_id=identifier_id)
        identifier_content = test_match_identifier_document['identifier_content']
        self.assertEqual(set(identifier_content), set([4]))

        headers = self.get_token_auth_headers('unittest3', 'Xie1@456')
        identifier_content = [8, 4, 1]
        data = json.dumps({
            'task_id': task_id, 
            'test_id': test_id,
            'identifier_content': identifier_content
        })
        response = self.client.post('/main_flow/match_test_identifier_content/' + user_id_3, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        stored = json_response['stored']
        test_id_response = json_response['test_id']
        self.assertEqual(stored, "assistor test match id stored")
        self.assertEqual(test_id, test_id_response)

        # test test_match_document
        test_match_document = test_match.search_test_match_document(test_id=test_id)
        assistor_information = test_match_document['assistor_information']
        assert user_id_3 in assistor_information
        identifier_id = assistor_information[user_id_3]['identifier_id']

        test_match_identifier_document = test_match_identifier.search_test_match_identifier_document(identifier_id=identifier_id)
        identifier_content = test_match_identifier_document['identifier_content']
        self.assertEqual(set(identifier_content), set([8, 4]))

        return task_id, test_id, assistor_username_list, user_id_list

    def unread_test_match_id_two_users_helper(self, task_id, test_id, assistor_username_list, user_id_list):

        user_id_1 = user_id_list[0]
        user_id_2 = user_id_list[1]
        user_id_3 = user_id_list[2]

        # Check the Notification of user 2
        headers = self.get_token_auth_headers('unittest1', 'Xie1@456')
        response = self.client.get('/main_flow/get_notifications/' + user_id_1, headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_1 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response_1['notification_result']['category']), 1)
        self.assertEqual(len(json_response_1['notification_result']['category']['unread_test_match_id']['test_id_dict']), 1)
        assert test_id in json_response_1['notification_result']['category']['unread_test_match_id']['test_id_dict']

        # Check the Notification of user 2
        headers = self.get_token_auth_headers('unittest2', 'Xie1@456')
        response = self.client.get('/main_flow/get_notifications/' + user_id_2, headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_2 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response_2['notification_result']['category']), 1)
        self.assertEqual(len(json_response_2['notification_result']['category']['unread_test_match_id']['test_id_dict']), 1)
        assert test_id in json_response_2['notification_result']['category']['unread_test_match_id']['test_id_dict']

        # User 3 cannot check the notification of user 2
        headers = self.get_token_auth_headers('unittest3', 'Xie1@456')
        response = self.client.get('/main_flow/get_notifications/' + user_id_2, headers=headers)
        self.assertEqual(response.status_code, 403)

        # Check the Notification of user 3
        headers = self.get_token_auth_headers('unittest3', 'Xie1@456')
        response = self.client.get('/main_flow/get_notifications/' + user_id_3, headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_3 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response_3['notification_result']['category']), 1)
        self.assertEqual(len(json_response_3['notification_result']['category']['unread_test_match_id']['test_id_dict']), 1)
        assert test_id in json_response_3['notification_result']['category']['unread_test_match_id']['test_id_dict']

        # 6. sponsor and assistors call update_match_id_notification() (in unread_match_id.py) and check updated notification (unread match id => 0)
        headers = self.get_token_auth_headers('unittest1', 'Xie1@456')
        data = json.dumps({
            'task_id': task_id,
            'test_id': test_id,
        })
        response = self.client.post('/main_flow/get_test_identifier_content/' + user_id_1, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertIsNotNone(json_response.get('assistor_random_id_to_identifier_content_dict'))

        # test test match identifier file
        test_match_document = test_match.search_test_match_document(test_id=test_id)
        user_random_id_1 = test_match_document['sponsor_information'][user_id_1]['sponsor_id_to_random_id']
        user_random_id_2 = test_match_document['assistor_information'][user_id_2]['assistor_id_to_random_id']
        user_random_id_3 = test_match_document['assistor_information'][user_id_3]['assistor_id_to_random_id']

        assistor_random_id_to_identifier_content_dict = json_response['assistor_random_id_to_identifier_content_dict']
        self.assertEqual(set(assistor_random_id_to_identifier_content_dict[user_random_id_2]), set([4]))
        self.assertEqual(set(assistor_random_id_to_identifier_content_dict[user_random_id_3]), set([8, 4]))

        headers = self.get_token_auth_headers('unittest2', 'Xie1@456')
        data = json.dumps({
            'task_id': task_id,
            'test_id': test_id,
        })
        response = self.client.post('/main_flow/get_test_identifier_content/' + user_id_2, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertIsNotNone(json_response.get('sponsor_random_id_to_identifier_content_dict'))
        sponsor_random_id_to_identifier_content_dict = json_response['sponsor_random_id_to_identifier_content_dict']
        # test idendifier content
        self.assertEqual(set(sponsor_random_id_to_identifier_content_dict[user_random_id_1]), set([4]))

        headers = self.get_token_auth_headers('unittest3', 'Xie1@456')
        data = json.dumps({
            'task_id': task_id,
            'test_id': test_id,
        })
        response = self.client.post('/main_flow/get_test_identifier_content/' + user_id_3, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertIsNotNone(json_response.get('sponsor_random_id_to_identifier_content_dict'))
        sponsor_random_id_to_identifier_content_dict = json_response['sponsor_random_id_to_identifier_content_dict']
        # test idendifier content
        self.assertEqual(set(sponsor_random_id_to_identifier_content_dict[user_random_id_1]), set([8, 4]))

        # 3. send_output() (in unread_situation.py) only assistor can send
        headers = self.get_token_auth_headers('unittest2', 'Xie1@456')
        output_content = [[[1,2,3], [4,5,6], [7,8,9]],[[2,3],[4,5]]]
        data = json.dumps({
            'output_content': output_content, 
            'test_id': test_id, 
            'task_id': task_id
        })
        response = self.client.post('/main_flow/send_test_output/' + user_id_2, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['send_test_output'], "send test output successfully")
        test_message_document = test_message.search_test_message_document(test_id=test_id)
        output_dict = test_message_document['rounds_1']['output_dict']
        self.assertEqual(len(output_dict), 1)
        output_id = output_dict[user_id_2]['output_id']
        
        test_message_output_document = test_message_output.search_test_message_output_document(output_id=output_id)
        output_content = test_message_output_document['output_content']
        self.assertEqual(output_content, [[[1,2,3], [4,5,6], [7,8,9]],[[2,3],[4,5]]])

        # should not have unread output now, the notification updates only when all assistors in 
        # current task have uploaded
        headers = self.get_token_auth_headers('unittest1', 'Xie1@456')
        response = self.client.get('/main_flow/get_notifications/' + user_id_1, headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response['notification_result']['category']), 0)

        headers = self.get_token_auth_headers('unittest3', 'Xie1@456')
        output_content = [[[6,321,6], [88,5,6], [7,87.6,9]],[[2]]]
        data = json.dumps({
            'output_content': output_content, 
            'test_id': test_id, 
            'task_id': task_id
        })
        response = self.client.post('/main_flow/send_test_output/' + user_id_3, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['send_test_output'], "send test output successfully")
        test_message_document = test_message.search_test_message_document(test_id=test_id)
        output_dict = test_message_document['rounds_1']['output_dict']
        self.assertEqual(len(output_dict), 2)
        output_id = output_dict[user_id_3]['output_id']
        
        test_message_output_document = test_message_output.search_test_message_output_document(output_id=output_id)
        output_content = test_message_output_document['output_content']
        self.assertEqual(output_content, [[[6,321,6], [88,5,6], [7,87.6,9]],[[2]]])


    def unread_test_output_two_users_helper(self, task_id, test_id, assistor_username_list, user_id_list):

        user_id_1 = user_id_list[0]
        user_id_2 = user_id_list[1]
        user_id_3 = user_id_list[2]

        # 14. sponsor check notification (unread output => 1)
        headers = self.get_token_auth_headers('unittest1', 'Xie1@456')
        response = self.client.get('/main_flow/get_notifications/' + user_id_1, headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_1 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response_1['notification_result']['category']), 1)
        self.assertEqual(len(json_response_1['notification_result']['category']['unread_test_output']['test_id_dict']), 1)
        assert test_id in json_response_1['notification_result']['category']['unread_test_output']['test_id_dict']
        
        # 16. sponsor calls: get_user_output() (in unread_output.py), gets output files
        data = json.dumps({
            'task_id': task_id, 
            'test_id': test_id,
        })
        response = self.client.post('/main_flow/get_test_output_content/' + user_id_1, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        assert 'assistor_random_id_to_output_content_dict' in json_response

        test_match_document = test_match.search_test_match_document(test_id=test_id)
        assistor_random_id_mapping = test_match_document['assistor_random_id_mapping']

        sponsor_information = test_match_document['sponsor_information']
        assistor_information = test_match_document['assistor_information']
        user_random_id_1 = sponsor_information[user_id_1]['sponsor_id_to_random_id']
        user_random_id_2 = assistor_information[user_id_2]['assistor_id_to_random_id']
        user_random_id_3 = assistor_information[user_id_3]['assistor_id_to_random_id']

        assistor_random_id_to_residual_dict = {}
        assistor_random_id_to_residual_dict[user_random_id_2] = [[3,321,6], [88,5,6], [7,99,9]]
        assistor_random_id_to_residual_dict[user_random_id_3] = [[6,321,6], [88,5,6], [7,87.6,9]]
