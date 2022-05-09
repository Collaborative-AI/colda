from __future__ import annotations

import time
import requests

from synspot.workflow.train_base import TrainBaseWorkflow

from synspot.workflow.utils import (
    obtain_notification_information
)

from typing import Any


class TrainSponsorOutput(TrainBaseWorkflow):

    @classmethod
    def train_sponsor_output(
        cls, train_id: str, train_id_dict: dict[str, Any]
    ) -> None:

        """
        Handle the single task of unread output.

        :param train_id: String. Task id of current task
        :param rounds: Integer. Current Round

        :returns: None

        :exception OSError: Placeholder.
        """

        user_id = super()._get_user_id()
        sender_random_id, role, cur_rounds_num = obtain_notification_information(
            notification_dict=train_id_dict
        )

        msgs = [
            "---- 5. Unread Output", 
            "5.1 Update the output notification"
        ]
        super()._store_log(
            user_id=user_id,
            task_id=train_id,
            msgs=msgs
        )

        data = {
            "train_id": train_id,
            "rounds": cur_rounds_num
        }
        get_output_content_response = super()._post_request_chaining(
            task_id=train_id,
            data=data,
            url_prefix=cls._url_prefix,
            url_root='get_output_content',
            url_suffix=user_id,
            status_code=200
        )

        msgs = ["5.2 Sponsor gets output model"]
        super()._store_log(
            user_id=user_id,
            task_id=train_id,
            msgs=msgs
        )

        assistor_random_id_to_output_content_dict = get_output_content_response['assistor_random_id_to_output_content_dict']
        assistor_output_contents = {}
        for assistor_random_id, output_content in assistor_random_id_to_output_content_dict.items():
            # from_id = assistor_random_id
            # cur_output = output_content
            # print("from_id", from_id)
            # call save_output
            # save_output_pos = save_output(root=root, self_id=user_id, train_id=train_id, mode=self.test_indicator, test_id=None, round=rounds, from_id=from_id)
            # # assert save_output_pos is not None
            # _, save_output_pos = handle_Algorithm_return_value("save_output_pos", save_output_pos, "200", "save_output")
            # assert save_output_pos is not None

            # write file
            # cur_output = json.loads(output[i]).split("\n")
            # print("cur_output", type(cur_output), cur_output)
            # save_file(save_output_pos[2], cur_output)

            # msg = ["5.3 Sponsor saves Output model\n"]
            # log_helper(msg, root, user_id, train_id)
            assistor_output_contents[assistor_random_id] = output_content
            # super()._store_database_record(
            #     database_type='train_algorithm'
            # )
            # get train_file_path, train_target_column from User_Sponsor_Table
            # task_mode, model_name, metric_name, task_name, task_description, train_file_path, train_id_column, train_data_column, train_target_column = self.Database_instance.get_User_Sponsor_Table(user_id=user_id, train_id=train_id, test_indicator=self.test_indicator)
        
        if super()._async_checker(
            database_type='train_algorithm', 
            user_id=user_id, 
            train_id=train_id,
            algorithm_data_name=f'trained_cooperative_model_rounds_{cur_rounds_num}',
            waiting_start_time=time.time()
        ) == False:
            return
        
        cls.train_calculate_result(
            user_id=user_id,
            train_id=train_id, 
            rounds=cur_rounds_num,
            assistor_output_contents=assistor_output_contents
        )
        
        return

    @classmethod
    def train_calculate_result(
        cls, 
        user_id: str,
        train_id: str, 
        rounds: int, 
        assistor_output_contents: dict[str, Any]
    ) -> None:

        """
        Helper Function. Dealing with the order issue

        :param train_id: String. Task id of current task
        :param rounds: Integer. Current Round
        :param train_file_path: String. The file path of train file
        :param train_target_column: String. The selected data column of train file

        :returns: None

        :exception OSError: Placeholder.
        """

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

        sponsor_trained_cooperative_model_output = super()._get_database_record(
            database_type='train_algorithm',
            user_id=user_id,
            train_id=train_id,
            algorithm_data_name='trained_cooperative_model_output',
        )

        sponsor_matched_identifers = super()._get_database_record(
            database_type='train_algorithm',
            user_id=user_id,
            train_id=train_id,
            algorithm_data_name='sponsor_matched_identifers',
        )

        sponsor_result = super()._get_database_record(
            database_type='train_algorithm',
            user_id=user_id,
            train_id=train_id,
            algorithm_data_name='sponsor_result',
        )

        # Calculate result for current round
        print('&&%%%%', type(assistor_output_contents))
        sponsor_alpha_result, sponsor_result = super()._calculate_result(
            rounds=rounds, 
            dataset_path=train_file_path, 
            target_idx=train_target_column, 
            skip_header=cls._skip_header, 
            task_mode=task_mode, 
            metric_name=metric_name,
            sponsor_trained_cooperative_model_output=sponsor_trained_cooperative_model_output,
            assistor_trained_cooperative_model_outputs=assistor_output_contents,
            sponsor_matched_identifers=sponsor_matched_identifers,
            last_round_result=sponsor_result,
        )
        # make_result_done = make_result(root=root, self_id=user_id, train_id=train_id, round=rounds, 
        #                                dataset_path=train_file_path, target_idx=train_target_column, skip_header=self.skip_header_default, 
        #                                task_mode=task_mode, metric_name=metric_name)
        # assert make_result_done is not None
        # make_result_done_indicator, make_result_done = handle_Algorithm_return_value("make_result_done", make_result_done, "200", "make_result")
        # assert make_result_done is not None

        super()._store_database_record(
            database_type='train_algorithm',
            user_id=user_id,
            train_id=train_id,
            algorithm_data_name='sponsor_result',
            algorithm_data=sponsor_result
        )

        msgs = ["5.4 Sponsor makes result done"]
        super()._store_log(
            user_id=user_id,
            task_id=train_id,
            msgs=msgs
        )

        if rounds >= cls._maxRound:
            msgs = ["---- Train Stage Ends"]
            super()._store_log(
                user_id=user_id,
                task_id=train_id,
                msgs=msgs
            )
            print('Sponsor: Training train_id: ', train_id, ' ends')
            return
        else:
            cls.train_calculate_next_round_residual(
                user_id=user_id,
                train_id=train_id,
                train_file_path=train_file_path,
                train_target_column=train_target_column,
                task_mode=task_mode,
                metric_name=metric_name,
                sponsor_matched_identifers=sponsor_matched_identifers,
                last_round_result=sponsor_result
            )
    
    @classmethod
    def train_calculate_next_round_residual(
        cls,
        user_id: str,
        train_id: str,
        train_file_path: str,
        train_target_column: str,
        task_mode: str,
        metric_name: str,
        sponsor_matched_identifers: Any,
        last_round_result: Any
    ) -> None:

        sponsor_residual = super()._calculate_residual(
            self_id=user_id, 
            train_id=train_id, 
            round=cls._initial_round_num, 
            dataset_path=train_file_path, 
            target_idx=train_target_column, 
            skip_header=cls._skip_header, 
            task_mode=task_mode, 
            metric_name=metric_name,
            last_round_result=last_round_result,
        )

        # call make_residual
        # make_residual_multiple_paths = make_residual(root=root, self_id=user_id, train_id=train_id, round=(rounds+1), 
        #                                                 dataset_path=train_file_path, target_idx=train_target_column, 
        #                                                 skip_header=self.skip_header_default, task_mode=task_mode, metric_name=metric_name)
        # assert make_residual_multiple_paths is not None
        # _, make_residual_multiple_paths = handle_Algorithm_return_value("make_residual_multiple_paths", make_residual_multiple_paths, "200", "make_residual")
        # assert make_residual_multiple_paths is not None

        msgs = ["5.5 Sponsor makes residual finished"]
        super()._store_log(
            user_id=user_id,
            task_id=train_id,
            msgs=msgs
        )
        # log_helper(msg, root, user_id, train_id)

        # residual_paths = make_residual_multiple_paths[2:]
        # assistor_random_id_to_residual_dict = {}
        # print('residual_paths', residual_paths)
        # for i in range(len(residual_paths)):
        #     data = load_file(residual_paths[i])
        #     # cur_residual_path_data = "\n".join(cur_residual_path_data)

        #     path_split = os.path.split(residual_paths[i])
        #     print('cur_path', path_split)
        #     assistor_random_id = path_split[-1].split(".")[0]
        #     print('cur_path', assistor_random_id)
        #     assistor_random_id_to_residual_dict[assistor_random_id] = data
        
        assistor_random_id_to_residual_dict = {}
        for assistor_random_id in sponsor_matched_identifers.keys():
            assistor_random_id_to_residual_dict[assistor_random_id] = sponsor_residual

        data = {
            "train_id": train_id,
            "assistor_random_id_to_residual_dict": assistor_random_id_to_residual_dict,
        }
        send_situation_response = super()._post_request_chaining(
            task_id=train_id,
            data=data,
            url_prefix=cls._url_prefix,
            url_root='send_situation',
            url_suffix=user_id,
            status_code=200
        )

        msgs = [
            "5.6 Sponsor updates situation done", 
            "---- 5. Unread Output Done"
        ]
        super()._store_log(
            user_id=user_id,
            task_id=train_id,
            msgs=msgs
        )
        
        print('Sponsor: Training train_id: ', train_id, ' is running')
        return True
