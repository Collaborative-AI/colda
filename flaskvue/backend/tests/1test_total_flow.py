from base64 import b64encode
from datetime import datetime, timedelta
import json
import unittest
from Items import create_app, db
from Items.models import User, Message, Notification, Matched
from tests import TestConfig


class Test_total_flow_APITestCase(unittest.TestCase):

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
    
    def test_total_flow_once(self):

        # 1 sponsor and 2 assistors:

        # 1. sponsor call: find_assistor() (in finc_assistor.py)
        # 2. get task_id

        # 3. assistors check notification (unread_request => 1)
        # 4. assistors call: match_assistor_id() (in match_id.py) and upload file
        # 5. assistors check updated notification (unread_request => 0)
        # 6. sponsor call: match_sponsor_id() (in match_id.py) and upload file
        # 7. sponsor and assistors check notification (unread match id) (unread match id => 1)

        # 8. sponsor and assistors call update_match_id_notification() (in unread_match_id.py) and check updated notification (unread match id => 0)
        # 9. sponsor and assistor call: get_user_match_id() (in unread_match_id.py), get matched id file
        # 10. sponsor calls send_situation() (in send_situation.py)
        # 11. sponsor and assistors check notification (unread situation => 1)
         
        # 12. sponsor and assistors call update_situation_notification() (in unread_situation.py) and check updated notification (unread situation => 0)
        # 13. assistors call send_output() (in unread situation.py)

        # 14. sponsor check notification (unread output => 1)
        # 15. sponsor calls: update_output_notification() (in unread_output.py) and check updated notification (unread output => 0)
        # 16. sponsor calls: get_user_output() (in unread_output.py), gets output files
        # 17. sponsor calls: send_situation(), goes into new round 

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

        # 1. sponsor call: find_assistor() (in finc_assistor.py)
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/create_new_train_task/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        # 2. get task id
        task_id = json_response['task_id']

        list_content = [2,3]
        # file = [['a','b','c'],[8,1,2],[4,5,6],[3,3,6],[12],[16],[17,19]]
        file = "8\n4\n3\n12\n16\n17"
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

        # 3. assistors check notification (unread_request => 1)
        # Check the Notification of user 2
        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response2 = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response2[-1]['name'], "unread request")
        self.assertEqual(json_response2[-1]['payload'], 1)

        # User 3 cannot check the notification of user 2
        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 403)

        # Check the Notification of user 3
        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response3 = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response3[-1]['name'], "unread request")
        self.assertEqual(json_response3[-1]['payload'], 1)

        # 4. update request notification
        headers = self.get_token_auth_headers('unittest2', '123')
        data = json.dumps({'response_data': json_response2})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)

        headers = self.get_token_auth_headers('unittest3', '123')
        data = json.dumps({'response_data': json_response3})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)

        # 5. assistors check updated notification (unread_request => 0)
        # Check the Notification of user 2
        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response[-1]['name'], "unread request")
        self.assertEqual(json_response[-1]['payload'], 0)

        # Check the Notification of user 3
        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response[-1]['name'], "unread request")
        self.assertEqual(json_response[-1]['payload'], 0)

        # 6. assistors call: match_assistor_id() (in match_id.py) and upload file
        # assistors upload ID file
        headers = self.get_token_auth_headers('unittest2', '123')
        # file_content = [['a','b','c'],[0,1,2],[4,5,6],[1,3,6],[12],[16],[17],[18]]
        file_content = "0\n4\n1\n12\n16\n17\n18"
        data = json.dumps({'task_id': task_id, 'file': file_content})
        response = self.client.post('/match_assistor_id/', headers=headers, data=data)

        headers = self.get_token_auth_headers('unittest3', '123')
        # file_content = [['a','b','c'],[2,1,2],[3,5,6],[4,3,6],[5],[12],[18]]
        file_content = "2\n3\n4\n5\n12\n18"
        data = json.dumps({'task_id': task_id, 'file': file_content})
        response = self.client.post('/match_assistor_id/', headers=headers, data=data)

        # 5. assistors check updated notification (unread_request => 0)
        # Check the Notification of sponsor
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_1 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response_1), 1)
        self.assertEqual(json_response_1[-1]['name'], "unread match id")
        self.assertEqual(json_response_1[-1]['payload'], 1)

        # Check the Notification of user 2
        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_2 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response_2), 2)
        self.assertEqual(json_response_2[-2]['name'], "unread request")
        self.assertEqual(json_response_2[-2]['payload'], 0)
        self.assertEqual(json_response_2[-1]['name'], "unread match id")
        self.assertEqual(json_response_2[-1]['payload'], 1)

        # Check the Notification of user 3
        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_3 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response_3), 2)
        self.assertEqual(json_response_3[-2]['name'], "unread request")
        self.assertEqual(json_response_3[-2]['payload'], 0)
        self.assertEqual(json_response_3[-1]['name'], "unread match id")
        self.assertEqual(json_response_3[-1]['payload'], 1)

        # 6. sponsor and assistors call update_match_id_notification() (in unread_match_id.py) and check updated notification (unread match id => 0)
        headers = self.get_token_auth_headers('unittest', '123')
        data = json.dumps({'response_data': json_response_1})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response_1 = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response_1["unread match id"]['check_dict'][str(task_id)], 1)

        headers = self.get_token_auth_headers('unittest2', '123')
        data = json.dumps({'response_data': json_response_2})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response_2 = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response_2["unread match id"]['check_dict'][str(task_id)], 0)

        headers = self.get_token_auth_headers('unittest3', '123')
        data = json.dumps({'response_data': json_response_3})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response_3 = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response_3["unread match id"]['check_dict'][str(task_id)], 0)
        
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 1)
        self.assertEqual(json_response[-1]['name'], "unread match id")
        self.assertEqual(json_response[-1]['payload'], 0)

        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 2)
        self.assertEqual(json_response[-2]['name'], "unread request")
        self.assertEqual(json_response[-2]['payload'], 0)
        self.assertEqual(json_response[-1]['name'], "unread match id")
        self.assertEqual(json_response[-1]['payload'], 0)

        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 2)
        self.assertEqual(json_response[-2]['name'], "unread request")
        self.assertEqual(json_response[-2]['payload'], 0)
        self.assertEqual(json_response[-1]['name'], "unread match id")
        self.assertEqual(json_response[-1]['payload'], 0)

        # 9. sponsor and assistor call: get_user_match_id() (in unread_match_id.py), get matched id file
        headers = self.get_token_auth_headers('unittest', '123')
        data = json.dumps({'task_id': task_id})
        response = self.client.post('/users/1/match_id_file/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertIsNotNone(json_response.get('match_id_file'))
        self.assertIsNotNone(json_response.get('assistor_random_id_pair'))
        # test match id file
        match_id_file_list = json_response['match_id_file']
        self.assertEqual(set(json.loads(match_id_file_list[0])), set(["4","12","16","17"]))
        self.assertEqual(set(json.loads(match_id_file_list[1])), set(["3","4","12"]))

        headers = self.get_token_auth_headers('unittest2', '123')
        data = json.dumps({'task_id': task_id})
        response = self.client.post('/users/2/match_id_file/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertIsNotNone(json_response.get('match_id_file'))
        self.assertIsNotNone(json_response.get('sponsor_random_id'))
        # test match id file
        match_id_file_list = json_response['match_id_file']
        self.assertEqual(set(json.loads(match_id_file_list[0])), set(["4","12","16","17"]))

        headers = self.get_token_auth_headers('unittest3', '123')
        data = json.dumps({'task_id': task_id})
        response = self.client.post('/users/3/match_id_file/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertIsNotNone(json_response.get('match_id_file'))
        self.assertIsNotNone(json_response.get('sponsor_random_id'))
        # test match id file
        match_id_file_list = json_response['match_id_file']
        self.assertEqual(set(json.loads(match_id_file_list[0])), set(["3","4","12"]))

        # 10. sponsor calls send_situation() (in send_situation.py)
        headers = self.get_token_auth_headers('unittest', '123')
        residual_list = [[[1,2,3], [4,5,6], [7,8,9]], [[1,2], [3,4]]]
        data = json.dumps({'residual_list': residual_list, 'task_id': task_id, "assistor_random_id_list": assistor_random_id_list})
        response = self.client.post('/send_situation/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['message'], 'Add Message Done, but not add unread situation')

        headers = self.get_token_auth_headers('unittest2', '123')
        data = json.dumps({'task_id': task_id})
        response = self.client.post('/assistor_write_match_index_done/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['assistor_write_match_index_done'], 'Assistors dont finish')

        headers = self.get_token_auth_headers('unittest3', '123')
        data = json.dumps({'task_id': task_id})
        response = self.client.post('/assistor_write_match_index_done/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['assistor_write_match_index_done'], 'Send unread situation')

        queries = Message.query.filter(Message.assistor_id != 1, Message.task_id == task_id, Message.rounds == 0, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), len(list_content))
        for i in range(len(queries)):
            self.assertEqual(queries[i].rounds, 0)
            self.assertEqual(queries[i].sender_id, 1)
            self.assertEqual(queries[i].assistor_id, list_content[i])
            self.assertEqual(json.loads(queries[i].situation), residual_list[i])

        # 11. sponsor and assistors check notification (unread situation => 1)
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_1 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response_1), 2)
        self.assertEqual(json_response_1[-1]['name'], "unread situation")
        self.assertEqual(json_response_1[-1]['payload'], 1)

        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_2 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response_2), 3)
        self.assertEqual(json_response_2[-1]['name'], "unread situation")
        self.assertEqual(json_response_2[-1]['payload'], 1)

        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_3 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response_3), 3)
        self.assertEqual(json_response_3[-1]['name'], "unread situation")
        self.assertEqual(json_response_3[-1]['payload'], 1)

        # 12. sponsor and assistors call update_situation_notification() (in unread_situation.py) and check updated notification (unread situation => 0)
        headers = self.get_token_auth_headers('unittest', '123')
        data = json.dumps({'response_data': json_response_1})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response['unread situation']['check_dict']), 1)
        self.assertEqual(len(json_response['unread situation']['rounds_dict']), 1)
        self.assertEqual(json_response['unread situation']['check_dict'][str(task_id)], 1)
        self.assertEqual(json_response['unread situation']['rounds_dict'][str(task_id)], 0)

        headers = self.get_token_auth_headers('unittest2', '123')
        data = json.dumps({'response_data': json_response_2})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response['unread situation']['check_dict']), 1)
        self.assertEqual(len(json_response['unread situation']['rounds_dict']), 1)
        self.assertEqual(json_response['unread situation']['check_dict'][str(task_id)], 0)
        self.assertEqual(json_response['unread situation']['rounds_dict'][str(task_id)], 0)

        headers = self.get_token_auth_headers('unittest3', '123')
        data = json.dumps({'response_data': json_response_3})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response['unread situation']['check_dict']), 1)
        self.assertEqual(len(json_response['unread situation']['rounds_dict']), 1)
        self.assertEqual(json_response['unread situation']['check_dict'][str(task_id)], 0)
        self.assertEqual(json_response['unread situation']['rounds_dict'][str(task_id)], 0)

        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 2)
        self.assertEqual(json_response[-1]['name'], "unread situation")
        self.assertEqual(json_response[-1]['payload'], 0)

        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 3)
        self.assertEqual(json_response[-1]['name'], "unread situation")
        self.assertEqual(json_response[-1]['payload'], 0)

        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 3)
        self.assertEqual(json_response[-1]['name'], "unread situation")
        self.assertEqual(json_response[-1]['payload'], 0)
        
        # 13. assistors call send_output() (in unread situation.py)
        headers = self.get_token_auth_headers('unittest2', '123')
        output_content = [[3,123,6], [88,5,6], [7,99,9]]
        data = json.dumps({'output': output_content, 'rounds': 0, 'task_id': task_id})
        response = self.client.post('/send_output/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['send_output'], "Sponsor doesnt finish training")
        queries = Message.query.filter(Message.assistor_id == 1, Message.task_id == task_id, Message.rounds == 0, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), 2)
        self.assertEqual(queries[-1].sender_id, 2)
        self.assertEqual(json.loads(queries[-1].output), [[3,123,6], [88,5,6], [7,99,9]])

        headers = self.get_token_auth_headers('unittest3', '123')
        output_content = [[6,123,6], [88,5,6], [7,87.6,9]]
        data = json.dumps({'output': output_content, 'rounds': 0, 'task_id': task_id})
        response = self.client.post('/send_output/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['send_output'], "Sponsor doesnt finish training")
        queries = Message.query.filter(Message.assistor_id == 1, Message.task_id == task_id, Message.rounds == 0, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), 3)
        self.assertEqual(queries[-1].sender_id, 3)
        self.assertEqual(json.loads(queries[-1].output), [[6,123,6], [88,5,6], [7,87.6,9]])

        headers = self.get_token_auth_headers('unittest', '123')
        data = json.dumps({'task_id': task_id})
        response = self.client.post('/Sponsor_situation_training_done/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['Sponsor_situation_training_done'], "Send unread output")

        # 14. sponsor check notification (unread output => 1)
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        print("json_response", json_response)
        self.assertEqual(len(json_response), 3)
        self.assertEqual(json_response[-2]['name'], "unread situation")
        self.assertEqual(json_response[-2]['payload'], 0)
        self.assertEqual(json_response[-1]['name'], "unread output")
        self.assertEqual(json_response[-1]['payload'], 2)

        # 15. sponsor calls: update_output_notification() (in unread_output.py) and check updated notification (unread output => 0)
        data = json.dumps({'response_data': json_response})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        # check rounds
        self.assertEqual(json_response["unread output"]['rounds_dict'][str(task_id)], 0)

        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 3)
        self.assertEqual(json_response[-2]['name'], "unread situation")
        self.assertEqual(json_response[-2]['payload'], 0)
        self.assertEqual(json_response[-1]['name'], "unread output")
        self.assertEqual(json_response[-1]['payload'], 0)

        # 16. sponsor calls: get_user_output() (in unread_output.py), gets output files
        data = json.dumps({'task_id': task_id, 'rounds': 0})
        response = self.client.post('/users/1/output/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json.loads(json_response['output'][0]), [[3,123,6], [88,5,6], [7,99,9]])
        self.assertEqual(json.loads(json_response['output'][1]), [[6,123,6], [88,5,6], [7,87.6,9]])

        # 17. sponsor calls: send_situation(), goes into new round 
        headers = self.get_token_auth_headers('unittest', '123')
        residual_list = [[[1,2,3], [4,5,6]], [[1,2]]]
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

    def test_total_flow_once_send_situation_send_output(self):

        # 1 sponsor and 2 assistors:

        # 1. sponsor call: find_assistor() (in finc_assistor.py)
        # 2. get task_id

        # 3. assistors check notification (unread_request => 1)
        # 4. assistors call: match_assistor_id() (in match_id.py) and upload file
        # 5. assistors check updated notification (unread_request => 0)
        # 6. sponsor call: match_sponsor_id() (in match_id.py) and upload file
        # 7. sponsor and assistors check notification (unread match id) (unread match id => 1)

        # 8. sponsor and assistors call update_match_id_notification() (in unread_match_id.py) and check updated notification (unread match id => 0)
        # 9. sponsor and assistor call: get_user_match_id() (in unread_match_id.py), get matched id file
        # 10. sponsor calls send_situation() (in send_situation.py)
        # 11. sponsor and assistors check notification (unread situation => 1)
         
        # 12. sponsor and assistors call update_situation_notification() (in unread_situation.py) and check updated notification (unread situation => 0)
        # 13. assistors call send_output() (in unread situation.py)

        # 14. sponsor check notification (unread output => 1)
        # 15. sponsor calls: update_output_notification() (in unread_output.py) and check updated notification (unread output => 0)
        # 16. sponsor calls: get_user_output() (in unread_output.py), gets output files
        # 17. sponsor calls: send_situation(), goes into new round 

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

        # 1. sponsor call: find_assistor() (in finc_assistor.py)
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/create_new_train_task/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        # 2. get task id
        task_id = json_response['task_id']

        list_content = [2,3]
        # file = [['a','b','c'],[8,1,2],[4,5,6],[3,3,6],[12],[16],[17,19]]
        file = "8\n4\n3\n12\n16\n17"
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

        # 3. assistors check notification (unread_request => 1)
        # Check the Notification of user 2
        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response2 = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response2[-1]['name'], "unread request")
        self.assertEqual(json_response2[-1]['payload'], 1)

        # User 3 cannot check the notification of user 2
        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 403)

        # Check the Notification of user 3
        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response3 = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response3[-1]['name'], "unread request")
        self.assertEqual(json_response3[-1]['payload'], 1)

        # 4. update request notification
        headers = self.get_token_auth_headers('unittest2', '123')
        data = json.dumps({'response_data': json_response2})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)

        headers = self.get_token_auth_headers('unittest3', '123')
        data = json.dumps({'response_data': json_response3})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)

        # 5. assistors check updated notification (unread_request => 0)
        # Check the Notification of user 2
        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response[-1]['name'], "unread request")
        self.assertEqual(json_response[-1]['payload'], 0)

        # Check the Notification of user 3
        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response[-1]['name'], "unread request")
        self.assertEqual(json_response[-1]['payload'], 0)

        # 6. assistors call: match_assistor_id() (in match_id.py) and upload file
        # assistors upload ID file
        headers = self.get_token_auth_headers('unittest2', '123')
        # file_content = [['a','b','c'],[0,1,2],[4,5,6],[1,3,6],[12],[16],[17],[18]]
        file_content = "0\n4\n1\n12\n16\n17\n18"
        data = json.dumps({'task_id': task_id, 'file': file_content})
        response = self.client.post('/match_assistor_id/', headers=headers, data=data)

        headers = self.get_token_auth_headers('unittest3', '123')
        # file_content = [['a','b','c'],[2,1,2],[3,5,6],[4,3,6],[5],[12],[18]]
        file_content = "2\n3\n4\n5\n12\n18"
        data = json.dumps({'task_id': task_id, 'file': file_content})
        response = self.client.post('/match_assistor_id/', headers=headers, data=data)

        # 5. assistors check updated notification (unread_request => 0)
        # Check the Notification of sponsor
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_1 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response_1), 1)
        self.assertEqual(json_response_1[-1]['name'], "unread match id")
        self.assertEqual(json_response_1[-1]['payload'], 1)

        # Check the Notification of user 2
        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_2 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response_2), 2)
        self.assertEqual(json_response_2[-2]['name'], "unread request")
        self.assertEqual(json_response_2[-2]['payload'], 0)
        self.assertEqual(json_response_2[-1]['name'], "unread match id")
        self.assertEqual(json_response_2[-1]['payload'], 1)

        # Check the Notification of user 3
        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_3 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response_3), 2)
        self.assertEqual(json_response_3[-2]['name'], "unread request")
        self.assertEqual(json_response_3[-2]['payload'], 0)
        self.assertEqual(json_response_3[-1]['name'], "unread match id")
        self.assertEqual(json_response_3[-1]['payload'], 1)

        # 6. sponsor and assistors call update_match_id_notification() (in unread_match_id.py) and check updated notification (unread match id => 0)
        headers = self.get_token_auth_headers('unittest', '123')
        data = json.dumps({'response_data': json_response_1})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response_1 = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response_1["unread match id"]['check_dict'][str(task_id)], 1)

        headers = self.get_token_auth_headers('unittest2', '123')
        data = json.dumps({'response_data': json_response_2})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response_2 = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response_2["unread match id"]['check_dict'][str(task_id)], 0)

        headers = self.get_token_auth_headers('unittest3', '123')
        data = json.dumps({'response_data': json_response_3})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response_3 = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response_3["unread match id"]['check_dict'][str(task_id)], 0)
        
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 1)
        self.assertEqual(json_response[-1]['name'], "unread match id")
        self.assertEqual(json_response[-1]['payload'], 0)

        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 2)
        self.assertEqual(json_response[-2]['name'], "unread request")
        self.assertEqual(json_response[-2]['payload'], 0)
        self.assertEqual(json_response[-1]['name'], "unread match id")
        self.assertEqual(json_response[-1]['payload'], 0)

        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 2)
        self.assertEqual(json_response[-2]['name'], "unread request")
        self.assertEqual(json_response[-2]['payload'], 0)
        self.assertEqual(json_response[-1]['name'], "unread match id")
        self.assertEqual(json_response[-1]['payload'], 0)

        # 9. sponsor and assistor call: get_user_match_id() (in unread_match_id.py), get matched id file
        headers = self.get_token_auth_headers('unittest', '123')
        data = json.dumps({'task_id': task_id})
        response = self.client.post('/users/1/match_id_file/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertIsNotNone(json_response.get('match_id_file'))
        self.assertIsNotNone(json_response.get('assistor_random_id_pair'))
        # test match id file
        match_id_file_list = json_response['match_id_file']
        self.assertEqual(set(json.loads(match_id_file_list[0])), set(["4","12","16","17"]))
        self.assertEqual(set(json.loads(match_id_file_list[1])), set(["3","4","12"]))

        headers = self.get_token_auth_headers('unittest2', '123')
        data = json.dumps({'task_id': task_id})
        response = self.client.post('/users/2/match_id_file/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertIsNotNone(json_response.get('match_id_file'))
        self.assertIsNotNone(json_response.get('sponsor_random_id'))
        # test match id file
        match_id_file_list = json_response['match_id_file']
        self.assertEqual(set(json.loads(match_id_file_list[0])), set(["4","12","16","17"]))

        headers = self.get_token_auth_headers('unittest3', '123')
        data = json.dumps({'task_id': task_id})
        response = self.client.post('/users/3/match_id_file/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertIsNotNone(json_response.get('match_id_file'))
        self.assertIsNotNone(json_response.get('sponsor_random_id'))
        # test match id file
        match_id_file_list = json_response['match_id_file']
        self.assertEqual(set(json.loads(match_id_file_list[0])), set(["3","4","12"]))

        # 10. sponsor calls send_situation() (in send_situation.py)
        headers = self.get_token_auth_headers('unittest3', '123')
        data = json.dumps({'task_id': task_id})
        response = self.client.post('/assistor_write_match_index_done/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['assistor_write_match_index_done'], 'Assistors dont finish')

        headers = self.get_token_auth_headers('unittest2', '123')
        data = json.dumps({'task_id': task_id})
        response = self.client.post('/assistor_write_match_index_done/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['assistor_write_match_index_done'], 'Situation doesnt update')

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

        # 11. sponsor and assistors check notification (unread situation => 1)
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_1 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response_1), 2)
        self.assertEqual(json_response_1[-1]['name'], "unread situation")
        self.assertEqual(json_response_1[-1]['payload'], 1)

        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_2 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response_2), 3)
        self.assertEqual(json_response_2[-1]['name'], "unread situation")
        self.assertEqual(json_response_2[-1]['payload'], 1)

        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_3 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response_3), 3)
        self.assertEqual(json_response_3[-1]['name'], "unread situation")
        self.assertEqual(json_response_3[-1]['payload'], 1)

        # 12. sponsor and assistors call update_situation_notification() (in unread_situation.py) and check updated notification (unread situation => 0)
        headers = self.get_token_auth_headers('unittest', '123')
        data = json.dumps({'response_data': json_response_1})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response['unread situation']['check_dict']), 1)
        self.assertEqual(len(json_response['unread situation']['rounds_dict']), 1)
        self.assertEqual(json_response['unread situation']['check_dict'][str(task_id)], 1)
        self.assertEqual(json_response['unread situation']['rounds_dict'][str(task_id)], 0)

        headers = self.get_token_auth_headers('unittest2', '123')
        data = json.dumps({'response_data': json_response_2})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response['unread situation']['check_dict']), 1)
        self.assertEqual(len(json_response['unread situation']['rounds_dict']), 1)
        self.assertEqual(json_response['unread situation']['check_dict'][str(task_id)], 0)
        self.assertEqual(json_response['unread situation']['rounds_dict'][str(task_id)], 0)

        headers = self.get_token_auth_headers('unittest3', '123')
        data = json.dumps({'response_data': json_response_3})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response['unread situation']['check_dict']), 1)
        self.assertEqual(len(json_response['unread situation']['rounds_dict']), 1)
        self.assertEqual(json_response['unread situation']['check_dict'][str(task_id)], 0)
        self.assertEqual(json_response['unread situation']['rounds_dict'][str(task_id)], 0)

        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 2)
        self.assertEqual(json_response[-1]['name'], "unread situation")
        self.assertEqual(json_response[-1]['payload'], 0)

        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 3)
        self.assertEqual(json_response[-1]['name'], "unread situation")
        self.assertEqual(json_response[-1]['payload'], 0)

        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 3)
        self.assertEqual(json_response[-1]['name'], "unread situation")
        self.assertEqual(json_response[-1]['payload'], 0)
        
        # 13. assistors call send_output() (in unread situation.py)
        headers = self.get_token_auth_headers('unittest', '123')
        data = json.dumps({'task_id': task_id})
        response = self.client.post('/Sponsor_situation_training_done/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['Sponsor_situation_training_done'], "Assistors havent upload all output")

        headers = self.get_token_auth_headers('unittest2', '123')
        output_content = [[3,123,6], [88,5,6], [7,99,9]]
        data = json.dumps({'output': output_content, 'rounds': 0, 'task_id': task_id})
        response = self.client.post('/send_output/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['send_output'], "Assistors havent upload all outputs")
        queries = Message.query.filter(Message.assistor_id == 1, Message.task_id == task_id, Message.rounds == 0, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), 2)
        self.assertEqual(queries[-1].sender_id, 2)
        self.assertEqual(json.loads(queries[-1].output), [[3,123,6], [88,5,6], [7,99,9]])

        headers = self.get_token_auth_headers('unittest3', '123')
        output_content = [[6,123,6], [88,5,6], [7,87.6,9]]
        data = json.dumps({'output': output_content, 'rounds': 0, 'task_id': task_id})
        response = self.client.post('/send_output/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['send_output'], "send output successfully")
        queries = Message.query.filter(Message.assistor_id == 1, Message.task_id == task_id, Message.rounds == 0, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), 3)
        self.assertEqual(queries[-1].sender_id, 3)
        self.assertEqual(json.loads(queries[-1].output), [[6,123,6], [88,5,6], [7,87.6,9]])


        # 14. sponsor check notification (unread output => 1)
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        print("json_response", json_response)
        self.assertEqual(len(json_response), 3)
        self.assertEqual(json_response[-2]['name'], "unread situation")
        self.assertEqual(json_response[-2]['payload'], 0)
        self.assertEqual(json_response[-1]['name'], "unread output")
        self.assertEqual(json_response[-1]['payload'], 2)

        # 15. sponsor calls: update_output_notification() (in unread_output.py) and check updated notification (unread output => 0)
        data = json.dumps({'response_data': json_response})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        # check rounds
        self.assertEqual(json_response["unread output"]['rounds_dict'][str(task_id)], 0)

        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 3)
        self.assertEqual(json_response[-2]['name'], "unread situation")
        self.assertEqual(json_response[-2]['payload'], 0)
        self.assertEqual(json_response[-1]['name'], "unread output")
        self.assertEqual(json_response[-1]['payload'], 0)

        # 16. sponsor calls: get_user_output() (in unread_output.py), gets output files
        data = json.dumps({'task_id': task_id, 'rounds': 0})
        response = self.client.post('/users/1/output/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json.loads(json_response['output'][0]), [[3,123,6], [88,5,6], [7,99,9]])
        self.assertEqual(json.loads(json_response['output'][1]), [[6,123,6], [88,5,6], [7,87.6,9]])

        # 17. sponsor calls: send_situation(), goes into new round 
        headers = self.get_token_auth_headers('unittest', '123')
        residual_list = [[[1,2,3], [4,5,6]], [[1,2]]]
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