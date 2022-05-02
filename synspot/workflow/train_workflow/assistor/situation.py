from __future__ import annotations

import time
import requests

from synspot.workflow.train_base import TrainBaseWorkflow

from synspot.workflow.utils import obtain_notification_information

from typing import Any


class TrainAssistorSituation(TrainBaseWorkflow):

    @classmethod
    def train_assistor_situation(
        cls, train_id: str, train_id_dict: dict[str, Any]
    ) -> None:

        user_id, root, token = cls._get_important_information()
        sender_random_id, role, cur_rounds_num = obtain_notification_information(notification_dict=train_id_dict)

        data = {
            "train_id": train_id,
            "rounds": cur_rounds_num
        }
        get_situation_content_response = cls._post_request_chaining(
            token=token,
            data=data,
            url_prefix=cls.__url_prefix,
            url_root='get_situation_content',
            url_suffix=user_id
        )

        
        # handle response from above request
        situation_content = get_situation_content_response['situation_content']
        sender_random_id = get_situation_content_response['sender_random_id']

        # cur_situation_file = load_json_data(assistor_get_situation_res["situation_content"], 'assistor_get_situation_res["situation_content"]')
        # from_id = load_json_data(assistor_get_situation_res["sender_random_id"], 'assistor_get_situation_res["sender_random_id"]')

        # call save_residual
        # save_residual_pos = save_residual(root=root, self_id=user_id, train_id=train_id, round=rounds)
        # # assert save_residual_pos is not None
        # _, save_residual_pos = handle_Algorithm_return_value("save_residual_pos", save_residual_pos,
        #                                                         "200", "save_residual")
        # assert save_residual_pos is not None

        # save match id file to designated position
        # save_file(save_residual_pos[2], cur_situation_file)

        # msg = ["4.3 Assistor Saved Residual File!\n"]
        # log_helper(msg, root, user_id, train_id)

        # select train_data_path 

        if cls._async_checker(
            database_type='train_algorithm', 
            user_id=user_id, 
            train_id=train_id,
            algorithm_data_name='assistor_matched_identifer',
            waiting_start_time=time.time()
        ) == False:
            return

        return cls.train_cooperative_model(
            user_id=user_id,
            token=token,
            train_id=train_id,
            rounds=cur_rounds_num,
            sender_random_id=sender_random_id,
            situation_content=situation_content,
        )

    @classmethod
    def train_cooperative_model(
        cls, 
        user_id: str,
        token: str,
        train_id: str, 
        rounds: int, 
        sender_random_id: str, 
        situation_content: Any
    ) -> None:
        
        """
        Handle the timing issue of unread situation of assistor.

        :param train_id: String. The task needed to be handled.
        :param rounds: Integer. Current round.
        :param train_file_path: String. The file path of train file
        :param train_data_column: String. The selected data column of train file

        :returns: None

        :exception OSError: Placeholder.
        """
        
        train_assistor_metadata = cls._get_database_record(
            database_type='train_assistor_metadata',
            user_id=user_id,
            train_id=train_id
        )

        train_id = train_assistor_metadata[0]
        mode = train_assistor_metadata[1]
        task_mode = train_assistor_metadata[2] 
        model_name = train_assistor_metadata[3] 
        task_name = train_assistor_metadata[4] 
        task_description = train_assistor_metadata[5] 
        train_file_path = train_assistor_metadata[6] 
        train_id_column = train_assistor_metadata[7] 
        train_data_column = train_assistor_metadata[8]

        assistor_matched_identifer = cls._get_database_record(
            database_type='train_algorithm',
            user_id=user_id,
            train_id=train_id,
            algorithm_data_name='assistor_matched_identifer'
        )
        
        trained_cooperative_model = cls._train_cooperative_model(
            dataset_path=train_file_path,
            data_idx=train_data_column,
            skip_header=cls.__skip_header,
            task_mode=task_mode,
            model_name=model_name,
            cur_round_residual=situation_content,
            role='assistor',
            matched_identifier=assistor_matched_identifer,
        )
        
        # train the model and get output
        # train_output = make_train(root=root, self_id=user_id, train_id=train_id, round=rounds, from_id=from_id, 
        #                           dataset_path=train_file_path, data_idx=train_data_column, skip_header=self.skip_header_default, 
        #                           task_mode=task_mode, model_name=model_name)
        # assert train_output is not None
        # train_output_indicator, train_output = handle_Algorithm_return_value("train_output", train_output, "200", "make_train")
        # assert train_output is not None

        # if train_output_indicator == False:
        #     args = [train_id, rounds, from_id, train_file_path, train_data_column, task_mode, model_name, waiting_start_time]
        #     print('unread_situation_assistor_train_part callback')
        #     threading.Timer(30, self.unread_situation_assistor_train_part, args)
        # elif train_output_indicator == True:

        msgs = [
            f'4.4 Assistor round {rounds} training done'
        ]
        cls._store_log(
            user_id=user_id,
            task_id=train_id,
            msgs=msgs
        )
        
        # read the file from designated position
        # Assistor_train_output_data = load_file(train_output[2])

        # initiate a request to send output
        # url = self.base_url + self.Network_instance.process_url(prefix='main_flow', url="/send_output", suffix=user_id)
        # data = {
        #     "train_id": train_id,
        #     "output_content": Assistor_train_output_data
        # }
        # try:
        #     assistor_send_output_res = requests.post(url, json=data, headers={'Authorization': 'Bearer ' + token})
            
        # except:
        #     print('assistor_send_output_res wrong')

        data = {
            "train_id": train_id,
            "output_content": trained_cooperative_model
        }
        send_output_response = cls._post_request_chaining(
            token=token,
            data=data,
            url_prefix=cls.__url_prefix,
            url_root='send_output',
            url_suffix=user_id
        )

        msgs = [
            '4.5 Assistor sends output', 
            '---- 4. Unread Situation Done', 
            '---- Train stage done'
        ]
        cls._store_log(
            user_id=user_id,
            task_id=train_id,
            msgs=msgs
        )
        
        print('Assistor: Training train_id: ', train_id, ' is running')
        return 'unread_situation_sponsor successfully'