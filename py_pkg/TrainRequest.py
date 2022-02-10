from gettext import find
from unittest import skip
import numpy as np
import requests
import json
import os
import argparse
import subprocess

from .Network import Network
from .PersonalInformation import PersonalInformation
from .Database_class import Database_class
from .SynSpot_utils import log_helper, load_json_data, load_file, save_file, handle_Algorithm_return_value
from .Error import check_Algorithm_return_value

from py_pkg.Algorithm import make_hash, save_match_id, make_match_idx, make_residual, make_train, save_output, make_result, save_residual, log
# from Database import Session, User_Default_Path, User_Chosen_Path, User_Pending_Page, assign_value_to_user_chosen_path_instance

class check_sponsor_class:
    sponsor = 1
    assistor = 0

class TrainRequest():
    __TrainRequest_instance = None

    def __init__(self):
        self.Network_instance = Network.get_Network_instance()
        self.PersonalInformation_instance = PersonalInformation.get_PersonalInformation_instance()
        self.Database_class_instance = Database_class.get_Database_class_instance()

        self.base_url = self.Network_instance.get_base_url()
        self.maxRound = 2
        self.skip_header_default = 1
        self.initial_round = 1
        self.test_indicator = 'train'
        # self.assistor_task_mode = 'regression'
        # self.exe_position = self.PersonalInformation_instance.get_exe_position()
        # self.root = self.PersonalInformation_instance.get_root()

    @classmethod
    def get_TrainRequest_instance(cls):
        if cls.__TrainRequest_instance == None:
            cls.__TrainRequest_instance = TrainRequest()

        return cls.__TrainRequest_instance

    def __obtain_important_information(self, get_train_id):
        user_id = self.PersonalInformation_instance.get_user_id()
        assert user_id is not None
        root = self.PersonalInformation_instance.get_root()
        assert root is not None
        token = self.Network_instance.get_token()
        assert token is not None

        task_id = None
        if get_train_id:
            task_id = self.__get_train_id()
        return user_id, root, token, task_id

    def handleTrainRequest(self, maxRound: int, assistors: list, train_file_path: str, train_id_column: str, train_data_column: str, 
                            train_target_column: str, task_mode: str, model_name: str, metric_name: str, task_name: str=None, task_description: str=None):
        
        """
        Parameters:
            maxRound - Integer. Maximum training round
            username - List. The List of assistors
            train_file_path - String. Input path address of training data path
            train_id_column - String. ID column of Input File
            train_data_column - String. Data column of Input File
            train_target_column - String. Target column of Input File
            task_name - String. Default is None
            task_description - String. Default is None

        Returns:
            None

        Raises:
            KeyError - raises an exception
        """

        return self.__find_assistor(maxRound=maxRound, assistors=assistors, train_file_path=train_file_path, train_id_column=train_id_column, 
                            train_data_column=train_data_column, train_target_column=train_target_column, task_mode=task_mode,
                            model_name=model_name, metric_name=metric_name, task_name=task_name, task_description=task_description)

    def __get_train_id(self):
        
        """
        Get new Task id for this task

        Parameters:
            None

        Returns:
            new_task_id - String. The new task id of new task

        Raises:
            KeyError - raises an exception
        """

        url = self.base_url + "/create_new_train_task/"
        token = self.Network_instance.get_token()
        try:
            get_train_id_response = requests.get(url, headers = {'Authorization': 'Bearer ' + token})
        except RuntimeError:
            print('get_train_id_response wrong')

        get_train_id_response_text = load_json_data(json_data=get_train_id_response, json_data_name='get_train_id_response', 
                                                    testing_key_value_pair=[('task_id', None)])

        new_task_id = get_train_id_response_text["task_id"]
        assert new_task_id is not None

        return new_task_id


    def __find_assistor(self, maxRound: int, assistors: list, train_file_path: str, train_id_column: str, train_data_column: str, train_target_column: str, task_mode: str, model_name: str, metric_name: str, task_name: str=None, task_description: str=None):
        
        """
        start task with all assistors

        Parameters:
            maxRound - Integer. Maximum training round
            username - List. The List of assistors
            train_file_path - String. Input path address of training data path
            train_id_column - String. ID column of Input File
            train_data_column - String. Data column of Input File
            train_target_column - String. Target column of Input File
            task_name - String. Default is None
            task_description - String. Default is None

        Returns:
            None

        Raises:
            KeyError - raises an exception
        """

        # obtain some important information
        user_id, root, token, task_id = self.__obtain_important_information(get_train_id=True)

        store_User_Sponsor_Table_res = self.Database_class_instance.store_User_Sponsor_Table(user_id=user_id, task_id=task_id, test_indicator=self.test_indicator, task_mode=task_mode, model_name=model_name, metric_name=metric_name,
                                                            task_name=task_name, task_description=task_description, train_file_path=train_file_path, train_id_column=train_id_column, train_data_column=train_data_column,
                                                            train_target_column=train_target_column)
        assert store_User_Sponsor_Table_res == 'User_Sponsor_Table stores successfully'


        # call make_hash in Algorithm module
        hash_id_file_address = make_hash(root=root, self_id=user_id, task_id=task_id, mode=self.test_indicator, test_id=None, dataset_path=train_file_path, id_idx=train_id_column, skip_header=self.skip_header_default)
        assert hash_id_file_address is not None
        hash_id_file_address = handle_Algorithm_return_value("hash_id_file_address", hash_id_file_address, "200", "make_hash")
        assert hash_id_file_address is not None

        # read file => array data type from np.genfromtxt
        # we need string type with \n between ids.
        hash_id_file_data = load_file(file_address=hash_id_file_address[2])

        # call find_assistor in server
        url = self.base_url + "/find_assistor/"

        data = {
            "id_file": hash_id_file_data,
            "task_id": task_id,
            "task_name": task_name,
            "task_mode": task_mode,
            "model_name": model_name,
            "metric_name": metric_name,
            "assistor_username_list": assistors,   
            "task_description": task_description
        }
        try:
            find_assistor_res = requests.post(url, json=data, headers={'Authorization': 'Bearer ' + token})
            find_assistor_res = load_json_data(json_data=find_assistor_res, json_data_name='find_assistor_res',
                                                testing_key_value_pair=[('task_id', task_id)])
        except RuntimeError:
            print('find_assistor_res wrong')

        # Record the history to log file
        msg = ["\n You are SPONSOR\n", "Task ID: " + task_id + "\n", "---------------------- Train Stage Starts\n",
               "---------------------- 1. Find assistor\n", "1.1 Sponsor calls for help\n", "1.2 Sponsor sends id file\n"]
        log_helper(msg, root, user_id, task_id)

        return ('handleTrainRequest successfully', task_id)

    def unread_request(self, unread_request_notification: dict):

        """
        Handle the unread request for three default mode: ["passive", "active", "auto"]

        Parameters:
            unread_request_notification - Dictionary.

        Returns:
            None

        Raises:
            KeyError - raises an exception
        """

        # obtain some important information
        user_id, root, token, _ = self.__obtain_important_information(get_train_id=False)
        
        default_mode = self.PersonalInformation_instance.get_default_mode()
        print('default_mode', default_mode)
        cur_unread_request_Taskid_dict = unread_request_notification["check_dict"]
        cur_unread_request_info_dict = unread_request_notification["info_dict"]

        for task_id in cur_unread_request_Taskid_dict:
            if default_mode == "auto":
                
                user_id, default_mode, default_task_mode, default_model_name, default_file_path, default_id_column, default_data_column = self.Database_class_instance.get_User_Default_Table(user_id)
                
                store_User_Assistor_Table_res = self.Database_class_instance.store_User_Assistor_Table(user_id=user_id, task_id=task_id, test_indicator=self.test_indicator, mode=default_mode, task_mode=default_task_mode, model_name=default_model_name, 
                                                            test_id=None, task_name=None, task_description=None, test_name=None, test_description=None, train_file_path=default_file_path, 
                                                            train_id_column=default_id_column, train_data_column=default_data_column, test_file_path=None, test_id_column=None, test_data_column=None)
                assert store_User_Assistor_Table_res == 'User_Assistor_Table stores successfully'

                hash_id_file_address = make_hash(root=root, self_id=user_id, task_id=task_id, mode=self.test_indicator, 
                                                test_id=None, dataset_path=default_file_path, id_idx=default_id_column, skip_header=self.skip_header_default)
                assert hash_id_file_address is not None
                hash_id_file_address = handle_Algorithm_return_value("hash_id_file_address", hash_id_file_address, "200", "make_hash")
                print('hash_id_file_address', hash_id_file_address)
                assert hash_id_file_address is not None

                hash_id_file_data = load_file(hash_id_file_address[2])

                # add log
                msg = ["\n You are Assistor\n", "Task ID: " + task_id + "\n", "----2. Unread Request\n", "2.1 Update the request notification\n"]
                log_helper(msg, root, user_id, task_id)
                
                url = self.base_url + '/match_assistor_id/'
                data = {
                    "task_id": task_id,
                    "file": hash_id_file_data
                }
                try:
                    match_assistor_id_res = requests.post(url, json=data, headers={'Authorization': 'Bearer ' + token})
                    match_assistor_id_res = load_json_data(json_data=match_assistor_id_res, json_data_name='match_assistor_id_res', 
                                                            testing_key_value_pair=[('stored', 'assistor match id stored')])
                except RuntimeError:
                    print('match_assistor_id_res wrong')

                # add log
                msg = ["2.2 assistor uploads id file\n", "----2. Unread Request Done\n"]
                log_helper(msg, root, user_id, task_id)
            elif default_mode == "manual":
                pass
            else:
                print('unread request: wrong mode')
        return 'unread_request successfully'

    def unread_match_id(self, unread_match_id_notification: dict):

        """
        Handle the unread_match_id. Two situations needed to be considered: sponsor and assistor

        Parameters:
            unread_match_id_notification - Dictionary.

        Returns:
            None

        Raises:
            KeyError - raises an exception
        """

        # obtain some important information
        user_id, root, token, _ = self.__obtain_important_information(get_train_id=False)

        cur_unread_match_id_Taskid_dict = unread_match_id_notification["check_dict"]
        for task_id in cur_unread_match_id_Taskid_dict:

            msg = ["----3. Unread Match ID\n", "3.1 Update the match id notification\n"]
            log_helper(msg, root, user_id, task_id)

            check_sponsor = cur_unread_match_id_Taskid_dict[task_id]
            if check_sponsor == check_sponsor_class.sponsor:
                msg = ["3.2 Unread_match_id_sponsor\n"]
                log_helper(msg, root, user_id, task_id)

                self.unread_match_id_sponsor(task_id)
            elif check_sponsor == check_sponsor_class.assistor:
                msg = ["3.2 Unread_match_id_assistor\n"]
                log_helper(msg, root, user_id, task_id)

                self.unread_match_id_assistor(task_id)

        return 'unread match id done'

    def unread_match_id_sponsor(self, task_id: str):

        """
        Handle the unread_match_id of sponsor.

        Parameters:
            task_id - String.

        Returns:
            None

        Raises:
            KeyError - raises an exception
        """

        # obtain some information
        user_id, root, token, _ = self.__obtain_important_information(get_train_id=False)

        url = self.base_url + "/users/" + user_id + "/match_id_file"
        data = {
            "task_id": task_id,
        }
        try:
            sponsor_get_match_id_file_res = requests.post(url, json=data, headers={'Authorization': 'Bearer ' + token})
            sponsor_get_match_id_file_res = load_json_data(json_data=sponsor_get_match_id_file_res, json_data_name='sponsor_get_match_id_file_res', 
                                                            testing_key_value_pair=[('match_id_file', None), ('assistor_random_id_pair', None)])
        except RuntimeError:
            print('sponsor_get_match_id_file_res wrong')

        msg = ["3.3 Sponsor gets matched id file\n"]
        log_helper(msg, root, user_id, task_id)

        match_id_file_list = load_json_data(sponsor_get_match_id_file_res["match_id_file"], 'sponsor_get_match_id_file_res["match_id_file"]')
        print("match_id_file_list", match_id_file_list)
        assistor_random_id_pair_list = load_json_data(sponsor_get_match_id_file_res["assistor_random_id_pair"], 'sponsor_get_match_id_file_res["assistor_random_id_pair"]')

        for i in range(len(match_id_file_list)):
            from_id = assistor_random_id_pair_list[i]
            # need to json load each item again to gain list
            cur_match_id_file = json.loads(match_id_file_list[i])
            # cur_match_id_file = "\n".join(cur_match_id_file)

            # call save_match_id
            save_match_id_file_pos = save_match_id(root=root, self_id=user_id, task_id=task_id, mode=self.test_indicator, 
                                                    test_id=None, from_id=from_id)
            assert save_match_id_file_pos is not None
            save_match_id_file_pos = handle_Algorithm_return_value("save_match_id_file_pos", save_match_id_file_pos,
                                                                   "200", "save_match_id")
            assert save_match_id_file_pos is not None

            # write file
            save_file(save_match_id_file_pos[2], cur_match_id_file)

            msg = ["3.4 Sponsor Saved Matched id File at " + save_match_id_file_pos[2] + "\n"]
            log_helper(msg, root, user_id, task_id)

            # call make_match_idx
            make_match_idx_done = make_match_idx(root=root, self_id=user_id, task_id=task_id, mode=self.test_indicator, test_id=None, from_id=from_id)
            assert make_match_idx_done is not None
            make_match_idx_done = handle_Algorithm_return_value("make_match_idx_done", make_match_idx_done, "200", "make_match_idx")
            assert make_match_idx_done is not None

            msg = ["3.5 Sponsor matches id to index\n"]
            log_helper(msg, root, user_id, task_id)

        # get train target column
        task_mode, model_name, metric_name, task_name, task_description, train_file_path, train_id_column, train_data_column, train_target_column = self.Database_class_instance.get_User_Sponsor_Table(user_id=user_id, task_id=task_id, test_indicator=self.test_indicator)
        print("train_file_path", train_file_path, train_target_column)

        # call make residual
        make_residual_multiple_paths = make_residual(root=root, self_id=user_id, task_id=task_id, round=self.initial_round, dataset_path=train_file_path, target_idx=train_target_column, skip_header=self.skip_header_default, task_mode=task_mode, metric_name=metric_name)
        assert make_residual_multiple_paths is not None
        make_residual_multiple_paths = handle_Algorithm_return_value("make_residual_multiple_paths", make_residual_multiple_paths, "200", "make_residual")
        assert make_residual_multiple_paths is not None

        msg = ["3.6 Sponsor makes residual finished\n"]
        log_helper(msg, root, user_id, task_id)

        residual_paths = make_residual_multiple_paths[2].split("?")
        assistor_random_id_list = []
        all_residual_data = []

        for i in range(len(residual_paths)):
            cur_residual_path_data = load_file(residual_paths[i])
            # cur_residual_path_data = "\n".join(cur_residual_path_data)
            all_residual_data.append(cur_residual_path_data)

            cur_path = residual_paths[i]
            path_split = os.path.split(cur_path)
            assistor_random_id = path_split[-1].split(".")[0]
            assistor_random_id_list.append(assistor_random_id)

        url = self.base_url + "/send_situation"
        data = {
            "task_id": task_id,
            "assistor_random_id_list": assistor_random_id_list,
            "residual_list": all_residual_data
        }
        try:
            send_situation_res = requests.post(url, json=data, headers={'Authorization': 'Bearer ' + token})
            send_situation_res = load_json_data(json_data=send_situation_res, json_data_name='send_situation_res', 
                                                testing_key_value_pair=[('message', 'send situation successfully!')])
        except RuntimeError:
            print('send_situation_res wrong')

        msg = ["3.7 Sponsor sends all situations" + "\n", "-------------------------- 3. Unread Match ID Done\n"]
        log_helper(msg, root, user_id, task_id)

        return 'unread_match_id_sponsor successfully'

    def unread_match_id_assistor(self, task_id: str):

        """
        Handle the unread_match_id of assistor.

        Parameters:
            task_id - String.

        Returns:
            None

        Raises:
            KeyError - raises an exception
        """

        # obtain basic information
        user_id, root, token, _ = self.__obtain_important_information(get_train_id=False)

        # initiate a request
        url = self.base_url + "/users/" + user_id + "/match_id_file"
        data = {
            "task_id": task_id,
        }
        try:
            assistor_get_match_id_file_res = requests.post(url, json=data, headers={'Authorization': 'Bearer ' + token})
            assistor_get_match_id_file_res = load_json_data(json_data=assistor_get_match_id_file_res, json_data_name='assistor_get_match_id_file_res', 
                                                            testing_key_value_pair=[('match_id_file', None), ('sponsor_random_id', None)])
        except RuntimeError:
            print('assistor_get_match_id_file_res wrong')

        msg = ["3.3 Assistor gets matched id file\n"]
        log_helper(msg, root, user_id, task_id)

        # handle the response from request, assistor only has one match_id_file. Use [0] to get directly.
        cur_match_id_file = load_json_data(assistor_get_match_id_file_res["match_id_file"][0], 'assistor_get_match_id_file_res["match_id_file"][0]')
        from_id = load_json_data(assistor_get_match_id_file_res["sponsor_random_id"][0], 'assistor_get_match_id_file_res["sponsor_random_id"][0]')

        # call save_match_id to get the designated position to save the match_id file
        save_match_id_file_pos = save_match_id(root=root, self_id=user_id, task_id=task_id, mode=self.test_indicator, test_id=None, from_id=from_id)
        assert save_match_id_file_pos is not None
        save_match_id_file_pos = handle_Algorithm_return_value("save_match_id_file_pos", save_match_id_file_pos,
                                                                "200", "save_match_id")
        assert save_match_id_file_pos is not None

        # save match id file to designated position
        save_file(save_match_id_file_pos[2], cur_match_id_file)

        msg = ["3.4 Assistor Saved Matched id File at " + save_match_id_file_pos[2] + "\n"]
        log_helper(msg, root, user_id, task_id)

        # call make_match_idx
        make_match_idx_done = make_match_idx(root=root, self_id=user_id, task_id=task_id, mode=self.test_indicator, test_id=None, from_id=from_id)
        assert make_match_idx_done is not None
        make_match_idx_done = handle_Algorithm_return_value("make_match_idx_done", make_match_idx_done, "200", "make_match_idx")
        assert make_match_idx_done is not None

        msg = ["3.5 Assistor matches id to index\n", "---- 3. Unread Match ID Done\n"]
        log_helper(msg, root, user_id, task_id)

        return 'unread_match_id_assistor successfully'

    def unread_situation(self, unread_situation_notification: dict):

        """
        Handle the unread_situation. Two situations needed to be considered: sponsor and assistor

        Parameters:
            unread_situation_notification - Dictionary.

        Returns:
            None

        Raises:
            KeyError - raises an exception
        """

        # obtain important information
        user_id, root, token, _ = self.__obtain_important_information(get_train_id=False)

        cur_unread_match_id_Taskid_dict = unread_situation_notification["check_dict"]
        cur_unread_situation_Rounds_dict = unread_situation_notification["rounds_dict"]

        for task_id in cur_unread_match_id_Taskid_dict:

            msg = ["-------------------------- 4. Unread Situation\n", "4.1 Update the situation notification\n"]
            log_helper(msg, root, user_id, task_id)

            check_sponsor = cur_unread_match_id_Taskid_dict[task_id]
            rounds = cur_unread_situation_Rounds_dict[task_id]

            if check_sponsor == check_sponsor_class.sponsor:
                self.unread_situation_sponsor(task_id, rounds)
            elif check_sponsor == check_sponsor_class.assistor:
                self.unread_situation_assistor(task_id, rounds)

        return 'unread situation done'


    def unread_situation_sponsor(self, task_id: str, rounds: int):

        """
        Handle the unread situation of sponsor.

        Parameters:
            task_id - String. The task needed to be handled.
            rounds - Integer. Current round.

        Returns:
            None

        Raises:
            KeyError - raises an exception
        """

        # obtain basic information
        user_id, root, token, _ = self.__obtain_important_information(get_train_id=False)

        msg = ["4.2 Cur round is: " + str(rounds) + "\n"]
        log_helper(msg, root, user_id, task_id)

        # get train_data_path from db
        task_mode, model_name, metric_name, task_name, task_description, train_file_path, train_id_column, train_data_column, train_target_column = self.Database_class_instance.get_User_Sponsor_Table(user_id=user_id, task_id=task_id, test_indicator=self.test_indicator)

        # call make train
        train_output = make_train(root=root, self_id=user_id, task_id=task_id, round=rounds, dataset_path=train_file_path, data_idx=train_data_column, skip_header=self.skip_header_default, task_mode=task_mode, model_name=model_name)
        assert train_output is not None
        train_output = handle_Algorithm_return_value("train_output", train_output, "200", "make_train")
        assert train_output is not None

        msg = ["4.3 Sponsor round " + str(rounds) + " training done." + "\n", "-------------------------- 4. Unread Situation Done\n"]
        log_helper(msg, root, user_id, task_id)

        return 'unread_situation_sponsor successfully'

    def unread_situation_assistor_train_part(self, task_id: str, rounds: int, from_id: str, train_file_path: str, train_data_column: str, task_mode: str, model_name: str):
        
        """
        Handle the timing issue of unread situation of assistor.

        Parameters:
            task_id - String. The task needed to be handled.
            rounds - Integer. Current round.
            train_file_path - String. The file path of train file
            train_data_column - String. The selected data column of train file

        Returns:
            None

        Raises:
            KeyError - raises an exception
        """

        # obtain basic information
        user_id, root, token, _ = self.__obtain_important_information(get_train_id=False)
        
        # train the model and get output
        print('sss')
        train_output = make_train(root=root, self_id=user_id, task_id=task_id, round=rounds, from_id=from_id, dataset_path=train_file_path, data_idx=train_data_column, skip_header=self.skip_header_default, task_mode=task_mode, model_name=model_name)
        assert train_output is not None
        train_output = handle_Algorithm_return_value("train_output", train_output, "200", "make_train")
        assert train_output is not None
        print('ssssss')
        msg = ["4.4 Assistor round " + str(rounds) + " training done." + "\n"]
        log_helper(msg, root, user_id, task_id)
        
        # read the file from designated position
        Assistor_train_output_data = load_file(train_output[2])
   
        # initiate a request to send output
        url = self.base_url + "/send_output/"
        data = {
            "task_id": task_id,
            "output": Assistor_train_output_data
        }
        try:
            assistor_send_output_res = requests.post(url, json=data, headers={'Authorization': 'Bearer ' + token})
            assistor_send_output_res = load_json_data(json_data=assistor_send_output_res, json_data_name='assistor_send_output_res', 
                                                            testing_key_value_pair=[('send_output', 'send output successfully')])
        except RuntimeError:
            print('assistor_send_output_res wrong')

        msg = ["4.5 Assistor sends output\n", "---- 4. Unread Situation Done\n", "---- Train stage done\n"]
        log_helper(msg, root, user_id, task_id)
        
        return 'unread_situation_sponsor successfully'


    def unread_situation_assistor(self, task_id: str, rounds: int):

        """
        Handle the unread situation of assistor.

        Parameters:
            task_id - String. The task needed to be handled.
            rounds - Integer. Current round.

        Returns:
            None

        Raises:
            KeyError - raises an exception
        """

        # obtain basic information
        user_id, root, token, _ = self.__obtain_important_information(get_train_id=False)

        # initiate a request
        url = self.base_url + "/users/" + user_id + "/situation_file"
        data = {
            "task_id": task_id,
            "rounds": rounds
        }
        try:
            assistor_get_situation_res = requests.post(url, json=data, headers={'Authorization': 'Bearer ' + token})
            assistor_get_situation_res = load_json_data(json_data=assistor_get_situation_res, json_data_name='assistor_get_situation_res', 
                                                            testing_key_value_pair=[('situation', None), ('sender_random_id', None)])
        except RuntimeError:
            print('assistor_get_situation_res wrong')

        # handle response from above request
        cur_situation_file = load_json_data(assistor_get_situation_res["situation"], 'assistor_get_situation_res["situation"]')
        from_id = load_json_data(assistor_get_situation_res["sender_random_id"], 'assistor_get_situation_res["sender_random_id"]')

        # call save_residual
        save_residual_pos = save_residual(root=root, self_id=user_id, task_id=task_id, round=rounds)
        assert save_residual_pos is not None
        save_residual_pos = handle_Algorithm_return_value("save_residual_pos", save_residual_pos,
                                                                "200", "save_residual")
        assert save_residual_pos is not None

        # save match id file to designated position
        save_file(save_residual_pos[2], cur_situation_file)

        msg = ["4.3 Assistor Saved Residual File!\n"]
        log_helper(msg, root, user_id, task_id)

        # select train_data_path
        mode, task_mode, model_name, task_name, task_description, train_file_path, train_id_column, train_data_column = self.Database_class_instance.get_User_Assistor_Table(user_id=user_id, task_id=task_id, test_indicator=self.test_indicator)
        print('get assistor table', mode, task_mode, model_name, task_name, task_description, train_file_path, train_id_column, train_data_column)
        self.unread_situation_assistor_train_part(task_id, rounds, from_id, train_file_path, train_data_column, task_mode, model_name)
        
        return 'unread_situation_assistor successfully'


    def unread_output(self, unread_output_notification: dict):

        """
        Handle the unread_output.

        Parameters:
         unread_output_notification - Dictionary.

        Returns:
         None

        Raises:
         KeyError - raises an exception
        """

        user_id, root, token, _ = self.__obtain_important_information(get_train_id=False)

        cur_unread_output_Rounds_dict = unread_output_notification["rounds_dict"]

        for task_id in cur_unread_output_Rounds_dict:

            msg = ["-------------------------- 5. Unread Output\n", "5.1 Update the output notification\n"]
            log_helper(msg, root, user_id, task_id)

            rounds = cur_unread_output_Rounds_dict[task_id]
            self.unread_output_singleTask(task_id, rounds)

        return 'unread output done'

    def unread_output_singleTask(self, task_id: str, rounds: int):

        """
        Handle the single task of unread output.

        Parameters:
         task_id - String. Task id of current task
         rounds - Integer. Current Round

        Returns:
         None

        Raises:
         KeyError - raises an exception
        """
        print("unread_output_singleTask", rounds)
        user_id, root, token, _ = self.__obtain_important_information(get_train_id=False)

        url = self.base_url + "/users/" + user_id + "/output/"
        data = {
            "task_id": task_id,
            "rounds": rounds
        }
        try:
            sponsor_get_output_res = requests.post(url, json=data, headers={'Authorization': 'Bearer ' + token})
            sponsor_get_output_res = load_json_data(json_data=sponsor_get_output_res, json_data_name='sponsor_get_output_res', 
                                                    testing_key_value_pair=[('output', None), ('sender_random_ids_list', None)])
        except RuntimeError:
            print('sponsor_get_output_res wrong')

        msg = ["5.2 Sponsor gets output model\n"]
        log_helper(msg, root, user_id, task_id)

        output = load_json_data(sponsor_get_output_res["output"], 'sponsor_get_output_res["output"]')
        sender_random_ids_list = load_json_data(sponsor_get_output_res["sender_random_ids_list"], 'sponsor_get_output_res["sender_random_ids_list"]')

        for i in range(len(output)):
            from_id = sender_random_ids_list[i]
            cur_output = output[i]
            print("from_id", from_id)
            # call save_output
            save_output_pos = save_output(root=root, self_id=user_id, task_id=task_id, mode=self.test_indicator, test_id=None, round=rounds, from_id=from_id)
            assert save_output_pos is not None
            save_output_pos = handle_Algorithm_return_value("save_output_pos", save_output_pos, "200", "save_output")
            assert save_output_pos is not None

            # write file
            # cur_output = json.loads(output[i]).split("\n")
            print("cur_output", type(cur_output), cur_output)
            save_file(save_output_pos[2], cur_output)

            msg = ["5.3 Sponsor saves Output model\n"]
            log_helper(msg, root, user_id, task_id)

            # get train_file_path, train_target_column from User_Sponsor_Table
            task_mode, model_name, metric_name, task_name, task_description, train_file_path, train_id_column, train_data_column, train_target_column = self.Database_class_instance.get_User_Sponsor_Table(user_id=user_id, task_id=task_id, test_indicator=self.test_indicator)
            print('zzzz', task_mode, model_name, metric_name, task_name, task_description, train_file_path, train_id_column, train_data_column, train_target_column)
            self.unread_output_make_result_helper(task_id, rounds, train_file_path, train_target_column, task_mode, metric_name)

        return

    def unread_output_make_result_helper(self, task_id: str, rounds: int, train_file_path: str, train_target_column: str, task_mode: str, metric_name: str):
        """
        Helper Function. Dealing with the order issue

        Parameters:
         task_id - String. Task id of current task
         rounds - Integer. Current Round
         train_file_path - String. The file path of train file
         train_target_column - String. The selected data column of train file

        Returns:
         None

        Raises:
         KeyError - raises an exception
        """
        user_id, root, token, _ = self.__obtain_important_information(get_train_id=False)

        # call make_result
        make_result_done = make_result(root=root, self_id=user_id, task_id=task_id, round=rounds, dataset_path=train_file_path, target_idx=train_target_column, skip_header=self.skip_header_default, task_mode=task_mode, metric_name=metric_name)
        assert make_result_done is not None
        make_result_done = handle_Algorithm_return_value("make_result_done", make_result_done, "200", "make_result")
        assert make_result_done is not None

        msg = ["5.4 Sponsor makes result done." + "\n"]
        log_helper(msg, root, user_id, task_id)

        if rounds >= self.maxRound:
            msg = ["---- Train Stage Ends\n"]
            log_helper(msg, root, user_id, task_id)
            return
        else:
            # call make_residual
            make_residual_multiple_paths = make_residual(root=root, self_id=user_id, task_id=task_id, round=(rounds+1), dataset_path=train_file_path, target_idx=train_target_column, skip_header=self.skip_header_default, task_mode=task_mode, metric_name=metric_name)
            assert make_residual_multiple_paths is not None
            make_residual_multiple_paths = handle_Algorithm_return_value("make_residual_multiple_paths", make_residual_multiple_paths, "200", "make_residual")
            assert make_residual_multiple_paths is not None

            msg = ["5.5 Sponsor makes residual finished\n"]
            log_helper(msg, root, user_id, task_id)

            all_residual_data = []
            assistor_random_id_list = []
            residual_paths = make_residual_multiple_paths[2:]
            print('residual_paths', residual_paths)
            for i in range(len(residual_paths)):
                data = load_file(residual_paths[i])
                # cur_residual_path_data = "\n".join(cur_residual_path_data)

                all_residual_data.append(data)

                path_split = os.path.split(residual_paths[i])
                print('cur_path', path_split)
                assistor_random_id = path_split[-1].split(".")[0]
                print('cur_path', assistor_random_id)
                assistor_random_id_list.append(assistor_random_id)

            url = self.base_url + "/send_situation"
            data = {
                "task_id": task_id,
                "assistor_random_id_list": assistor_random_id_list,
                "residual_list": all_residual_data
            }
            try:
                send_situation_res = requests.post(url, json=data, headers={'Authorization': 'Bearer ' + token})
                send_situation_res = load_json_data(json_data=send_situation_res, json_data_name='send_situation_res', 
                                                    testing_key_value_pair=[('message', 'send situation successfully!')])
            except RuntimeError:
                print('send_situation_res wrong')

            msg = ["5.6 Sponsor updates situation done\n", "-------------------------- 5. Unread Output Done\n"]
            log_helper(msg, root, user_id, task_id)

            return 'unread_output successfully'

    def unread_train_stop(self, unread_train_stop_notification: dict):
        """
        Stop Train and delete related files

        Parameters:
         unread_train_stop_notification - Dictionary.

        Returns:
         None

        Raises:
         KeyError - raises an exception
        """

        return






