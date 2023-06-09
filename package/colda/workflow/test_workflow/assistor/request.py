from __future__ import annotations

from workflow.test_workflow.test_base import TestBaseWorkflow

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
class TestAssistorRequest(TestBaseWorkflow):
    '''
    Handle test assistor request stage.

    Methods
    -------
    test_assistor_request
    '''
    @classmethod
    def test_assistor_request(
        cls, 
        test_id: str, 
        test_id_dict: dict[str, Any]
    ) -> None:
        ''' 
        Execute test assistor request logic.

        Parameters
        ----------
        test_id: str 
        test_id_dict : dict[str, Any]

        Returns
        -------
        None
        '''
        default_mode = get_default_mode()
        user_id = get_user_id()

        _, _, _, train_id = obtain_notification_information(
            notification_dict=test_id_dict,
            test_indicator='test'
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
                f"Test ID: {test_id}", 
                "---- 2. Unread Test Request", 
                "Test 2.1: Update the request notification"
            ]
            super()._store_log(
                user_id=user_id,
                task_id=test_id,
                msgs=msgs
            )
            
            data = {
                "train_id": train_id,
                "test_id": test_id,
                "identifier_content": assistor_encrypted_identifier
            }
            match_test_identifier_content_response = super()._post_request_chaining(
                task_id=test_id,
                data=data,
                url_prefix=super()._url_prefix,
                url_root='match_test_identifier_content',
                url_suffix=user_id,
                status_code=200
            )

            super()._store_database_record(
                database_type='test_assistor_metadata',
                user_id=user_id, 
                train_id=train_id, 
                mode=default_mode, 
                task_mode=default_task_mode, 
                model_name=default_model_name, 
                test_id=test_id,
                test_file_path=default_file_path, 
                test_id_column=default_id_column, 
                test_data_column=default_data_column, 
                test_name=None, 
                test_description=None,   
            )

            super()._store_database_record(
                database_type='test_algorithm',
                user_id=user_id, 
                test_id=test_id, 
                algorithm_data_name='assistor_encrypted_identifier',
                algorithm_data=assistor_encrypted_identifier
            )

            # add log
            msgs = [
                "Test 2.2: assistor uploads id file", 
                "---- Test 2: Unread Test Request Done"
            ]
            super()._store_log(
                user_id=user_id,
                task_id=test_id,
                msgs=msgs
            )

        elif default_mode == "manual":
            pass
        else:
            print('unread test request: wrong mode')

        print(f'Assistor: Testing test_id: {test_id} is running')
        print('Sponsor test stage 1: request done')
        return True
