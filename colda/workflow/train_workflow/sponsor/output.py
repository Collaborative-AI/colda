from __future__ import annotations
from re import L

import time

from colda.workflow.train_workflow.train_base import TrainBaseWorkflow

from colda.workflow.utils import (
    obtain_notification_information
)

from colda._typing import (
    Task_Mode,
    Model_Name,
    Metric_Name
)
from typing import Any

from typeguard import typechecked


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
            url_prefix=super()._url_prefix,
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
        
        if super()._async_checker(
            database_type='train_algorithm', 
            user_id=user_id, 
            task_id=train_id,
            algorithm_data_name=['trained_cooperative_model', f'rounds_{cur_rounds_num}'],
            stage='train',
            waiting_start_time=time.time()
        ) == False:
            return
        
        return cls.train_calculate_result(
            user_id=user_id,
            train_id=train_id, 
            cur_rounds_num=cur_rounds_num,
            assistor_random_id_to_output_content_dict=assistor_random_id_to_output_content_dict
        )
        
    @classmethod
    def train_calculate_result(
        cls, 
        user_id: str,
        train_id: str, 
        cur_rounds_num: int, 
        assistor_random_id_to_output_content_dict: dict[str, Any]
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
            algorithm_data_name=['sponsor_trained_result', f'rounds_{cur_rounds_num-1}'],
        )

        # Calculate result for current round
        print('&&%%%%', type(assistor_random_id_to_output_content_dict))
        sponsor_alpha_result, sponsor_result = super()._calculate_result(
            user_id=user_id,
            train_id=train_id,
            rounds=cur_rounds_num, 
            dataset_path=train_file_path, 
            target_idx=train_target_column, 
            skip_header=super()._skip_header, 
            task_mode=task_mode, 
            metric_name=metric_name,
            sponsor_trained_cooperative_model_output=sponsor_trained_cooperative_model_output,
            assistor_trained_cooperative_model_outputs=assistor_random_id_to_output_content_dict,
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
            algorithm_data_name=['sponsor_trained_alpha', f'rounds_{cur_rounds_num}'],
            algorithm_data=sponsor_alpha_result
        )

        super()._store_database_record(
            database_type='train_algorithm',
            user_id=user_id,
            train_id=train_id,
            algorithm_data_name=['sponsor_trained_result', f'rounds_{cur_rounds_num}'],
            algorithm_data=sponsor_result
        )

        msgs = ["5.4 Sponsor makes result done"]
        super()._store_log(
            user_id=user_id,
            task_id=train_id,
            msgs=msgs
        )

        if cur_rounds_num >= super()._max_round:
            msgs = ["---- Train Stage Ends"]
            super()._store_log(
                user_id=user_id,
                task_id=train_id,
                msgs=msgs
            )
            print('Sponsor: Training train_id: ', train_id, ' ends')
            return
        else:
            return cls.train_calculate_next_round_residual(
                user_id=user_id,
                train_id=train_id,
                train_file_path=train_file_path,
                train_target_column=train_target_column,
                task_mode=task_mode,
                metric_name=metric_name,
                cur_rounds_num=cur_rounds_num,
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
        task_mode: Task_Mode,
        metric_name: Metric_Name,
        cur_rounds_num: int,
        sponsor_matched_identifers: Any,
        last_round_result: Any
    ) -> None:

        print('daozheli1')
        new_rounds_num = cur_rounds_num + 1
        _, residual_dict = super()._calculate_residual(
            self_id=user_id, 
            train_id=train_id, 
            round=new_rounds_num, 
            dataset_path=train_file_path, 
            target_idx=train_target_column, 
            skip_header=super()._skip_header, 
            task_mode=task_mode, 
            metric_name=metric_name,
            sponsor_matched_identifers=sponsor_matched_identifers,
            last_round_result=last_round_result,
        )
        # call make_residual
        # make_residual_multiple_paths = make_residual(root=root, self_id=user_id, train_id=train_id, round=(rounds+1), 
        #                                                 dataset_path=train_file_path, target_idx=train_target_column, 
        #                                                 skip_header=self.skip_header_default, task_mode=task_mode, metric_name=metric_name)
        # assert make_residual_multiple_paths is not None
        # _, make_residual_multiple_paths = handle_Algorithm_return_value("make_residual_multiple_paths", make_residual_multiple_paths, "200", "make_residual")
        # assert make_residual_multiple_paths is not None
        print('daozheli2', residual_dict)
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
            assistor_random_id_to_residual_dict[assistor_random_id] = residual_dict[assistor_random_id]

        data = {
            "train_id": train_id,
            "assistor_random_id_to_residual_dict": assistor_random_id_to_residual_dict,
        }
        send_situation_response = super()._post_request_chaining(
            task_id=train_id,
            data=data,
            url_prefix=super()._url_prefix,
            url_root='send_situation',
            url_suffix=user_id,
            status_code=200
        )
        print('daozheli3')
        
        res = cls._get_all_database_records(
            database_type='train_algorithm'
        )
        # print(res[(user_id, train_id)]['sponsor_residual'])

        cls._store_database_record(
            database_type='train_algorithm',
            user_id=user_id,
            train_id=train_id,
            algorithm_data_name='residual_dict',
            algorithm_data=residual_dict
        )

        print('daozheli3.5')
        res = cls._get_all_database_records(
            database_type='train_algorithm'
        )
        # print(res[(user_id, train_id)]['sponsor_residual'])

        msgs = [
            "5.6 Sponsor updates situation done", 
            "---- 5. Unread Output Done"
        ]
        super()._store_log(
            user_id=user_id,
            task_id=train_id,
            msgs=msgs
        )
        print('daozheli4')
        print('Sponsor: Training train_id: ', train_id, ' is running')
        return True
