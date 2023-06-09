from __future__ import annotations

import collections

from workflow.train_workflow.train_base import TrainBaseWorkflow

from pi.api import get_user_id

from typing import Any

from typeguard import typechecked


#@typechecked
class TrainSponsorMatchIdentifier(TrainBaseWorkflow):
    '''
    Handle sponsor match identifier stage.

    Methods
    -------
    train_sponsor_match_identifier
    '''

    @classmethod
    def train_sponsor_match_identifier(
        cls, train_id: str, train_id_dict: dict[str, Any]
    ) -> None:
        ''' 
        Execute sponsor match identifier logic.

        Parameters
        ----------
        train_id: str 
        train_id_dict : dict[str, Any]

        Returns
        -------
        None
        '''
        user_id = get_user_id()

        msgs = [
            "---- 3. Unread Match ID", 
            "3.1 Update the match id notification",
            "3.2 unread_match_identifier_sponsor",
        ]
        super()._store_log(
            user_id=user_id,
            task_id=train_id,
            msgs=msgs
        )
        
        data = {
            "train_id": train_id,
        }
        get_identifier_content_response = super()._post_request_chaining(
            task_id=train_id,
            data=data,
            url_prefix=super()._url_prefix,
            url_root='get_identifier_content',
            url_suffix=user_id,
            status_code=200
        )

        msg = [
            "3.3 Sponsor gets matched id file"
        ]
        super()._store_log(
            user_id=user_id,
            task_id=train_id,
            msgs=msg
        )

        assistor_random_id_to_identifier_content_dict = get_identifier_content_response['assistor_random_id_to_identifier_content_dict']

        sponsor_encrypted_identifer = super()._get_database_record(
            database_type='train_algorithm',
            user_id=user_id, 
            train_id=train_id, 
            algorithm_data_name='sponsor_encrypted_identifer',
        )
        sponsor_matched_identifers = collections.defaultdict(list)
        for assistor_random_id, assistor_encrypted_identifer in assistor_random_id_to_identifier_content_dict.items():
            # msg = ["3.4 Sponsor Saved Matched id File at " + save_match_id_file_pos[2]]
            # super()._store_log(
            #     user_id=user_id,
            #     task_id=train_id,
            #     msgs=msg
            # )
            
            sponsor_matched_identifer = super()._match_identifier(
                self_id_data=sponsor_encrypted_identifer,
                from_id_data=assistor_encrypted_identifer
            )

            sponsor_matched_identifers[assistor_random_id] = sponsor_matched_identifer

        super()._store_database_record(
            database_type='train_algorithm',
            user_id=user_id,
            train_id=train_id,
            algorithm_data_name='sponsor_matched_identifers',
            algorithm_data=sponsor_matched_identifers
        )

        # assert make_match_idx_done is not None
        # _, make_match_idx_done = handle_Algorithm_return_value("make_match_idx_done", make_match_idx_done, "200", "make_match_idx")
        # assert make_match_idx_done is not None

        msgs = [
            "3.5 Sponsor matches id to index"
        ]
        super()._store_log(
            user_id=user_id,
            task_id=train_id,
            msgs=msgs
        )

        # get the metadata of this task that stored before
        # get train target column
        sponsor_metadata_record = super()._get_database_record(
            database_type='train_sponsor_metadata',
            user_id=user_id,
            train_id=train_id
        )
        train_id = sponsor_metadata_record[0]
        task_mode = sponsor_metadata_record[1]
        model_name = sponsor_metadata_record[2]
        metric_name = sponsor_metadata_record[3]
        train_file_path = sponsor_metadata_record[4]
        train_id_column = sponsor_metadata_record[5]
        train_data_column = sponsor_metadata_record[6]
        train_target_column = sponsor_metadata_record[7]
        task_name = sponsor_metadata_record[8]
        task_description = sponsor_metadata_record[9]
        
        # print("train_file_path", train_file_path, train_target_column)

        # call make residual
        sponsor_trained_result, residual_dict = super()._calculate_residual(
            round=cls._initial_round_num, 
            dataset_path=train_file_path, 
            target_idx=train_target_column, 
            skip_header=super()._skip_header, 
            task_mode=task_mode, 
            metric_name=metric_name,
            sponsor_matched_identifers=sponsor_matched_identifers,
            last_round_result=None,
        )
        # print('~~sponsor_trained_result', sponsor_trained_result, len(sponsor_trained_result))
        super()._store_database_record(
            database_type='train_algorithm',
            user_id=user_id,
            train_id=train_id,
            algorithm_data_name=['sponsor_trained_result', 'rounds_0'],
            algorithm_data=sponsor_trained_result
        )

        super()._store_database_record(
            database_type='train_algorithm',
            user_id=user_id,
            train_id=train_id,
            algorithm_data_name='residual_dict',
            algorithm_data=residual_dict
        )

        msg = [
            "3.6 Sponsor makes residual finished"
        ]
        super()._store_log(
            user_id=user_id,
            task_id=train_id,
            msgs=msg
        )

        assistor_random_id_to_residual_dict = {}
        for assistor_random_id in assistor_random_id_to_identifier_content_dict.keys():
            assistor_random_id_to_residual_dict[assistor_random_id] = residual_dict[assistor_random_id]
            # print('8989000', residual_dict[assistor_random_id])

        data = {
            "train_id": train_id,
            "assistor_random_id_to_residual_dict": assistor_random_id_to_residual_dict
        }
        send_situation_response = super()._post_request_chaining(
            task_id=train_id,
            data=data,
            url_prefix=super()._url_prefix,
            url_root='send_situation',
            url_suffix=user_id,
            status_code=200
        )

        msg = [
            "3.7 Sponsor sends all situations", 
            "---- 3. Unread Match ID Done"
        ]
        super()._store_log(
            user_id=user_id,
            task_id=train_id,
            msgs=msg
        )
        print('Sponsor: Training train_id: ', train_id, ' is running')
        print('Sponsor stage 2: match id done')
        return True
