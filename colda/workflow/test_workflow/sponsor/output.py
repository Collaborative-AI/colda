from __future__ import annotations

import time

from colda.workflow.test_base import TestBaseWorkflow

from colda.workflow.utils import (
    obtain_notification_information
)

from typing import Any

from typeguard import typechecked


class TestSponsorOutput(TestBaseWorkflow):

    @classmethod
    def test_sponsor_output(
        cls, 
        test_id: str, 
        test_id_dict: dict[str, Any]
    ) -> None:

        """
        Handle the single task of unread output.

        :param train_id: String. Task id of current task
        :param rounds: Integer. Current Round

        :returns: None

        :exception OSError: Placeholder.
        """

        user_id = super()._get_user_id()
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
        # assistor_output_contents = {}
        # for assistor_random_id, output_content in assistor_random_id_to_output_content_dict.items():
        #     # from_id = assistor_random_id
        #     # cur_output = output_content
        #     # print("from_id", from_id)
        #     # call save_output
        #     # save_output_pos = save_output(root=root, self_id=user_id, train_id=train_id, mode=self.test_indicator, test_id=None, round=rounds, from_id=from_id)
        #     # # assert save_output_pos is not None
        #     # _, save_output_pos = handle_Algorithm_return_value("save_output_pos", save_output_pos, "200", "save_output")
        #     # assert save_output_pos is not None

        #     # write file
        #     # cur_output = json.loads(output[i]).split("\n")
        #     # print("cur_output", type(cur_output), cur_output)
        #     # save_file(save_output_pos[2], cur_output)

        #     # msg = ["5.3 Sponsor saves Output model\n"]
        #     # log_helper(msg, root, user_id, train_id)
        #     assistor_output_contents[assistor_random_id] = output_content
            # super()._store_database_record(
            #     database_type='train_algorithm'
            # )
            # get train_file_path, train_target_column from User_Sponsor_Table
            # task_mode, model_name, metric_name, task_name, task_description, train_file_path, train_id_column, train_data_column, train_target_column = self.Database_instance.get_User_Sponsor_Table(user_id=user_id, train_id=train_id, test_indicator=self.test_indicator)
        
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

        # Calculate result for current round
        print('&&%%%%', type(assistor_random_id_to_output_content_dict))
        evaluation = super()._evaluate_results(
            user_id=user_id,
            test_id=test_id,
            max_round=super()._max_round, 
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
        # make_result_done = make_result(root=root, self_id=user_id, train_id=train_id, round=rounds, 
        #                                dataset_path=train_file_path, target_idx=train_target_column, skip_header=self.skip_header_default, 
        #                                task_mode=task_mode, metric_name=metric_name)
        # assert make_result_done is not None
        # make_result_done_indicator, make_result_done = handle_Algorithm_return_value("make_result_done", make_result_done, "200", "make_result")
        # assert make_result_done is not None

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

        
