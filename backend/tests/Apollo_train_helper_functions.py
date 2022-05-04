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

class Train_Helper_API_TestCase(unittest.TestCase):

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
        # print('ssads', dir(pyMongo.db))
        # pyMongo.db.drop_collection()
        for collecion_names in pyMongo.db.list_collection_names():
            pyMongo.db.drop_collection(collecion_names)
        # pyMongo.db.User.drop()
        # pyMongo.db.Notification.drop()
        # pyMongo.db.Pending.drop()
        # pyMongo.db.Train_Message.drop()
        # pyMongo.db.Train_Message_Situation.drop()
        # pyMongo.db.Train_Message_Output.drop()
        # pyMongo.db.Test_Message.drop()
        # pyMongo.db.Test_Message_Situation.drop()
        # pyMongo.db.Test_Message_Output.drop()
        # pyMongo.db.Train_Match.drop()
        # pyMongo.db.Train_Match_Identifier.drop()
        # pyMongo.db.Test_Match.drop()
        # pyMongo.db.Test_Match_Identifier.drop()
        # pyMongo.db.Train_Task.drop()
        # pyMongo.db.Test_Task.drop()
        # pyMongo.db.Stop.drop()

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
    
    def retrieve_file_content(self, document, key):
        if document['is_large_file'] == False:
            file_content = document[key]
        elif document['is_large_file'] == True:
            gridfs_file_id = document[key]
            file_content = mongoDB.retrieve_large_file(base='fs', file_id=gridfs_file_id)
        return file_content

    def init_train_user_file_content(self, indicator):
        file_content_dict = collections.defaultdict(dict)
        if indicator == 'small_data':
            file_content_dict['user_1']['identifier_content'] = [8, 4, 3, 12, 16, 17]
            file_content_dict['user_2']['identifier_content'] = [0, 4, 1, 12, 16, 17, 18]
            file_content_dict['user_3']['identifier_content'] = [2, 3, 4, 5, 12, 18]

            file_content_dict['user_1']['situation_content'] = None
            file_content_dict['user_2']['situation_content'] = [[1,2,3], [4,5,6], [7,8,9]]
            file_content_dict['user_3']['situation_content'] = [[1,2], [3,4]]

            file_content_dict['user_1']['output_content'] = None
            file_content_dict['user_2']['output_content'] = [[3,321,6], [88,5,6], [7,99,9]]
            file_content_dict['user_3']['output_content'] = [[6,321,6], [88,5,6], [7,87.6,9]]
        elif indicator == 'large_data':
            file_content_dict['user_1']['identifier_content'] = [1 for _ in range(3000000)]
            file_content_dict['user_2']['identifier_content'] = [1 for _ in range(3000000)]
            file_content_dict['user_3']['identifier_content'] = [1 for _ in range(3000000)]

            file_content_dict['user_1']['situation_content'] = [1 for _ in range(3000000)]
            file_content_dict['user_2']['situation_content'] = [1 for _ in range(3000000)]
            file_content_dict['user_3']['situation_content'] = [1 for _ in range(3000000)]

            file_content_dict['user_1']['output_content'] = None
            file_content_dict['user_2']['output_content'] = [1 for _ in range(3000000)]
            file_content_dict['user_3']['output_content'] = [1 for _ in range(3000000)]

        return file_content_dict
    

    # def set_user_file_content(self, user, content_key, content):
    def find_assistor_two_assistors_helper(self, **kwargs):

        file_content_dict = kwargs['file_content_dict']
        user_1_identifier_content = file_content_dict['user_1']['identifier_content']

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
            print('trainDDDD')
            user_id_3 = user_document['user_id']

        print('train_user_id_1', user_id_1)
        print('train_user_id_2', user_id_2)
        print('train_user_id_3', user_id_3)

        # 附带JWT到请求头中
        headers = self.get_token_auth_headers('unittest1', 'Xie1@456')
        response = self.client.get('/main_flow/create_new_train_task/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        train_id = json_response['train_id']
        self.train_id = train_id

        # If we add non-exist username, such as unittest4, 'wrong username' will be returned
        assistor_username_list = ['unittest2', 'unittest4']
        identifier_content = user_1_identifier_content
        data = json.dumps({
            'assistor_username_list': assistor_username_list, 
            'identifier_content': identifier_content, 
            'train_id': train_id, 
            'task_mode': 'regression', 
            'model_name': 'LinearRegression', 
            'metric_name': 'RMSE',
            'task_name': 'unittest', 
            'task_description': 'unittest_desciption'
        })
        response = self.client.post('/main_flow/find_assistor/' + user_id_1, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response, "wrong username")

        headers = self.get_token_auth_headers('unittest1', 'Xie1@456')
        assistor_username_list = ['unittest2', 'unittest3']
        identifier_content = user_1_identifier_content
        data = json.dumps({
            'assistor_username_list': assistor_username_list, 
            'identifier_content': identifier_content,      
            'train_id': train_id, 
            'task_mode': 'regression', 
            'model_name': 'LinearRegression', 
            'metric_name': 'RMSE',
            'task_name': 'unittest', 
            'task_description': 'unittest_desciption'
        })
        response = self.client.post('/main_flow/find_assistor/' + user_id_1, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        print('json_response', json_response)
        self.assertEqual(json_response['train_id'], train_id)
        assistor_num = json_response['assistor_num']

        # check Train_Match database new rows, include sponsor to sponsor
        train_match_document = train_match.search_train_match_document(train_id=train_id)
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

        self.assertEqual(train_match_document['train_id'], train_id)
        self.assertEqual(total_assistor_num, assistor_num)
        self.assertEqual(sponsor_id, user_id_1)
        self.assertEqual(sponsor_random_id_mapping[sponsor_random_id], sponsor_id)
        self.assertEqual(len(assistor_information), 0)
        self.assertEqual(len(asssistor_random_id_mapping), 0)
        self.assertEqual(len(sponsor_terminate_id_dict), 0)
        self.assertEqual(len(assistor_terminate_id_dict), 0)

        train_match_identifier_document = train_match_identifier.search_train_match_identifier_document(identifier_id=sponsor_identifier_id)
        identifier_content = self.retrieve_file_content(train_match_identifier_document, 'identifier_content')
        self.assertEqual(identifier_content, user_1_identifier_content)
        
        train_task_document = train_task.search_train_task_document(train_id=train_id)
        task_name = train_task_document['task_name']
        task_description = train_task_document['task_description']
        task_mode = train_task_document['task_mode']
        model_name = train_task_document['model_name']
        metric_name = train_task_document['metric_name']
        assistor_id_dict = train_task_document['assistor_id_dict']
        test_task_dict = train_task_document['test_task_dict']

        self.assertEqual(train_task_document['train_id'], train_id)
        self.assertEqual(task_name, 'unittest')
        self.assertEqual(task_description, 'unittest_desciption')
        self.assertEqual(task_mode, 'regression')
        self.assertEqual(model_name, 'LinearRegression')
        self.assertEqual(metric_name, 'RMSE')
        self.assertEqual(train_task_document['sponsor_id'], sponsor_id)
        self.assertEqual(assistor_id_dict, {
            user_id_2: None, 
            user_id_3: None
        })
        self.assertEqual(len(test_task_dict), 0)

        assistor_username_list = ['unittest2', 'unittest3']
        user_id_list = [user_id_1, user_id_2, user_id_3]
        return train_id, assistor_username_list, user_id_list 
    
    def unread_request_two_users_helper(self, train_id, assistor_username_list, user_id_list, **kwargs):
        
        user_id_1 = user_id_list[0]
        user_id_2 = user_id_list[1]
        user_id_3 = user_id_list[2]

        file_content_dict = kwargs['file_content_dict']
        user_1_identifier_content = file_content_dict['user_1']['identifier_content']
        user_2_identifier_content = file_content_dict['user_2']['identifier_content']
        user_3_identifier_content = file_content_dict['user_3']['identifier_content']

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
        
        self.assertEqual(len(json_response_2['notification_result']['category']['unread_request']['train_id_dict']), 1)
        assert train_id in json_response_2['notification_result']['category']['unread_request']['train_id_dict']

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
        self.assertEqual(len(json_response_3['notification_result']['category']['unread_request']['train_id_dict']), 1)
        assert train_id in json_response_3['notification_result']['category']['unread_request']['train_id_dict']

        # 5. assistor uploads the ID file
        headers = self.get_token_auth_headers('unittest2', 'Xie1@456')
        identifier_content = user_2_identifier_content
        data = json.dumps({
            'train_id': train_id, 
            'identifier_content': identifier_content
        })
        response = self.client.post('/main_flow/match_identifier_content/' + user_id_2, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        stored = json_response['stored']
        train_id_response = json_response['train_id']
        self.assertEqual(stored, "assistor match id stored")
        self.assertEqual(train_id, train_id_response)

        # test train_match_document
        train_match_document = train_match.search_train_match_document(train_id=train_id)
        assistor_information = train_match_document['assistor_information']
        assert user_id_2 in assistor_information
        identifier_id = assistor_information[user_id_2]['identifier_id']

        train_match_identifier_document = train_match_identifier.search_train_match_identifier_document(identifier_id=identifier_id)
        identifier_content = self.retrieve_file_content(train_match_identifier_document, 'identifier_content')
        self.assertEqual(set(identifier_content), set(user_1_identifier_content) & set(user_2_identifier_content))

        # should not exist notification yet for sponsor
        headers = self.get_token_auth_headers('unittest1', 'Xie1@456')
        response = self.client.get('/main_flow/get_notifications/' + user_id_1, headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response['notification_result']['category']), 0)
        
        headers = self.get_token_auth_headers('unittest3', 'Xie1@456')
        identifier_content = user_3_identifier_content
        data = json.dumps({
            'train_id': train_id, 
            'identifier_content': identifier_content
        })
        response = self.client.post('/main_flow/match_identifier_content/' + user_id_3, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        stored = json_response['stored']
        train_id = json_response['train_id']
        self.assertEqual(stored, "assistor match id stored")
        self.assertEqual(train_id, train_id_response)

         # test train_match_document
        train_match_document = train_match.search_train_match_document(train_id=train_id)
        assistor_information = train_match_document['assistor_information']
        assert user_id_3 in assistor_information
        identifier_id = assistor_information[user_id_3]['identifier_id']

        train_match_identifier_document = train_match_identifier.search_train_match_identifier_document(identifier_id=identifier_id)
        identifier_content = self.retrieve_file_content(train_match_identifier_document, 'identifier_content')
        self.assertEqual(set(identifier_content), set(user_1_identifier_content) & set(user_3_identifier_content))

        return train_id, assistor_username_list, user_id_list

    def unread_match_identifier_two_users_helper(self, train_id, assistor_username_list, user_id_list, **kwargs):
        
        user_id_1 = user_id_list[0]
        user_id_2 = user_id_list[1]
        user_id_3 = user_id_list[2]

        file_content_dict = kwargs['file_content_dict']
        user_1_identifier_content = file_content_dict['user_1']['identifier_content']
        user_2_identifier_content = file_content_dict['user_2']['identifier_content']
        user_3_identifier_content = file_content_dict['user_3']['identifier_content']

        user_2_situation_content = file_content_dict['user_2']['situation_content']
        user_3_situation_content = file_content_dict['user_3']['situation_content']

        # Check the Notification of user 2
        headers = self.get_token_auth_headers('unittest1', 'Xie1@456')
        response = self.client.get('/main_flow/get_notifications/' + user_id_1, headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_1 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response_1['notification_result']['category']), 1)
        self.assertEqual(len(json_response_1['notification_result']['category']['unread_match_identifier']['train_id_dict']), 1)
        assert train_id in json_response_1['notification_result']['category']['unread_match_identifier']['train_id_dict']

        # Check the Notification of user 2
        headers = self.get_token_auth_headers('unittest2', 'Xie1@456')
        response = self.client.get('/main_flow/get_notifications/' + user_id_2, headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_2 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response_2['notification_result']['category']), 1)
        self.assertEqual(len(json_response_2['notification_result']['category']['unread_match_identifier']['train_id_dict']), 1)
        assert train_id in json_response_2['notification_result']['category']['unread_match_identifier']['train_id_dict']

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
        self.assertEqual(len(json_response_3['notification_result']['category']['unread_match_identifier']['train_id_dict']), 1)
        assert train_id in json_response_3['notification_result']['category']['unread_match_identifier']['train_id_dict']

        # 6. sponsor and assistors call update_match_id_notification() (in unread_match_identifier.py) and check updated notification (unread match id => 0)
        headers = self.get_token_auth_headers('unittest1', 'Xie1@456')
        data = json.dumps({
            'train_id': train_id
        })
        response = self.client.post('/main_flow/get_identifier_content/' + user_id_1, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertIsNotNone(json_response.get('assistor_random_id_to_identifier_content_dict'))

        # test match id file
        train_match_document = train_match.search_train_match_document(train_id=train_id)
        user_random_id_1 = train_match_document['sponsor_information'][user_id_1]['sponsor_id_to_random_id']
        user_random_id_2 = train_match_document['assistor_information'][user_id_2]['assistor_id_to_random_id']
        user_random_id_3 = train_match_document['assistor_information'][user_id_3]['assistor_id_to_random_id']

        assistor_random_id_to_identifier_content_dict = json_response['assistor_random_id_to_identifier_content_dict']
        self.assertEqual(set(assistor_random_id_to_identifier_content_dict[user_random_id_2]), set(user_1_identifier_content) & set(user_2_identifier_content))
        self.assertEqual(set(assistor_random_id_to_identifier_content_dict[user_random_id_3]), set(user_1_identifier_content) & set(user_3_identifier_content))

        headers = self.get_token_auth_headers('unittest2', 'Xie1@456')
        data = json.dumps({
            'train_id': train_id
        })
        response = self.client.post('/main_flow/get_identifier_content/' + user_id_2, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertIsNotNone(json_response.get('sponsor_random_id_to_identifier_content_dict'))
        sponsor_random_id_to_identifier_content_dict = json_response['sponsor_random_id_to_identifier_content_dict']
        # test idendifier content
        self.assertEqual(set(sponsor_random_id_to_identifier_content_dict[user_random_id_1]), set(user_1_identifier_content) & set(user_2_identifier_content))

        headers = self.get_token_auth_headers('unittest3', 'Xie1@456')
        data = json.dumps({
            'train_id': train_id
        })
        response = self.client.post('/main_flow/get_identifier_content/' + user_id_3, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertIsNotNone(json_response.get('sponsor_random_id_to_identifier_content_dict'))
        sponsor_random_id_to_identifier_content_dict = json_response['sponsor_random_id_to_identifier_content_dict']
        # test idendifier content
        self.assertEqual(set(sponsor_random_id_to_identifier_content_dict[user_random_id_1]), set(user_1_identifier_content) & set(user_3_identifier_content))

        headers = self.get_token_auth_headers('unittest1', 'Xie1@456')
        assistor_random_id_to_residual_dict = {}
        assistor_random_id_to_residual_dict[user_random_id_2] = user_2_situation_content
        assistor_random_id_to_residual_dict[user_random_id_3] = user_3_situation_content
        data = json.dumps({
            'train_id': train_id,
            'assistor_random_id_to_residual_dict': assistor_random_id_to_residual_dict
        })
        response = self.client.post('/main_flow/send_situation/' + user_id_1, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['message'], 'send situation successfully!')

        train_message_document = train_message.search_train_message_document(train_id=train_id)
        situation_dict = train_message_document['rounds_1']['situation_dict']
        self.assertEqual(len(situation_dict), 3)
        for recipient_id in situation_dict:
            situation_id = situation_dict[recipient_id]['situation_id']
            train_message_situation_document = train_message_situation.search_train_message_situation_document(situation_id=situation_id)
            situation_content = self.retrieve_file_content(train_message_situation_document, 'situation_content')
            sender_id = train_message_situation_document['sender_id']
            sender_random_id = train_message_situation_document['sender_random_id']

            if recipient_id == user_id_2:
                self.assertEqual(situation_content, user_2_situation_content)
                self.assertEqual(sender_id, user_id_1)
                self.assertEqual(sender_random_id, user_random_id_1)
            elif recipient_id == user_id_3:
                self.assertEqual(situation_content, user_3_situation_content)
                self.assertEqual(sender_id, user_id_1)
                self.assertEqual(sender_random_id, user_random_id_1)
        
        return train_id, assistor_username_list, user_id_list

    def unread_situation_two_users_helper(self, train_id, assistor_username_list, user_id_list, test_rounds_num=1, **kwargs):     

        user_id_1 = user_id_list[0]
        user_id_2 = user_id_list[1]
        user_id_3 = user_id_list[2]

        file_content_dict = kwargs['file_content_dict']
        user_2_situation_content = file_content_dict['user_2']['situation_content']
        user_3_situation_content = file_content_dict['user_3']['situation_content']

        user_2_output_content = file_content_dict['user_2']['output_content']
        user_3_output_content = file_content_dict['user_3']['output_content']

        # 11. sponsor and assistors check notification (unread situation => 1)
        headers = self.get_token_auth_headers('unittest1', 'Xie1@456')
        response = self.client.get('/main_flow/get_notifications/' + user_id_1, headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_1 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response_1['notification_result']['category']), 1)
        self.assertEqual(len(json_response_1['notification_result']['category']['unread_situation']['train_id_dict']), 1)
        assert train_id in json_response_1['notification_result']['category']['unread_situation']['train_id_dict']
        self.assertEqual(json_response_1['notification_result']['category']['unread_situation']['train_id_dict'][train_id]['cur_rounds_num'], test_rounds_num)

        headers = self.get_token_auth_headers('unittest2', 'Xie1@456')
        response = self.client.get('/main_flow/get_notifications/' + user_id_2, headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_2 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response_2['notification_result']['category']), 1)
        self.assertEqual(len(json_response_2['notification_result']['category']['unread_situation']['train_id_dict']), 1)
        assert train_id in json_response_2['notification_result']['category']['unread_situation']['train_id_dict']
        self.assertEqual(json_response_2['notification_result']['category']['unread_situation']['train_id_dict'][train_id]['cur_rounds_num'], test_rounds_num)

        headers = self.get_token_auth_headers('unittest3', 'Xie1@456')
        response = self.client.get('/main_flow/get_notifications/' + user_id_3, headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_3 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response_3['notification_result']['category']), 1)
        self.assertEqual(len(json_response_3['notification_result']['category']['unread_situation']['train_id_dict']), 1)
        assert train_id in json_response_3['notification_result']['category']['unread_situation']['train_id_dict']
        self.assertEqual(json_response_3['notification_result']['category']['unread_situation']['train_id_dict'][train_id]['cur_rounds_num'], test_rounds_num)

        # if sponsor_stop, everything of this round will be cleaned and we cant get into the Sponsor_situation_training_done() or send_output() function
        # if sponsor_stop:
        #     return
        
        train_message_document = train_message.search_train_message_document(train_id=train_id)
        cur_rounds_num = train_message_document['cur_rounds_num']
        self.assertEqual(cur_rounds_num, test_rounds_num)
        train_match_document = train_match.search_train_match_document(train_id=train_id)
        sponsor_random_id = train_match_document['sponsor_information'][user_id_1]['sponsor_id_to_random_id']

        headers = self.get_token_auth_headers('unittest2', 'Xie1@456')
        data = json.dumps({
            'train_id': train_id, 
            'rounds': cur_rounds_num
        })
        response = self.client.post('/main_flow/get_situation_content/' + user_id_2, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response_2 = json.loads(response.get_data(as_text=True))
        situation_content = json_response_2['situation_content']
        sender_random_id = json_response_2['sender_random_id']
        self.assertEqual(situation_content, user_2_situation_content)
        self.assertEqual(sender_random_id, sponsor_random_id)

        headers = self.get_token_auth_headers('unittest3', 'Xie1@456')
        data = json.dumps({
            'train_id': train_id, 
            'rounds': cur_rounds_num
        })
        response = self.client.post('/main_flow/get_situation_content/' + user_id_3, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response_3 = json.loads(response.get_data(as_text=True))
        situation_content = json_response_3['situation_content']
        sender_random_id = json_response_3['sender_random_id']
        self.assertEqual(situation_content, user_3_situation_content)
        self.assertEqual(sender_random_id, sponsor_random_id)


        headers = self.get_token_auth_headers('unittest2', 'Xie1@456')
        output_content = user_2_output_content
        data = json.dumps({
            'train_id': train_id, 
            'output_content': output_content
        })
        response = self.client.post('/main_flow/send_output/' + user_id_2, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['send_output'], "send output successfully")

        headers = self.get_token_auth_headers('unittest3', 'Xie1@456')
        output_content = user_3_output_content
        data = json.dumps({
            'train_id': train_id, 
            'output_content': output_content
        })
        response = self.client.post('/main_flow/send_output/' + user_id_3, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['send_output'], "send output successfully")

        train_message_document = train_message.search_train_message_document(train_id=train_id)
        output_dict = train_message_document['rounds_' + str(cur_rounds_num)]['output_dict']

        output_id = output_dict[user_id_2]['output_id']
        train_message_output_document = train_message_output.search_train_message_output_document(output_id=output_id)
        output_content = self.retrieve_file_content(train_message_output_document, 'output_content')
        self.assertEqual(output_content, user_2_output_content)

        output_id = output_dict[user_id_3]['output_id']
        train_message_output_document = train_message_output.search_train_message_output_document(output_id=output_id)
        output_content = self.retrieve_file_content(train_message_output_document, 'output_content')
        self.assertEqual(output_content, user_3_output_content)

    def unread_output_two_users_helper(self, train_id, assistor_username_list, user_id_list, test_rounds_num=1, **kwargs):
        
        user_id_1 = user_id_list[0]
        user_id_2 = user_id_list[1]
        user_id_3 = user_id_list[2]

        file_content_dict = kwargs['file_content_dict']
        user_2_situation_content = file_content_dict['user_2']['situation_content']
        user_3_situation_content = file_content_dict['user_3']['situation_content']

        user_2_output_content = file_content_dict['user_2']['output_content']
        user_3_output_content = file_content_dict['user_3']['output_content']

        train_message_document = train_message.search_train_message_document(train_id=train_id)
        cur_rounds_num = train_message_document['cur_rounds_num']
        self.assertEqual(cur_rounds_num, test_rounds_num)

        # 14. sponsor check notification (unread output => 1)
        headers = self.get_token_auth_headers('unittest1', 'Xie1@456')
        response = self.client.get('/main_flow/get_notifications/' + user_id_1, headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_1 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response_1['notification_result']['category']), 1)
        self.assertEqual(len(json_response_1['notification_result']['category']['unread_output']['train_id_dict']), 1)
        assert train_id in json_response_1['notification_result']['category']['unread_output']['train_id_dict']
        self.assertEqual(json_response_1['notification_result']['category']['unread_output']['train_id_dict'][train_id]['cur_rounds_num'], test_rounds_num)
        
        # 16. sponsor calls: get_user_output() (in unread_output.py), gets output files
        data = json.dumps({
            'train_id': train_id, 
            'rounds': cur_rounds_num
        })
        response = self.client.post('/main_flow/get_output_content/' + user_id_1, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        assert 'assistor_random_id_to_output_content_dict' in json_response

        train_match_document = train_match.search_train_match_document(train_id=train_id)
        assistor_random_id_mapping = train_match_document['assistor_random_id_mapping']

        for assistor_random_id, output_content in assistor_random_id_mapping.items():
            assistor_id = assistor_random_id_mapping[assistor_random_id]
            if assistor_id == user_id_2:
                self.assertEqual(output_content, user_2_output_content)
            elif assistor_id == user_id_3:
                self.assertEqual(output_content, user_3_output_content)

        sponsor_information = train_match_document['sponsor_information']
        assistor_information = train_match_document['assistor_information']
        user_random_id_1 = sponsor_information[user_id_1]['sponsor_id_to_random_id']
        user_random_id_2 = assistor_information[user_id_2]['assistor_id_to_random_id']
        user_random_id_3 = assistor_information[user_id_3]['assistor_id_to_random_id']

        assistor_random_id_to_residual_dict = {}
        assistor_random_id_to_residual_dict[user_random_id_2] = user_2_situation_content
        assistor_random_id_to_residual_dict[user_random_id_3] = user_3_situation_content

        # 17. sponsor calls: send_situation(), goes into new round 
        headers = self.get_token_auth_headers('unittest1', 'Xie1@456')
        data = json.dumps({
            'train_id': train_id, 
            "assistor_random_id_to_residual_dict": assistor_random_id_to_residual_dict
        })
        response = self.client.post('/main_flow/send_situation/' + user_id_1, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['message'], 'send situation successfully!')

        train_message_document = train_message.search_train_message_document(train_id=train_id)
        cur_rounds_num = train_message_document['cur_rounds_num']
        self.assertEqual(cur_rounds_num, test_rounds_num+1)
        situation_dict = train_message_document['rounds_' + str(cur_rounds_num)]['situation_dict']
        self.assertEqual(len(situation_dict), 3)
        for recipient_id in situation_dict:
            situation_id = situation_dict[recipient_id]['situation_id']
            train_message_situation_document = train_message_situation.search_train_message_situation_document(situation_id=situation_id)
            situation_content = self.retrieve_file_content(train_message_situation_document, 'situation_content')
            sender_id = train_message_situation_document['sender_id']
            sender_random_id = train_message_situation_document['sender_random_id']

            if recipient_id == user_id_2:
                self.assertEqual(situation_content, user_2_situation_content)
                self.assertEqual(sender_id, user_id_1)
                self.assertEqual(sender_random_id, user_random_id_1)
            elif recipient_id == user_id_3:
                self.assertEqual(situation_content, user_3_situation_content)
                self.assertEqual(sender_id, user_id_1)
                self.assertEqual(sender_random_id, user_random_id_1)
