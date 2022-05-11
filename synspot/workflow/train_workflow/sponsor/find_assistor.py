from __future__ import annotations

from synspot.workflow.train_base import TrainBaseWorkflow


class TrainSponsorFindAssistor(TrainBaseWorkflow):

    @classmethod
    def __get_train_id(cls) -> str:
        
        """
        Get new Task id for this task

        :returns: new_train_id. String`. The new task id of new task

        :exception OSError: 
        """

        create_new_train_task_response = super()._get_request_chaining(
            task_id=None,
            url_prefix=super()._url_prefix,
            url_root='create_new_train_task',
            url_suffix=None,
            status_code=200
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
        user_id = super()._get_user_id()
        
        # call make_hash in Algorithm module
        sponsor_encrypted_identifer = super()._encrypt_identifier(
            dataset_path=train_file_path, 
            id_idx=train_id_column, 
            skip_header=super()._skip_header
        )        

        data = {
            "identifier_content": sponsor_encrypted_identifer,
            "train_id": train_id,
            "task_mode": task_mode,
            "model_name": model_name,
            "metric_name": metric_name,
            "assistor_username_list": assistors,
            "task_name": task_name,   
            "task_description": task_description
        }

        find_assistor_response = super()._post_request_chaining(
            task_id=train_id,
            data=data,
            url_prefix=super()._url_prefix,
            url_root='find_assistor',
            url_suffix=user_id,
            status_code=200
        )

        super()._store_database_record(
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
        
        super()._store_database_record(
            database_type='train_algorithm',
            user_id=user_id, 
            train_id=train_id, 
            algorithm_data_name='sponsor_encrypted_identifer',
            algorithm_data=sponsor_encrypted_identifer
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
        super()._store_log(
            user_id=user_id,
            task_id=train_id,
            msgs=msgs
        )

        print('Training train_id: ', train_id)
        print('Sponsor: Training train_id: ', train_id, ' is running')
        return (True, train_id)