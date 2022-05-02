from __future__ import annotations

import requests

from synspot.workflow.train_base import TrainBaseWorkflow

from synspot.workflow.utils import (
    obtain_notification_information
)

from typing import Any


class TrainAssistorRequest(TrainBaseWorkflow):

    @classmethod
    def train_assistor_request(
        cls, train_id: str, train_id_dict: dict[str, Any]
    ) -> None:

        default_mode = cls._get_default_mode()
        user_id, root, token = cls._get_important_information()
        print(f'Default_mode: {default_mode}')

        sender_random_id, role, cur_rounds_num = obtain_notification_information(notification_dict=train_id_dict)
        
        if default_mode == "auto":

            default_record = cls._get_database_record(
                database_type='default_metadata',
                user_id=user_id
            )

            default_mode = default_record[0]
            default_task_mode = default_record[1]
            default_model_name = default_record[2]
            default_file_path = default_record[3]
            default_id_column = default_record[4]
            default_data_column = default_record[5]
            
            encrypted_identifier = cls._encrypt_identifier(
                dataset_path=default_file_path, 
                id_idx=default_id_column, 
                skip_header=cls.__skip_header
            )

            # add log
            msgs = [
                "You are Assistor", 
                f"Train ID: {train_id}", 
                "---- 2. Unread Request", 
                "2.1 Update the request notification"
            ]
            cls._store_log(
                user_id=user_id,
                task_id=train_id,
                msgs=msgs
            )
            
            data = {
                "train_id": train_id,
                "identifier_content": encrypted_identifier
            }
            match_identifier_content_response = cls._post_request_chaining(
                token=token,
                data=data,
                url_prefix=cls.__url_prefix,
                url_root='match_identifier_content',
                url_suffix=user_id
            )

            cls._store_database_record(
                database_type='train_assistor_metadata',
                user_id=user_id, 
                train_id=train_id, 
                mode=default_mode, 
                task_mode=default_task_mode, 
                model_name=default_model_name, 
                train_file_path=default_file_path, 
                train_id_column=default_id_column, 
                train_data_column=default_data_column, 
                task_name=None, 
                task_description=None,   
            )

            cls._store_database_record(
                database_type='train_algorithm',
                user_id=user_id, 
                train_id=train_id, 
                algorithm_data_name='encrypted_identifier',
                algorithm_data=encrypted_identifier
            )

            # add log
            msgs = [
                "2.2 assistor uploads id file", 
                "---- 2. Unread Request Done"
            ]
            cls._store_log(
                user_id=user_id,
                task_id=train_id,
                msgs=msgs
            )

        elif default_mode == "manual":
            pass
        else:
            print('unread request: wrong mode')

        print('Assistor: Training train_id: ', train_id, ' is running')
        return 'unread_request successfully'
