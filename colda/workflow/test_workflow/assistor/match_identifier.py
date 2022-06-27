from __future__ import annotations

from colda.workflow.test_workflow.test_base import TestBaseWorkflow

from colda.workflow.utils import (
    obtain_notification_information
)

from colda.pi.api import get_user_id

from typing import Any

from typeguard import typechecked


#@typechecked
class TestAssistorMatchIdentifier(TestBaseWorkflow):
    '''
    Handle test assistor match identifier stage.

    Attributes
    ----------
    None

    Methods
    -------
    test_assistor_match_identifier
    '''

    @classmethod
    def test_assistor_match_identifier(
        cls, 
        test_id: str, 
        test_id_dict: dict[str, Any]
    ) -> None:
        ''' 
        Execute train assistor match identifier logic.

        Parameters
        ----------
        test_id: str 
        test_id_dict : dict[str, Any]

        Returns
        -------
        None
        '''
        user_id = get_user_id()
        _, _, _, train_id = obtain_notification_information(
            notification_dict=test_id_dict,
            test_indicator='test'
        )

        msgs = [
            "Test: ---- 3. Unread Match ID", 
            "Test 3.1: Update the match id notification",
            "Test 3.2: unread_match_identifier_assistor",
        ]
        super()._store_log(
            user_id=user_id,
            task_id=test_id,
            msgs=msgs
        )

        data = {
            "train_id": train_id,
            "test_id": test_id,
        }
        get_test_identifier_content_response = super()._post_request_chaining(
            task_id=test_id,
            data=data,
            url_prefix=super()._url_prefix,
            url_root='get_test_identifier_content',
            url_suffix=user_id,
            status_code=200
        )
        
        msgs = ["Test 3.3: Assistor gets matched id file"]
        super()._store_log(
            user_id=user_id,
            task_id=test_id,
            msgs=msgs
        )
        
        # handle the response from request, assistor only has one match_id_file. 
        sponsor_random_id_to_identifier_content_dict = get_test_identifier_content_response['sponsor_random_id_to_identifier_content_dict']

        # get the first key of sponsor_random_id_to_identifier_content_dict
        sponsor_random_id = next(iter(sponsor_random_id_to_identifier_content_dict))
        sponsor_encrypted_identifier = sponsor_random_id_to_identifier_content_dict[sponsor_random_id]
        
        assistor_encrypted_identifier = super()._get_database_record(
            database_type='test_algorithm',
            user_id=user_id, 
            test_id=test_id, 
            algorithm_data_name='assistor_encrypted_identifier',
        )

        # print('assistor_encrypted_identifier', assistor_encrypted_identifier)
        assistor_matched_identifer = super()._match_identifier(
            self_id_data=assistor_encrypted_identifier,
            from_id_data=sponsor_encrypted_identifier
        )

        super()._store_database_record(
            database_type='test_algorithm',
            user_id=user_id,
            test_id=test_id,
            algorithm_data_name='assistor_matched_identifer',
            algorithm_data=assistor_matched_identifer
        )

        return cls.test_cooperative_model(
            user_id=user_id,
            train_id=train_id,
            test_id=test_id,
            assistor_matched_identifer=assistor_matched_identifer
        )

    @classmethod
    def test_cooperative_model(
        cls,
        user_id: str,
        train_id: str,
        test_id: str,
        assistor_matched_identifer: dict[str]
    ) -> None:
        ''' 
        In test stage, we dont need to wait the training 
        target sent by the sponsor.
        We test the trained model using test dataset directly

        Parameters
        ----------
        user_id : str
        train_id : str
        test_id : str
        assistor_matched_identifer : dict[str]

        Returns
        -------
        None
        '''
        test_assistor_metadata = super()._get_database_record(
            database_type='test_assistor_metadata',
            user_id=user_id,
            test_id=test_id
        )
        print('@@@_______', test_assistor_metadata)
        train_id = test_assistor_metadata[0]
        mode = test_assistor_metadata[1]
        task_mode = test_assistor_metadata[2] 
        model_name = test_assistor_metadata[3] 
        test_id = test_assistor_metadata[4]
        test_file_path = test_assistor_metadata[5] 
        test_id_column = test_assistor_metadata[6] 
        test_data_column = test_assistor_metadata[7]
        test_name = test_assistor_metadata[8] 
        test_description = test_assistor_metadata[9]

        trained_models_of_each_round = super()._get_database_record(
            database_type='train_algorithm',
            user_id=user_id,
            train_id=train_id,
            algorithm_data_name='trained_cooperative_model',
        )

        test_cooperative_model_outputs = super()._test_cooperative_model(
            user_id=user_id,
            test_id=test_id,
            max_round=super()._max_round,
            matched_identifier=assistor_matched_identifer,
            trained_models_of_each_round=trained_models_of_each_round,
            dataset_path=test_file_path, 
            data_idx=test_data_column, 
            skip_header=super()._skip_header,
            role='assistor',
        )

        data = {
            "train_id": train_id,
            "test_id": test_id,
            "output_content": test_cooperative_model_outputs,
        }
        print('test_cooperative_model_outputs', test_cooperative_model_outputs, type(test_cooperative_model_outputs))
        send_test_output_response = super()._post_request_chaining(
            task_id=test_id,
            data=data,
            url_prefix=super()._url_prefix,
            url_root='send_test_output',
            url_suffix=user_id,
            status_code=200
        )

        msgs = [
            "Test 3.5: Assistor matches id to index", 
            "Test ---- 3. Unread Test Match ID Done"
        ]
        super()._store_log(
            user_id=user_id,
            task_id=test_id,
            msgs=msgs
        )

        print(f'Assistor: Testing test_id: {test_id} is running')
        return True
    
