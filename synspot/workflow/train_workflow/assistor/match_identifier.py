from __future__ import annotations

import requests

from synspot.workflow.train_base import TrainBaseWorkflow

from synspot.utils import(
    ParseJson
)

from typing import Any


class TrainAssistorMatchIdentifier(TrainBaseWorkflow):

    @classmethod
    def train_assistor_match_identifier(
        cls, train_id: str, train_id_dict: dict[str, Any]
    ) -> None:
        # initiate a request

        msgs = [
            "---- 3. Unread Match ID", 
            "3.1 Update the match id notification",
            "3.2 unread_match_identifier_assistor",
        ]
        cls._store_log(
            user_id=user_id,
            task_id=train_id,
            msgs=msgs
        )

        user_id, root, token = cls._get_important_information()
        
        data = {
            "train_id": train_id,
        }
        get_identifier_content_response = cls._post_request_chaining(
            task_id=train_id,
            data=data,
            url_prefix=cls._url_prefix,
            url_root='get_identifier_content',
            url_suffix=user_id,
            status_code=200
        )
        
        msgs = ["3.3 Assistor gets matched id file"]
        cls._store_log(
            user_id=user_id,
            task_id=train_id,
            msgs=msgs
        )
        
        # handle the response from request, assistor only has one match_id_file. 
        sponsor_random_id_to_identifier_content_dict = get_identifier_content_response['sponsor_random_id_to_identifier_content_dict']

        # get the first key of sponsor_random_id_to_identifier_content_dict
        sponsor_random_id = next(iter(sponsor_random_id_to_identifier_content_dict))
        sponsor_identifier_data = sponsor_random_id_to_identifier_content_dict[sponsor_random_id]
        
        assistor_identifier_data = cls._get_database_record(
            database_type='train_algorithm',
            user_id=user_id, 
            train_id=train_id, 
            algorithm_data_name='encrypted_identifer',
        )

        assistor_matched_identifer = cls._match_identifier(
            self_id_data=sponsor_identifier_data,
            from_id_data=assistor_identifier_data
        )

        cls._store_database_record(
            database_type='train_algorithm',
            user_id=user_id,
            train_id=train_id,
            algorithm_data_name='assistor_matched_identifer',
            algorithm_data=assistor_matched_identifer
        )

        # make_match_idx_done = make_match_idx(root=root, self_id=user_id, train_id=train_id, mode=self.test_indicator, test_id=None, from_id=sponsor_random_id)
        # # assert make_match_idx_done is not None
        # _, make_match_idx_done = handle_Algorithm_return_value("make_match_idx_done", make_match_idx_done, "200", "make_match_idx")
        # # assert make_match_idx_done is not None

        msgs = [
            "3.5 Assistor matches id to index", 
            "---- 3. Unread Match ID Done"
        ]
        cls._store_log(
            user_id=user_id,
            task_id=train_id,
            msgs=msgs
        )

        print('Assistor: Training train_id: ', train_id, ' is running')
        return True
    
