from __future__ import annotations

from colda.workflow.test_workflow.test_base import TestBaseWorkflow

from colda.pi.api import get_user_id

from typing import Union

from typeguard import typechecked


#@typechecked
class TestSponsorFindAssistor(TestBaseWorkflow):
    '''
    Handle test sponsor find assistor.

    Attributes
    ----------
    None

    Methods
    -------
    find_test_assistor
    '''

    @classmethod
    def __get_test_id(cls) -> str:
        ''' 
        Get new test id for this test task.

        Parameters
        ----------
        None

        Returns
        -------
        str
        '''
        create_new_test_task_response = super()._get_request_chaining(
            task_id=None,
            url_prefix=super()._url_prefix,
            url_root='create_new_test_task',
            url_suffix=None,
            status_code=200
        )
        new_test_id = create_new_test_task_response["test_id"]
        return new_test_id

    @classmethod
    def find_test_assistor(
        cls, 
        train_id: str,
        test_file_path: str, 
        test_id_column: str, 
        test_data_column: str, 
        test_target_column: str, 
        test_name: Union[str, None], 
        test_description: Union[str, None]
    ) -> str:
        ''' 
        Execute test sponsor find assistor logic.

        Parameters
        ----------
        train_id : str
        test_file_path : str
        test_id_column : str 
        test_data_column : str
        test_target_column : str
        test_name : Union[str, None]
        test_description : Union[str, None]

        Returns
        -------
        None
        '''
        test_id = cls.__get_test_id()
        user_id = get_user_id()
        
        # Retrieve data of train_id
        sponsor_metadata_record = super()._get_database_record(
            database_type='train_sponsor_metadata',
            user_id=user_id,
            train_id=train_id
        )
        task_mode = sponsor_metadata_record[1]
        model_name = sponsor_metadata_record[2]
        metric_name = sponsor_metadata_record[3]

        # call make_hash in Algorithm module
        sponsor_encrypted_identifer = super()._encrypt_identifier(
            dataset_path=test_file_path, 
            id_idx=test_id_column, 
            skip_header=super()._skip_header
        )        

        data = {
            "train_id": train_id,
            "task_mode": task_mode,
            "model_name": model_name,
            "metric_name": metric_name,
            "test_id": test_id,
            "test_name": test_name,   
            "test_description": test_description,
            "identifier_content": sponsor_encrypted_identifer
        }
        find_test_assistor_response = super()._post_request_chaining(
            task_id=test_id,
            data=data,
            url_prefix=super()._url_prefix,
            url_root='find_test_assistor',
            url_suffix=user_id,
            status_code=200
        )

        super()._store_database_record(
            database_type='test_sponsor_metadata',
            user_id=user_id, 
            train_id=train_id, 
            task_mode=task_mode, 
            model_name=model_name, 
            metric_name=metric_name,
            test_id=test_id,
            test_file_path=test_file_path, 
            test_id_column=test_id_column, 
            test_data_column=test_data_column,
            test_target_column=test_target_column,
            test_name=test_name, 
            test_description=test_description, 
        )
        
        super()._store_database_record(
            database_type='test_algorithm',
            user_id=user_id, 
            test_id=test_id, 
            algorithm_data_name='sponsor_encrypted_identifer',
            algorithm_data=sponsor_encrypted_identifer
        )

        # Record the history to log file
        msgs = [
            "You are SPONSOR", 
            f"Test ID: {test_id}", 
            "---- Test Stage Starts",
            "---- Test 1: Find assistor", 
            "Test 1.1: Sponsor calls for help", 
            "Test 1.2: Sponsor sends id file"
        ]
        super()._store_log(
            user_id=user_id,
            task_id=test_id,
            msgs=msgs
        )

        print('Testing test_id: ', test_id)
        print('Sponsor: Testing test_id: ', test_id, ' is running')
        print('Sponsor test stage 1: find assistor done')
        return test_id