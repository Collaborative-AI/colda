from base64 import b64encode
from datetime import datetime, timedelta
import json
import unittest
from Items import create_app, db
from Items.models import User, Message, Notification, Matched
from tests import TestConfig


class Unread_Match_ID_APITestCase(unittest.TestCase):

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
    
    def test_update_match_id_notification_one_recipient(self):
        
        # Simulate 1 recipient.
        # 1. Construct 1 Matched row in find_recipient().(find_recipient.py)
        # 2. Recipient upload ID file
        # 3. Sponsor upload, match the same ID (match_id.py)
        # 4. Check Notifications
        # 5. update_match_id_notification() (unread_match_id.py)
        # 6. Check Notifications

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
        data = json.dumps({'recipient_id_list': json.dumps(list_content)})
        response = self.client.post('/find_recipient/', headers=headers, data=data)
        json_response = json.loads(response.get_data(as_text=True))
        task_id = json_response['task_id']

        # 2. Recipient upload ID file
        headers = self.get_token_auth_headers('unittest2', '123')
        file_content = [['a','b','c'],[0,1,2],[4,5,6],[1,3,6],[]]
        data = json.dumps({'task_id': task_id, 'file': json.dumps(file_content)})
        response = self.client.post('/match_recipient_id/', headers=headers, data=data)

        # 3. Sponsor upload, match the same ID
        headers = self.get_token_auth_headers('unittest', '123')
        file_content = [['a','b','c'],[8,1,2],[4,5,6],[3,3,6],[]]
        data = json.dumps({'task_id': task_id, 'file': json.dumps(file_content)})
        response = self.client.post('/match_sponsor_id/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['stored'], "sponsor stores match id file successfully")
        self.assertEqual(json_response['task_id'], task_id)
        query = Matched.query.filter(Matched.task_id == task_id, Matched.sponsor_id == 1).all()
        self.assertEqual(json.loads(query[0].Matched_id_file), [4])

        # 4. Check the Notification of sponsor
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 1)
        self.assertEqual(json_response[0]['name'], "unread match id")
        self.assertEqual(json_response[0]['payload'], 1)

        # 5. Check Update_situation_notification() (unread_match_id.py)
        data = json.dumps({'task_id_list': json_response[0]['task_id_list'], 
            'sender_random_id_list': json_response[0]['sender_random_id_list']})
        response = self.client.post('/update_match_id_notification/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))

        self.assertEqual(json_response['check_sponsor'][str(task_id)], 1)

        # 6. Check Notification
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 1)
        self.assertEqual(json_response[0]['name'], "unread match id")
        self.assertEqual(json_response[0]['payload'], 0)

        # 4. Check the Notification of user 2
        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 2)
        self.assertEqual(json_response[0]['name'], "unread request")
        self.assertEqual(json_response[0]['payload'], 0)
        self.assertEqual(json_response[1]['name'], "unread match id")
        self.assertEqual(json_response[1]['payload'], 1)

        # 5. Check Update_match_id_notification() (unread_match_id.py)
        data = json.dumps({'task_id_list': json_response[1]['task_id_list'], 
            'sender_random_id_list': json_response[1]['sender_random_id_list']})
        response = self.client.post('/update_match_id_notification/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['check_sponsor'][str(task_id)], 0)

        # 6. Check Notification
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)

        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 2)
        self.assertEqual(json_response[0]['name'], "unread request")
        self.assertEqual(json_response[0]['payload'], 0)
        self.assertEqual(json_response[1]['name'], "unread match id")
        self.assertEqual(json_response[1]['payload'], 0)
        

    def test_update_match_id_notification_two_recipients(self):
        
        # Simulate 1 recipient.
        # 1. Construct 1 Matched row in find_recipient().(find_recipient.py)
        # 2. Recipient upload ID file
        # 3. Sponsor upload, match the same ID (match_id.py)
        # 4. Check Notifications
        # 5. update_match_id_notification() (unread_match_id.py)
        # 6. Check Notifications
        
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
        data = json.dumps({'recipient_id_list': json.dumps(list_content)})
        response = self.client.post('/find_recipient/', headers=headers, data=data)
        json_response = json.loads(response.get_data(as_text=True))
        task_id = json_response['task_id']

        # 2. Recipient upload ID file
        headers = self.get_token_auth_headers('unittest2', '123')
        file_content = [['a','b','c'],[0,1,2],[4,5,6],[2,3,6],[]]
        data = json.dumps({'task_id': task_id, 'file': json.dumps(file_content)})
        response = self.client.post('/match_recipient_id/', headers=headers, data=data)

        headers = self.get_token_auth_headers('unittest3', '123')
        file_content = [['a','b','c'],[2,1,2],[3,5,6],[4,3,6],[5],[12],[18],[]]
        data = json.dumps({'task_id': task_id, 'file': json.dumps(file_content)})
        response = self.client.post('/match_recipient_id/', headers=headers, data=data)

        # 3. Sponsor upload, match the same ID
        headers = self.get_token_auth_headers('unittest', '123')
        file_content = [['a','b','c'],[8,1,2],[4,5,6],[3,3,6],[]]
        data = json.dumps({'task_id': task_id, 'file': json.dumps(file_content)})
        response = self.client.post('/match_sponsor_id/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))

        # check sponsor match id file with user 2
        query = Matched.query.filter(Matched.task_id == task_id, Matched.recipient_id_pair == 2).all()
        self.assertEqual(json.loads(query[0].Matched_id_file), [4])

        # check sponsor match id file with user 3
        query = Matched.query.filter(Matched.task_id == task_id, Matched.recipient_id_pair == 3).all()
        self.assertEqual(json.loads(query[0].Matched_id_file), [3,4])

        # 4. Check the Notification of sponsor (updated in match_sponsor_id() (in match_id.py)) of sponsor
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 1)
        self.assertEqual(json_response[0]['name'], "unread match id")
        self.assertEqual(json_response[0]['payload'], 1)

        # 5. Check update_match_id_notification() (unread_match_id.py) result of sponsor
        data = json.dumps({'task_id_list': json_response[0]['task_id_list'], 
            'sender_random_id_list': json_response[0]['sender_random_id_list']})
        response = self.client.post('/update_match_id_notification/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['check_sponsor'][str(task_id)], 1)

        # 6. Check Notification
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 1)
        self.assertEqual(json_response[0]['name'], "unread match id")
        self.assertEqual(json_response[0]['payload'], 0)

        # 4. Check the Notification of user 2
        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 2)
        self.assertEqual(json_response[0]['name'], "unread request")
        self.assertEqual(json_response[0]['payload'], 0)
        self.assertEqual(json_response[1]['name'], "unread match id")
        self.assertEqual(json_response[1]['payload'], 1)

        # 5. Check Update_match_id_notification() (unread_match_id.py)
        data = json.dumps({'task_id_list': json_response[1]['task_id_list'], 
            'sender_random_id_list': json_response[1]['sender_random_id_list']})
        response = self.client.post('/update_match_id_notification/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['check_sponsor'][str(task_id)], 0)

        # 6. Check Notification
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)

        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 2)
        self.assertEqual(json_response[0]['name'], "unread request")
        self.assertEqual(json_response[0]['payload'], 0)
        self.assertEqual(json_response[1]['name'], "unread match id")
        self.assertEqual(json_response[1]['payload'], 0)

         # 4. Check the Notification of user 3
        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 2)
        self.assertEqual(json_response[0]['name'], "unread request")
        self.assertEqual(json_response[0]['payload'], 0)
        self.assertEqual(json_response[1]['name'], "unread match id")
        self.assertEqual(json_response[1]['payload'], 1)

        # 5. Check Update_match_id_notification() (unread_match_id.py)
        data = json.dumps({'task_id_list': json_response[1]['task_id_list'], 
            'sender_random_id_list': json_response[1]['sender_random_id_list']})
        response = self.client.post('/update_match_id_notification/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['check_sponsor'][str(task_id)], 0)

        # 6. Check Notification
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)

        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 2)
        self.assertEqual(json_response[0]['name'], "unread request")
        self.assertEqual(json_response[0]['payload'], 0)
        self.assertEqual(json_response[1]['name'], "unread match id")
        self.assertEqual(json_response[1]['payload'], 0)

    def test_get_user_match_id(self):

        # Simulate 1 recipient.
        # 1. Construct 1 Matched row in find_recipient().
        # 2. Match the sponsor ID file and the recipient ID file (match_id.py)
        # 2. Call get_user_match_id(gain the match id file for sponsor/recipient), check the response

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
        data = json.dumps({'recipient_id_list': json.dumps(list_content)})
        response = self.client.post('/find_recipient/', headers=headers, data=data)
        json_response = json.loads(response.get_data(as_text=True))
        task_id = json_response['task_id']

         # 2. Recipient upload ID file
        headers = self.get_token_auth_headers('unittest2', '123')
        file_content = [['a','b','c'],[0,1,2],[4,5,6],[1,3,6],[]]
        data = json.dumps({'task_id': task_id, 'file': json.dumps(file_content)})
        response = self.client.post('/match_recipient_id/', headers=headers, data=data)

        # 3. Sponsor upload, match the same ID
        headers = self.get_token_auth_headers('unittest', '123')
        file_content = [['a','b','c'],[8,1,2],[4,5,6],[3,3,6],[]]
        data = json.dumps({'task_id': task_id, 'file': json.dumps(file_content)})
        response = self.client.post('/match_sponsor_id/', headers=headers, data=data)
        
        # 4. check sponsor: sponsor call get_user_match_id()
        headers = self.get_token_auth_headers('unittest', '123')
        data = json.dumps({'task_id': task_id})
        # get => params; post => data
        response = self.client.get('/users/1/match_id_file/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        
        json_response = json.loads(response.get_data(as_text=True))
        self.assertIsNotNone(json_response.get('match_id_file'))
        self.assertIsNotNone(json_response.get('recipient_random_id_pair'))

        # test match id file
        match_id_file_list = json_response['match_id_file']
        self.assertEqual(json.loads(match_id_file_list[0]), [4])

        # test recipient random id pair
        recipient_random_id_pair_list = json_response['recipient_random_id_pair']
        query = Matched.query.filter(Matched.task_id == task_id, Matched.recipient_id_pair == 2).all()
        self.assertEqual(recipient_random_id_pair_list[0], query[0].recipient_random_id_pair)

        # 5. check recipient: recipient call get_user_match_id()
        headers = self.get_token_auth_headers('unittest2', '123')
        data = json.dumps({'task_id': task_id})
        response = self.client.get('/users/2/match_id_file/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        
        json_response = json.loads(response.get_data(as_text=True))
        self.assertIsNotNone(json_response.get('match_id_file'))
        self.assertIsNotNone(json_response.get('sponsor_random_id'))

        # test match id file
        match_id_file_list = json_response['match_id_file']
        self.assertEqual(json.loads(match_id_file_list[0]), [4])

        # test sponsor random id
        sponsor_random_id_list = json_response['sponsor_random_id']
        query = Matched.query.filter(Matched.task_id == task_id, Matched.recipient_id_pair == 2).all()
        self.assertEqual(sponsor_random_id_list[0], query[0].sponsor_random_id)


        