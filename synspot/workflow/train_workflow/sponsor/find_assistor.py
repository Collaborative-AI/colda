from __future__ import annotations

import requests

from synspot.workflow.base import BaseWorkflow

from synspot.workflow.utils import (
    load_json_data,
    log_helper
)


class TrainSponsorFindAssistor(BaseWorkflow):

    @classmethod
    def __get_train_id(cls) -> str:
        
        """
        Get new Task id for this task

        :returns: new_train_id. String`. The new task id of new task

        :exception OSError: 
        """

        _, _, token = cls._get_important_information()

        url = cls._process_url(prefix='main_flow', url="/create_new_train_task")
        create_new_train_task_response = cls._get_request(
            url=url,
            token=token,
            request_name='create_new_train_task'
        )

        get_train_id_response_text = load_json_data(json_data=get_train_id_response, json_data_name='get_train_id_response', 
                                                    testing_key_value_pair=[('train_id', None)])

        new_train_id = get_train_id_response_text["train_id"]
        # assert new_train_id is not None

        return new_train_id


    @classmethod
    def find_assistor(
        cls, 
        maxRound: int, 
        assistors: list, 
        train_file_path: str, 
        train_id_column: str, 
        train_data_column: str, 
        train_target_column: str, 
        task_mode: str, 
        model_name: str, 
        metric_name: str, 
        task_name: str = None, 
        task_description: str = None
    ) -> None:

        train_id = cls.__get_train_id()
        user_id, root, token = cls._get_important_information()
        
        # assert store_User_Sponsor_Table_res == 'User_Sponsor_Table stores successfully'


        # call make_hash in Algorithm module
        hash_id_file_data = cls.__TrainAlgorithm_instance.make_hash(
            # self_id=user_id, 
            # train_id=train_id, 
            # mode=self.test_indicator, 
            # test_id=None, 
            dataset_path=train_file_path, 
            id_idx=train_id_column, 
            skip_header=cls.__skip_header
        )


        # hash_id_file_address = make_hash(root=root, self_id=user_id, train_id=train_id, mode=self.test_indicator, test_id=None, dataset_path=train_file_path, id_idx=train_id_column, skip_header=self.skip_header_default)
        # assert hash_id_file_address is not None
        # _, hash_id_file_address = handle_Algorithm_return_value("hash_id_file_address", hash_id_file_address, "200", "make_hash")
        # assert hash_id_file_address is not None

        # read file => array data type from np.genfromtxt
        # we need string type with \n between ids.
        # hash_id_file_data = load_file(file_address=hash_id_file_address[2])

        # call find_assistor in server
        url = cls._process_url(prefix='main_flow', url="/find_assistor", suffix=user_id)

        data = {
            "identifier_content": hash_id_file_data,
            "train_id": train_id,
            "task_name": task_name,
            "task_mode": task_mode,
            "model_name": model_name,
            "metric_name": metric_name,
            "assistor_username_list": assistors,   
            "task_description": task_description
        }

        find_assistor_response = cls._post_request(
            url=url,
            token=token,
            request_name='find_assistor',
            data=data
        )

        find_assistor_res = load_json_data(json_data=find_assistor_res, json_data_name='find_assistor_res',
                                                testing_key_value_pair=[('train_id', train_id)])

        res = cls.__TrainSponsorMetadataDatabase_instance.store_record(
            user_id=user_id, 
            train_id=train_id, 
            task_mode=task_mode, 
            model_name=model_name, 
            metric_name=metric_name,
            train_file_path=train_file_path, 
            train_id_column=train_id_column, 
            train_data_column=train_data_column,
            train_target_column=train_target_column,
            task_name=task_name, 
            task_description=task_description, 
        )

        res = cls.__TrainAlgorithmDatabase_instance.store_record(
            user_id=user_id, 
            train_id=train_id, 
            algorithm_data_name='hash_id_file_data',
            algorithm_data=hash_id_file_data
        )

        # Record the history to log file
        msg = [
            "\n You are SPONSOR\n", 
            f"Train ID: {train_id} \n", 
            "---- Train Stage Starts \n",
            "---- 1. Find assistor \n", 
            "1.1 Sponsor calls for help \n", 
            "1.2 Sponsor sends id file \n"
        ]
        log_helper(msg, root, user_id, train_id)

        print('Training train_id: ', train_id)
        print('Sponsor: Training train_id: ', train_id, ' is running')
    
        return ('handleTrainRequest successfully', train_id)