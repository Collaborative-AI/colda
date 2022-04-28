
class TrainSponsorOutput:

    
    def unread_output_singleTask(self, task_id: str, rounds: int):

        """
        Handle the single task of unread output.

        :param task_id: String. Task id of current task
        :param rounds: Integer. Current Round

        :returns: None

        :exception OSError: Placeholder.
        """
        print("unread_output_singleTask", rounds)
        user_id, root, token, _ = self.__obtain_important_information(get_train_id=False)

        url = self.base_url + self.Network_instance.process_url(prefix='main_flow', url="/get_output_content", suffix=user_id)
        data = {
            "task_id": task_id,
            "rounds": rounds
        }
        try:
            sponsor_get_output_res = requests.post(url, json=data, headers={'Authorization': 'Bearer ' + token})
            sponsor_get_output_res = load_json_data(json_data=sponsor_get_output_res, json_data_name='sponsor_get_output_res', 
                                                    testing_key_value_pair=[('assistor_random_id_to_output_content_dict', None)])
        except:
            print('sponsor_get_output_res wrong')

        msg = ["5.2 Sponsor gets output model\n"]
        log_helper(msg, root, user_id, task_id)

        assistor_random_id_to_output_content_dict = load_json_data(sponsor_get_output_res['assistor_random_id_to_output_content_dict'], 'sponsor_get_output_res[assistor_random_id_to_output_content_dict]')

        for assistor_random_id, output_content in assistor_random_id_to_output_content_dict.items():
            from_id = assistor_random_id
            cur_output = output_content
            print("from_id", from_id)
            # call save_output
            save_output_pos = save_output(root=root, self_id=user_id, task_id=task_id, mode=self.test_indicator, test_id=None, round=rounds, from_id=from_id)
            # assert save_output_pos is not None
            _, save_output_pos = handle_Algorithm_return_value("save_output_pos", save_output_pos, "200", "save_output")
            # assert save_output_pos is not None

            # write file
            # cur_output = json.loads(output[i]).split("\n")
            print("cur_output", type(cur_output), cur_output)
            save_file(save_output_pos[2], cur_output)

            msg = ["5.3 Sponsor saves Output model\n"]
            log_helper(msg, root, user_id, task_id)

            # get train_file_path, train_target_column from User_Sponsor_Table
            task_mode, model_name, metric_name, task_name, task_description, train_file_path, train_id_column, train_data_column, train_target_column = self.Database_instance.get_User_Sponsor_Table(user_id=user_id, task_id=task_id, test_indicator=self.test_indicator)
            print('zzzz', task_mode, model_name, metric_name, task_name, task_description, train_file_path, train_id_column, train_data_column, train_target_column)
            waiting_start_time = time.time()
            self.unread_output_make_result_helper(task_id, rounds, train_file_path, train_target_column, task_mode, metric_name, waiting_start_time)

        return

    def unread_output_make_result_helper(self, task_id: str, rounds: int, train_file_path: str, train_target_column: str, task_mode: str, metric_name: str, waiting_start_time: float):
        """
        Helper Function. Dealing with the order issue

        :param task_id: String. Task id of current task
        :param rounds: Integer. Current Round
        :param train_file_path: String. The file path of train file
        :param train_target_column: String. The selected data column of train file

        :returns: None

        :exception OSError: Placeholder.
        """
        waiting_current_time = time.time()
        time_interval = waiting_current_time - waiting_start_time
        if time_interval > 30 * 60:
            raise ValueError('Sorry, the test stopped due to slow computation')

        user_id, root, token, _ = self.__obtain_important_information(get_train_id=False)

        # call make_result
        make_result_done = make_result(root=root, self_id=user_id, task_id=task_id, round=rounds, 
                                       dataset_path=train_file_path, target_idx=train_target_column, skip_header=self.skip_header_default, 
                                       task_mode=task_mode, metric_name=metric_name)
        # assert make_result_done is not None
        make_result_done_indicator, make_result_done = handle_Algorithm_return_value("make_result_done", make_result_done, "200", "make_result")
        # assert make_result_done is not None

        if make_result_done_indicator == False:
            args = [task_id, rounds, train_file_path, train_target_column, task_mode, metric_name, waiting_start_time]
            print('unread_output_make_result_helper callback')
            threading.Timer(30, self.unread_output_make_result_helper, args)
        elif make_result_done_indicator == True:
            msg = ["5.4 Sponsor makes result done." + "\n"]
            log_helper(msg, root, user_id, task_id)

            if rounds >= self.maxRound:
                msg = ["---- Train Stage Ends\n"]
                log_helper(msg, root, user_id, task_id)
                print('Sponsor: Training task_id: ', task_id, ' ends')
                return
            else:

                # call make_residual
                make_residual_multiple_paths = make_residual(root=root, self_id=user_id, task_id=task_id, round=(rounds+1), 
                                                             dataset_path=train_file_path, target_idx=train_target_column, 
                                                             skip_header=self.skip_header_default, task_mode=task_mode, metric_name=metric_name)
                # assert make_residual_multiple_paths is not None
                _, make_residual_multiple_paths = handle_Algorithm_return_value("make_residual_multiple_paths", make_residual_multiple_paths, "200", "make_residual")
                # assert make_residual_multiple_paths is not None

                msg = ["5.5 Sponsor makes residual finished\n"]
                log_helper(msg, root, user_id, task_id)

                residual_paths = make_residual_multiple_paths[2:]
                assistor_random_id_to_residual_dict = {}
                print('residual_paths', residual_paths)
                for i in range(len(residual_paths)):
                    data = load_file(residual_paths[i])
                    # cur_residual_path_data = "\n".join(cur_residual_path_data)

                    path_split = os.path.split(residual_paths[i])
                    print('cur_path', path_split)
                    assistor_random_id = path_split[-1].split(".")[0]
                    print('cur_path', assistor_random_id)
                    assistor_random_id_to_residual_dict[assistor_random_id] = data
                
                url = self.base_url + self.Network_instance.process_url(prefix='main_flow', url="/send_situation", suffix=user_id)
                data = {
                    "task_id": task_id,
                    "assistor_random_id_to_residual_dict": assistor_random_id_to_residual_dict,
                }
                try:
                    send_situation_res = requests.post(url, json=data, headers={'Authorization': 'Bearer ' + token})
                    send_situation_res = load_json_data(json_data=send_situation_res, json_data_name='send_situation_res', 
                                                        testing_key_value_pair=[('message', 'send situation successfully!')])
                except:
                    print('send_situation_res wrong')

                msg = ["5.6 Sponsor updates situation done\n", "-------------------------- 5. Unread Output Done\n"]
                log_helper(msg, root, user_id, task_id)
                
                print('Sponsor: Training task_id: ', task_id, ' is running')
                return 'unread_output successfully'
