from __future__ import annotations

import time

from colda.workflow.test_workflow.test_base import TestBaseWorkflow

from colda.workflow.utils import (
    obtain_notification_information
)

from colda.pi.api import get_user_id

from typing import Any

from typeguard import typechecked


class TestSponsorOutput(TestBaseWorkflow):
    '''
    Handle test sponsor output stage.

    Methods
    -------
    test_sponsor_output
    '''

    @classmethod
    def test_sponsor_output(
        cls, 
        test_id: str, 
        test_id_dict: dict[str, Any]
    ) -> None:
        ''' 
        Execute test sponsor output logic.

        Parameters
        ----------
        test_id : str 
        test_id_dict : dict[str, Any]

        Returns
        -------
        None
        '''
        user_id = get_user_id()
        _, _, cur_rounds_num, train_id = obtain_notification_information(
            notification_dict=test_id_dict,
            test_indicator='test'
        )

        msgs = [
            "Test ---- 5. Unread Output", 
            "Test 5.1: Update the output notification"
        ]
        super()._store_log(
            user_id=user_id,
            task_id=test_id,
            msgs=msgs
        )

        data = {
            "train_id": train_id,
            "test_id": test_id
        }
        get_test_output_content_response = super()._post_request_chaining(
            task_id=test_id,
            data=data,
            url_prefix=super()._url_prefix,
            url_root='get_test_output_content',
            url_suffix=user_id,
            status_code=200
        )

        msgs = ["Test 5.2: Sponsor gets output model"]
        super()._store_log(
            user_id=user_id,
            task_id=test_id,
            msgs=msgs
        )

        assistor_random_id_to_output_content_dict = get_test_output_content_response['assistor_random_id_to_output_content_dict']
        
        if super()._async_checker(
            database_type='test_algorithm', 
            user_id=user_id, 
            task_id=test_id,
            algorithm_data_name='test_cooperative_model_outputs',
            stage='test',
            waiting_start_time=time.time()
        ) == False:
            return
        
        cls.evaluation(
            user_id=user_id,
            test_id=test_id, 
            rounds=cur_rounds_num,
            assistor_random_id_to_output_content_dict=assistor_random_id_to_output_content_dict
        )
        
        return

    @classmethod
    def evaluation(
        cls, 
        user_id: str,
        test_id: str, 
        rounds: int, 
        assistor_random_id_to_output_content_dict: dict[str, Any]
    ) -> None:
        ''' 
        Function to avoid async case.
        When sponsor gets the test output content sent
        by assistors, the sponsor may not complete its
        own testing model step. We need to wait till it
        complete.

        Parameters
        ----------
        user_id : str
        test_id : str 
        rounds : int
        assistor_random_id_to_output_content_dict : dict[str, Any]

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

        test_cooperative_model_outputs = super()._get_database_record(
            database_type='test_algorithm',
            user_id=user_id,
            test_id=test_id,
            algorithm_data_name='test_cooperative_model_outputs',
        )

        sponsor_matched_identifers = super()._get_database_record(
            database_type='test_algorithm',
            user_id=user_id,
            test_id=test_id,
            algorithm_data_name='sponsor_matched_identifers',
        )

        trained_result_rounds_0 = super()._get_database_record(
            database_type='train_algorithm',
            user_id=user_id,
            train_id=train_id,
            algorithm_data_name=['sponsor_trained_result', 'rounds_0'],
        )

        sponsor_trained_alpha = super()._get_database_record(
            database_type='train_algorithm',
            user_id=user_id,
            train_id=train_id,
            algorithm_data_name='sponsor_trained_alpha',
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

        # Calculate result for current round
        # print('&&%%%%', type(assistor_random_id_to_output_content_dict))
        evaluation = super()._evaluate_results(
            user_id=user_id,
            test_id=test_id,
            max_round=max_round, 
            dataset_path=test_file_path, 
            target_idx=test_target_column, 
            skip_header=super()._skip_header, 
            task_mode=task_mode, 
            metric_name=metric_name,
            sponsor_test_cooperative_model_output_every_round=test_cooperative_model_outputs,
            assistor_test_cooperative_model_output_every_round=assistor_random_id_to_output_content_dict,
            trained_result_rounds_0=trained_result_rounds_0,
            trained_alpha_every_round=sponsor_trained_alpha,
            matched_identifier=sponsor_matched_identifers,
            role='sponsor'
        )
    
        super()._store_database_record(
            database_type='test_algorithm',
            user_id=user_id,
            test_id=test_id,
            algorithm_data_name='evaluation',
            algorithm_data=evaluation
        )

        msgs = [
            'Test 5.4: Sponsor makes eval done',
            f'Test of {test_id} done'
        ]
        super()._store_log(
            user_id=user_id,
            task_id=test_id,
            msgs=msgs
        )

        print('Sponsor test stage 3: output done')
        return 

        
