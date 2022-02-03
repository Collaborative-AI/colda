import requests
import json
import numpy as np

from .Network import Network
from .PersonalInformation import PersonalInformation
from .Database_class import Database_class
from .Error import check_Algorithm_return_value
from .apollo_utils import log_helper, handle_Algorithm_return_value

from py_pkg.Algorithm import make_eval, make_test, make_hash, save_match_id, make_match_idx, make_residual, make_train, save_output, make_result, save_residual, log
# from Database import Session, User_Default_Path, User_Chosen_Path, User_Pending_Page, assign_value_to_user_chosen_path_instance


class TestRequest:
    __TestRequest_instance = None

    def __init__(self):
        self.Network_instance = Network.get_Network_instance()
        self.PersonalInformation_instance = PersonalInformation.get_PersonalInformation_instance()
        self.Database_class_instance = Database_class.get_Database_class_instance()

        self.test_indicator = 'test'
        self.skip_header_default = 1
        self.base_url = self.Network_instance.get_base_url()

    @classmethod
    def get_TestRequest_instance(cls):
        if cls.__TestRequest_instance == None:
            cls.__TestRequest_instance = TestRequest()

        return cls.__TestRequest_instance


    def handleTestRequest(self, task_id: str, task_name: str, test_name: str, task_mode: str,
                        model_name: str, metric_name: str, testing_data_path: str):

        """
        Parameters:
            task_id - String. The task that the user wanted to test
            task_name - String. The name of the task that the user wanted to test
            test_name - String. The name of current test
            task_mode - String. The task_mode of current test
            model_name - String. The model_name of current test
            metric_name - String. The metric_name of current test
            testing_data_path - String. Input path address of testing data path

        Returns:
            None

        Raises:
            KeyError - raises an exception
        """

        self.__find_test_assistor(task_id, task_name, test_name, task_mode, model_name, metric_name, testing_data_path)
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
        try:
            get_test_id_response = requests.get(url, headers = {'Authorization': 'Bearer ' + token})
        except RuntimeError:
            print('get_test_id_response wrong')
        get_test_id_response = json.loads(get_test_id_response.text)
        print("get_test_id_response", get_test_id_response)

        new_test_id = get_test_id_response["test_id"]

        return new_test_id

    def __find_test_assistor(self, task_id: str, task_mode: str, model_name: str, metric_name: str, test_file_path: str,
                            test_id_column: str, test_data_column: str, test_target_column: str, test_name: str=None, test_description: str=None):

        """
        start testing with all assistors of the task

        Parameters:
            task_id - String. The task that the user wanted to test
            task_name - String. The name of the task that the user wanted to test
            test_name - String. The name of current test
            task_mode - String. The task_mode of current test
            model_name - String. The model_name of current test
            metric_name - String. The metric_name of current test
            testing_data_path - String. Input path address of testing data path
            testing_id_path - String. Input path address of testing id path
            test_description - String. Test description

        Returns:
            None

        Raises:
            KeyError - raises an exception
        """

        # obtain some important information
        user_id = self.PersonalInformation_instance.get_user_id()
        test_id = self.__get_test_id()
        root = self.PersonalInformation_instance.get_root()

        # store information in db
        self.Database_class_instance.store_User_Sponsor_Table(user_id=user_id, task_id=task_id, test_id=test_id, test_indicator=self.test_indicator, task_mode=task_mode, model_name=model_name, metric_name=metric_name,
                                                            test_name=test_name, test_description=test_description, test_file_path=test_file_path, test_id_column=test_id_column, test_data_column=test_data_column,
                                                            test_target_column=test_target_column)

        # call make_hash in Algorithm module
        test_hash_id_file_address = make_hash(root=root, self_id=user_id, task_id=task_id, mode=self.test_indicator, test_id=test_id, dataset_path=test_file_path, id_idx=test_id_column, skip_header=self.skip_header_default)
        assert test_hash_id_file_address is not None
        test_hash_id_file_address = handle_Algorithm_return_value("test_hash_id_file_address", test_hash_id_file_address, "200", "make_hash")
        assert test_hash_id_file_address is not None

        # read file => array data type from np.genfromtxt
        # we need string type with \n between ids.
        test_hash_id_file_data = np.genfromtxt(test_hash_id_file_address[2], delimiter=',', dtype=np.str_)
        assert test_hash_id_file_data is not None
        test_hash_id_file_data = list(test_hash_id_file_data)
        print("test_hash_id_file_data", test_hash_id_file_data, type(test_hash_id_file_data))

        # call find assistor in server
        url = self.base_url + "/find_test_assistor/"
        token = self.Network_instance.get_token()

        data = {
            "task_id": task_id,
            'test_id': test_id,
            'test_name': test_name,
            'test_description': test_description,
            'task_mode': task_mode,
            'model_name': model_name,
            'metric_name': metric_name,
            'id_file': test_hash_id_file_data,
        }

        print(data)
        try:
            find_test_assistor_res = requests.post(url, data=data, headers={'Authorization': 'Bearer ' + token})
        except RuntimeError:
            print('find_test_assistor_res wrong')
        find_test_assistor_res = json.loads(find_test_assistor_res.text)
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

        # obtain some important information
        user_id = self.PersonalInformation_instance.get_user_id()
        root = self.PersonalInformation_instance.get_root()
        token = self.Network_instance.get_token()

        user_id, default_mode, default_file_path, default_id_column, default_data_column, default_model_name = self.Database_class_instance.get_User_Default_Table()
        if default_mode == "manual":
            # Insert to DB
            pass

        elif default_mode == "auto":
            # get default path
            
            cur_unread_test_request_Testid_dict = unread_test_request_notification["check_dict"]
            test_id_to_task_id = unread_test_request_notification["test_id_to_task_id"]

            for test_id in cur_unread_test_request_Testid_dict:
                task_id = test_id_to_task_id[test_id]

                # Insert default into User_Assistor_Table
                
                # call make_hash in Algorithm module
                test_hash_id_file_address = make_hash(root=root, self_id=user_id, task_id=task_id, mode=self.test_indicator, test_id=test_id, dataset_path=default_file_path, id_idx=default_id_column, skip_header=self.skip_header_default)
                assert test_hash_id_file_address is not None
                test_hash_id_file_address = handle_Algorithm_return_value("test_hash_id_file_address", test_hash_id_file_address, "200", "make_hash")
                assert test_hash_id_file_address is not None

                # read file => array data type from np.genfromtxt
                # we need string type with \n between ids.
                test_hash_id_file_data = np.genfromtxt(test_hash_id_file_address[2], delimiter=',', dtype=np.str_)
                assert test_hash_id_file_data is not None
                test_hash_id_file_data = list(test_hash_id_file_data)

                url = self.base_url + "/match_test_assistor_id/"
                token = self.Network_instance.get_token()
                data = {
                    "file": test_hash_id_file_data,
                    'task_id': task_id,
                    "test_id": test_id,
                }
                try:
                    match_test_assistor_id_res = requests.post(url, data=data, headers={'Authorization': 'Bearer ' + token})
                except RuntimeError:
                    print('match_test_assistor_id_res wrong')
                match_test_assistor_id_res = json.loads(match_test_assistor_id_res.text)
                print("match_test_assistor_id_res", match_test_assistor_id_res)

        else:
            print('default_mode wrong')

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
                self.unread_test_match_id_sponsor(task_id, test_id, cur_max_round)
            elif check_sponsor == 0:
                self.unread_test_match_id_assistor(task_id, test_id, cur_max_round)

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

        # obtain some information
        token = self.Network_instance.get_token()
        root = self.PersonalInformation_instance.get_root()
        user_id = self.PersonalInformation_instance.get_user_id()
        
        # initiate a request to get test_match_id_file
        url = self.base_url + "/users/" + user_id + "/test_match_id_file"
        data = {
            "test_id": test_id,
        }
        try:
            sponsor_get_test_match_id_file_res = requests.post(url, data=data, headers={'Authorization': 'Bearer ' + token})
        except RuntimeError:
            print('sponsor_get_test_match_id_file_res wrong')

        sponsor_get_test_match_id_file_res = json.loads(sponsor_get_test_match_id_file_res.text)
    
        match_id_file_list = sponsor_get_test_match_id_file_res["match_id_file"]
        assistor_random_id_pair_list = sponsor_get_test_match_id_file_res["assistor_random_id_pair"]

        for i in range(len(match_id_file_list)):
            from_id = assistor_random_id_pair_list[i]
            cur_match_id_file = json.loads(match_id_file_list[i])
            cur_match_id_file = "\n".join(cur_match_id_file)

            # call save_match_id
            test_save_match_id_file_pos = save_match_id(root=root, self_id=user_id, task_id=task_id, mode=self.test_indicator, 
                                                    test_id=test_id, from_id=from_id)
            assert test_save_match_id_file_pos is not None
            test_save_match_id_file_pos = handle_Algorithm_return_value("test_save_match_id_file_pos", test_save_match_id_file_pos,
                                                                   "200", "save_match_id")
            assert test_save_match_id_file_pos is not None

            # write file
            np.savetxt(test_save_match_id_file_pos[2], cur_match_id_file, delimiter=",", fmt="%s")
            msg = ["Test: 3.4 Sponsor Saved Matched id File at " + test_save_match_id_file_pos[2] + "\n"]
            log_helper(msg, root, user_id, task_id)

            # call make_match_idx
            test_make_match_idx_done = make_match_idx(root=root, self_id=user_id, task_id=task_id, mode=self.test_indicator, test_id=test_id, from_id=from_id)
            assert test_make_match_idx_done is not None
            test_make_match_idx_done = handle_Algorithm_return_value("test_make_match_idx_done", test_make_match_idx_done, "200", "make_match_idx")
            assert test_make_match_idx_done is not None

        # Get information from User Sponsor Table
        task_mode, model_name, metric_name, test_name, test_description, test_file_path, test_id_column, test_data_column, test_target_column = self.Database_class_instance.get_User_Sponsor_Table(user_id=user_id, test_id=test_id, test_indicator=self.test_indicator)
        print("test_file_path", test_file_path, test_data_column)

        # call make_test
        test_done = make_test(root=root, self_id=user_id, tsak_id=task_id, test_id=test_id, round=cur_max_round, from_id=from_id, dataset_path=test_file_path, data_idx=test_data_column, skip_header=self.skip_header_default)
        assert test_done is not None
        test_done = handle_Algorithm_return_value("test_done", test_done, "200", "make_test")
        assert test_done is not None

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

        # obtain basic information
        user_id = self.PersonalInformation_instance.get_user_id()
        token = self.Network_instance.get_token()
        root = self.PersonalInformation_instance.get_root()

        url = self.base_url + "/users/" + user_id + "/test_match_id_file"
        data = {
            "task_id": task_id,
            "test_id": test_id,
        }
        try:
            assistor_get_test_match_id_file_res = requests.post(url, data=data, headers={'Authorization': 'Bearer ' + token})
        except RuntimeError:
            print('assistor_get_test_match_id_file_res wrong')
        assistor_get_test_match_id_file_res = json.loads(assistor_get_test_match_id_file_res.text)
        print("assistor_get_test_match_id_file_res", assistor_get_test_match_id_file_res)
  
        from_id = assistor_get_test_match_id_file_res["sponsor_random_id"]
        cur_match_id_file = assistor_get_test_match_id_file_res["match_id_file"][0]
        cur_match_id_file = "\n".join(cur_match_id_file)

        # call test_save_match_id
        test_save_match_id_file_pos = save_match_id(root=root, self_id=user_id, task_id=task_id, mode=self.test_indicator, 
                                                    test_id=test_id, from_id=from_id)
        assert test_save_match_id_file_pos is not None
        test_save_match_id_file_pos = handle_Algorithm_return_value("test_save_match_id_file_pos", test_save_match_id_file_pos,
                                                                "200", "save_match_id")
        assert test_save_match_id_file_pos is not None

        # save match id file to designated position
        np.savetxt(test_save_match_id_file_pos[2], cur_match_id_file, delimiter=",", fmt="%s")
        msg = ["3.4 Assistor Saved Matched id File at " + test_save_match_id_file_pos[2] + "\n"]
        log_helper(msg, root, user_id, task_id)

        # call make_match_idx
        test_make_match_idx_done = make_match_idx(root=root, self_id=user_id, task_id=task_id, mode=self.test_indicator, test_id=test_id, from_id=from_id)
        assert test_make_match_idx_done is not None
        test_make_match_idx_done = handle_Algorithm_return_value("test_make_match_idx_done", test_make_match_idx_done, "200", "make_match_idx")
        assert test_make_match_idx_done is not None

        msg = ["3.5 Assistor matches id to index\n"]
        log_helper(msg, root, user_id, task_id)
        msg = ["-------------------------- 3. Unread Match ID Done\n"]
        log_helper(msg, root, user_id, task_id)

        # select select_default_test_data_path from db
        mode, model_name, test_name, test_description, test_file_path, test_id_column, test_data_column = self.Database_class_instance.get_User_Assistor_Table(user_id=user_id, test_id=test_id, test_indicator=self.test_indicator)

        # call make test
        test_done = make_test(root=root, self_id=user_id, tsak_id=task_id, test_id=test_id, round=cur_max_round, from_id=from_id, dataset_path=test_file_path, data_idx=test_data_column, skip_header=self.skip_header_default)
        assert test_done is not None
        test_done = handle_Algorithm_return_value("test_done", test_done, "200", "make_test")
        assert test_done is not None

        all_test_output = []
        make_test_lists = test_done[3:]

        for i in range(len(make_test_lists)):
            data = np.genfromtext(make_test_lists[i], delimiter=',', dtype=np.str_)
            all_test_output.append(data)

        url = self.base_url + "/send_test_output/"
        data = {
            "output": all_test_output,
            "test_id": test_id,
            "task_id": task_id,
        }
        try:
            assistor_send_test_output_res = requests.post(url, data=data,
                                                            headers={'Authorization': 'Bearer ' + token})
        except RuntimeError:
            print('assistor_send_test_output_res wrong')

        assistor_send_test_output_res = json.loads(assistor_send_test_output_res.text)
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
            self.unread_test_output_singleTask(task_id, task_id)

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

        # obtain some important information
        user_id = self.PersonalInformation_instance.get_user_id()
        root = self.PersonalInformation_instance.get_root()
        token = self.Network_instance.get_token()

        url = self.base_url + "/test_output/"
        data = {
            "task_id": task_id,
            "test_id": test_id,
        }
        try:
            sponsor_get_test_output_res = requests.post(url, data=data, headers={'Authorization': 'Bearer ' + token})
        except RuntimeError:
            print('sponsor_get_test_output_res wrong')
        sponsor_get_test_output_res = json.loads(sponsor_get_test_output_res.text)
        print("sponsor_get_test_output_res", sponsor_get_test_output_res)
        output = sponsor_get_test_output_res["output"]
        sender_random_ids_list = sponsor_get_test_output_res["sender_random_ids_list"]

        # iterate the match_id_file
        # List[List[List]] structure: [[[data from one assistor],[data from one assistor]],[[data from another assistor],[data from another assistor]]]
        for i in range(len(output)):
            from_id = sender_random_ids_list[i]
            multiple_outputs_from_one_assistor = json.loads(output[i])

            for j in range(len(multiple_outputs_from_one_assistor)):
                cur_output = multiple_outputs_from_one_assistor[j]

                # call save_output
                test_save_output_pos = save_output(root=root, self_id=user_id, task_id=task_id, model=self.test_indicator, test_id=test_id, round=(j+1), from_id=from_id)
                assert test_save_output_pos is not None
                test_save_output_pos = handle_Algorithm_return_value("test_save_output_pos", test_save_output_pos, "200", "save_output")
                assert test_save_output_pos is not None
                np.savetxt(test_save_output_pos[2], cur_output, delimiter=",", fmt="%s")
                
        max_round = len(output[0])
        self.unread_test_output_make_eval_helper(task_id, test_id, max_round)

        return

    def unread_test_output_make_eval_helper(self, task_id: str, test_id: str, max_round: int):
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

        # obtain some important information
        user_id = self.PersonalInformation_instance.get_user_id()
        root = self.PersonalInformation_instance.get_root()
        token = self.Network_instance.get_token()

        # select data from sponsor table
        task_mode, model_name, metric_name, test_name, test_description, test_file_path, test_id_column, test_data_column, test_target_column = self.Database_class_instance.get_User_Sponsor_Table(user_id=user_id, test_id=test_id, test_indicator=self.test_indicator)

        # call make_eval
        eval_done = make_eval(root=root, self_id=user_id, task_id=task_id, test_id=test_id, round=max_round, dataset_path=test_file_path, target=test_target_column, skip_header=self.skip_header_default, task_mode=task_mode, metric_name=metric_name)
        assert eval_done is not None
        eval_done = handle_Algorithm_return_value("eval_done", eval_done, "200", "make_eval")
        assert eval_done is not None

        return
