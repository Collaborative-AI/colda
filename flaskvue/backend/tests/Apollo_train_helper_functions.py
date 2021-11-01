from base64 import b64encode
from datetime import datetime, timedelta
import json
import unittest
from Items import create_app, db
from Items.models import User, Message, Notification, Matched
from tests import TestConfig


class Train_Helper_API_TestCase(unittest.TestCase):

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
    
    def find_assistor_two_assistors_helper(self):

        # Check 1 sponsor with 2 assistors
        # Construct 2 new Matched rows
        # Check the Notification of each assistor

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

        # 附带JWT到请求头中
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/create_new_train_task/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        task_id = json_response['task_id']
        self.task_id = task_id

        list_content = ['unittest2', 'unittest4']
        # file = [['a','b','c'],[0,1,2],[4,5,6],[1,3,6]]
        file = "8\n4\n3\n12\n16\n17"
        data = json.dumps({'assistor_username_list': list_content, 'id_file': file, 'task_id': task_id, 'task_name': "", 'task_description': ""})
        response = self.client.post('/find_assistor/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response, "wrong username")

        headers = self.get_token_auth_headers('unittest', '123')
        list_content = ['unittest2', 'unittest3']
        # file = [['a','b','c'],[0,1,2],[4,5,6],[1,3,6]]
        file = "8\n4\n3\n12\n16\n17"
        data = json.dumps({'assistor_username_list': list_content, 'id_file': file, 'task_id': task_id, 'task_name': "", 'task_description': ""})
        response = self.client.post('/find_assistor/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['task_id'], task_id)
        assistor_num = json_response['assistor_num']

        # check Matched database new rows, include sponsor to sponsor
        queries = Matched.query.filter(Matched.task_id == task_id, Matched.test_indicator == "train").all()
        self.assertEqual(len(queries), assistor_num+1)
        sponsor_random_id = queries[0].sponsor_random_id
        for i in range(len(queries)):
            print("query", queries[i].sponsor_id)
            self.assertEqual(queries[i].sponsor_id, 1) 
            self.assertEqual(queries[i].task_id, task_id)
            self.assertEqual(queries[i].sponsor_random_id, sponsor_random_id)
            # self.assertEqual(set(json.loads(queries[i].Matched_id_file)), set([0, 4, 1]))
            self.assertEqual(set(json.loads(queries[i].Matched_id_file)), set(["8", "4", "3","12","16","17"]))

        queries = Matched.query.filter(Matched.task_id == task_id, Matched.assistor_id_pair != 1, Matched.test_indicator == "train").all()
        self.assertEqual(len(queries), len(list_content))
        assistor_random_id_list = []
        for i in range(len(queries)):
            assistor_random_id_list.append(queries[i].assistor_random_id_pair)

        # check the row that sponsor to sponsor
        queries = Matched.query.filter(Matched.task_id == task_id, Matched.assistor_id_pair == 1, Matched.test_indicator == "train").all()
        self.assertEqual(len(queries), 1)
        self.assertEqual(queries[0].sponsor_id, 1)
        
        return task_id, list_content, assistor_random_id_list
    
    def unread_request_two_users_helper(self, task_id, list_content, assistor_random_id_list):

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

        # 3. update request notification
        headers = self.get_token_auth_headers('unittest2', '123')
        data = json.dumps({'response_data': json_response2})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)

        headers = self.get_token_auth_headers('unittest3', '123')
        data = json.dumps({'response_data': json_response3})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)

        # 4. check update notification
        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response[-1]['name'], "unread request")
        self.assertEqual(json_response[-1]['payload'], 0)

        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response[-1]['name'], "unread request")
        self.assertEqual(json_response[-1]['payload'], 0)

         # 5. assistor uploads the ID file
        headers = self.get_token_auth_headers('unittest2', '123')
        # file_content = [['a','b','c'],[0,1,2],[4,5,6],[3,3,6]]
        file_content = "0\n4\n1\n12\n16\n17\n18"
        data = json.dumps({'task_id': task_id, 'file': file_content})
        response = self.client.post('/match_assistor_id/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        stored = json_response['stored']
        task_id_response = json_response['task_id']
        self.assertEqual(stored, "assistor match id stored")
        self.assertEqual(task_id, task_id_response)
        # test matched id file
        query = Matched.query.filter(Matched.task_id == task_id, Matched.assistor_id_pair == 2, Matched.test_indicator == "train").all()
        self.assertEqual(set(json.loads(query[0].Matched_id_file)), set(["4","12","16","17"]))

        # should not exist notification yet
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 0)
        
        headers = self.get_token_auth_headers('unittest3', '123')
        # file_content = [['a','b','c'],[0,1,2],[5,5,6],[3,3,6]]
        file_content = "2\n3\n4\n5\n12\n18"
        data = json.dumps({'task_id': task_id, 'file': file_content})
        response = self.client.post('/match_assistor_id/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        stored = json_response['stored']
        task_id_response = json_response['task_id']
        self.assertEqual(stored, "assistor match id stored")
        self.assertEqual(task_id, task_id_response)
        # test matched id file
        query = Matched.query.filter(Matched.task_id == task_id, Matched.assistor_id_pair == 3, Matched.test_indicator == "train").all()
        self.assertEqual(set(json.loads(query[0].Matched_id_file)), set(["3","4","12"]))

        return task_id, list_content, assistor_random_id_list

    def unread_match_id_two_users_helper(self, task_id, list_content, assistor_random_id_list):
        
        # 6. Check Updated Notification
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_1 = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response_1[-1]['name'], "unread match id")
        self.assertEqual(json_response_1[-1]['payload'], 1)

        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_2 = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response_2[-2]['name'], "unread request")
        self.assertEqual(json_response_2[-2]['payload'], 0)
        self.assertEqual(json_response_2[-1]['name'], "unread match id")
        self.assertEqual(json_response_2[-1]['payload'], 1)

        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_3 = json.loads(response.get_data(as_text=True))
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
        # headers = self.get_token_auth_headers('unittest3', '123')
        # data = json.dumps({'task_id': task_id})
        # response = self.client.post('/assistor_write_match_index_done/', headers=headers, data=data)
        # self.assertEqual(response.status_code, 200)
        # json_response = json.loads(response.get_data(as_text=True))
        # self.assertEqual(json_response['assistor_write_match_index_done'], 'Assistors dont finish')

        # headers = self.get_token_auth_headers('unittest2', '123')
        # data = json.dumps({'task_id': task_id})
        # response = self.client.post('/assistor_write_match_index_done/', headers=headers, data=data)
        # self.assertEqual(response.status_code, 200)
        # json_response = json.loads(response.get_data(as_text=True))
        # self.assertEqual(json_response['assistor_write_match_index_done'], 'Situation doesnt update')

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
        
        return task_id, list_content, assistor_random_id_list

    def unread_situation_two_users_helper(self, task_id, list_content, assistor_random_id_list, test_round, sponsor_stop, user2_stop, user3_stop):     

        # 11. sponsor and assistors check notification (unread situation => 1)
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_1 = json.loads(response.get_data(as_text=True))
        print("********", json_response_1)
        if sponsor_stop or user2_stop or user2_stop:
            if test_round == 0:
                self.assertEqual(len(json_response_1), 3)
            else:
                self.assertEqual(len(json_response_1), 4)
            
            self.assertEqual(json_response_1[-1]['name'], "unread train stop")
        else:
            if test_round == 0:
                self.assertEqual(len(json_response_1), 2)
            else:
                self.assertEqual(len(json_response_1), 3)
 
            self.assertEqual(json_response_1[-1]['name'], "unread situation")
            self.assertEqual(json_response_1[-1]['payload'], 1)

        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_2 = json.loads(response.get_data(as_text=True))
        if user2_stop or sponsor_stop:
            self.assertEqual(len(json_response_2), 4)
            self.assertEqual(json_response_2[-2]['name'], "unread situation")
            self.assertEqual(json_response_2[-2]['payload'], 1)
            self.assertEqual(json_response_2[-1]['name'], "unread train stop")
            self.assertEqual(json_response_2[-1]['payload'], 1)
        else:
            self.assertEqual(len(json_response_2), 3)
            self.assertEqual(json_response_2[-1]['name'], "unread situation")
            self.assertEqual(json_response_2[-1]['payload'], 1)

        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_3 = json.loads(response.get_data(as_text=True))
        if user3_stop or sponsor_stop:
            self.assertEqual(len(json_response_3), 4)
            self.assertEqual(json_response_3[-2]['name'], "unread situation")
            self.assertEqual(json_response_3[-2]['payload'], 1)
            self.assertEqual(json_response_3[-1]['name'], "unread train stop")
            self.assertEqual(json_response_3[-1]['payload'], 1)
        else:
            self.assertEqual(len(json_response_3), 3)
            self.assertEqual(json_response_3[-1]['name'], "unread situation")
            self.assertEqual(json_response_3[-1]['payload'], 1)
        
        # 12. sponsor and assistors call update_situation_notification() (in unread_situation.py) and check updated notification (unread situation => 0)
        headers = self.get_token_auth_headers('unittest', '123')
        data = json.dumps({'response_data': json_response_1})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        print("((", json_response)
        if sponsor_stop:
            self.assertEqual(len(json_response['unread situation']['check_dict']), 0)
            self.assertEqual(len(json_response['unread situation']['rounds_dict']), 0)
        else:
            self.assertEqual(len(json_response['unread situation']['check_dict']), 1)
            self.assertEqual(len(json_response['unread situation']['rounds_dict']), 1)
            self.assertEqual(json_response['unread situation']['check_dict'][str(task_id)], 1)
            self.assertEqual(json_response['unread situation']['rounds_dict'][str(task_id)], test_round)

        if sponsor_stop:
            self.assertEqual(len(json_response["unread train stop"]['task_id_to_deleted_user_id'][task_id]), 2)
            self.assertEqual(len(json_response["unread train stop"]['most_recent_round'][task_id]), 2)
            self.assertEqual(json_response["unread train stop"]['task_id_to_deleted_user_id'][task_id][0], 2)
            self.assertEqual(json_response["unread train stop"]['most_recent_round'][task_id][0], test_round)
            self.assertEqual(json_response["unread train stop"]['task_id_to_deleted_user_id'][task_id][1], 3)
            self.assertEqual(json_response["unread train stop"]['most_recent_round'][task_id][1], test_round)
        elif user2_stop:
            self.assertEqual(len(json_response["unread train stop"]['task_id_to_deleted_user_id'][task_id]), 1)
            self.assertEqual(len(json_response["unread train stop"]['most_recent_round'][task_id]), 1)
            self.assertEqual(json_response["unread train stop"]['task_id_to_deleted_user_id'][task_id][0], 2)
            self.assertEqual(json_response["unread train stop"]['most_recent_round'][task_id][0], test_round)
        elif user3_stop:
            self.assertEqual(len(json_response["unread train stop"]['task_id_to_deleted_user_id'][task_id]), 1)
            self.assertEqual(len(json_response["unread train stop"]['most_recent_round'][task_id]), 1)
            self.assertEqual(json_response["unread train stop"]['task_id_to_deleted_user_id'][task_id][0], 3)
            self.assertEqual(json_response["unread train stop"]['most_recent_round'][task_id][0], test_round)


        headers = self.get_token_auth_headers('unittest2', '123')
        data = json.dumps({'response_data': json_response_2})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        
        # if sponsor_stop or user2_stop, the Message DB will not have record, thus length of dict is 0
        if sponsor_stop or user2_stop:
            self.assertEqual(len(json_response['unread situation']['check_dict']), 0)
            self.assertEqual(len(json_response['unread situation']['rounds_dict']), 0)
        else:
            self.assertEqual(len(json_response['unread situation']['check_dict']), 1)
            self.assertEqual(len(json_response['unread situation']['rounds_dict']), 1)
            self.assertEqual(json_response['unread situation']['check_dict'][str(task_id)], 0)
            self.assertEqual(json_response['unread situation']['rounds_dict'][str(task_id)], test_round)

        if sponsor_stop or user2_stop:
            self.assertEqual(len(json_response["unread train stop"]['task_id_to_deleted_user_id'][task_id]), 1)
            self.assertEqual(len(json_response["unread train stop"]['most_recent_round'][task_id]), 1)
            self.assertEqual(json_response["unread train stop"]['task_id_to_deleted_user_id'][task_id][0], 1)
            self.assertEqual(json_response["unread train stop"]['most_recent_round'][task_id][0], test_round)


        headers = self.get_token_auth_headers('unittest3', '123')
        data = json.dumps({'response_data': json_response_3})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        
        if sponsor_stop or user3_stop:
            self.assertEqual(len(json_response['unread situation']['check_dict']), 0)
            self.assertEqual(len(json_response['unread situation']['rounds_dict']), 0)
        else:
            self.assertEqual(len(json_response['unread situation']['check_dict']), 1)
            self.assertEqual(len(json_response['unread situation']['rounds_dict']), 1)
            self.assertEqual(json_response['unread situation']['check_dict'][str(task_id)], 0)
            self.assertEqual(json_response['unread situation']['rounds_dict'][str(task_id)], test_round)

        if sponsor_stop or user3_stop:
            self.assertEqual(len(json_response["unread train stop"]['task_id_to_deleted_user_id'][task_id]), 1)
            self.assertEqual(len(json_response["unread train stop"]['most_recent_round'][task_id]), 1)
            self.assertEqual(json_response["unread train stop"]['task_id_to_deleted_user_id'][task_id][0], 1)
            self.assertEqual(json_response["unread train stop"]['most_recent_round'][task_id][0], test_round)


        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        if sponsor_stop or user2_stop or user2_stop:
            if test_round == 0:
                self.assertEqual(len(json_response), 3)
            else:
                self.assertEqual(len(json_response), 4)
            
            self.assertEqual(json_response[-1]['name'], "unread train stop")
        else:
            if test_round == 0:
                self.assertEqual(len(json_response), 2)
            else:
                self.assertEqual(len(json_response), 3)
 
            self.assertEqual(json_response[-1]['name'], "unread situation")
            self.assertEqual(json_response[-1]['payload'], 0)

        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        if user2_stop or sponsor_stop:
            self.assertEqual(len(json_response), 4)
            self.assertEqual(json_response[-2]['name'], "unread situation")
            self.assertEqual(json_response[-2]['payload'], 0)
            self.assertEqual(json_response[-1]['name'], "unread train stop")
            self.assertEqual(json_response[-1]['payload'], 0)
        else:
            self.assertEqual(len(json_response), 3)
            self.assertEqual(json_response[-1]['name'], "unread situation")
            self.assertEqual(json_response[-1]['payload'], 0)

        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        if user3_stop or sponsor_stop:
            self.assertEqual(len(json_response), 4)
            self.assertEqual(json_response[-2]['name'], "unread situation")
            self.assertEqual(json_response[-2]['payload'], 0)
            self.assertEqual(json_response[-1]['name'], "unread train stop")
            self.assertEqual(json_response[-1]['payload'], 0)
        else:
            self.assertEqual(len(json_response), 3)
            self.assertEqual(json_response[-1]['name'], "unread situation")
            self.assertEqual(json_response[-1]['payload'], 0)

        # if sponsor_stop, everything of this round will be cleaned and we cant get into the Sponsor_situation_training_done() or send_output() function
        if sponsor_stop:
            return
        
        # 13. assistors call send_output() (in unread situation.py)
        # headers = self.get_token_auth_headers('unittest', '123')
        # data = json.dumps({'task_id': task_id})
        # response = self.client.post('/Sponsor_situation_training_done/', headers=headers, data=data)
        # self.assertEqual(response.status_code, 200)
        # json_response = json.loads(response.get_data(as_text=True))
        # self.assertEqual(json_response['Sponsor_situation_training_done'], "Assistors havent upload all output")

        if not user2_stop and not user3_stop:
            headers = self.get_token_auth_headers('unittest2', '123')
            output_content = [[3,123,6], [88,5,6], [7,99,9]]
            data = json.dumps({'output': output_content, 'rounds': test_round, 'task_id': task_id})
            response = self.client.post('/send_output/', headers=headers, data=data)
            self.assertEqual(response.status_code, 200)
            json_response = json.loads(response.get_data(as_text=True))
            # self.assertEqual(json_response['send_output'], "Assistors havent upload all outputs")
            self.assertEqual(json_response['send_output'], "send output successfully")
            queries = Message.query.filter(Message.assistor_id == 1, Message.task_id == task_id, Message.rounds == test_round, Message.test_indicator == "train").all()
            self.assertEqual(len(queries), 2)
            self.assertEqual(queries[-1].sender_id, 2)
            self.assertEqual(json.loads(queries[-1].output), [[3,123,6], [88,5,6], [7,99,9]])

            headers = self.get_token_auth_headers('unittest3', '123')
            output_content = [[6,123,6], [88,5,6], [7,87.6,9]]
            data = json.dumps({'output': output_content, 'rounds': test_round, 'task_id': task_id})
            response = self.client.post('/send_output/', headers=headers, data=data)
            self.assertEqual(response.status_code, 200)
            json_response = json.loads(response.get_data(as_text=True))
            self.assertEqual(json_response['send_output'], "send output successfully")
            queries = Message.query.filter(Message.assistor_id == 1, Message.task_id == task_id, Message.rounds == test_round, Message.test_indicator == "train").all()
            self.assertEqual(len(queries), 3)
            self.assertEqual(queries[-1].sender_id, 3)
            self.assertEqual(json.loads(queries[-1].output), [[6,123,6], [88,5,6], [7,87.6,9]])
        
        if user2_stop:
            headers = self.get_token_auth_headers('unittest3', '123')
            output_content = [[6,123,6], [88,5,6], [7,87.6,9]]
            data = json.dumps({'output': output_content, 'rounds': test_round, 'task_id': task_id})
            response = self.client.post('/send_output/', headers=headers, data=data)
            self.assertEqual(response.status_code, 200)
            json_response = json.loads(response.get_data(as_text=True))
            self.assertEqual(json_response['send_output'], "send output successfully")
            queries = Message.query.filter(Message.assistor_id == 1, Message.task_id == task_id, Message.rounds == test_round, Message.test_indicator == "train").all()
            self.assertEqual(len(queries), 2)
            self.assertEqual(queries[-1].sender_id, 3)
            self.assertEqual(json.loads(queries[-1].output), [[6,123,6], [88,5,6], [7,87.6,9]])
            
        if user3_stop:
            headers = self.get_token_auth_headers('unittest2', '123')
            output_content = [[3,123,6], [88,5,6], [7,99,9]]
            data = json.dumps({'output': output_content, 'rounds': test_round, 'task_id': task_id})
            response = self.client.post('/send_output/', headers=headers, data=data)
            self.assertEqual(response.status_code, 200)
            json_response = json.loads(response.get_data(as_text=True))
            self.assertEqual(json_response['send_output'], "send output successfully")
            queries = Message.query.filter(Message.assistor_id == 1, Message.task_id == task_id, Message.rounds == test_round, Message.test_indicator == "train").all()
            self.assertEqual(len(queries), 2)
            self.assertEqual(queries[-1].sender_id, 2)
            self.assertEqual(json.loads(queries[-1].output), [[3,123,6], [88,5,6], [7,99,9]])


    def unread_output_two_users_helper(self, task_id, list_content, assistor_random_id_list, test_round, sponsor_stop, user2_stop, user3_stop):

        # 14. sponsor check notification (unread output => 1)
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        print("json_response", json_response, test_round, sponsor_stop, user2_stop, user3_stop)
        if sponsor_stop:
            self.assertEqual(len(json_response), 4)
            self.assertEqual(json_response[-3]['name'], "unread situation")
            self.assertEqual(json_response[-3]['payload'], 0)
            self.assertEqual(json_response[-2]['name'], "unread output")
            self.assertEqual(json_response[-2]['payload'], 2)
            self.assertEqual(json_response[-1]['name'], "unread train stop")
            self.assertEqual(json_response[-1]['payload'], 2)
        elif user2_stop or user3_stop:
            self.assertEqual(len(json_response), 4)
            self.assertEqual(json_response[-3]['name'], "unread situation")
            self.assertEqual(json_response[-3]['payload'], 0)
            self.assertEqual(json_response[-2]['name'], "unread output")
            self.assertEqual(json_response[-2]['payload'], 2)
            self.assertEqual(json_response[-1]['name'], "unread train stop")
            self.assertEqual(json_response[-1]['payload'], 1)
        else:
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
        print("))", json_response)
        if sponsor_stop:
            self.assertEqual(len(json_response["unread output"]['rounds_dict']), 0)
        else:
            self.assertEqual(json_response["unread output"]['rounds_dict'][str(task_id)], test_round)

        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        if sponsor_stop or user2_stop or user3_stop:
            self.assertEqual(len(json_response), 4)
            self.assertEqual(json_response[-3]['name'], "unread situation")
            self.assertEqual(json_response[-3]['payload'], 0)
            self.assertEqual(json_response[-2]['name'], "unread output")
            self.assertEqual(json_response[-2]['payload'], 0)
            self.assertEqual(json_response[-1]['name'], "unread train stop")
            self.assertEqual(json_response[-1]['payload'], 0)
        else:
            self.assertEqual(len(json_response), 3)
            self.assertEqual(json_response[-2]['name'], "unread situation")
            self.assertEqual(json_response[-2]['payload'], 0)
            self.assertEqual(json_response[-1]['name'], "unread output")
            self.assertEqual(json_response[-1]['payload'], 0)

        # 16. sponsor calls: get_user_output() (in unread_output.py), gets output files
        data = json.dumps({'task_id': task_id, 'rounds': test_round})
        response = self.client.post('/users/1/output/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        print("zzzzz", json_response)
        if sponsor_stop:
            self.assertEqual(len(json_response['output']), 0)
            return
        elif user2_stop or user3_stop:
            self.assertEqual(len(json_response['output']), 1)
        else:
            self.assertEqual(len(json_response['output']), 2)

        if not user2_stop and not user3_stop:
            self.assertEqual(json.loads(json_response['output'][0]), [[3,123,6], [88,5,6], [7,99,9]])
            self.assertEqual(json.loads(json_response['output'][1]), [[6,123,6], [88,5,6], [7,87.6,9]])
        elif user2_stop:
            self.assertEqual(json.loads(json_response['output'][0]), [[6,123,6], [88,5,6], [7,87.6,9]])
        elif user3_stop:
            self.assertEqual(json.loads(json_response['output'][0]), [[3,123,6], [88,5,6], [7,99,9]])


        # 17. sponsor calls: send_situation(), goes into new round 
        headers = self.get_token_auth_headers('unittest', '123')
        residual_list = [[[1,2,3], [4,5,6]], [[1,2]]]
        data = json.dumps({'residual_list': residual_list, 'task_id': task_id, "assistor_random_id_list": assistor_random_id_list})
        response = self.client.post('/send_situation/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['message'], 'send situation successfully!')

        queries = Message.query.filter(Message.assistor_id != 1, Message.task_id == task_id, Message.rounds == test_round+1, Message.test_indicator == "train").all()
        if not user2_stop and not user3_stop:
            self.assertEqual(len(queries), len(list_content))
            for i in range(len(queries)):
                self.assertEqual(queries[i].rounds, test_round+1)
                self.assertEqual(queries[i].sender_id, 1)
                self.assertEqual(queries[i].assistor_id, list_content[i])
                self.assertEqual(json.loads(queries[i].situation), residual_list[i])
        elif user2_stop:
            self.assertEqual(len(queries), len(list_content)-1)
            for i in range(len(queries)):
                self.assertEqual(queries[i].rounds, test_round+1)
                self.assertEqual(queries[i].sender_id, 1)
                self.assertEqual(json.loads(queries[i].situation), residual_list[1])
        elif user3_stop:
            self.assertEqual(len(queries), len(list_content)-1)
            for i in range(len(queries)):
                self.assertEqual(queries[i].rounds, test_round+1)
                self.assertEqual(queries[i].sender_id, 1)
                self.assertEqual(json.loads(queries[i].situation), residual_list[0])

    

    def unread_match_id_two_users_helper_without_send_situation(self, task_id, list_content, assistor_random_id_list):
        # 6. Check Updated Notification
        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_1 = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response_1[-1]['name'], "unread match id")
        self.assertEqual(json_response_1[-1]['payload'], 1)

        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_2 = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response_2[-2]['name'], "unread request")
        self.assertEqual(json_response_2[-2]['payload'], 0)
        self.assertEqual(json_response_2[-1]['name'], "unread match id")
        self.assertEqual(json_response_2[-1]['payload'], 1)

        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_3 = json.loads(response.get_data(as_text=True))
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
        # headers = self.get_token_auth_headers('unittest3', '123')
        # data = json.dumps({'task_id': task_id})
        # response = self.client.post('/assistor_write_match_index_done/', headers=headers, data=data)
        # self.assertEqual(response.status_code, 200)
        # json_response = json.loads(response.get_data(as_text=True))
        # self.assertEqual(json_response['assistor_write_match_index_done'], 'Assistors dont finish')

        # headers = self.get_token_auth_headers('unittest2', '123')
        # data = json.dumps({'task_id': task_id})
        # response = self.client.post('/assistor_write_match_index_done/', headers=headers, data=data)
        # self.assertEqual(response.status_code, 200)
        # json_response = json.loads(response.get_data(as_text=True))
        # self.assertEqual(json_response['assistor_write_match_index_done'], 'Situation doesnt update')