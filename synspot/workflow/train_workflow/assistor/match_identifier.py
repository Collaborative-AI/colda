from __future__ import annotations

import requests

from synspot.workflow.base import BaseWorkflow

from synspot.utils import(
    log_helper,
    ParseJson
)


class TrainAssistorMatchIdentifier(BaseWorkflow):

    @classmethod
    def train_assistor_match_identifier(cls, train_id, train_id_dict):
        # initiate a request

        user_id, root, token = cls._get_important_information()
        url = cls._process_url(prefix='main_flow', url="/get_identifier_content", suffix=user_id)

        data = {
            "train_id": train_id,
        }
        get_identifier_content_response = cls._post_request(
            url=url,
            token=token,
            request_name='get_identifier_content',
            data=data
        )

        assistor_get_match_id_file_res = load_json_data(json_data=assistor_get_match_id_file_res, json_data_name='assistor_get_match_id_file_res', 
                                                            testing_key_value_pair=[('sponsor_random_id_to_identifier_content_dict', None)])

        msg = ["3.3 Assistor gets matched id file\n"]
        log_helper(msg, root, user_id, train_id)

        # handle the response from request, assistor only has one match_id_file. 
        sponsor_random_id_to_identifier_content_dict = load_json_data(assistor_get_match_id_file_res['sponsor_random_id_to_identifier_content_dict'])

        # get the first key of sponsor_random_id_to_identifier_content_dict
        sponsor_random_id = next(iter(sponsor_random_id_to_identifier_content_dict))
        sponsor_identifier_data = sponsor_random_id_to_identifier_content_dict[sponsor_random_id]
        # call save_match_id to get the designated position to save the match_id file
        # save_match_id_file_pos = save_match_id(root=root, self_id=user_id, train_id=train_id, mode=self.test_indicator, test_id=None, from_id=sponsor_random_id)
        # # assert save_match_id_file_pos is not None
        # _, save_match_id_file_pos = handle_Algorithm_return_value("save_match_id_file_pos", save_match_id_file_pos,
                                                                # "200", "save_match_id")
        # assert save_match_id_file_pos is not None

        # save match id file to designated position
        # save_file(save_match_id_file_pos[2], identifier_content)

        # msg = ["3.4 Assistor Saved Matched id File at " + save_match_id_file_pos[2] + "\n"]
        # log_helper(msg, root, user_id, train_id)
        
        assistor_identifier_data = cls.__TrainAlgorithmDatabase_instance.get_record(
            user_id=user_id, 
            train_id=train_id, 
            algorithm_data_name='hash_id_file_data',
        )

        # call make_match_idx
        matching_identifer = cls.__TrainAlgorithm_instance.make_match_idx(
            self_id_data=sponsor_identifier_data,
            from_id_data=assistor_identifier_data
        )

        cls.__TrainAlgorithmDatabase_instance.store_record(
            user_id=user_id,
            train_id=train_id,
            algorithm_data_name='assistor_matching_identifer',
            algorithm_data=matching_identifer
        )
        # make_match_idx_done = make_match_idx(root=root, self_id=user_id, train_id=train_id, mode=self.test_indicator, test_id=None, from_id=sponsor_random_id)
        # # assert make_match_idx_done is not None
        # _, make_match_idx_done = handle_Algorithm_return_value("make_match_idx_done", make_match_idx_done, "200", "make_match_idx")
        # # assert make_match_idx_done is not None

        msg = ["3.5 Assistor matches id to index\n", "---- 3. Unread Match ID Done\n"]
        log_helper(msg, root, user_id, train_id)

        print('Assistor: Training train_id: ', train_id, ' is running')
        return 'unread_match_identifier_assistor successfully'
    pass
