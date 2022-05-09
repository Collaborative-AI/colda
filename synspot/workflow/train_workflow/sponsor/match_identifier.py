from __future__ import annotations

import json
import requests
import collections
from synspot import database

from synspot.workflow.train_base import TrainBaseWorkflow

from synspot.utils import(
    ParseJson
)

from typing import Any


class TrainSponsorMatchIdentifier(TrainBaseWorkflow):

    @classmethod
    def train_sponsor_match_identifier(
            cls, train_id: str, train_id_dict: dict[str, Any]
        ) -> None:
        print('train_sponsor_match_identifier')
        user_id = super()._get_user_id()

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
            url_prefix=cls._url_prefix,
            url_root='get_identifier_content',
            url_suffix=user_id,
            status_code=200
        )

        msg = [
            "3.3 Sponsor gets matched id file \n"
        ]
        super()._store_log(
            user_id=user_id,
            task_id=train_id,
            msgs=msg
        )

        assistor_random_id_to_identifier_content_dict = get_identifier_content_response['assistor_random_id_to_identifier_content_dict']

        sponsor_matched_identifers = collections.defaultdict(list)
        for assistor_random_id, identifier_content in assistor_random_id_to_identifier_content_dict.items():
            assistor_identifier_data = ParseJson.load_json_recursion(identifier_content)

            # msg = ["3.4 Sponsor Saved Matched id File at " + save_match_id_file_pos[2]]
            # super()._store_log(
            #     user_id=user_id,
            #     task_id=train_id,
            #     msgs=msg
            # )
            
            sponsor_identifier_data = super()._get_database_record(
                database_type='train_algorithm',
                user_id=user_id, 
                train_id=train_id, 
                algorithm_data_name='encrypted_identifer',
            )

            sponsor_matched_identifer = super()._match_identifier(
                self_id_data=sponsor_identifier_data,
                from_id_data=assistor_identifier_data
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
        task_mode = sponsor_metadata_record[0]
        model_name = sponsor_metadata_record[1]
        metric_name = sponsor_metadata_record[2]
        train_file_path = sponsor_metadata_record[3]
        train_id_column = sponsor_metadata_record[4]
        train_data_column = sponsor_metadata_record[5]
        train_target_column = sponsor_metadata_record[6]
        task_name = sponsor_metadata_record[7]
        task_description = sponsor_metadata_record[8]
        
        print("train_file_path", train_file_path, train_target_column)

        # call make residual
        sponsor_result, sponsor_residual = super()._calculate_residual(
            self_id=user_id, 
            train_id=train_id, 
            round=cls._initial_round_num, 
            dataset_path=train_file_path, 
            target_idx=train_target_column, 
            skip_header=cls._skip_header, 
            task_mode=task_mode, 
            metric_name=metric_name,
            last_round_result=None,
        )

        super()._store_database_record(
            database_type='train_algorithm',
            user_id=user_id,
            train_id=train_id,
            algorithm_data_name='sponsor_result',
            algorithm_data=sponsor_result
        )

        super()._store_database_record(
            database_type='train_algorithm',
            user_id=user_id,
            train_id=train_id,
            algorithm_data_name='sponsor_residual',
            algorithm_data=sponsor_residual
        )

        msg = [
            "3.6 Sponsor makes residual finished"
        ]
        super()._store_log(
            user_id=user_id,
            task_id=train_id,
            msgs=msg
        )

        # residual_paths = make_residual_multiple_paths[2].split("?")
        assistor_random_id_to_residual_dict = {}
        for assistor_random_id in assistor_random_id_to_identifier_content_dict.keys():
            assistor_random_id_to_residual_dict[assistor_random_id] = sponsor_residual

        data = {
            "train_id": train_id,
            "assistor_random_id_to_residual_dict": assistor_random_id_to_residual_dict
        }
        send_situation_response = super()._post_request_chaining(
            task_id=train_id,
            data=data,
            url_prefix=cls._url_prefix,
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
        print('sponsor_match_id_done')
        print('Sponsor: Training train_id: ', train_id, ' is running')
        return True
