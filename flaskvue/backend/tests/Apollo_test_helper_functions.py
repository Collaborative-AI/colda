from base64 import b64encode
from datetime import datetime, timedelta
import json
import unittest
from Items import create_app, db
# from Items.models import User, Message, Notification, Matched
from tests import TestConfig


class Test_Helper_API_TestCase(unittest.TestCase):
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

    def find_test_assistor_no_data_helper(self):

        # check find_assistor function with no data uploaded
        u1 = User(username='unittest', email='john@163.com', confirmed='true')
        u1.set_password('Xie1@456')
        db.session.add(u1)
        db.session.commit()

        # 附带JWT到请求头中
        headers = self.get_token_auth_headers('unittest', 'Xie1@456')
        
        response = self.client.post('/find_test_assistor/', headers=headers)
        self.assertEqual(response.status_code, 400)

        data = json.dumps({'assistor_id_list': None})
        response = self.client.post('/find_test_assistor/', headers=headers, data=data)
        self.assertEqual(response.status_code, 400)
    
    
    def find_test_assistor_two_assistors_helper(self):

        # Check 1 sponsor with 2 assistors
        # Construct 2 new Matched rows
        # Check the Notification of each assistor

        u1 = User(username='unittest', email='john@163.com', confirmed='true')
        u1.set_password('Xie1@456')
        u2 = User(username='unittest2', email='john@163.com', confirmed='true')
        u2.set_password('Xie1@456')
        u3 = User(username='unittest3', email='john@163.com', confirmed='true')
        u3.set_password('Xie1@456')
        db.session.add(u1)
        db.session.add(u2)
        db.session.add(u3)
        db.session.commit()

        # 附带JWT到请求头中
        headers = self.get_token_auth_headers('unittest', 'Xie1@456')
        response = self.client.get('/create_new_train_task/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        task_id = json_response['task_id']

        list_content = ['unittest2', 'unittest3']
        # file = [['a','b','c'],[0,1,2],[4,5,6],[1,3,6]]
        file = "0\n4\n1"
        data = json.dumps({'assistor_username_list': list_content, 'id_file': file, 'task_id': task_id, 'task_mode':"", 'model_name':"", 'metric_name':"",'task_name': "", 'task_description': ""})
        response = self.client.post('/find_assistor/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['task_id'], task_id)
        assistor_num = json_response['assistor_num']

        queries = Matched.query.filter(Matched.task_id == task_id, Matched.assistor_id_pair != 1, Matched.test_indicator == "train").all()
        self.assertEqual(len(queries), len(list_content))
        assistor_random_id_list = []
        for i in range(len(queries)):
            assistor_random_id_list.append(queries[i].assistor_random_id_pair)
        
        # check Matched database new rows, include sponsor to sponsor
        queries = Matched.query.filter(Matched.task_id == task_id, Matched.test_indicator == 'train').all()
        self.assertEqual(len(queries), assistor_num+1)
        sponsor_random_id = queries[0].sponsor_random_id
        for i in range(len(queries)):
            self.assertEqual(queries[i].sponsor_id, 1) 
            self.assertEqual(queries[i].task_id, task_id)
            self.assertEqual(queries[i].sponsor_random_id, sponsor_random_id)
            self.assertEqual(set(json.loads(queries[i].Matched_id_file)), set(["0", "4", "1"]))
            self.assertEqual(set(json.loads(queries[i].Matched_id_file)), set(["0", "4", "1"]))

        # create test id
        headers = self.get_token_auth_headers('unittest', 'Xie1@456')
        response = self.client.get('/create_new_test_task/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        test_id = json_response['test_id']

        # file = [['a','b','c'],[0,1,2],[5,5,6],[1,3,6]]
        file = "8\n4\n3"
        data = json.dumps({'assistor_username_list': list_content, 'id_file': file, 'task_id': task_id, 'test_id': test_id, 'task_mode':"", 'model_name':"", 'metric_name':"", 'test_name': "", 'test_description': ""})
        response = self.client.post('/find_test_assistor/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['task_id'], task_id)
        self.assertEqual(json_response['test_id'], test_id)
        assistor_num = json_response['assistor_num']

        # check Matched database new rows, include sponsor to sponsor
        queries = Matched.query.filter(Matched.test_id == test_id, Matched.test_indicator == 'test').all()
        self.assertEqual(len(queries), assistor_num+1)
        sponsor_random_id = queries[0].sponsor_random_id
        for i in range(len(queries)):
            self.assertEqual(queries[i].sponsor_id, 1) 
            self.assertEqual(queries[i].task_id, task_id)
            self.assertEqual(queries[i].test_id, test_id)
            self.assertEqual(queries[i].sponsor_random_id, sponsor_random_id)
            self.assertEqual(set(json.loads(queries[i].Matched_id_file)), set(["8", "4", "3"]))

        # check the row that sponsor to sponsor
        queries = Matched.query.filter(Matched.task_id == task_id).all()
        self.assertEqual(len(queries), 6)
        self.assertEqual(queries[0].sponsor_id, 1)
        queries = Matched.query.filter(Matched.task_id == task_id, Matched.test_indicator == 'train').all()
        self.assertEqual(len(queries), 3)
        self.assertEqual(queries[0].sponsor_id, 1)
        queries = Matched.query.filter(Matched.task_id == task_id, Matched.test_id == test_id, Matched.test_indicator == 'test').all()
        self.assertEqual(len(queries), 3)
        self.assertEqual(queries[0].sponsor_id, 1)
        
        list_content = [2,3]
        return task_id, test_id, list_content

    def unread_test_request_two_users_helper(self, task_id, test_id, list_content):

        # Check the Notification of user 2
        headers = self.get_token_auth_headers('unittest2', 'Xie1@456')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response2 = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response2[-1]['name'], "unread test request")
        self.assertEqual(json_response2[-1]['payload'], 1)

        # User 3 cannot check the notification of user 2
        headers = self.get_token_auth_headers('unittest3', 'Xie1@456')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 403)

        # Check the Notification of user 3
        headers = self.get_token_auth_headers('unittest3', 'Xie1@456')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response3 = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response3[-1]['name'], "unread test request")
        self.assertEqual(json_response3[-1]['payload'], 1)

        # 3. update request notification
        headers = self.get_token_auth_headers('unittest2', 'Xie1@456')
        data = json.dumps({'response_data': json_response2})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)

        headers = self.get_token_auth_headers('unittest3', 'Xie1@456')
        data = json.dumps({'response_data': json_response3})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)

        # 4. check update notification
        headers = self.get_token_auth_headers('unittest2', 'Xie1@456')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response[-1]['name'], "unread test request")
        self.assertEqual(json_response[-1]['payload'], 0)

        headers = self.get_token_auth_headers('unittest3', 'Xie1@456')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response[-1]['name'], "unread test request")
        self.assertEqual(json_response[-1]['payload'], 0)

        # 5. assistor upload ID file
        headers = self.get_token_auth_headers('unittest2', 'Xie1@456')
        # file_content = [['a','b','c'],[0,1,2],[4,5,6],[1,3,6]]
        file_content = "0\n4\n1"
        data = json.dumps({'task_id': task_id, 'test_id': test_id, 'file': file_content})
        response = self.client.post('/match_test_assistor_id/', headers=headers, data=data)
        query = Matched.query.filter(Matched.test_id == test_id, Matched.assistor_id_pair == 2, Matched.test_indicator == "test").all()
        self.assertEqual(json.loads(query[0].Matched_id_file), ["4"])

        headers = self.get_token_auth_headers('unittest3', 'Xie1@456')
        # file_content = [['a','b','c'],[8,1,2],[4,5,6],[1,3,6]]
        file_content = "8\n4\n1"
        data = json.dumps({'task_id': task_id, 'test_id': test_id, 'file': file_content})
        response = self.client.post('/match_test_assistor_id/', headers=headers, data=data)
        query = Matched.query.filter(Matched.test_id == test_id, Matched.assistor_id_pair == 3, Matched.test_indicator == "test").first()
        self.assertEqual(set(json.loads(query.Matched_id_file)), set(["8", "4"]))


    def unread_test_match_id_two_users_helper(self, task_id, test_id, list_content):

        # 6. Check the Notification of sponsor and assistor
        headers = self.get_token_auth_headers('unittest', 'Xie1@456')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 1)
        self.assertEqual(json_response[-1]['name'], "unread test match id")
        self.assertEqual(json_response[-1]['payload'], 1)

        headers = self.get_token_auth_headers('unittest2', 'Xie1@456')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response2 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response2), 3)
        self.assertEqual(json_response2[-2]['name'], "unread test request")
        self.assertEqual(json_response2[-2]['payload'], 0)
        self.assertEqual(json_response2[-1]['name'], "unread test match id")
        self.assertEqual(json_response2[-1]['payload'], 1)

        headers = self.get_token_auth_headers('unittest3', 'Xie1@456')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response3 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response3), 3)
        self.assertEqual(json_response3[-2]['name'], "unread test request")
        self.assertEqual(json_response3[-2]['payload'], 0)
        self.assertEqual(json_response3[-1]['name'], "unread test match id")
        self.assertEqual(json_response3[-1]['payload'], 1)

        # check get test_identifier_content
        headers = self.get_token_auth_headers('unittest', 'Xie1@456')
        data = json.dumps({'test_id': test_id, 'task_id': task_id})
        response = self.client.post('/users/1/test_identifier_content/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response4 = json.loads(response.get_data(as_text=True))
        self.assertEqual(set(json.loads(json_response4['identifier_content'][0])), set(['4']))
        self.assertEqual(set(json.loads(json_response4['identifier_content'][1])), set(['8','4']))

        headers = self.get_token_auth_headers('unittest2', 'Xie1@456')
        data = json.dumps({'test_id': test_id, 'task_id': task_id})
        response = self.client.post('/users/2/test_identifier_content/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response4 = json.loads(response.get_data(as_text=True))


        headers = self.get_token_auth_headers('unittest3', 'Xie1@456')
        data = json.dumps({'test_id': test_id, 'task_id': task_id})
        response = self.client.post('/users/3/test_identifier_content/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response4 = json.loads(response.get_data(as_text=True))


        # 7. Check update_all_notifications() (update_all_notifications.py)
        headers = self.get_token_auth_headers('unittest', 'Xie1@456')
        data = json.dumps({'response_data': json_response})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response["unread test match id"]['check_dict'][str(test_id)], 1)

        headers = self.get_token_auth_headers('unittest2', 'Xie1@456')
        data = json.dumps({'response_data': json_response2})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response["unread test match id"]['check_dict'][str(test_id)], 0)

        headers = self.get_token_auth_headers('unittest3', 'Xie1@456')
        data = json.dumps({'response_data': json_response3})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response["unread test match id"]['check_dict'][str(test_id)], 0)

        # 8. Check updated Notification
        headers = self.get_token_auth_headers('unittest', 'Xie1@456')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 1)
        self.assertEqual(json_response[-1]['name'], "unread test match id")
        self.assertEqual(json_response[-1]['payload'], 0)

        headers = self.get_token_auth_headers('unittest2', 'Xie1@456')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 3)
        self.assertEqual(json_response[-2]['name'], "unread test request")
        self.assertEqual(json_response[-2]['payload'], 0)
        self.assertEqual(json_response[-1]['name'], "unread test match id")
        self.assertEqual(json_response[-1]['payload'], 0)

        headers = self.get_token_auth_headers('unittest3', 'Xie1@456')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 3)
        self.assertEqual(json_response[-2]['name'], "unread test request")
        self.assertEqual(json_response[-2]['payload'], 0)
        self.assertEqual(json_response[-1]['name'], "unread test match id")
        self.assertEqual(json_response[-1]['payload'], 0)

        # 3. send_output() (in unread_situation.py) only assistor can send
        headers = self.get_token_auth_headers('unittest2', 'Xie1@456')
        output = [[[1,2,3], [4,5,6], [7,8,9]],[[2,3],[4,5]]]
        data = json.dumps({'output': output, 'test_id': test_id, 'task_id': task_id})
        response = self.client.post('/send_test_output/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['send_test_output'], "send test output successfully")
        queries = Message.query.filter(Message.assistor_id == 1, Message.test_id == test_id, Message.test_indicator == "test").all()
        self.assertEqual(len(queries), 1)
        self.assertEqual(queries[0].sender_id, 2)
        self.assertEqual(json.loads(queries[0].output), [[[1,2,3], [4,5,6], [7,8,9]],[[2,3],[4,5]]])

        # should not have unread output now, the notification updates only when all assistors in 
        # current task have uploaded
        headers = self.get_token_auth_headers('unittest', 'Xie1@456')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        print('zzzzzzz', json_response)
        self.assertEqual(len(json_response), 1)

        headers = self.get_token_auth_headers('unittest3', 'Xie1@456')
        output = [[[6,321,6], [88,5,6], [7,87.6,9]],[[2]]]
        data = json.dumps({'output': output, 'test_id': test_id, 'task_id': task_id})
        response = self.client.post('/send_test_output/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['send_test_output'], "send test output successfully")
        queries = Message.query.filter(Message.assistor_id == 1, Message.test_id == test_id, Message.test_indicator == "test").all()
        self.assertEqual(len(queries), 2)
        self.assertEqual(queries[1].sender_id, 3)
        self.assertEqual(json.loads(queries[1].output), [[[6,321,6], [88,5,6], [7,87.6,9]],[[2]]])



    def unread_test_output_two_users_helper(self, task_id, test_id, list_content):

        # 4. check new notification
        headers = self.get_token_auth_headers('unittest', 'Xie1@456')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        print("--------------------------------------")
        print("json_response----------", json_response)
        self.assertEqual(len(json_response), 2)
        self.assertEqual(json_response[-1]['name'], "unread test output")
        self.assertEqual(json_response[-1]['payload'], 2)

        # 5. check sent test output
        headers = self.get_token_auth_headers('unittest', 'Xie1@456')
        data = json.dumps({'test_id': test_id, 'task_id': task_id})
        response = self.client.post('/test_output/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response4 = json.loads(response.get_data(as_text=True))
        self.assertEqual(json.loads(json_response4['output'][0]), [[[1,2,3], [4,5,6], [7,8,9]],[[2,3],[4,5]]])
        self.assertEqual(json.loads(json_response4['output'][1]), [[[6,321,6], [88,5,6], [7,87.6,9]],[[2]]])
