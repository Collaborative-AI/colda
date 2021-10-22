import requests
import json

from Network import Network
from PersonalInformation import PersonalInformation

class TestRequest:
    __TestRequest_instance = None

    def __init__(self):
        self.Network_instance = Network.get_Network_instance()
        self.PersonalInformation_instance = PersonalInformation.get_PersonalInformation_instance()
        self.base_url = self.Network_instance.get_base_url()

    @classmethod
    def get_TestRequest_instance(cls):
        if cls.__TestRequest_instance == None:
            cls.__TestRequest_instance = TestRequest()

        return cls.__TestRequest_instance


    def handleTestRequest(self, task_id: str, testing_data_path: str):
        """
        Parameters:
         task_id - String. The task that the user wanted to test
         testing_data_path - String. Input path address of testing data path

        Returns:
         None

        Raises:
         KeyError - raises an exception
        """

        self.__find_test_assistor(task_id, testing_data_path)
        return

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
        token = self.Network_instance.get_token()
        get_test_id_response = requests.get(url, headers = {'Authorization': 'Bearer ' + token})
        print("get_test_id_response", get_test_id_response)

        new_test_id = json.loads(get_test_id_response.text)["test_id"]

        return new_test_id

    def __find_test_assistor(self, task_id: str, testing_data_path: str):
        """
        start testing with all assistors of the task

        Parameters:
         task_id - String. The task that the user wanted to test
         testing_data_path - String. Input path address of testing data path

        Returns:
         None

        Raises:
         KeyError - raises an exception
        """

        url = self.base_url + "/find_test_assistor/"
        token = self.Network_instance.get_token()
        test_id = self.__get_test_id()
        test_hash_id_file_data = None
        data = {
            "test_id": test_id,
            "task_id": task_id,
            "id_file": test_hash_id_file_data,
        }
        print(data)
        find_test_assistor_res = requests.post(url, data=data, headers={'Authorization': 'Bearer ' + token})
        print("find_test_assistor_res", find_test_assistor_res)

        return

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

        default_mode = self.PersonalInformation_instance.get_default_mode()
        if default_mode == "active":
            # Insert to DB
            pass

        elif default_mode == "passive":
            # get default path

            cur_unread_test_request_Testid_dict = unread_test_request_notification["check_dict"]
            test_id_to_task_id = unread_test_request_notification["test_id_to_task_id"]

            for test_id in cur_unread_test_request_Testid_dict:
                task_id = test_id_to_task_id[test_id]
                # hash_id_file_dat = make hash

                url = self.base_url + "/match_test_assistor_id/"
                token = self.Network_instance.get_token()
                test_hash_id_file_data = None
                test_id = test_id
                file = test_hash_id_file_data
                data = {
                    "test_id": test_id,
                    "file": test_hash_id_file_data,
                }
                match_test_assistor_id_res = requests.post(url, data=data, headers={'Authorization': 'Bearer ' + token})
                print("match_test_assistor_id_res", match_test_assistor_id_res)

        elif default_mode == "auto":
            pass

        return

    def unread_test_match_id(self, unread_test_match_id_notification: dict):
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
            cur_max_round = max_rounds_dict[test_id]

            if check_sponsor == 1:
                self.unread_match_id_sponsor(task_id, test_id, cur_max_round)
            elif check_sponsor == 0:
                self.unread_match_id_assistor(task_id, test_id, cur_max_round)

        return

    def unread_test_match_id_sponsor(self, task_id: str, test_id: str, cur_max_round: int):

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

        user_id = self.PersonalInformation_instance.get_user_id()
        url = self.base_url + "/users/" + user_id + "/test_match_id_file"
        token = self.Network_instance.get_token()
        data = {
            "test_id": test_id,
        }
        sponsor_get_test_match_id_file_res = requests.post(url, data=data, headers={'Authorization': 'Bearer ' + token})
        print("sponsor_get_test_match_id_file_res", sponsor_get_test_match_id_file_res)
        match_id_file_list = json.loads(sponsor_get_test_match_id_file_res.text)["match_id_file"]
        assistor_random_id_pair_list = json.loads(sponsor_get_test_match_id_file_res.text)["assistor_random_id_pair"]

        for i in range(len(match_id_file_list)):
            from_id = assistor_random_id_pair_list[i]
            cur_match_id_file = match_id_file_list[i]
            cur_match_id_file = "\n".join(cur_match_id_file)

            # call save_match_id
            save_match_id_file_pos

            # call make_match_idx

        # get select_test_data_path
        select_test_data_path = None

        # call make_test


        return

    def unread_test_match_id_assistor(self, task_id: str, test_id: str, cur_max_round: int):

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

        user_id = self.PersonalInformation_instance.get_user_id()
        url = self.base_url + "/users/" + user_id + "/test_match_id_file"
        token = self.Network_instance.get_token()
        data = {
            "test_id": test_id,
        }
        assistor_get_test_match_id_file_res = requests.post(url, data=data, headers={'Authorization': 'Bearer ' + token})
        print("assistor_get_test_match_id_file_res", assistor_get_test_match_id_file_res)
        cur_match_id_file = json.loads(get_match_id_file_res.text)["match_id_file"][0]
        cur_match_id_file = "\n".join(cur_match_id_file)
        from_id = json.loads(get_match_id_file_res.text)["sponsor_random_id"]

        # call save_match_id
        save_match_id_file_pos

        # call make_match_idx

        # select select_default_test_data_path from db

        # call make test
        all_test_output = []

        url = self.base_url + "/send_test_output/"
        token = self.Network_instance.get_token()
        data = {
            "output": all_test_output,
            "test_id": test_id,
        }
        assistor_send_test_output_res = requests.post(url, data=data,
                                                            headers={'Authorization': 'Bearer ' + token})
        print("assistor_send_test_output_res", assistor_send_test_output_res)

        return


    def unread_test_output(self, unread_test_output_notification: dict):

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
            self.unread_output_singleTask(task_id, task_id)


        return

    def unread_test_output_singleTask(self, task_id: str, test_id: str):

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

        user_id = self.PersonalInformation_instance.get_user_id()
        url = self.base_url + "/test_output/"
        token = self.Network_instance.get_token()
        data = {
            "test_id": test_id,
        }

        sponsor_get_test_output_res = requests.post(url, data=data, headers={'Authorization': 'Bearer ' + token})
        print("sponsor_get_test_output_res", sponsor_get_test_output_res)
        output = json.loads(sponsor_get_test_output_res.text)["output"]
        sender_random_ids_list = json.loads(sponsor_get_test_output_res.text)["sender_random_ids_list"]

        for i in range(len(output)):
            from_id = sender_random_ids_list[i]

            # call save_output

            train_target_path = None
            train_file_path = None
            train_target_column = None

            self.unread_output_make_result_helper(task_id, rounds, train_file_path, train_target_column)

        return

    def unread_test_output_make_eval_helper(self, task_id: str, test_id: str):
        """
        Helper Function. Dealing with the order issue

        Parameters:
         task_id - String. Task id of current task
         test_id - Strubg. Test id of current test

        Returns:
         None

        Raises:
         KeyError - raises an exception
        """


        return
