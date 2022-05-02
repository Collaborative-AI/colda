from __future__ import annotations

import requests

from synspot.workflow.train_base import TrainBaseWorkflow

from synspot.utils.log import GetWorkflowLog


class TrainSponsorFindAssistor(TrainBaseWorkflow):

    @classmethod
    def __get_train_id(cls) -> str:
        
        """
        Get new Task id for this task

        :returns: new_train_id. String`. The new task id of new task

        :exception OSError: 
        """

        _, _, token = cls._get_important_information()

        create_new_train_task_response = cls._get_request_chaining(
            token=token,
            url_prefix=cls.__url_prefix,
            url_root='create_new_train_task'
        )
        new_train_id = create_new_train_task_response["train_id"]
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
        
        # call make_hash in Algorithm module
        encrypted_identifer = cls._encrypt_identifier(
            dataset_path=train_file_path, 
            id_idx=train_id_column, 
            skip_header=cls.__skip_header
        )        

        data = {
            "identifier_content": encrypted_identifer,
            "train_id": train_id,
            "task_name": task_name,
            "task_mode": task_mode,
            "model_name": model_name,
            "metric_name": metric_name,
            "assistor_username_list": assistors,   
            "task_description": task_description
        }
        find_assistor_response = cls._post_request_chaining(
            token=token,
            data=data,
            url_prefix=cls.__url_prefix,
            url_root='find_assistor',
            url_suffix=user_id
        )

        cls._store_database_record(
            database_type='train_sponsor_metadata',
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
        
        cls._store_database_record(
            database_type='train_algorithm',
            user_id=user_id, 
            train_id=train_id, 
            algorithm_data_name='encrypted_identifer',
            algorithm_data=encrypted_identifer
        )

        # Record the history to log file
        msgs = [
            "You are SPONSOR", 
            f"Train ID: {train_id}", 
            "---- Train Stage Starts",
            "---- 1. Find assistor", 
            "1.1 Sponsor calls for help", 
            "1.2 Sponsor sends id file"
        ]
        cls._store_log(
            user_id=user_id,
            task_id=train_id,
            msgs=msgs
        )

        print('Training train_id: ', train_id)
        print('Sponsor: Training train_id: ', train_id, ' is running')
        return ('handleTrainRequest successfully', train_id)