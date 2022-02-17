import requests
import json
import time
import threading
import numpy as np

from .Network import Network
from .PersonalInformation import PersonalInformation
from .Database_class import Database_class
from .Error import check_Algorithm_return_value
from .SynSpot_utils import log_helper, load_json_data, load_file, save_file, handle_Algorithm_return_value

from .Algorithm import make_eval, make_test, make_hash, save_match_id, make_match_idx, make_residual, make_train, save_output, make_result, save_residual, log
# from Database import Session, User_Default_Path, User_Chosen_Path, User_Pending_Page, assign_value_to_user_chosen_path_instance

class check_sponsor_class:
    sponsor = 1
    assistor = 0

class TestRequest:
    __TestRequest_instance = None

    def __init__(self):
        self.Network_instance = Network.get_Network_instance()
        self.PersonalInformation_instance = PersonalInformation.get_PersonalInformation_instance()
        self.Database_class_instance = Database_class.get_Database_class_instance()

        self.base_url = self.Network_instance.base_url
        self.skip_header_default = 1
        self.test_indicator = 'test'

    @classmethod
    def get_TestRequest_instance(cls):
        if cls.__TestRequest_instance == None:
            cls.__TestRequest_instance = TestRequest()

        return cls.__TestRequest_instance

    def __obtain_important_information(self, get_test_id):
        """
        Obtain the information we need: user_id, root, token, task_id

        Parameters:
            get_train_id - Boolean. Indicate if we need to get the new train id

        Returns:
            user_id - String. The user_id of current user
            root - String. The root of storing intermediate information
            token - String. Token we need for verification
            task_id - None or String. If get_train_id is True, return String.
                If get_train_id is False, return None

        Raises:
            None
        """
        user_id = self.PersonalInformation_instance.user_id
        assert user_id is not None
        root = self.PersonalInformation_instance.root
        assert root is not None
        token = self.Network_instance.token
        assert token is not None

        test_id = None
        if get_test_id:
            test_id = self.__get_test_id()
        return user_id, root, token, test_id

    def handleTestRequest(self, task_id: str, test_file_path: str, test_id_column: str, test_data_column: str, 
                            test_target_column: str, test_name: str, test_description: str):

        """
        Call __find_test_assistor for further execution

        Parameters:
            task_id - String. The task that the user wanted to test
            test_file_path - String. Input path address of testing data path
            test_id_column - String. ID column of Input File
            test_data_column - String. Data column of Input File
            test_target_column - String. Target column of Input File
            test_name - None or String. The name of current test
            test_description - None or String. The description of current test

        Returns:
            String. 'handleTestRequest successfully'

        Raises:
            None
        """
        user_id, root, token, _ = self.__obtain_important_information(get_test_id=False)
        print('handleTestRequest', task_id)
        task_mode, model_name, metric_name, task_name, task_description, train_file_path, train_id_column, train_data_column, train_target_column = self.Database_class_instance.get_User_Sponsor_Table(user_id=user_id, task_id=task_id, test_indicator='train')
        # retrieve mode from user_sponsor_db
        return self.__find_test_assistor(task_id=task_id, task_name=task_name, task_description=task_description, task_mode=task_mode, model_name=model_name, metric_name=metric_name, 
                                  test_file_path=test_file_path, test_id_column=test_id_column, test_data_column=test_data_column, test_target_column=test_target_column, test_name=test_name,
                                  test_description=test_description)

    def __get_test_id(self):

        """
        Get new Test id for this test

        Parameters:
            None

        Returns:
            new_test_id - String. The new test id of new task

        Raises:
            KeyError - raises an exception
        """

        url = self.base_url + "/create_new_test_task/"
        token = self.Network_instance.token
        try:
            get_test_id_response = requests.get(url, headers = {'Authorization': 'Bearer ' + token})
            get_test_id_response = load_json_data(json_data=get_test_id_response, json_data_name='get_test_id_response', 
                                                    testing_key_value_pair=[('test_id', None)])
        except:
            print('get_test_id_response wrong')

        new_test_id = get_test_id_response["test_id"]
        return new_test_id

    def __find_test_assistor(self, task_id: str, task_name: str, task_description: str, task_mode: str, model_name: str, metric_name: str, test_file_path: str, test_id_column: str, test_data_column: str, 
                            test_target_column: str, test_name: str=None, test_description: str=None):

        """
        start testing with all assistors of the task

        Parameters:
            task_id - String. The task that the user wanted to test
            task_name - String. The name of the task that the user wanted to test
            task_description - String. The description of the task that the user wanted to test
            task_mode - String. Classification or Regression
            model_name - String. Specific model, such as LinearRegression, DecisionTree.
            metric_name - String. Metric to measure the result, such as MAD, RMSE, R2.
            test_file_path - String. Input path address of testing data path
            test_id_column - String. ID column of Input File
            test_data_column - String. Data column of Input File
            test_target_column - String. Target column of Input File
            test_name - None or String. The name of current test
            test_description - None or String. The description of current test

        Returns:
            None

        Raises:
            KeyError - raises an exception
        """

        # obtain some important information
        user_id, root, token, test_id = self.__obtain_important_information(get_test_id=True)

        # store information in db
        store_User_Sponsor_Table_res = self.Database_class_instance.store_User_Sponsor_Table(user_id=user_id, task_id=task_id, test_indicator=self.test_indicator, task_mode=task_mode, model_name=model_name, metric_name=metric_name,
                                                            test_id=test_id, task_name=task_name, task_description=task_description, test_name=test_name, test_description=test_description, train_file_path=None, 
                                                            train_id_column=None, train_data_column=None, train_target_column=None, test_file_path=test_file_path, test_id_column=test_id_column, test_data_column=test_data_column,
                                                            test_target_column=test_target_column)
        assert store_User_Sponsor_Table_res == 'User_Sponsor_Table stores successfully'

        # call make_hash in Algorithm module
        test_hash_id_file_address = make_hash(root=root, self_id=user_id, task_id=task_id, mode=self.test_indicator, test_id=test_id, dataset_path=test_file_path, id_idx=test_id_column, skip_header=self.skip_header_default)
        assert test_hash_id_file_address is not None
        _, test_hash_id_file_address = handle_Algorithm_return_value("test_hash_id_file_address", test_hash_id_file_address, "200", "make_hash")
        assert test_hash_id_file_address is not None

        # read file => array data type from np.genfromtxt
        # we need string type with \n between ids.
        test_hash_id_file_data = load_file(test_hash_id_file_address[2])

        # call find assistor in server
        url = self.base_url + "/find_test_assistor/"
        data = {
            "task_id": task_id,
            "task_name": task_name,
            'test_id': test_id,
            'test_name': test_name,
            'test_description': test_description,
            'task_mode': task_mode,
            'model_name': model_name,
            'metric_name': metric_name,
            'id_file': test_hash_id_file_data,
        }
        try:
            find_test_assistor_res = requests.post(url, json=data, headers={'Authorization': 'Bearer ' + token})
            find_test_assistor_res = load_json_data(json_data=find_test_assistor_res, json_data_name='find_test_assistor_res', 
                                                    testing_key_value_pair=[('task_id', None), ('assistor_num', None), ('test_id', None)])
        except:
            print('find_test_assistor_res wrong')

        print('Sponsor: Testing test_id: ', test_id, ' is running')
        return ('handleTestRequest successfully', test_id)

    def unread_test_request(self, unread_test_request_notification: dict):

        """
        Handle the unread test request for three default mode: ["passive", "active", "auto"]

        Parameters:
            unread_test_request_notification - Dictionary.

        Returns:
            None

        Raises:
            KeyError - raises an exception
        """

        # obtain some important information
        user_id, root, token, _ = self.__obtain_important_information(get_test_id=False)

        user_id, default_mode, default_task_mode, default_model_name, default_file_path, default_id_column, default_data_column = self.Database_class_instance.get_User_Default_Table(user_id)
        print('zhei', user_id, default_mode, default_task_mode, default_file_path, default_id_column, default_data_column, default_model_name)

        cur_unread_test_request_Testid_dict = unread_test_request_notification["check_dict"]
        test_id_to_task_id = unread_test_request_notification["test_id_to_task_id"]

        if default_mode == "manual":
            # Insert to DB
            pass

        elif default_mode == "auto":
            # get default path

            for test_id in cur_unread_test_request_Testid_dict:
                task_id = test_id_to_task_id[test_id]

                # Insert default into User_Assistor_Table
                store_User_Assistor_Table_res = self.Database_class_instance.store_User_Assistor_Table(user_id=user_id, task_id=task_id, test_indicator=self.test_indicator, mode=default_mode, task_mode=default_task_mode, model_name=default_model_name, 
                                                            test_id=test_id, task_name=None, task_description=None, test_name=None, test_description=None, train_file_path=None, 
                                                            train_id_column=None, train_data_column=None, test_file_path=default_file_path, test_id_column=default_id_column, test_data_column=default_data_column)
                assert store_User_Assistor_Table_res == 'User_Assistor_Table stores successfully'

                # call make_hash in Algorithm module
                test_hash_id_file_address = make_hash(root=root, self_id=user_id, task_id=task_id, mode=self.test_indicator, test_id=test_id, dataset_path=default_file_path, id_idx=default_id_column, skip_header=self.skip_header_default)
                print('sssss')
                assert test_hash_id_file_address is not None
                _, test_hash_id_file_address = handle_Algorithm_return_value("test_hash_id_file_address", test_hash_id_file_address, "200", "make_hash")
                assert test_hash_id_file_address is not None

                # read file => array data type from np.genfromtxt
                # we need string type with \n between ids.
                test_hash_id_file_data = load_file(test_hash_id_file_address[2])

                url = self.base_url + "/match_test_assistor_id/"
                data = {
                    "file": test_hash_id_file_data,
                    'task_id': task_id,
                    "test_id": test_id,
                }
                try:
                    match_test_assistor_id_res = requests.post(url, json=data, headers={'Authorization': 'Bearer ' + token})
                    match_test_assistor_id_res = load_json_data(json_data=match_test_assistor_id_res, json_data_name='match_test_assistor_id_res', 
                                                    testing_key_value_pair=[('test_id', None), ('stored', 'assistor test match id stored')])
                except:
                    print('match_test_assistor_id_res wrong')
        else:
            print('default_mode wrong')

        print('Assistor: Testing test_id: ', test_id, ' is running')
        return 'unread_test_request done'

    def unread_test_match_id(self, unread_test_match_id_notification: dict, unittest_callbacks=None):
        """
        Handle the unread_test_match_id. Two situations needed to be considered: sponsor and assistor

        Parameters:
            unread_test_match_id_notification - Dictionary.

        Returns:
            None

        Raises:
            KeyError - raises an exception
        """

        cur_unread_test_match_id_Testid_dict = unread_test_match_id_notification["check_dict"]
        test_id_to_task_id = unread_test_match_id_notification["test_id_to_task_id"]
        max_rounds_dict = unread_test_match_id_notification["max_rounds"]

        for test_id in cur_unread_test_match_id_Testid_dict:
            task_id = test_id_to_task_id[test_id]
            check_sponsor = cur_unread_test_match_id_Testid_dict[test_id]
            max_round = max_rounds_dict[test_id]

            if check_sponsor == check_sponsor_class.sponsor:
                self.unread_test_match_id_sponsor(task_id, test_id, max_round, unittest_callbacks)
            elif check_sponsor == check_sponsor_class.assistor:
                self.unread_test_match_id_assistor(task_id, test_id, max_round, unittest_callbacks)

        return 'unread_test_match_id done'

    def unread_test_match_id_sponsor(self, task_id: str, test_id: str, max_round: int, unittest_callbacks):

        """
        Handle the unread_test_match_id of sponsor.

        Parameters:
            task_id - String.
            test_id - String.
            cur_max_round - Integer.

        Returns:
            None

        Raises:
            KeyError - raises an exception
        """

        # obtain some information
        user_id, root, token, _ = self.__obtain_important_information(get_test_id=False)
        
        # initiate a request to get test_match_id_file
        url = self.base_url + "/users/" + user_id + "/test_match_id_file"
        data = {
            "task_id": task_id,
            "test_id": test_id,
        }
        try:
            sponsor_get_test_match_id_file_res = requests.post(url, json=data, headers={'Authorization': 'Bearer ' + token})
            sponsor_get_test_match_id_file_res = load_json_data(json_data=sponsor_get_test_match_id_file_res, json_data_name='sponsor_get_test_match_id_file_res', 
                                                    testing_key_value_pair=[('match_id_file', None), ('assistor_random_id_pair', None)])
            print('sponsor_get_test_match_id_file_res', sponsor_get_test_match_id_file_res)
        except:
            print('sponsor_get_test_match_id_file_res wrong')
    
        match_id_file_list = load_json_data(sponsor_get_test_match_id_file_res["match_id_file"], 'sponsor_get_test_match_id_file_res["match_id_file"]')
        assistor_random_id_pair_list = load_json_data(sponsor_get_test_match_id_file_res["assistor_random_id_pair"], 'sponsor_get_test_match_id_file_res["assistor_random_id_pair"]')
        print('match_id_file_list', match_id_file_list, type(match_id_file_list), len(match_id_file_list))
        for i in range(len(match_id_file_list)):
            from_id = assistor_random_id_pair_list[i]
            cur_match_id_file = match_id_file_list[i]

            # call save_match_id
            test_save_match_id_file_pos = save_match_id(root=root, self_id=user_id, task_id=task_id, mode=self.test_indicator, 
                                                    test_id=test_id, from_id=from_id)
            assert test_save_match_id_file_pos is not None
            _, test_save_match_id_file_pos = handle_Algorithm_return_value("test_save_match_id_file_pos", test_save_match_id_file_pos,
                                                                   "200", "save_match_id")
            assert test_save_match_id_file_pos is not None

            # write file
            save_file(test_save_match_id_file_pos[2], cur_match_id_file)
            msg = ["Test: 3.4 Sponsor Saved Matched id File at " + test_save_match_id_file_pos[2] + "\n"]
            log_helper(msg, root, user_id, task_id)

            # call make_match_idx
            test_make_match_idx_done = make_match_idx(root=root, self_id=user_id, task_id=task_id, mode=self.test_indicator, test_id=test_id, from_id=from_id)
            assert test_make_match_idx_done is not None
            _, test_make_match_idx_done = handle_Algorithm_return_value("test_make_match_idx_done", test_make_match_idx_done, "200", "make_match_idx")
            assert test_make_match_idx_done is not None
            print('from_id', from_id, cur_match_id_file)
        # Get information from User Sponsor Table
        task_mode, model_name, metric_name, test_name, test_description, test_file_path, test_id_column, test_data_column, test_target_column = self.Database_class_instance.get_User_Sponsor_Table(user_id=user_id, test_id=test_id, test_indicator=self.test_indicator)
        print("test_file_path", test_file_path, test_data_column)

        # call make_test
        print('max_round', max_round)
        print('make_test', root, user_id, task_id, test_id, max_round, from_id, test_file_path, test_data_column, self.skip_header_default)
        test_done = make_test(root=root, self_id=user_id, task_id=task_id, test_id=test_id, round=max_round, from_id=None, dataset_path=test_file_path, data_idx=test_data_column, skip_header=self.skip_header_default)
        assert test_done is not None
        _, test_done = handle_Algorithm_return_value("test_done", test_done, "200", "make_test")
        assert test_done is not None
        # print('test_done', test_done)
        if unittest_callbacks:
            assert unittest_callbacks(load_json_data(test_done[2], 'test_done[2]')) == True

        print('Sponsor: Testing test_id: ', test_id, ' is running')
        return

    def unread_test_match_id_assistor(self, task_id: str, test_id: str, cur_max_round: int, unittest_callbacks):

        """
        Handle the unread_test_match_id of assistor.

        Parameters:
            task_id - String.
            test_id - String.
            cur_max_round - Integer.

        Returns:
            None

        Raises:
            KeyError - raises an exception
        """

        # obtain basic information
        user_id, root, token, _ = self.__obtain_important_information(get_test_id=False)

        url = self.base_url + "/users/" + user_id + "/test_match_id_file"
        data = {
            "task_id": task_id,
            "test_id": test_id,
        }
        try:
            assistor_get_test_match_id_file_res = requests.post(url, json=data, headers={'Authorization': 'Bearer ' + token})
            assistor_get_test_match_id_file_res = load_json_data(json_data=assistor_get_test_match_id_file_res, json_data_name='assistor_get_test_match_id_file_res', 
                                                    testing_key_value_pair=[('match_id_file', None), ('sponsor_random_id', None)])
        except:
            print('assistor_get_test_match_id_file_res wrong')
  
        from_id = load_json_data(assistor_get_test_match_id_file_res["sponsor_random_id"][0], 'assistor_get_test_match_id_file_res["sponsor_random_id"][0]')
        cur_match_id_file = load_json_data(assistor_get_test_match_id_file_res["match_id_file"][0], 'assistor_get_test_match_id_file_res["match_id_file"][0]')

        # call test_save_match_id
        test_save_match_id_file_pos = save_match_id(root=root, self_id=user_id, task_id=task_id, mode=self.test_indicator, 
                                                    test_id=test_id, from_id=from_id)
        assert test_save_match_id_file_pos is not None
        _, test_save_match_id_file_pos = handle_Algorithm_return_value("test_save_match_id_file_pos", test_save_match_id_file_pos,
                                                                "200", "save_match_id")
        assert test_save_match_id_file_pos is not None

        # save match id file to designated position
        save_file(test_save_match_id_file_pos[2], cur_match_id_file)
        msg = ["3.4 Assistor Saved Matched id File at " + test_save_match_id_file_pos[2] + "\n"]
        log_helper(msg, root, user_id, task_id)

        # call make_match_idx
        test_make_match_idx_done = make_match_idx(root=root, self_id=user_id, task_id=task_id, mode=self.test_indicator, test_id=test_id, from_id=from_id)
        assert test_make_match_idx_done is not None
        _, test_make_match_idx_done = handle_Algorithm_return_value("test_make_match_idx_done", test_make_match_idx_done, "200", "make_match_idx")
        assert test_make_match_idx_done is not None

        msg = ["3.5 Assistor matches id to index\n"]
        log_helper(msg, root, user_id, task_id)
        msg = ["-------------------------- 3. Unread Match ID Done\n"]
        log_helper(msg, root, user_id, task_id)

        # select select_default_test_data_path from db
        mode, task_mode, model_name, test_name, test_description, test_file_path, test_id_column, test_data_column = self.Database_class_instance.get_User_Assistor_Table(user_id=user_id, test_id=test_id, test_indicator=self.test_indicator)

        # call make test
        test_done = make_test(root=root, self_id=user_id, task_id=task_id, test_id=test_id, round=cur_max_round, from_id=from_id, dataset_path=test_file_path, data_idx=test_data_column, skip_header=self.skip_header_default)
        assert test_done is not None
        _, test_done = handle_Algorithm_return_value("test_done", test_done, "200", "make_test")
        assert test_done is not None

        if unittest_callbacks:
            assert unittest_callbacks(load_json_data(test_done[2], 'test_done[2]')) == True

        all_test_output = []
        make_test_lists = test_done[3:4]

        for i in range(len(make_test_lists)):
            data = load_file(make_test_lists[i])
            all_test_output.append(data)

        url = self.base_url + "/send_test_output/"
        data = {
            "output": all_test_output,
            "test_id": test_id,
            "task_id": task_id,
        }
        try:
            assistor_send_test_output_res = requests.post(url, json=data, headers={'Authorization': 'Bearer ' + token})
            assistor_send_test_output_res = load_json_data(json_data=assistor_send_test_output_res, json_data_name='assistor_send_test_output_res', 
                                                        testing_key_value_pair=[('send_test_output', 'send test output successfully')])
        except:
            print('assistor_send_test_output_res wrong')

        print('Assistor: Testing test_id: ', test_id, ' is running')
        return


    def unread_test_output(self, unread_test_output_notification: dict, unittest_callbacks=None):

        """
        Handle the unread_test_output.

        Parameters:
            unread_test_output_notification - Dictionary.

        Returns:
            None

        Raises:
            KeyError - raises an exception
        """

        cur_unread_test_output_Testid_dict = unread_test_output_notification["check_dict"]
        test_id_to_task_id = unread_test_output_notification["test_id_to_task_id"]

        for test_id in cur_unread_test_output_Testid_dict:
            task_id = test_id_to_task_id[test_id]
            self.unread_test_output_singleTask(task_id, test_id, unittest_callbacks)
            print('Sponsor: Testing test_id: ', test_id, ' is running')
            print('Sponsor: Testing test_id: ', test_id, ' done')
            
        return 'unread_test_output done'

    def unread_test_output_singleTask(self, task_id: str, test_id: str, unittest_callbacks):

        """
        Handle the single task of unread output.

        Parameters:
            task_id - String. Task id of current task
            test_id - Strubg. Test id of current test

        Returns:
            None

        Raises:
            KeyError - raises an exception
        """

        # obtain some important information
        user_id, root, token, _ = self.__obtain_important_information(get_test_id=False)

        url = self.base_url + "/test_output/"
        data = {
            "task_id": task_id,
            "test_id": test_id,
        }
        try:
            sponsor_get_test_output_res = requests.post(url, json=data, headers={'Authorization': 'Bearer ' + token})
            sponsor_get_test_output_res = load_json_data(json_data=sponsor_get_test_output_res, json_data_name='sponsor_get_test_output_res', 
                                                    testing_key_value_pair=[('output', None), ('sender_random_ids_list', None)])
        except:
            print('sponsor_get_test_output_res wrong')

        output = load_json_data(sponsor_get_test_output_res["output"], 'sponsor_get_test_output_res["output"]')
        print('asss', output)
        sender_random_ids_list = load_json_data(sponsor_get_test_output_res["sender_random_ids_list"], 'sponsor_get_test_output_res["sender_random_ids_list"]')

        # iterate the match_id_file
        # List[List[List]] structure: [[[data from one assistor],[data from one assistor]],[[data from another assistor],[data from another assistor]]]
        max_round = 1
        for i in range(len(output)):
            from_id = sender_random_ids_list[i]
            multiple_outputs_from_one_assistor = load_json_data(json_data=output[i], json_data_name='output[i]')
            max_round = max(len(multiple_outputs_from_one_assistor), max_round)

            for j in range(len(multiple_outputs_from_one_assistor)):
                cur_output = multiple_outputs_from_one_assistor[j]

                # call save_output
                test_save_output_pos = save_output(root=root, self_id=user_id, task_id=task_id, mode=self.test_indicator, test_id=test_id, round=(j+1), from_id=from_id)
                assert test_save_output_pos is not None
                _, test_save_output_pos = handle_Algorithm_return_value("test_save_output_pos", test_save_output_pos, "200", "save_output")
                assert test_save_output_pos is not None
                save_file(test_save_output_pos[2], cur_output)
                
        # max_round = len(output[0])
        print('max_round', max_round)
        waiting_start_time = time.time()
        self.unread_test_output_make_eval_helper(task_id, test_id, max_round, waiting_start_time, unittest_callbacks)

        return

    def unread_test_output_make_eval_helper(self, task_id: str, test_id: str, max_round: int, waiting_start_time: float, unittest_callbacks):
        """
        Helper Function. Dealing with the order issue

        Parameters:
            task_id - String. Task id of current task
            test_id - Strubg. Test id of current test
            max_round - Integer. The max_round of train task of current test

        Returns:
            None

        Raises:
            KeyError - raises an exception
        """

        waiting_current_time = time.time()
        time_interval = waiting_current_time - waiting_start_time
        if time_interval > 30 * 60:
            raise ValueError('Sorry, the test stopped due to slow computation')

        # obtain some important information
        user_id, root, token, _ = self.__obtain_important_information(get_test_id=False)

        # select data from sponsor table
        task_mode, model_name, metric_name, test_name, test_description, test_file_path, test_id_column, test_data_column, test_target_column = self.Database_class_instance.get_User_Sponsor_Table(user_id=user_id, test_id=test_id, test_indicator=self.test_indicator)

        # call make_eval
        eval_done = make_eval(root=root, self_id=user_id, task_id=task_id, test_id=test_id, round=max_round, dataset_path=test_file_path, target_idx=test_target_column, skip_header=self.skip_header_default, task_mode=task_mode, metric_name=metric_name, task_path=None)
        assert eval_done is not None
        eval_done_indicator, eval_done = handle_Algorithm_return_value("eval_done", eval_done, "200", "make_eval")
        assert eval_done is not None

        if eval_done_indicator == False:
            args = [task_id, test_id, max_round, waiting_start_time, unittest_callbacks]
            print('unread_test_output_make_eval_helper callback')
            threading.Timer(30, self.unread_test_output_make_eval_helper, args)
        elif eval_done_indicator == True:
            if unittest_callbacks:
                assert unittest_callbacks(load_json_data(eval_done[2], 'eval_done[2]')) == True
