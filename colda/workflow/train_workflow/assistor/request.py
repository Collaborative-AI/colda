from __future__ import annotations

from workflow.train_workflow.train_base import TrainBaseWorkflow

from workflow.utils import (
    obtain_notification_information
)

from pi.api import (
    get_user_id,
    get_default_mode
)

from typing import Any

from typeguard import typechecked


#@typechecked
class TrainAssistorRequest(TrainBaseWorkflow):
    '''
    Handle train assistor request stage.

    Methods
    -------
    train_assistor_request
    '''

    @classmethod
    def train_assistor_request(
        cls, train_id: str, train_id_dict: dict[str, Any]
    ) -> None:
        ''' 
        Execute train assistor request logic.

        Parameters
        ----------
        train_id: str 
        train_id_dict : dict[str, Any]

        Returns
        -------
        None
        '''
        default_mode = get_default_mode()
        user_id = get_user_id()

        sender_random_id, role, cur_rounds_num = obtain_notification_information(
            notification_dict=train_id_dict
        )
        
        if default_mode == "auto":

            default_record = super()._get_database_record(
                database_type='default_metadata',
                user_id=user_id
            )

            default_mode = default_record[0]
            default_task_mode = default_record[1]
            default_model_name = default_record[2]
            default_file_path = default_record[3]
            default_id_column = default_record[4]
            default_data_column = default_record[5]
            
            assistor_encrypted_identifier = super()._encrypt_identifier(
                dataset_path=default_file_path, 
                id_idx=default_id_column, 
                skip_header=super()._skip_header
            )
            # print('assistor_encrypted_identifier', assistor_encrypted_identifier)
            # add log
            msgs = [
                "You are Assistor", 
                f"Train ID: {train_id}", 
                "---- 2. Unread Request", 
                "2.1 Update the request notification"
            ]
            super()._store_log(
                user_id=user_id,
                task_id=train_id,
                msgs=msgs
            )
            
            data = {
                "train_id": train_id,
                "identifier_content": assistor_encrypted_identifier
            }
            match_identifier_content_response = super()._post_request_chaining(
                task_id=train_id,
                data=data,
                url_prefix=super()._url_prefix,
                url_root='match_identifier_content',
                url_suffix=user_id,
                status_code=200
            )

            super()._store_database_record(
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

            super()._store_database_record(
                database_type='train_algorithm',
                user_id=user_id, 
                train_id=train_id, 
                algorithm_data_name='assistor_encrypted_identifier',
                algorithm_data=assistor_encrypted_identifier
            )

            # add log
            msgs = [
                "2.2 assistor uploads id file", 
                "---- 2. Unread Request Done"
            ]
            super()._store_log(
                user_id=user_id,
                task_id=train_id,
                msgs=msgs
            )

        elif default_mode == "manual":
            pass
        else:
            print('unread request: wrong mode')
        print('Assistor: Training train_id: ', train_id, ' is running')
        print('Assistor stage 1: request done')
        return True
