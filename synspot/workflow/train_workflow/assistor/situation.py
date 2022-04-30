from __future__ import annotations

import requests

from synspot.workflow.base import BaseWorkflow



class TrainAssistorSituation(BaseWorkflow):

    # initiate a request

    @classmethod
    def train_assistor_situation(cls):
        url = self.base_url + self.Network_instance.process_url(prefix='main_flow', url="/get_situation_content", suffix=user_id)
        data = {
            "train_id": train_id,
            "rounds": rounds
        }
        try:
            assistor_get_situation_res = requests.post(url, json=data, headers={'Authorization': 'Bearer ' + token})
            assistor_get_situation_res = load_json_data(json_data=assistor_get_situation_res, json_data_name='assistor_get_situation_res', 
                                                            testing_key_value_pair=[('situation_content', None), ('sender_random_id', None)])
        except:
            print('assistor_get_situation_res wrong')

        # handle response from above request
        cur_situation_file = load_json_data(assistor_get_situation_res["situation_content"], 'assistor_get_situation_res["situation_content"]')
        from_id = load_json_data(assistor_get_situation_res["sender_random_id"], 'assistor_get_situation_res["sender_random_id"]')

        # call save_residual
        save_residual_pos = save_residual(root=root, self_id=user_id, train_id=train_id, round=rounds)
        # assert save_residual_pos is not None
        _, save_residual_pos = handle_Algorithm_return_value("save_residual_pos", save_residual_pos,
                                                                "200", "save_residual")
        # assert save_residual_pos is not None

        # save match id file to designated position
        save_file(save_residual_pos[2], cur_situation_file)

        msg = ["4.3 Assistor Saved Residual File!\n"]
        log_helper(msg, root, user_id, train_id)

        # select train_data_path
        mode, task_mode, model_name, task_name, task_description, train_file_path, train_id_column, train_data_column = self.Database_instance.get_User_Assistor_Table(user_id=user_id, train_id=train_id, test_indicator=self.test_indicator)
        print('get assistor table', mode, task_mode, model_name, task_name, task_description, train_file_path, train_id_column, train_data_column)
        waiting_start_time = time.time()
        self.unread_situation_assistor_train_part(train_id, rounds, from_id, train_file_path, train_data_column, task_mode, model_name, waiting_start_time)
        
        return 'unread_situation_assistor successfully'

    @classmethod
    def unread_situation_assistor_train_part(cls, train_id: str, rounds: int, from_id: str, train_file_path: str, train_data_column: str, task_mode: str, model_name: str, waiting_start_time: float):
        
        """
        Handle the timing issue of unread situation of assistor.

        :param train_id: String. The task needed to be handled.
        :param rounds: Integer. Current round.
        :param train_file_path: String. The file path of train file
        :param train_data_column: String. The selected data column of train file

        :returns: None

        :exception OSError: Placeholder.
        """
        waiting_current_time = time.time()
        time_interval = waiting_current_time - waiting_start_time
        if time_interval > 30 * 60:
            raise ValueError('Sorry, the test stopped due to slow computation')
        # obtain basic information
        user_id, root, token, _ = self.__obtain_important_information(get_train_id=False)
        
        # train the model and get output
        train_output = make_train(root=root, self_id=user_id, train_id=train_id, round=rounds, from_id=from_id, 
                                  dataset_path=train_file_path, data_idx=train_data_column, skip_header=self.skip_header_default, 
                                  task_mode=task_mode, model_name=model_name)
        # assert train_output is not None
        train_output_indicator, train_output = handle_Algorithm_return_value("train_output", train_output, "200", "make_train")
        # assert train_output is not None

        if train_output_indicator == False:
            args = [train_id, rounds, from_id, train_file_path, train_data_column, task_mode, model_name, waiting_start_time]
            print('unread_situation_assistor_train_part callback')
            threading.Timer(30, self.unread_situation_assistor_train_part, args)
        elif train_output_indicator == True:
            msg = ["4.4 Assistor round " + str(rounds) + " training done." + "\n"]
            log_helper(msg, root, user_id, train_id)
            
            # read the file from designated position
            Assistor_train_output_data = load_file(train_output[2])
    
            # initiate a request to send output
            url = self.base_url + self.Network_instance.process_url(prefix='main_flow', url="/send_output", suffix=user_id)
            data = {
                "train_id": train_id,
                "output_content": Assistor_train_output_data
            }
            try:
                assistor_send_output_res = requests.post(url, json=data, headers={'Authorization': 'Bearer ' + token})
                assistor_send_output_res = load_json_data(json_data=assistor_send_output_res, json_data_name='assistor_send_output_res', 
                                                                testing_key_value_pair=[('send_output', 'send output successfully')])
            except:
                print('assistor_send_output_res wrong')

            msg = ["4.5 Assistor sends output\n", "---- 4. Unread Situation Done\n", "---- Train stage done\n"]
            log_helper(msg, root, user_id, train_id)
            
            print('Assistor: Training train_id: ', train_id, ' is running')
            return 'unread_situation_sponsor successfully'