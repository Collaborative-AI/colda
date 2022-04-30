from __future__ import annotations

import json
import requests

from synspot.workflow.base import BaseWorkflow

from synspot.utils import(
    log_helper,
    ParseJson
)

class TrainSponsorMatchIdentifier(BaseWorkflow):

    @classmethod
    def train_sponsor_match_identifier(cls, train_id, train_id_dict):

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

        # 验证
        sponsor_get_match_id_file_res = load_json_data(json_data=sponsor_get_match_id_file_res, json_data_name='sponsor_get_match_id_file_res', 
                                                            testing_key_value_pair=[('assistor_random_id_to_identifier_content_dict', None)])

        msg = [
            "3.3 Sponsor gets matched id file \n"
        ]
        log_helper(msg, root, user_id, train_id)

        assistor_random_id_to_identifier_content_dict = sponsor_get_match_id_file_res['assistor_random_id_to_identifier_content_dict']
        # match_id_file_list = load_json_data(sponsor_get_match_id_file_res["match_id_file"], 'sponsor_get_match_id_file_res["match_id_file"]')
        # print("match_id_file_list", match_id_file_list)
        # assistor_random_id_pair_list = load_json_data(sponsor_get_match_id_file_res["assistor_random_id_pair"], 'sponsor_get_match_id_file_res["assistor_random_id_pair"]')

        matching_identifers = []
        for assistor_random_id, identifier_content in assistor_random_id_to_identifier_content_dict.items():
            from_id = assistor_random_id
            # need to json load each item again to gain list
            assistor_identifier_data = ParseJson.load_json_recursion(identifier_content)
            # cur_match_id_file = "\n".join(cur_match_id_file)

            # call save_match_id
            # save_match_id_file_pos = save_match_id(root=root, self_id=user_id, train_id=train_id, mode=self.test_indicator, 
            #                                         test_id=None, from_id=from_id)
            # # assert save_match_id_file_pos is not None
            # _, save_match_id_file_pos = handle_Algorithm_return_value("save_match_id_file_pos", save_match_id_file_pos,
            #                                                        "200", "save_match_id")
            # # assert save_match_id_file_pos is not None

            # # write file
            # save_file(save_match_id_file_pos[2], cur_match_id_file)

            msg = ["3.4 Sponsor Saved Matched id File at " + save_match_id_file_pos[2] + "\n"]
            log_helper(msg, root, user_id, train_id)

            
            sponsor_identifier_data = cls.__TrainAlgorithmDatabase_instance.get_record(
                user_id=user_id, 
                train_id=train_id, 
                algorithm_data_name='hash_id_file_data',
            )

            # call make_match_idx to match identifier
            matching_identifer = cls.__TrainAlgorithm_instance.make_match_idx(
                self_id_data=sponsor_identifier_data,
                from_id_data=assistor_identifier_data
            )
            matching_identifers.append(matching_identifer)

        cls.__TrainAlgorithmDatabase_instance.store_record(
            user_id=user_id,
            train_id=train_id,
            algorithm_data_name='sponsor_matching_identifer',
            algorithm_data=matching_identifers
        )
        # assert make_match_idx_done is not None
        # _, make_match_idx_done = handle_Algorithm_return_value("make_match_idx_done", make_match_idx_done, "200", "make_match_idx")
        # assert make_match_idx_done is not None

        msg = [
            "3.5 Sponsor matches id to index \n"
        ]
        log_helper(msg, root, user_id, train_id)

        # get the metadata of this task that stored before
        # get train target column
        sponsor_metadata_record = cls.__TrainSponsorMetadataDatabase_instance.get_record(
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
        sponsor_residual = cls.__TrainAlgorithm_instance.make_residual(
            self_id=user_id, 
            train_id=train_id, 
            round=cls.__initial_round_num, 
            dataset_path=train_file_path, 
            target_idx=train_target_column, 
            skip_header=cls.__skip_header, 
            task_mode=task_mode, 
            metric_name=metric_name,
            last_round_result=None,
        )
        # make_residual_multiple_paths = make_residual()
        # assert make_residual_multiple_paths is not None
        # _, make_residual_multiple_paths = handle_Algorithm_return_value("make_residual_multiple_paths", make_residual_multiple_paths, "200", "make_residual")
        # assert make_residual_multiple_paths is not None

        msg = [
            "3.6 Sponsor makes residual finished \n"
        ]
        log_helper(msg, root, user_id, train_id)

        # residual_paths = make_residual_multiple_paths[2].split("?")
        assistor_random_id_to_residual_dict = {}
        for assistor_random_id in assistor_random_id_to_identifier_content_dict.keys():
            assistor_random_id_to_residual_dict[assistor_random_id] = sponsor_residual

        # for i in range(len(residual_paths)):
        #     cur_residual_path_data = load_file(residual_paths[i])
        #     # cur_residual_path_data = "\n".join(cur_residual_path_data)

        #     cur_path = residual_paths[i]
        #     path_split = os.path.split(cur_path)
        #     assistor_random_id = path_split[-1].split(".")[0]
        #     assistor_random_id_to_residual_dict[assistor_random_id] = cur_residual_path_data

        url = cls._process_url(prefix='main_flow', url="/send_situation", suffix=user_id)
        data = {
            "train_id": train_id,
            "assistor_random_id_to_residual_dict": assistor_random_id_to_residual_dict
        }
        send_situation_response = cls._post_request(
            url=url,
            token=token,
            request_name='send_situation',
            data=data
        )
        
        send_situation_res = load_json_data(json_data=send_situation_res, json_data_name='send_situation_res', 
                                            testing_key_value_pair=[('message', 'send situation successfully!')])

        msg = [
            "3.7 Sponsor sends all situations \n", 
            "---- 3. Unread Match ID Done \n"
        ]
        log_helper(msg, root, user_id, train_id)

        print('Sponsor: Training train_id: ', train_id, ' is running')
        return 'unread_match_identifier_sponsor successfully'
