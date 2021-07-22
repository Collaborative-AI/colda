from base64 import b64encode
from datetime import datetime, timedelta
import json
import unittest
from Items import create_app, db
from Items.models import User, Message, Notification, Matched
from tests import TestConfig


class Unread_Test_Match_ID_APITestCase(unittest.TestCase):

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
    
    def test_update_test_match_id_notification_one_recipient(self):
        
        # Simulate 1 recipient.
        # 1. Construct 1 Matched row in find_recipient().(find_recipient.py)
        # 2. recipients check notification (unread_request => 1)
        # 3. recipients update request notification
        # 4. recipients check updated notification (unread_request => 0)
        # 5. Recipient upload ID file
        # 6. Check the Notification of sponsor and recipient
        # 7. Check update_all_notifications() (update_all_notifications.py)
        # 8. Check updated Notification

        u1 = User(username='unittest', email='john@163.com')
        u1.set_password('123')
        u2 = User(username='unittest2', email='john@163.com')
        u2.set_password('123')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()

        # 1. Construct 1 Matched row in find_recipient.
        headers = self.get_token_auth_headers('unittest', '123')
        list_content = [2]
        file = [['a','b','c'],[8,1,2],[4,5,6],[3,3,6],[]]
        data = json.dumps({'recipient_id_list': list_content, 'id_file': file})
        response = self.client.post('/find_recipient/', headers=headers, data=data)
        json_response = json.loads(response.get_data(as_text=True))
        task_id = json_response['task_id']

        headers = self.get_token_auth_headers('unittest', '123')
        file = [['a','b','c'],[0,1,2],[4,5,6],[1,3,6],[]]
        data = json.dumps({'task_id': task_id, 'id_file': file})
        response = self.client.post('/find_test_recipient/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)

        # 2. recipients check notification (unread_request => 1)
        # Check the Notification of user 2
        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response[-1]['name'], "unread test request")
        self.assertEqual(json_response[-1]['payload'], 1)

        # 3. update request notification
        headers = self.get_token_auth_headers('unittest2', '123')
        data = json.dumps({'response_data': json_response})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        
        # 4. recipients check updated notification (unread_request => 0)
        # Check the Notification of user 2
        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response[-1]['name'], "unread test request")
        self.assertEqual(json_response[-1]['payload'], 0)

        # 5. Recipient upload ID file
        headers = self.get_token_auth_headers('unittest2', '123')
        file_content = [['a','b','c'],[0,1,2],[4,5,6],[1,3,6],[]]
        data = json.dumps({'task_id': task_id, 'file': file_content})
        response = self.client.post('/match_test_recipient_id/', headers=headers, data=data)
        query = Matched.query.filter(Matched.task_id == task_id, Matched.sponsor_id == 1, Matched.test_indicator == "test").all()
        self.assertEqual(set(json.loads(query[0].Matched_id_file)), set([0,1,4]))

        # 6. Check the Notification of sponsor and recipient
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 1)
        self.assertEqual(json_response[-1]['name'], "unread test match id")
        self.assertEqual(json_response[-1]['payload'], 1)

        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response2 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response2), 3)
        self.assertEqual(json_response2[-2]['name'], "unread test request")
        self.assertEqual(json_response2[-2]['payload'], 0)
        self.assertEqual(json_response2[-1]['name'], "unread test match id")
        self.assertEqual(json_response2[-1]['payload'], 1)

        # 7. Check update_all_notifications() (update_all_notifications.py)
        headers = self.get_token_auth_headers('unittest', '123')
        data = json.dumps({'response_data': json_response})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response["unread test match id"]['check_dict'][str(task_id)], 1)

        headers = self.get_token_auth_headers('unittest2', '123')
        data = json.dumps({'response_data': json_response2})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response["unread test match id"]['check_dict'][str(task_id)], 0)

        # 8. Check updated Notification
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 1)
        self.assertEqual(json_response[-1]['name'], "unread test match id")
        self.assertEqual(json_response[-1]['payload'], 0)

        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 3)
        self.assertEqual(json_response[-2]['name'], "unread test request")
        self.assertEqual(json_response[-2]['payload'], 0)
        self.assertEqual(json_response[-1]['name'], "unread test match id")
        self.assertEqual(json_response[-1]['payload'], 0)
        

    def test_update_test_match_id_notification_two_recipients(self):
         # Simulate 1 recipient.
        # 1. Construct 1 Matched row in find_recipient().(find_recipient.py)
        # 2. recipients check notification (unread_request => 1)
        # 3. recipients update request notification
        # 4. recipients check updated notification (unread_request => 0)
        # 5. Recipient upload ID file
        # 6. Check the Notification of sponsor and recipient
        # 7. Check update_all_notifications() (update_all_notifications.py)
        # 8. Check updated Notification

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

        # 1. Construct 1 Matched row in find_recipient.
        headers = self.get_token_auth_headers('unittest', '123')
        list_content = [2,3]
        file = [['a','b','c'],[8,1,2],[4,5,6],[3,3,6],[]]
        data = json.dumps({'recipient_id_list': list_content, 'id_file': file})
        response = self.client.post('/find_recipient/', headers=headers, data=data)
        json_response = json.loads(response.get_data(as_text=True))
        task_id = json_response['task_id']

        headers = self.get_token_auth_headers('unittest', '123')
        file = [['a','b','c'],[8,1,2],[4,5,6],[3,3,6],[]]
        data = json.dumps({'task_id': task_id, 'id_file': file})
        response = self.client.post('/find_test_recipient/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)

        # 2. recipients check notification (unread_request => 1)
        # Check the Notification of user 2
        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response[-1]['name'], "unread test request")
        self.assertEqual(json_response[-1]['payload'], 1)

        # Check the Notification of user 3
        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response[-1]['name'], "unread test request")
        self.assertEqual(json_response[-1]['payload'], 1)

        # 3. update request notification
        headers = self.get_token_auth_headers('unittest2', '123')
        data = json.dumps({'response_data': json_response})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        
        headers = self.get_token_auth_headers('unittest3', '123')
        data = json.dumps({'response_data': json_response})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)

        # 4. recipients check updated notification (unread_request => 0)
        # Check the Notification of user 2
        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response[-1]['name'], "unread test request")
        self.assertEqual(json_response[-1]['payload'], 0)

        # Check the Notification of user 3
        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response[-1]['name'], "unread test request")
        self.assertEqual(json_response[-1]['payload'], 0)

        # 5. Recipient upload ID file
        headers = self.get_token_auth_headers('unittest2', '123')
        file_content = [['a','b','c'],[0,1,2],[4,5,6],[1,3,6],[]]
        data = json.dumps({'task_id': task_id, 'file': file_content})
        response = self.client.post('/match_test_recipient_id/', headers=headers, data=data)
        query = Matched.query.filter(Matched.task_id == task_id, Matched.sponsor_id == 1, Matched.test_indicator == "test").all()
        self.assertEqual(json.loads(query[0].Matched_id_file), [4])

        headers = self.get_token_auth_headers('unittest3', '123')
        file_content = [['a','b','c'],[8,1,2],[4,5,6],[1,3,6],[]]
        data = json.dumps({'task_id': task_id, 'file': file_content})
        response = self.client.post('/match_test_recipient_id/', headers=headers, data=data)
        query = Matched.query.filter(Matched.task_id == task_id, Matched.recipient_id_pair == 3, Matched.test_indicator == "test").first()
        self.assertEqual(set(json.loads(query.Matched_id_file)), set([8, 4]))

        # 6. Check the Notification of sponsor and recipient
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 1)
        self.assertEqual(json_response[-1]['name'], "unread test match id")
        self.assertEqual(json_response[-1]['payload'], 1)

        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response2 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response2), 3)
        self.assertEqual(json_response2[-2]['name'], "unread test request")
        self.assertEqual(json_response2[-2]['payload'], 0)
        self.assertEqual(json_response2[-1]['name'], "unread test match id")
        self.assertEqual(json_response2[-1]['payload'], 1)

        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response3 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response3), 3)
        self.assertEqual(json_response3[-2]['name'], "unread test request")
        self.assertEqual(json_response3[-2]['payload'], 0)
        self.assertEqual(json_response3[-1]['name'], "unread test match id")
        self.assertEqual(json_response3[-1]['payload'], 1)

        # check get test_match_id_file
        headers = self.get_token_auth_headers('unittest', '123')
        data = json.dumps({'task_id': task_id})
        response = self.client.post('/users/1/test_match_id_file/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response4 = json.loads(response.get_data(as_text=True))
        self.assertEqual(set(json.loads(json_response4['match_id_file'][0])), set([4]))
        self.assertEqual(set(json.loads(json_response4['match_id_file'][1])), set([8,4]))

        # 7. Check update_all_notifications() (update_all_notifications.py)
        headers = self.get_token_auth_headers('unittest', '123')
        data = json.dumps({'response_data': json_response})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response["unread test match id"]['check_dict'][str(task_id)], 1)

        headers = self.get_token_auth_headers('unittest2', '123')
        data = json.dumps({'response_data': json_response2})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response["unread test match id"]['check_dict'][str(task_id)], 0)

        headers = self.get_token_auth_headers('unittest3', '123')
        data = json.dumps({'response_data': json_response3})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response["unread test match id"]['check_dict'][str(task_id)], 0)

        # 8. Check updated Notification
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 1)
        self.assertEqual(json_response[-1]['name'], "unread test match id")
        self.assertEqual(json_response[-1]['payload'], 0)

        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 3)
        self.assertEqual(json_response[-2]['name'], "unread test request")
        self.assertEqual(json_response[-2]['payload'], 0)
        self.assertEqual(json_response[-1]['name'], "unread test match id")
        self.assertEqual(json_response[-1]['payload'], 0)

        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 3)
        self.assertEqual(json_response[-2]['name'], "unread test request")
        self.assertEqual(json_response[-2]['payload'], 0)
        self.assertEqual(json_response[-1]['name'], "unread test match id")
        self.assertEqual(json_response[-1]['payload'], 0)
            
    def test_send_test_output(self):

        # sponsor and 2 recipients, only recipient  would go into send_output()
        # 1. find_recipient() (in find_recipient.py)
        # 2. send_situation() (in send_situation.py)
        # 3. send_output() (in unread_situation.py) only recipient can send
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

        # 1. find_recipient() (in find_recipient.py)
        headers = self.get_token_auth_headers('unittest', '123')
        list_content = [2,3]
        file = [['a','b','c'],[0,1,2],[4,5,6],[1,3,6],[]]
        data = json.dumps({'recipient_id_list': list_content, 'id_file': file})
        response = self.client.post('/find_recipient/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        task_id = json_response['task_id']

        headers = self.get_token_auth_headers('unittest', '123')
        file = [['a','b','c'],[8,1,2],[4,5,6],[3,3,6],[]]
        data = json.dumps({'task_id': task_id, 'id_file': file})
        response = self.client.post('/find_test_recipient/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)

        # 3. send_output() (in unread_situation.py) only recipient can send
        headers = self.get_token_auth_headers('unittest2', '123')
        output = [[[1,2,3], [4,5,6], [7,8,9]],[[2,3],[4,5]]]
        data = json.dumps({'output': output, 'task_id': task_id})
        response = self.client.post('/send_test_output/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['send_test_output'], "send test output successfully")
        queries = Message.query.filter(Message.recipient_id == 1, Message.task_id == task_id, Message.test_indicator == "test").all()
        self.assertEqual(len(queries), 1)
        self.assertEqual(queries[0].sender_id, 2)
        self.assertEqual(json.loads(queries[0].output), [[[1,2,3], [4,5,6], [7,8,9]],[[2,3],[4,5]]])

        # should not have unread output now, the notification updates only when all recipients in 
        # current task have uploaded
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 0)

        headers = self.get_token_auth_headers('unittest3', '123')
        output = [[[6,123,6], [88,5,6], [7,87.6,9]],[[2]]]
        data = json.dumps({'output': output, 'task_id': task_id})
        response = self.client.post('/send_test_output/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['send_test_output'], "send test output successfully")
        queries = Message.query.filter(Message.recipient_id == 1, Message.task_id == task_id, Message.test_indicator == "test").all()
        self.assertEqual(len(queries), 2)
        self.assertEqual(queries[1].sender_id, 3)
        self.assertEqual(json.loads(queries[1].output), [[[6,123,6], [88,5,6], [7,87.6,9]],[[2]]])

        # 4. check new notification
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        print("--------------------------------------")
        print("json_response----------", json_response)
        self.assertEqual(len(json_response), 1)
        self.assertEqual(json_response[-1]['name'], "unread test output")
        self.assertEqual(json_response[-1]['payload'], 2)

        # 5. check sent test output
        headers = self.get_token_auth_headers('unittest', '123')
        data = json.dumps({'task_id': task_id})
        response = self.client.post('/users/1/test_output/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response4 = json.loads(response.get_data(as_text=True))
        self.assertEqual(json.loads(json_response4['output'][0]), [[[1,2,3], [4,5,6], [7,8,9]],[[2,3],[4,5]]])
        self.assertEqual(json.loads(json_response4['output'][1]), [[[6,123,6], [88,5,6], [7,87.6,9]],[[2]]])