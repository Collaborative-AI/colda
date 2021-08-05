from base64 import b64encode
from datetime import datetime, timedelta
import json
import unittest
from Items import create_app, db
from Items.models import User, Message, Notification, Matched
from tests import TestConfig


class Unread_Situation_APITestCase(unittest.TestCase):

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
    
    def test_update_situation_notification(self):

        # sponsor and 2 assistors, only sponsor would go into this function
        # 1. find_assistor() (in find_assistor.py)
        # 2. send_situation() (in send_situation.py)
        # 3. check new notification
        # 4. update_situation_notification() (in unread_situation.py)
        # 5. assistor check situation file from sponsor
        # 6. check new notification

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

        # 1. find_assistor() (in find_assistor.py)
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/create_new_train_task/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        task_id = json_response['task_id']

        list_content = [2,3]
        file = [['a','b','c'],[0,1,2],[4,5,6],[1,3,6],[]]
        data = json.dumps({'assistor_id_list': list_content, 'id_file': file, 'task_id': task_id})
        response = self.client.post('/find_assistor/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['task_id'], task_id)

        queries = Matched.query.filter(Matched.task_id == task_id, Matched.assistor_id_pair != 1, Matched.test_indicator == "train").all()
        self.assertEqual(len(queries), len(list_content))
        assistor_random_id_list = []
        for i in range(len(queries)):
            assistor_random_id_list.append(queries[i].assistor_random_id_pair)
        
        # 2. send_situation() (in send_situation.py)
        headers = self.get_token_auth_headers('unittest', '123')
        residual_list = [[[1,2,3], [4,5,6], [7,8,9]], [[1,2], [3,4]]]
        data = json.dumps({'residual_list': residual_list, 'task_id': task_id, "assistor_random_id_list": assistor_random_id_list})
        response = self.client.post('/send_situation/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['message'], 'send situation successfully!')

        queries = Message.query.filter(Message.assistor_id != 1, Message.task_id == task_id, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), len(list_content))
        for i in range(len(queries)):
            self.assertEqual(queries[i].rounds, 0)
            self.assertEqual(queries[i].sender_id, 1)
            self.assertEqual(queries[i].assistor_id, list_content[i])
            self.assertEqual(json.loads(queries[i].situation), residual_list[i])
          
        # 3. check new notification
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 1)
        self.assertEqual(json_response[0]['name'], "unread situation")
        self.assertEqual(json_response[0]['payload'], 1)

        # 4. update_situation_notification() (in unread_situation.py)
        data = json.dumps({'response_data': json_response})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response['unread situation']['check_dict']), 1)
        self.assertEqual(len(json_response['unread situation']['rounds_dict']), 1)
        self.assertEqual(json_response['unread situation']['check_dict'][str(task_id)], 1)
        self.assertEqual(json_response['unread situation']['rounds_dict'][str(task_id)], 0)

        # 5. check new notification
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 1)
        self.assertEqual(json_response[-1]['name'], "unread situation")
        self.assertEqual(json_response[-1]['payload'], 0)

         # 3. check new notification
        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 2)
        self.assertEqual(json_response[-1]['name'], "unread situation")
        self.assertEqual(json_response[-1]['payload'], 1)

        # 4. update_situation_notification() (in unread_situation.py)
        data = json.dumps({'response_data': json_response})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response['unread situation']['check_dict']), 1)
        self.assertEqual(len(json_response['unread situation']['rounds_dict']), 1)
        self.assertEqual(json_response['unread situation']['check_dict'][str(task_id)], 0)
        self.assertEqual(json_response['unread situation']['rounds_dict'][str(task_id)], 0)

        # 5. get_user_situation()
        data = json.dumps({'task_id': task_id, 'rounds': 0})
        response = self.client.post('/users/2/situation_file/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json.loads(json_response['situation']), [[1,2,3], [4,5,6], [7,8,9]])

        # 6. check new notification
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 2)
        self.assertEqual(json_response[1]['name'], "unread situation")
        self.assertEqual(json_response[1]['payload'], 0)

        # 3. check new notification
        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 2)
        self.assertEqual(json_response[1]['name'], "unread situation")
        self.assertEqual(json_response[1]['payload'], 1)

        # 4. update_situation_notification() (in unread_situation.py)
        data = json.dumps({'response_data': json_response})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response['unread situation']['check_dict']), 1)
        self.assertEqual(len(json_response['unread situation']['rounds_dict']), 1)
        self.assertEqual(json_response['unread situation']['check_dict'][str(task_id)], 0)
        self.assertEqual(json_response['unread situation']['rounds_dict'][str(task_id)], 0)

        # 5. get_user_situation()
        data = json.dumps({'task_id': task_id, 'rounds': 0})
        response = self.client.post('/users/3/situation_file/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json.loads(json_response['situation']), [[1,2], [3,4]])

        # 6. check new notification
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 2)
        self.assertEqual(json_response[1]['name'], "unread situation")
        self.assertEqual(json_response[1]['payload'], 0)

    def test_noninitial_round_update_situation_notification(self):

        # sponsor and 2 assistors, only sponsor would go into this function
        # 1. find_assistor() (in find_assistor.py)
        # 2. send_situation() (in send_situation.py)
        # 3. send_situation() again (in send_situation.py)
        # 4. check notification
        # 5. update_situation_notification() (in unread_situation.py)
        # 6. check new notification

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

        # 1. find_assistor() (in find_assistor.py)
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/create_new_train_task/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        task_id = json_response['task_id']

        list_content = [2,3]
        file = [['a','b','c'],[0,1,2],[4,5,6],[1,3,6],[]]
        data = json.dumps({'assistor_id_list': list_content, 'id_file': file, 'task_id': task_id})
        response = self.client.post('/find_assistor/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['task_id'], task_id)

        queries = Matched.query.filter(Matched.task_id == task_id, Matched.assistor_id_pair != 1, Matched.test_indicator == "train").all()
        self.assertEqual(len(queries), len(list_content))
        assistor_random_id_list = []
        for i in range(len(queries)):
            assistor_random_id_list.append(queries[i].assistor_random_id_pair)
        
        # 2. send_situation() (in send_situation.py)
        headers = self.get_token_auth_headers('unittest', '123')
        residual_list = [[[1,2,3], [4,5,6], [7,8,9]], [[1,2], [3,4]]]
        data = json.dumps({'residual_list': residual_list, 'task_id': task_id, "assistor_random_id_list": assistor_random_id_list})
        response = self.client.post('/send_situation/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['message'], 'send situation successfully!')

        queries = Message.query.filter(Message.assistor_id != 1, Message.task_id == task_id, Message.rounds == 0, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), len(list_content))
        for i in range(len(queries)):
            self.assertEqual(queries[i].rounds, 0)
            self.assertEqual(queries[i].sender_id, 1)
            self.assertEqual(queries[i].assistor_id, list_content[i])
            self.assertEqual(json.loads(queries[i].situation), residual_list[i])
        
        # 3. send_situation() again (in send_situation.py)
        headers = self.get_token_auth_headers('unittest', '123')
        residual_list = [[[3,2,1], [4,5,6], [7,8,9]], [[15,2], [3,4]]]
        data = json.dumps({'residual_list': residual_list, 'task_id': task_id, "assistor_random_id_list": assistor_random_id_list})
        response = self.client.post('/send_situation/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['message'], 'send situation successfully!')

        queries = Message.query.filter(Message.assistor_id != 1, Message.task_id == task_id, Message.rounds == 1, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), len(list_content))
        for i in range(len(queries)):
            self.assertEqual(queries[i].rounds, 1)
            self.assertEqual(queries[i].sender_id, 1)
            self.assertEqual(queries[i].assistor_id, list_content[i])
            self.assertEqual(json.loads(queries[i].situation), residual_list[i])

        # 4. check notification
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 1)
        self.assertEqual(json_response[-1]['name'], "unread situation")
        self.assertEqual(json_response[-1]['payload'], 2)

        # 5. update_situation_notification() (in unread_situation.py)
        data = json.dumps({'response_data': json_response})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response['unread situation']['check_dict']), 1)
        self.assertEqual(len(json_response['unread situation']['rounds_dict']), 1)
        self.assertEqual(json_response['unread situation']['check_dict'][str(task_id)], 1)
        self.assertEqual(json_response['unread situation']['rounds_dict'][str(task_id)], 1)

        # 6. check new notification
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 1)
        self.assertEqual(json_response[-1]['name'], "unread situation")
        self.assertEqual(json_response[-1]['payload'], 0)

        # 4. check notification
        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 2)
        self.assertEqual(json_response[-1]['name'], "unread situation")
        self.assertEqual(json_response[-1]['payload'], 2)

        # 5. update_situation_notification() (in unread_situation.py)
        data = json.dumps({'response_data': json_response})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response['unread situation']['check_dict']), 1)
        self.assertEqual(len(json_response['unread situation']['rounds_dict']), 1)
        self.assertEqual(json_response['unread situation']['check_dict'][str(task_id)], 0)
        self.assertEqual(json_response['unread situation']['rounds_dict'][str(task_id)], 1)

        # 6. check new notification
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 2)
        self.assertEqual(json_response[-1]['name'], "unread situation")
        self.assertEqual(json_response[-1]['payload'], 0)

        # 4. check notification
        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 2)
        self.assertEqual(json_response[-1]['name'], "unread situation")
        self.assertEqual(json_response[-1]['payload'], 2)

        # 5. update_situation_notification() (in unread_situation.py)
        data = json.dumps({'response_data': json_response})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response['unread situation']['check_dict']), 1)
        self.assertEqual(len(json_response['unread situation']['rounds_dict']), 1)
        self.assertEqual(json_response['unread situation']['check_dict'][str(task_id)], 0)
        self.assertEqual(json_response['unread situation']['rounds_dict'][str(task_id)], 1)

        # 6. check new notification
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 2)
        self.assertEqual(json_response[-1]['name'], "unread situation")
        self.assertEqual(json_response[-1]['payload'], 0)

    def test_send_output(self):

        # sponsor and 2 assistors, only assistor  would go into send_output()
        # 1. find_assistor() (in find_assistor.py)
        # 2. send_situation() (in send_situation.py)
        # 3. send_output() (in unread_situation.py) only assistor can send
        # 4. check new notification

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

        # 1. find_assistor() (in find_assistor.py)
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/create_new_train_task/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        task_id = json_response['task_id']

        list_content = [2,3]
        file = [['a','b','c'],[0,1,2],[4,5,6],[1,3,6],[]]
        data = json.dumps({'assistor_id_list': list_content, 'id_file': file, 'task_id': task_id})
        response = self.client.post('/find_assistor/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['task_id'], task_id)

        queries = Matched.query.filter(Matched.task_id == task_id, Matched.assistor_id_pair != 1, Matched.test_indicator == "train").all()
        self.assertEqual(len(queries), len(list_content))
        assistor_random_id_list = []
        for i in range(len(queries)):
            assistor_random_id_list.append(queries[i].assistor_random_id_pair)

        # 2. send_situation() (in send_situation.py)
        headers = self.get_token_auth_headers('unittest', '123')
        residual_list = [[[1,2,3], [4,5,6], [7,8,9]], [[1,2], [3,4]]]
        data = json.dumps({'residual_list': residual_list, 'task_id': task_id, "assistor_random_id_list": assistor_random_id_list})
        response = self.client.post('/send_situation/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['message'], 'send situation successfully!')

        # 3. send_output() (in unread_situation.py) only assistor can send
        headers = self.get_token_auth_headers('unittest2', '123')
        output_content = [[3,123,6], [88,5,6], [7,99,9]]
        data = json.dumps({'output': output_content, 'rounds': 0, 'task_id': task_id})
        response = self.client.post('/send_output/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['send_output'], "send output successfully")
        queries = Message.query.filter(Message.assistor_id == 1, Message.task_id == task_id, Message.rounds == 0, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), 2)
        self.assertEqual(queries[1].sender_id, 2)
        self.assertEqual(json.loads(queries[1].output), [[3,123,6], [88,5,6], [7,99,9]])

        # should not have unread output now, the notification updates only when all assistors in 
        # current task have uploaded
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
        queries = Message.query.filter(Message.assistor_id == 1, Message.task_id == task_id, Message.rounds == 0, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), 3)
        self.assertEqual(queries[2].sender_id, 3)
        self.assertEqual(json.loads(queries[2].output), [[6,123,6], [88,5,6], [7,87.6,9]])

        # 4. check new notification
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        print("--------------------------------------")
        print("json_response----------", json_response)
        self.assertEqual(len(json_response), 2)
        # self.assertEqual(len(json_response[-1]['sender_random_id_list']))
        self.assertEqual(json_response[-2]['name'], "unread situation")
        self.assertEqual(json_response[-2]['payload'], 1)
        self.assertEqual(json_response[-1]['name'], "unread output")
        self.assertEqual(json_response[-1]['payload'], 2)