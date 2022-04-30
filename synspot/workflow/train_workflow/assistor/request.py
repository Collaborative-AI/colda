from __future__ import annotations

import requests

from synspot.workflow.base import BaseWorkflow

from synspot.workflow.utils import (
    load_json_data,
    log_helper,
    obtain_notification_information
)

class TrainAssistorRequest(BaseWorkflow):

    @classmethod
    def train_assistor_request(cls, train_id, train_id_dict):
        default_mode = cls._get_default_mode()
        user_id, root, token = cls._get_important_information()
        print(f'Default_mode: {default_mode}')

        sender_random_id, role, cur_rounds_num = obtain_notification_information(notification_dict=train_id_dict)
        
        if default_mode == "auto":
            default_record = cls.__DefaultMetadataDatabase_instance.get_record(user_id=user_id)

            user_id = default_record[0]
            default_mode = default_record[1]
            default_task_mode = default_record[2]
            default_model_name = default_record[3]
            default_file_path = default_record[4]
            default_id_column = default_record[5]
            default_data_column = default_record[6]
            
            # assert store_User_Assistor_Table_res == 'User_Assistor_Table stores successfully'

            # hash_id_file_address = make_hash(root=root, self_id=user_id, train_id=train_id, mode=self.test_indicator, 
            #                                 test_id=None, dataset_path=default_file_path, id_idx=default_id_column, skip_header=self.skip_header_default)
            # # assert hash_id_file_address is not None
            # _, hash_id_file_address = handle_Algorithm_return_value("hash_id_file_address", hash_id_file_address, "200", "make_hash")
            # print('hash_id_file_address', hash_id_file_address)
            # # assert hash_id_file_address is not None

            # hash_id_file_data = load_file(hash_id_file_address[2])

            hash_id_file_data = cls.__TrainAlgorithm_instance.make_hash(
                # self_id=user_id, 
                # train_id=train_id, 
                # mode=self.test_indicator, 
                # test_id=None, 
                dataset_path=default_file_path, 
                id_idx=default_id_column, 
                skip_header=cls.__skip_header
            )

            # add log
            msg = [
                "\n You are Assistor \n", 
                f"Task ID: {train_id} \n", 
                "---- 2. Unread Request \n", 
                "2.1 Update the request notification \n"
            ]
            log_helper(msg, root, user_id, train_id)
            
            url = cls._process_url(prefix='main_flow', url="/match_identifier_content", suffix=user_id)

            data = {
                "train_id": train_id,
                "identifier_content": hash_id_file_data
            }
            match_identifier_content_response = cls._post_request(
                url=url,
                token=token,
                request_name='match_identifier_content',
                data=data
            )

            match_assistor_id_res = load_json_data(json_data=match_assistor_id_res, json_data_name='match_assistor_id_res', 
                                                        testing_key_value_pair=[('stored', 'assistor match id stored')])
            
            res = cls.__TrainAssistorMetadataDatabase_instance.store_record(
                user_id=user_id, 
                train_id=train_id, 
                mode=default_mode, 
                task_mode=default_task_mode, 
                model_name=default_model_name, 
                train_file_path=default_file_path, 
                train_id_column=default_id_column, 
                train_data_column=default_data_column, 
                task_name=None, 
                task_description=None,               
            )

            res = cls.__TrainAlgorithmDatabase_instance.store_record(
                user_id=user_id, 
                train_id=train_id, 
                algorithm_data_name='hash_id_file_data',
                algorithm_data=hash_id_file_data
            )

            # add log
            msg = [
                "2.2 assistor uploads id file \n", 
                "---- 2. Unread Request Done \n"
            ]
            log_helper(msg, root, user_id, train_id)

        elif default_mode == "manual":
            pass
        else:
            print('unread request: wrong mode')

        print('Assistor: Training train_id: ', train_id, ' is running')
        return 'unread_request successfully'
