import json
from Apollo_train_helper_functions import Train_Helper_API_TestCase
from Items.models import User, Message, Notification, Matched

class Stop_Train_API_TestCase(Train_Helper_API_TestCase):

    def test_train_stop_situation_of_assistor_two_users(self):

        '''
            Round: 0
            One assistor stop before send situation()
            We should observe that:
                1. “unread task id” exists in user2's notification and sponsor's notification
                2. the Matched DB row which assistor_pair == user2_id equals to "true"
                3. the Message DB has 1 row (except the row that sponsor sends to itself)
                4. after update_all_notifications, we should have 2 dicts and its value should corresponding to what we want
        '''
        

        task_id, list_content, assistor_random_id_list = self.find_assistor_two_assistors_helper()
        self.unread_request_two_users_helper(task_id, list_content, assistor_random_id_list)
        self.unread_match_id_two_users_helper_without_send_situation(task_id, list_content, assistor_random_id_list)

        headers = self.get_token_auth_headers('unittest2', '123')
        data = json.dumps({'task_id': task_id})
        response = self.client.post('/stop_train_task/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['assistor delete successfully'], 'successfully')
        self.assertEqual(json_response['check sponsor'], 'false')
        self.assertEqual(json_response['most recent round'], 0)

        queries = Matched.query.filter(Matched.task_id == task_id, Matched.assistor_id_pair == 2, Matched.test_indicator == "train", Matched.Terminate == "true").all()
        self.assertEqual(len(queries), len(list_content)-1)

        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response[-1]['name'], "unread train stop")
        self.assertEqual(json_response[-1]['payload'], 1)
        self.assertEqual(json_response[-1]['task_id_list'][0], task_id)

        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_2 = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response_2[-1]['name'], "unread train stop")
        self.assertEqual(json_response_2[-1]['payload'], 1)
        self.assertEqual(json_response_2[-1]['task_id_list'][0], task_id)
        
        headers = self.get_token_auth_headers('unittest', '123')
        data = json.dumps({'response_data': json_response})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response["unread train stop"]['task_id_to_deleted_user_id'][task_id]), 1)
        self.assertEqual(len(json_response["unread train stop"]['most_recent_round'][task_id]), 1)
        self.assertEqual(json_response["unread train stop"]['task_id_to_deleted_user_id'][task_id][0], 2)
        self.assertEqual(json_response["unread train stop"]['most_recent_round'][task_id][0], 0)

        headers = self.get_token_auth_headers('unittest2', '123')
        data = json.dumps({'response_data': json_response_2})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response_2 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response_2["unread train stop"]['task_id_to_deleted_user_id'][task_id]), 1)
        self.assertEqual(len(json_response_2["unread train stop"]['most_recent_round'][task_id]), 1)
        self.assertEqual(json_response_2["unread train stop"]['task_id_to_deleted_user_id'][task_id][0], 1)
        self.assertEqual(json_response_2["unread train stop"]['most_recent_round'][task_id][0], 0)
        
        headers = self.get_token_auth_headers('unittest', '123')
        residual_list = [[[1,2,3], [4,5,6], [7,8,9]], [[1,2], [3,4]]]
        data = json.dumps({'residual_list': residual_list, 'task_id': task_id, "assistor_random_id_list": assistor_random_id_list})
        response = self.client.post('/send_situation/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['message'], 'send situation successfully!')

        queries = Message.query.filter(Message.assistor_id != 1, Message.task_id == task_id, Message.rounds == 0, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), len(list_content)-1)
    
    def test_train_stop_situation_of_sponsor_two_users(self):
        
        '''
            Round: 0
            Sponsor stops before send situation()
            We should observe that:
                1. “unread task id” exists in assistors' notification (each has one) and sponsor's notification (has 2 because we have 2 assistors)
                2. all the Matched DB rows of current task_id equals0 to "true"
                3. the Message DB has 0 row
                4. after update_all_notifications, we should have 2 dicts and its value should corresponding to what we want
        '''


        task_id, list_content, assistor_random_id_list = self.find_assistor_two_assistors_helper()
        self.unread_request_two_users_helper(task_id, list_content, assistor_random_id_list)
        self.unread_match_id_two_users_helper_without_send_situation(task_id, list_content, assistor_random_id_list)

        headers = self.get_token_auth_headers('unittest', '123')
        data = json.dumps({'task_id': task_id})
        response = self.client.post('/stop_train_task/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['sponsor delete successfully'], 'successfully')
        self.assertEqual(json_response['check sponsor'], 'true')
        self.assertEqual(json_response['most recent round'], 0)
        
        queries = Matched.query.filter(Matched.task_id == task_id, Matched.test_indicator == "train", Matched.Terminate == "true").all()
        self.assertEqual(len(queries), len(list_content)+1)

        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_1 = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response_1[-1]['name'], "unread train stop")
        self.assertEqual(json_response_1[-1]['payload'], 2)
        self.assertEqual(json_response_1[-1]['task_id_list'][0], task_id)
        
        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_2 = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response_2[-1]['name'], "unread train stop")
        self.assertEqual(json_response_2[-1]['payload'], 1)
        self.assertEqual(json_response_2[-1]['task_id_list'][0], task_id)

        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_3 = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response_3[-1]['name'], "unread train stop")
        self.assertEqual(json_response_3[-1]['payload'], 1)
        self.assertEqual(json_response_3[-1]['task_id_list'][0], task_id)

        headers = self.get_token_auth_headers('unittest', '123')
        data = json.dumps({'response_data': json_response_1})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response_1 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response_1["unread train stop"]['task_id_to_deleted_user_id'][task_id]), 2)
        self.assertEqual(len(json_response_1["unread train stop"]['most_recent_round'][task_id]), 2)
        self.assertEqual(json_response_1["unread train stop"]['task_id_to_deleted_user_id'][task_id][0], 2)
        self.assertEqual(json_response_1["unread train stop"]['most_recent_round'][task_id][0], 0)
        self.assertEqual(json_response_1["unread train stop"]['task_id_to_deleted_user_id'][task_id][1], 3)
        self.assertEqual(json_response_1["unread train stop"]['most_recent_round'][task_id][1], 0)

        headers = self.get_token_auth_headers('unittest2', '123')
        data = json.dumps({'response_data': json_response_2})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response_2 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response_2["unread train stop"]['task_id_to_deleted_user_id'][task_id]), 1)
        self.assertEqual(len(json_response_2["unread train stop"]['most_recent_round'][task_id]), 1)
        self.assertEqual(json_response_2["unread train stop"]['task_id_to_deleted_user_id'][task_id][0], 1)
        self.assertEqual(json_response_2["unread train stop"]['most_recent_round'][task_id][0], 0)
        
        headers = self.get_token_auth_headers('unittest3', '123')
        data = json.dumps({'response_data': json_response_3})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response_3 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response_3["unread train stop"]['task_id_to_deleted_user_id'][task_id]), 1)
        self.assertEqual(len(json_response_3["unread train stop"]['most_recent_round'][task_id]), 1)
        self.assertEqual(json_response_3["unread train stop"]['task_id_to_deleted_user_id'][task_id][0], 1)
        self.assertEqual(json_response_3["unread train stop"]['most_recent_round'][task_id][0], 0)

        headers = self.get_token_auth_headers('unittest', '123')
        residual_list = [[[1,2,3], [4,5,6], [7,8,9]], [[1,2], [3,4]]]
        data = json.dumps({'residual_list': residual_list, 'task_id': task_id, "assistor_random_id_list": assistor_random_id_list})
        response = self.client.post('/send_situation/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['message'], 'send situation successfully!')

        queries = Message.query.filter(Message.task_id == task_id, Message.rounds == 0, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), 0)
    
    def test_train_stop_assistor_after_sending_situation_of_assistor_two_users(self):

        '''
            Round: 0
            One assistor stop before send situation()
            We should observe that:
                1. “unread task id” exists in user2's notification and sponsor's notification
                2. the Matched DB row which assistor_pair == user2_id equals to "true"
                3. the Message DB has len(list_content)-1 row (all message about user2 should be deleted in round 0)
                4. after update_all_notifications, we should have 2 dicts and its value should corresponding to what we want
        '''


        task_id, list_content, assistor_random_id_list = self.find_assistor_two_assistors_helper()
        self.unread_request_two_users_helper(task_id, list_content, assistor_random_id_list)
        self.unread_match_id_two_users_helper(task_id, list_content, assistor_random_id_list)
        
        headers = self.get_token_auth_headers('unittest2', '123')
        data = json.dumps({'task_id': task_id})
        response = self.client.post('/stop_train_task/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['assistor delete successfully'], 'successfully')
        self.assertEqual(json_response['check sponsor'], 'false')
        self.assertEqual(json_response['most recent round'], 0)

        queries = Matched.query.filter(Matched.task_id == task_id, Matched.assistor_id_pair == 2, Matched.test_indicator == "train", Matched.Terminate == "true").all()
        self.assertEqual(len(queries), 1)

        queries = Message.query.filter(Message.assistor_id != 1, Message.task_id == task_id, Message.rounds == 0, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), len(list_content)-1)

        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response[-1]['name'], "unread train stop")
        self.assertEqual(json_response[-1]['payload'], 1)
        self.assertEqual(json_response[-1]['task_id_list'][0], task_id)

        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_2 = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response_2[-1]['name'], "unread train stop")
        self.assertEqual(json_response_2[-1]['payload'], 1)
        self.assertEqual(json_response_2[-1]['task_id_list'][0], task_id)
        
        headers = self.get_token_auth_headers('unittest', '123')
        data = json.dumps({'response_data': json_response})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response["unread train stop"]['task_id_to_deleted_user_id'][task_id]), 1)
        self.assertEqual(len(json_response["unread train stop"]['most_recent_round'][task_id]), 1)
        self.assertEqual(json_response["unread train stop"]['task_id_to_deleted_user_id'][task_id][0], 2)
        self.assertEqual(json_response["unread train stop"]['most_recent_round'][task_id][0], 0)

        headers = self.get_token_auth_headers('unittest2', '123')
        data = json.dumps({'response_data': json_response_2})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response_2 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response_2["unread train stop"]['task_id_to_deleted_user_id'][task_id]), 1)
        self.assertEqual(len(json_response_2["unread train stop"]['most_recent_round'][task_id]), 1)
        self.assertEqual(json_response_2["unread train stop"]['task_id_to_deleted_user_id'][task_id][0], 1)
        self.assertEqual(json_response_2["unread train stop"]['most_recent_round'][task_id][0], 0)
        

    def test_train_stop_sponsor_after_sending_situation_of_sponsor_two_users(self):

        '''
            Round: 0
            Sponsor stops before send situation()
            We should observe that:
                1. “unread task id” exists in assistors' notification (each has one) and sponsor's notification (has 2 because we have 2 assistors)
                2. all the Matched DB rows of current task_id equals0 to "true"
                3. the Message DB has 0 row
                4. after update_all_notifications, we should have 2 dicts and its value should corresponding to what we want
        '''


        task_id, list_content, assistor_random_id_list = self.find_assistor_two_assistors_helper()
        self.unread_request_two_users_helper(task_id, list_content, assistor_random_id_list)
        self.unread_match_id_two_users_helper(task_id, list_content, assistor_random_id_list)
        
        headers = self.get_token_auth_headers('unittest', '123')
        data = json.dumps({'task_id': task_id})
        response = self.client.post('/stop_train_task/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['sponsor delete successfully'], 'successfully')
        self.assertEqual(json_response['check sponsor'], 'true')
        self.assertEqual(json_response['most recent round'], 0)

        queries = Matched.query.filter(Matched.task_id == task_id, Matched.test_indicator == "train", Matched.Terminate == "true").all()
        self.assertEqual(len(queries), len(list_content)+1)

        queries = Message.query.filter(Message.task_id == task_id, Message.rounds == 0, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), 0)

        headers = self.get_token_auth_headers('unittest', '123')
        response = self.client.get('/users/1/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_1 = json.loads(response.get_data(as_text=True))
        print("------//", json_response_1, len(json_response_1))
        self.assertEqual(json_response_1[-1]['name'], "unread train stop")
        self.assertEqual(json_response_1[-1]['payload'], 2)
        self.assertEqual(json_response_1[-1]['task_id_list'][0], task_id)
        
        headers = self.get_token_auth_headers('unittest2', '123')
        response = self.client.get('/users/2/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_2 = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response_2[-1]['name'], "unread train stop")
        self.assertEqual(json_response_2[-1]['payload'], 1)
        self.assertEqual(json_response_2[-1]['task_id_list'][0], task_id)

        headers = self.get_token_auth_headers('unittest3', '123')
        response = self.client.get('/users/3/notifications/', headers=headers)
        self.assertEqual(response.status_code, 200)
        json_response_3 = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response_3[-1]['name'], "unread train stop")
        self.assertEqual(json_response_3[-1]['payload'], 1)
        self.assertEqual(json_response_3[-1]['task_id_list'][0], task_id)

        headers = self.get_token_auth_headers('unittest', '123')
        data = json.dumps({'response_data': json_response_1})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response_1 = json.loads(response.get_data(as_text=True))
        print("--------", json_response_1)
        self.assertEqual(len(json_response_1["unread train stop"]['task_id_to_deleted_user_id'][task_id]), 2)
        self.assertEqual(len(json_response_1["unread train stop"]['most_recent_round'][task_id]), 2)
        self.assertEqual(json_response_1["unread train stop"]['task_id_to_deleted_user_id'][task_id][0], 2)
        self.assertEqual(json_response_1["unread train stop"]['most_recent_round'][task_id][0], 0)
        self.assertEqual(json_response_1["unread train stop"]['task_id_to_deleted_user_id'][task_id][1], 3)
        self.assertEqual(json_response_1["unread train stop"]['most_recent_round'][task_id][1], 0)

        headers = self.get_token_auth_headers('unittest2', '123')
        data = json.dumps({'response_data': json_response_2})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response_2 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response_2["unread train stop"]['task_id_to_deleted_user_id'][task_id]), 1)
        self.assertEqual(len(json_response_2["unread train stop"]['most_recent_round'][task_id]), 1)
        self.assertEqual(json_response_2["unread train stop"]['task_id_to_deleted_user_id'][task_id][0], 1)
        self.assertEqual(json_response_2["unread train stop"]['most_recent_round'][task_id][0], 0)
        
        headers = self.get_token_auth_headers('unittest3', '123')
        data = json.dumps({'response_data': json_response_3})
        response = self.client.post('/update_all_notifications/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response_3 = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response_3["unread train stop"]['task_id_to_deleted_user_id'][task_id]), 1)
        self.assertEqual(len(json_response_3["unread train stop"]['most_recent_round'][task_id]), 1)
        self.assertEqual(json_response_3["unread train stop"]['task_id_to_deleted_user_id'][task_id][0], 1)
        self.assertEqual(json_response_3["unread train stop"]['most_recent_round'][task_id][0], 0)
        
        

    def test_train_stop_assistor_after_unread_match_id(self):

        '''
            Round: 0
            One assistor stop before send situation()
            We should observe that:
                1. “unread task id” exists in user2's notification and sponsor's notification
                2. the Matched DB row which assistor_pair == user2_id equals to "true"
                3. the Message DB has len(list_content)+1 row (all message about user2 should be deleted in round 0)
                4. after update_all_notifications, we should have 2 dicts and its value should corresponding to what we want
        '''


        task_id, list_content, assistor_random_id_list = self.find_assistor_two_assistors_helper()
        self.unread_request_two_users_helper(task_id, list_content, assistor_random_id_list)
        self.unread_match_id_two_users_helper(task_id, list_content, assistor_random_id_list)
        
        headers = self.get_token_auth_headers('unittest2', '123')
        data = json.dumps({'task_id': task_id})
        response = self.client.post('/stop_train_task/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['assistor delete successfully'], 'successfully')
        self.assertEqual(json_response['check sponsor'], 'false')
        self.assertEqual(json_response['most recent round'], 0)

        queries = Matched.query.filter(Matched.task_id == task_id, Matched.test_indicator == "train", Matched.Terminate == "true").all()
        self.assertEqual(len(queries), 1)

        queries = Message.query.filter(Message.assistor_id != 1, Message.task_id == task_id, Message.rounds == 0, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), len(list_content)-1)
        
        self.unread_situation_two_users_helper(task_id, list_content, assistor_random_id_list, 0, False, True, False)
        
        queries = Message.query.filter(Message.assistor_id != 1, Message.task_id == task_id, Message.rounds == 0, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), 1)

        queries = Message.query.filter(Message.task_id == task_id, Message.rounds == 0, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), len(list_content)+1)
    
    def test_train_stop_sponsor_after_unread_match_id(self):

        '''
            Round: 0
            Sponsor stops before send situation()
            We should observe that:
                1. “unread task id” exists in assistors' notification (each has one) and sponsor's notification (has 2 because we have 2 assistors)
                2. all the Matched DB rows of current task_id equals0 to "true"
                3. the Message DB has 0 row
                4. after update_all_notifications, we should have 2 dicts and its value should corresponding to what we want
        '''


        task_id, list_content, assistor_random_id_list = self.find_assistor_two_assistors_helper()
        self.unread_request_two_users_helper(task_id, list_content, assistor_random_id_list)
        self.unread_match_id_two_users_helper(task_id, list_content, assistor_random_id_list)
        
        headers = self.get_token_auth_headers('unittest', '123')
        data = json.dumps({'task_id': task_id})
        response = self.client.post('/stop_train_task/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['sponsor delete successfully'], 'successfully')
        self.assertEqual(json_response['check sponsor'], 'true')
        self.assertEqual(json_response['most recent round'], 0)

        queries = Matched.query.filter(Matched.task_id == task_id, Matched.assistor_id_pair == 2, Matched.test_indicator == "train", Matched.Terminate == "true").all()
        self.assertEqual(len(queries), 1)

        queries = Message.query.filter(Message.task_id == task_id, Message.rounds == 0, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), 0)
        
        self.unread_situation_two_users_helper(task_id, list_content, assistor_random_id_list, 0, True, False, False)
        
        queries = Message.query.filter(Message.task_id == task_id, Message.rounds == 0, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), 0)

    def test_train_stop_assistor_after_unread_situation(self):

        '''
            Round: 0
            One assistor stop before send situation()
            We should observe that:
                1. “unread task id” exists in user2's notification and sponsor's notification
                2. the Matched DB row which assistor_pair == user2_id equals to "true"
                3. the Message DB has len(list_content)+1 row (all message about user2 should be deleted in round 0)
                4. after update_all_notifications, we should have 2 dicts and its value should corresponding to what we want
        '''


        task_id, list_content, assistor_random_id_list = self.find_assistor_two_assistors_helper()
        self.unread_request_two_users_helper(task_id, list_content, assistor_random_id_list)
        self.unread_match_id_two_users_helper(task_id, list_content, assistor_random_id_list)
        self.unread_situation_two_users_helper(task_id, list_content, assistor_random_id_list, 0, False, False, False)

        queries = Message.query.filter(Message.assistor_id == 2, Message.task_id == task_id, Message.rounds == 0, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), 1)

        queries = Message.query.filter(Message.sender_id == 2, Message.task_id == task_id, Message.rounds == 0, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), 1)

        queries = Message.query.filter(Message.task_id == task_id, Message.rounds == 0, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), 2*(len(list_content)+1)-1)

        headers = self.get_token_auth_headers('unittest2', '123')
        data = json.dumps({'task_id': task_id})
        response = self.client.post('/stop_train_task/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['assistor delete successfully'], 'successfully')
        self.assertEqual(json_response['check sponsor'], 'false')
        self.assertEqual(json_response['most recent round'], 0)

        queries = Matched.query.filter(Matched.task_id == task_id, Matched.test_indicator == "train", Matched.Terminate == "true").all()
        self.assertEqual(len(queries), 1)

        queries = Message.query.filter(Message.assistor_id == 2, Message.task_id == task_id, Message.rounds == 0, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), 0)

        queries = Message.query.filter(Message.sender_id == 2, Message.task_id == task_id, Message.rounds == 0, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), 0)
        
        self.unread_output_two_users_helper(task_id, list_content, assistor_random_id_list, 0, False, True, False)
    
    def test_train_stop_sponsor_after_unread_situation(self):

        '''
            Round: 0
            Sponsor stops before send situation()
            We should observe that:
                1. “unread task id” exists in assistors' notification (each has one) and sponsor's notification (has 2 because we have 2 assistors)
                2. all the Matched DB rows of current task_id equals0 to "true"
                3. the Message DB has 0 row
                4. after update_all_notifications, we should have 2 dicts and its value should corresponding to what we want
        '''


        task_id, list_content, assistor_random_id_list = self.find_assistor_two_assistors_helper()
        self.unread_request_two_users_helper(task_id, list_content, assistor_random_id_list)
        self.unread_match_id_two_users_helper(task_id, list_content, assistor_random_id_list)
        self.unread_situation_two_users_helper(task_id, list_content, assistor_random_id_list, 0, False, False, False)

        queries = Message.query.filter(Message.assistor_id == 2, Message.task_id == task_id, Message.rounds == 0, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), 1)

        queries = Message.query.filter(Message.sender_id == 2, Message.task_id == task_id, Message.rounds == 0, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), 1)

        queries = Message.query.filter(Message.task_id == task_id, Message.rounds == 0, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), 2*(len(list_content)+1)-1)

        headers = self.get_token_auth_headers('unittest', '123')
        data = json.dumps({'task_id': task_id})
        response = self.client.post('/stop_train_task/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['sponsor delete successfully'], 'successfully')
        self.assertEqual(json_response['check sponsor'], 'true')
        self.assertEqual(json_response['most recent round'], 0)

        queries = Matched.query.filter(Matched.task_id == task_id, Matched.test_indicator == "train", Matched.Terminate == "true").all()
        self.assertEqual(len(queries), len(list_content)+1)

        queries = Message.query.filter(Message.task_id == task_id, Message.rounds == 0, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), 0)
        
        self.unread_output_two_users_helper(task_id, list_content, assistor_random_id_list, 0, True, False, False)


    def test_train_stop_assistor_before_unread_situation_in_round_2(self):

        '''
            Round: 0
            One assistor stop before send situation()
            We should observe that:
                1. “unread task id” exists in user2's notification and sponsor's notification
                2. the Matched DB row which assistor_pair == user2_id equals to "true"
                3. the Message DB has  row (all message about user2 should be deleted in round 0)
                4. after update_all_notifications, we should have 2 dicts and its value should corresponding to what we want
        '''

        # first round
        task_id, list_content, assistor_random_id_list = self.find_assistor_two_assistors_helper()
        self.unread_request_two_users_helper(task_id, list_content, assistor_random_id_list)
        self.unread_match_id_two_users_helper(task_id, list_content, assistor_random_id_list)
        self.unread_situation_two_users_helper(task_id, list_content, assistor_random_id_list, 0, False, False, False)
        self.unread_output_two_users_helper(task_id, list_content, assistor_random_id_list, 0, False, False, False)

        queries = Matched.query.filter(Matched.task_id == task_id, Matched.test_indicator == "train", Matched.Terminate == "false").all()
        self.assertEqual(len(queries), len(list_content)+1)

        queries = Message.query.filter(Message.task_id == task_id, Message.rounds == 0, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), (len(list_content)+1)*2-1)

        queries = Message.query.filter(Message.task_id == task_id, Message.rounds == 1, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), (len(list_content)+1))

        headers = self.get_token_auth_headers('unittest2', '123')
        data = json.dumps({'task_id': task_id})
        response = self.client.post('/stop_train_task/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['assistor delete successfully'], 'successfully')
        self.assertEqual(json_response['check sponsor'], 'false')
        self.assertEqual(json_response['most recent round'], 1)

        queries = Matched.query.filter(Matched.task_id == task_id, Matched.test_indicator == "train", Matched.Terminate == "true").all()
        self.assertEqual(len(queries), 1)

        queries = Message.query.filter(Message.task_id == task_id, Message.rounds == 0, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), (len(list_content)+1)*2-1)

        queries = Message.query.filter(Message.task_id == task_id, Message.rounds == 1, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), len(list_content))

        self.unread_situation_two_users_helper(task_id, list_content, assistor_random_id_list, 1, False, True, False)
        

    def test_train_stop_sponsor_before_unread_situation_in_round_2(self):

        '''
            Round: 0
            Sponsor stops before send situation()
            We should observe that:
                1. “unread task id” exists in assistors' notification (each has one) and sponsor's notification (has 2 because we have 2 assistors)
                2. all the Matched DB rows of current task_id equals0 to "true"
                3. the Message DB has 0 row
                4. after update_all_notifications, we should have 2 dicts and its value should corresponding to what we want
        '''

        # first round
        task_id, list_content, assistor_random_id_list = self.find_assistor_two_assistors_helper()
        self.unread_request_two_users_helper(task_id, list_content, assistor_random_id_list)
        self.unread_match_id_two_users_helper(task_id, list_content, assistor_random_id_list)
        self.unread_situation_two_users_helper(task_id, list_content, assistor_random_id_list, 0, False, False, False)
        self.unread_output_two_users_helper(task_id, list_content, assistor_random_id_list, 0, False, False, False)

        queries = Matched.query.filter(Matched.task_id == task_id, Matched.test_indicator == "train", Matched.Terminate == "false").all()
        self.assertEqual(len(queries), len(list_content)+1)

        queries = Message.query.filter(Message.task_id == task_id, Message.rounds == 0, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), (len(list_content)+1)*2-1)

        queries = Message.query.filter(Message.task_id == task_id, Message.rounds == 1, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), (len(list_content)+1))

        headers = self.get_token_auth_headers('unittest', '123')
        data = json.dumps({'task_id': task_id})
        response = self.client.post('/stop_train_task/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['sponsor delete successfully'], 'successfully')
        self.assertEqual(json_response['check sponsor'], 'true')
        self.assertEqual(json_response['most recent round'], 1)

        queries = Matched.query.filter(Matched.task_id == task_id, Matched.test_indicator == "train", Matched.Terminate == "true").all()
        self.assertEqual(len(queries), len(list_content)+1)

        queries = Message.query.filter(Message.task_id == task_id, Message.rounds == 0, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), (len(list_content)+1)*2-1)

        queries = Message.query.filter(Message.task_id == task_id, Message.rounds == 1, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), 0)

        self.unread_situation_two_users_helper(task_id, list_content, assistor_random_id_list, 1, True, False, False)




    def test_train_stop_assistor_after_unread_situation_in_round_2(self):

        '''
            Round: 0
            One assistor stop before send situation()
            We should observe that:
                1. “unread task id” exists in user2's notification and sponsor's notification
                2. the Matched DB row which assistor_pair == user2_id equals to "true"
                3. the Message DB has  row (all message about user2 should be deleted in round 0)
                4. after update_all_notifications, we should have 2 dicts and its value should corresponding to what we want
        '''

        # first round
        task_id, list_content, assistor_random_id_list = self.find_assistor_two_assistors_helper()
        self.unread_request_two_users_helper(task_id, list_content, assistor_random_id_list)
        self.unread_match_id_two_users_helper(task_id, list_content, assistor_random_id_list)
        self.unread_situation_two_users_helper(task_id, list_content, assistor_random_id_list, 0, False, False, False)
        self.unread_output_two_users_helper(task_id, list_content, assistor_random_id_list, 0, False, False, False)

        self.unread_situation_two_users_helper(task_id, list_content, assistor_random_id_list, 1, False, False, False)

        queries = Matched.query.filter(Matched.task_id == task_id, Matched.test_indicator == "train", Matched.Terminate == "false").all()
        self.assertEqual(len(queries), len(list_content)+1)

        queries = Message.query.filter(Message.task_id == task_id, Message.rounds == 0, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), (len(list_content)+1)*2-1)

        queries = Message.query.filter(Message.task_id == task_id, Message.rounds == 1, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), (len(list_content)+1)*2-1)

        headers = self.get_token_auth_headers('unittest2', '123')
        data = json.dumps({'task_id': task_id})
        response = self.client.post('/stop_train_task/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['assistor delete successfully'], 'successfully')
        self.assertEqual(json_response['check sponsor'], 'false')
        self.assertEqual(json_response['most recent round'], 1)

        queries = Matched.query.filter(Matched.task_id == task_id, Matched.test_indicator == "train", Matched.Terminate == "true").all()
        self.assertEqual(len(queries), 1)

        queries = Message.query.filter(Message.task_id == task_id, Message.rounds == 0, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), (len(list_content)+1)*2-1)

        queries = Message.query.filter(Message.task_id == task_id, Message.rounds == 1, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), len(list_content)+1)

        self.unread_output_two_users_helper(task_id, list_content, assistor_random_id_list, 1, False, True, False)
        
        queries = Message.query.filter(Message.task_id == task_id, Message.rounds == 0, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), (len(list_content)+1)*2-1)

        queries = Message.query.filter(Message.task_id == task_id, Message.rounds == 1, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), len(list_content)+1)

    


    def test_train_stop_sponsor_after_unread_situation_in_round_2(self):

        '''
            Round: 0
            Sponsor stops before send situation()
            We should observe that:
                1. “unread task id” exists in assistors' notification (each has one) and sponsor's notification (has 2 because we have 2 assistors)
                2. all the Matched DB rows of current task_id equals0 to "true"
                3. the Message DB has 0 row
                4. after update_all_notifications, we should have 2 dicts and its value should corresponding to what we want
        '''

        # first round
        task_id, list_content, assistor_random_id_list = self.find_assistor_two_assistors_helper()
        self.unread_request_two_users_helper(task_id, list_content, assistor_random_id_list)
        self.unread_match_id_two_users_helper(task_id, list_content, assistor_random_id_list)
        self.unread_situation_two_users_helper(task_id, list_content, assistor_random_id_list, 0, False, False, False)
        self.unread_output_two_users_helper(task_id, list_content, assistor_random_id_list, 0, False, False, False)

        self.unread_situation_two_users_helper(task_id, list_content, assistor_random_id_list, 1, False, False, False)

        queries = Matched.query.filter(Matched.task_id == task_id, Matched.test_indicator == "train", Matched.Terminate == "false").all()
        self.assertEqual(len(queries), len(list_content)+1)

        queries = Message.query.filter(Message.task_id == task_id, Message.rounds == 0, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), 2*(len(list_content)+1)-1)

        queries = Message.query.filter(Message.task_id == task_id, Message.rounds == 1, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), 2*(len(list_content)+1)-1)

        headers = self.get_token_auth_headers('unittest', '123')
        data = json.dumps({'task_id': task_id})
        response = self.client.post('/stop_train_task/', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['sponsor delete successfully'], 'successfully')
        self.assertEqual(json_response['check sponsor'], 'true')
        self.assertEqual(json_response['most recent round'], 1)

        queries = Matched.query.filter(Matched.task_id == task_id, Matched.test_indicator == "train", Matched.Terminate == "true").all()
        self.assertEqual(len(queries), len(list_content)+1)

        queries = Message.query.filter(Message.task_id == task_id, Message.rounds == 0, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), (len(list_content)+1)*2-1)

        queries = Message.query.filter(Message.task_id == task_id, Message.rounds == 1, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), 0)

        self.unread_output_two_users_helper(task_id, list_content, assistor_random_id_list, 1, True, False, False)
        
        queries = Message.query.filter(Message.task_id == task_id, Message.rounds == 0, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), (len(list_content)+1)*2-1)

        queries = Message.query.filter(Message.task_id == task_id, Message.rounds == 1, Message.test_indicator == "train").all()
        self.assertEqual(len(queries), 0)

        