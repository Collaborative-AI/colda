from __future__ import annotations
from cgi import test

import collections

from workflow.test_workflow.test_base import TestBaseWorkflow

from pi.api import get_user_id

from workflow.utils import (
    obtain_notification_information
)

from typing import Any

from typeguard import typechecked


#@typechecked
class TestSponsorMatchIdentifier(TestBaseWorkflow):
    '''
    Handle test sponsor match identifier stage.

    Methods
    -------
    test_sponsor_match_identifier
    '''

    @classmethod
    def test_sponsor_match_identifier(
        cls, 
        test_id: str, 
        test_id_dict: dict[str, Any]
    ) -> None:
        ''' 
        Execute test sponsor match identifier logic.

        Parameters
        ----------
        test_id : str 
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
            "---- Test 3: Unread Match ID", 
            "Test 3.1: Update the match id notification",
            "Test 3.2: unread_test_match_identifier_sponsor",
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

        msg = [
            "Test 3.3: Sponsor gets matched id file"
        ]
        super()._store_log(
            user_id=user_id,
            task_id=test_id,
            msgs=msg
        )

        assistor_random_id_to_identifier_content_dict = get_test_identifier_content_response['assistor_random_id_to_identifier_content_dict']

        sponsor_encrypted_identifer = super()._get_database_record(
            database_type='test_algorithm',
            user_id=user_id, 
            test_id=test_id, 
            algorithm_data_name='sponsor_encrypted_identifer',
        )

        sponsor_matched_identifers = collections.defaultdict(list)
        for assistor_random_id, assistor_encrypted_identifer in assistor_random_id_to_identifier_content_dict.items():
            
            sponsor_matched_identifer = super()._match_identifier(
                self_id_data=sponsor_encrypted_identifer,
                from_id_data=assistor_encrypted_identifer
            )

            sponsor_matched_identifers[assistor_random_id] = sponsor_matched_identifer

        super()._store_database_record(
            database_type='test_algorithm',
            user_id=user_id,
            test_id=test_id,
            algorithm_data_name='sponsor_matched_identifers',
            algorithm_data=sponsor_matched_identifers
        )

        cls.test_cooperative_model(
            user_id=user_id,
            test_id=test_id,
            sponsor_matched_identifers=sponsor_matched_identifers
        )
    
    @classmethod
    def test_cooperative_model(
        cls, 
        user_id: str,
        test_id: str,
        sponsor_matched_identifers: dict[str, Any],
    ) -> None:
        ''' 
        In test stage, we dont need to wait the training 
        model output sent by the assistors.
        We test the trained model using test dataset directly

        Parameters
        ----------
        user_id : str
        test_id : str
        sponsor_matched_identifers : dict[str]

        Returns
        -------
        None
        '''
        sponsor_metadata_record = super()._get_database_record(
            database_type='test_sponsor_metadata',
            user_id=user_id,
            test_id=test_id
        )
        train_id = sponsor_metadata_record[0]
        task_mode = sponsor_metadata_record[1]
        model_name = sponsor_metadata_record[2]
        metric_name = sponsor_metadata_record[3]
        test_id = sponsor_metadata_record[4]
        test_file_path = sponsor_metadata_record[5]
        test_id_column = sponsor_metadata_record[6]
        test_data_column = sponsor_metadata_record[7]
        test_target_column = sponsor_metadata_record[8]
        test_name = sponsor_metadata_record[9]
        test_description = sponsor_metadata_record[10]

        trained_models_of_each_round = super()._get_database_record(
            database_type='train_algorithm',
            user_id=user_id,
            train_id=train_id,
            algorithm_data_name='trained_cooperative_model',
        )

        data = {
            'train_id': train_id
        }
        max_round = super()._post_request_chaining(
            task_id=train_id,
            data=data,
            url_prefix=super()._url_prefix,
            url_root='get_max_round',
        )['max_round'] 

        test_cooperative_model_outputs = super()._test_cooperative_model(
            user_id=user_id,
            test_id=test_id,
            max_round=max_round,
            matched_identifier=sponsor_matched_identifers,
            trained_models_of_each_round=trained_models_of_each_round,
            dataset_path=test_file_path, 
            data_idx=test_data_column,
            skip_header=super()._skip_header,
            role='sponsor',
        )

        sponsor_metadata_record = super()._store_database_record(
            database_type='test_algorithm',
            user_id=user_id,
            test_id=test_id,
            algorithm_data_name='test_cooperative_model_outputs',
            algorithm_data=test_cooperative_model_outputs
        )

        msgs = [
            "Test 3.5: Sponsor matches id to index"
            "Test ---- 3. Unread Test Match ID Done"
        ]
        super()._store_log(
            user_id=user_id,
            task_id=test_id,
            msgs=msgs
        )

        print(f'Sponsor: Testing test_id: {test_id} is running')
        print('Sponsor test stage 2: match_id done')
        return True
