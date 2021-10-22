import numpy as np
import requests
import json
import argparse
import subprocess

from Network import Network
from PersonalInformation import PersonalInformation

# from Algorithm import *
from Database import Session, User_Default_Path, User_Chosen_Path, User_Pending_Page, assign_value_to_user_chosen_path_instance


parser = argparse.ArgumentParser()
parser.add_argument('func', type=str)
parser.add_argument('--root', default=None, type=str)
parser.add_argument('--self_id', default=None, type=str)
parser.add_argument('--task_id', default=None, type=str)
parser.add_argument('--mode', default=None, type=str)
parser.add_argument('--round', default=None, type=int)
parser.add_argument('--test_id', default=None, type=str)
parser.add_argument('--from_id', default=None, type=str)
parser.add_argument('--dataset_path', default=None, type=str)
parser.add_argument('--id_idx', default=None, type=str)
parser.add_argument('--data_idx', default=None, type=str)
parser.add_argument('--target_idx', default=None, type=str)
args = vars(parser.parse_args())


class TrainRequest():

    def __init__(self):
        self.Network_instance = Network.get_Network_instance()
        self.PersonalInformation_instance = PersonalInformation.get_PersonalInformation_instance()
        self.base_url = self.Network_instance.get_base_url()
        self.exe_position = self.PersonalInformation_instance.get_exe_position()
        self.root = self.PersonalInformation_instance.get_root()

    def handleTrainRequest(self, maxRound: int, assistors: list, train_file_path: str, train_id_column: str, train_data_column: str, train_target_column: str, task_name: str=None, task_description: str=None):
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

        self.__find_assistor(maxRound, assistors, train_file_path, train_id_column, train_data_column, train_target_column, task_name, task_description)
        return

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
        get_train_id_response = requests.get(url, headers = {'Authorization': 'Bearer ' + token})
        get_train_id_response_text = json.loads(get_train_id_response.text)
        print("get_train_id_response", get_train_id_response_text)

        new_task_id = get_train_id_response_text["task_id"]
        print("new_task_id", new_task_id)

        return new_task_id




    def __find_assistor(self, maxRound: int, assistors: list, train_file_path: str, train_id_column: str, train_data_column: str, train_target_column: str, task_name: str=None, task_description: str=None):
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

        user_id = self.PersonalInformation_instance.get_user_id()
        task_id = self.__get_train_id()

        # store id_column, data_column, target_column into database
        session = Session()
        user_chosen_path = User_Chosen_Path()
        user_chosen_path = assign_value_to_user_chosen_path_instance(user_chosen_path, user_id, "train", task_id, train_file_path, train_id_column, train_data_column, train_target_column, task_name, task_description)
        session.add(user_chosen_path)
        session.commit()

        # call make_hash in Algorithm module
        command = (self.exe_position + ' make_hash --root ' + self.root + ' --self_id ' + user_id + ' --task_id ' +
                  task_id + ' --mode train' + ' --dataset_path ' + train_file_path + ' --id_idx ' + train_id_column)
        res = subprocess.check_output(command)
        print("!!res", res)
        res = res.split("?")

        url = self.base_url + "/find_assistor/"
        token = self.Network_instance.get_token()

        hash_id_file_data = "1\n2\n3"
        hash_id_file_data = np.genfromtxt(res[2], delimiter=',')

        data = {
            "assistor_id_list": assistors,
            "task_id": task_id,
            "id_file": hash_id_file_data,
        }
        print(data)
        find_assistor_res = requests.post(url, data = data, headers = {'Authorization': 'Bearer ' + token})
        print("find_assistor_res", find_assistor_res)

        return

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
        session = Session()
        aa = User_Default_Path()
        aa.id = 5
        aa.user_id = "aa"
        session.add(aa)
        session.commit()

        default_mode = self.PersonalInformation_instance.get_default_mode()
        Algorithm.ceshi()
        if default_mode == "active":
            # Insert to DB
            pass

        elif default_mode == "passive":
            # get default path

            cur_unread_request_Taskid_dict = unread_request_notification["check_dict"]
            for task_id in cur_unread_request_Taskid_dict:
                # hash_id_file_dat = make hash

                url = self.base_url + "/match_assistor_id/"
                token = self.Network_instance.get_token()
                task_id = task_id
                file = hash_id_file_data
                data = {
                    "task_id": task_id,
                    "file": hash_id_file_data,
                }
                match_assistor_id_res = requests.post(url, data=data, headers={'Authorization': 'Bearer ' + token})
                print("match_assistor_id_res", match_assistor_id_res)

        elif default_mode == "auto":
            pass

        return

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

        cur_unread_match_id_Taskid_dict = unread_match_id_notification["check_dict"]
        for task_id in cur_unread_match_id_Taskid_dict:

            check_sponsor = cur_unread_match_id_Taskid_dict[task_id]
            if check_sponsor == 1:
                self.unread_match_id_sponsor(task_id)
            elif check_sponsor == 0:
                self.unread_match_id_assistor(task_id)

        return

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

        user_id = self.PersonalInformation_instance.get_user_id()
        url = self.base_url + "/users/" + user_id + "/match_id_file"
        token = self.Network_instance.get_token()
        data = {
            "task_id": task_id,
        }
        sponsor_get_match_id_file_res = requests.post(url, data=data, headers={'Authorization': 'Bearer ' + token})
        print("sponsor_get_match_id_file_res", sponsor_get_match_id_file_res)
        match_id_file_list = json.loads(get_match_id_file_res.text)["match_id_file"]
        assistor_random_id_pair_list = json.loads(get_match_id_file_res.text)["assistor_random_id_pair"]

        for i in range(len(match_id_file_list)):
            from_id = assistor_random_id_pair_list[i]
            cur_match_id_file = match_id_file_list[i]
            cur_match_id_file = "\n".join(cur_match_id_file)

            # call save_match_id
            save_match_id_file_pos

            # call make_match_idx

        # get train target column

        # make residual
        url = self.base_url + "/send_situation"
        data = {
            "task_id": task_id,
            "assistor_random_id_list": assistor_random_id_list,
            "residual_list": residual_list
        }
        send_situation_res = requests.post(url, data=data, headers={'Authorization': 'Bearer ' + token})
        print("send_situation_res", send_situation_res)

        return

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
        user_id = self.PersonalInformation_instance.get_user_id()
        url = self.base_url + "/users/" + user_id + "/match_id_file"
        token = self.Network_instance.get_token()
        data = {
            "task_id": task_id,
        }
        assistor_get_match_id_file_res = requests.post(url, data=data, headers={'Authorization': 'Bearer ' + token})
        print("assistor_get_match_id_file_res", assistor_get_match_id_file_res)
        cur_match_id_file = json.loads(get_match_id_file_res.text)["match_id_file"][0]
        cur_match_id_file = "\n".join(cur_match_id_file)
        from_id = json.loads(get_match_id_file_res.text)["sponsor_random_id"]

        # call save_match_id
        save_match_id_file_pos

        # call make_match_idx

        return

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

        cur_unread_match_id_Taskid_dict = unread_situation_notification["check_dict"]
        cur_unread_situation_Rounds_dict = unread_situation_notification["rounds_dict"]
        for task_id in cur_unread_match_id_Taskid_dict:

            check_sponsor = cur_unread_match_id_Taskid_dict[task_id]
            rounds = cur_unread_situation_Rounds_dict[task_id]

            if check_sponsor == 1:
                self.unread_situation_sponsor(task_id, rounds)
            elif check_sponsor == 0:
                self.unread_situation_sponsor(task_id, rounds)

        return


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

        # get train_data_path from db
        # make train
        user_id = self.PersonalInformation_instance.get_user_id()
        url = self.base_url + "/users/" + user_id + "/match_id_file"
        token = self.Network_instance.get_token()
        data = {
            "task_id": task_id,
        }


        return

    def unread_situation_assistor_train_part(self, task_id: str, rounds: int, from_id: str, default_train_file_path: str, default_train_data_column: str):
        """
        Handle the timing issue of unread situation of assistor.

        Parameters:
         task_id - String. The task needed to be handled.
         rounds - Integer. Current round.
         default_train_file_path - String. The file path of train file
         default_train_data_column - String. The selected data column of train file

        Returns:
         None

        Raises:
         KeyError - raises an exception
        """

        # call make_train

        Assistor_train_output_data = None

        url = self.base_url + "/send_output/"
        token = self.Network_instance.get_token()
        data = {
            "task_id": task_id,
            "output": Assistor_train_output_data
        }
        assistor_send_output_res = requests.post(url, data=data, headers={'Authorization': 'Bearer ' + token})
        print("assistor_send_output_res", assistor_send_output_res)

        return


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

        # make train
        user_id = self.PersonalInformation_instance.get_user_id()
        url = self.base_url + "/users/" + user_id + "/situation_file"
        token = self.Network_instance.get_token()
        data = {
            "task_id": task_id,
            "rounds": rounds
        }
        assistor_get_situation_res = requests.post(url, data=data, headers={'Authorization': 'Bearer ' + token})
        print("assistor_get_situation_res", assistor_get_situation_res)
        cur_situation_file = json.loads(get_match_id_file_res.text)["situation"]
        from_id = json.loads(assistor_get_situation_res.text)["sender_random_id"]

        # call save_residual

        # select train_data_path
        train_data_path = None
        default_train_file_path = None
        default_train_data_column = None

        self.unread_situation_assistor_train_part(task_id, rounds, from_id, default_train_file_path, default_train_data_column)
        return


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

        cur_unread_output_Rounds_dict = unread_output_notification["rounds_dict"]
        for task_id in cur_unread_output_Rounds_dict:
            rounds = cur_unread_output_Rounds_dict[task_id]
            self.unread_output_singleTask(rounds, task_id)

        return

    def unread_output_singleTask(self, task_id, rounds):

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

        user_id = self.PersonalInformation_instance.get_user_id()
        url = self.base_url + "/users/" + user_id + "/output/"
        token = self.Network_instance.get_token()
        data = {
            "task_id": task_id,
            "rounds": rounds
        }
        sponsor_get_output_res = requests.post(url, data=data, headers={'Authorization': 'Bearer ' + token})
        output = json.loads(sponsor_get_output_res.text)["output"]
        sender_random_ids_list = json.loads(sponsor_get_output_res.text)["sender_random_ids_list"]

        for i in range(len(output)):
            from_id = sender_random_ids_list[i]

            # call save_output

            train_target_path = None
            train_file_path = None
            train_target_column = None

            self.unread_output_make_result_helper(task_id, rounds, train_file_path, train_target_column)

        return

    def unread_output_make_result_helper(self, task_id: str, rounds: int, train_file_path: str, train_target_column: str):
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

        # call make_result

        # call make_residual
        all_residual_data = []
        assistor_random_id_list = []

        user_id = self.PersonalInformation_instance.get_user_id()
        url = self.base_url + "/send_situation/"
        token = self.Network_instance.get_token()
        data = {
            "residual_list": all_residual_data,
            "task_id": task_id,
            "assistor_random_id_list": assistor_random_id_list
        }
        sponsor_send_situation_res = requests.post(url, data=data, headers={'Authorization': 'Bearer ' + token})
        print("sponsor_send_situation_res", sponsor_send_situation_res)

        return

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






