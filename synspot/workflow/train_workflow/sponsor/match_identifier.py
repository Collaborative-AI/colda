


class TrainSponsorMatchIdentifier:

    @classmethod
    def unread_sponsor_match_identifier(cls):

        url = self.base_url + self.Network_instance.process_url(prefix='main_flow', url="/get_identifier_content", suffix=user_id)
        data = {
            "task_id": task_id,
        }
        try:
            sponsor_get_match_id_file_res = requests.post(url, json=data, headers={'Authorization': 'Bearer ' + token})
            sponsor_get_match_id_file_res = load_json_data(json_data=sponsor_get_match_id_file_res, json_data_name='sponsor_get_match_id_file_res', 
                                                            testing_key_value_pair=[('assistor_random_id_to_identifier_content_dict', None)])
        except:
            print('sponsor_get_match_id_file_res wrong')

        msg = ["3.3 Sponsor gets matched id file\n"]
        log_helper(msg, root, user_id, task_id)
        assistor_random_id_to_identifier_content_dict = load_json_data(sponsor_get_match_id_file_res['assistor_random_id_to_identifier_content_dict'])
        # match_id_file_list = load_json_data(sponsor_get_match_id_file_res["match_id_file"], 'sponsor_get_match_id_file_res["match_id_file"]')
        # print("match_id_file_list", match_id_file_list)
        # assistor_random_id_pair_list = load_json_data(sponsor_get_match_id_file_res["assistor_random_id_pair"], 'sponsor_get_match_id_file_res["assistor_random_id_pair"]')

        for assistor_random_id, identifier_content in assistor_random_id_to_identifier_content_dict.items():
            from_id = assistor_random_id
            # need to json load each item again to gain list
            cur_match_id_file = json.loads(identifier_content)
            # cur_match_id_file = "\n".join(cur_match_id_file)

            # call save_match_id
            save_match_id_file_pos = save_match_id(root=root, self_id=user_id, task_id=task_id, mode=self.test_indicator, 
                                                    test_id=None, from_id=from_id)
            # assert save_match_id_file_pos is not None
            _, save_match_id_file_pos = handle_Algorithm_return_value("save_match_id_file_pos", save_match_id_file_pos,
                                                                   "200", "save_match_id")
            # assert save_match_id_file_pos is not None

            # write file
            save_file(save_match_id_file_pos[2], cur_match_id_file)

            msg = ["3.4 Sponsor Saved Matched id File at " + save_match_id_file_pos[2] + "\n"]
            log_helper(msg, root, user_id, task_id)

            # call make_match_idx
            make_match_idx_done = make_match_idx(root=root, self_id=user_id, task_id=task_id, mode=self.test_indicator, test_id=None, from_id=from_id)
            # assert make_match_idx_done is not None
            _, make_match_idx_done = handle_Algorithm_return_value("make_match_idx_done", make_match_idx_done, "200", "make_match_idx")
            # assert make_match_idx_done is not None

            msg = ["3.5 Sponsor matches id to index\n"]
            log_helper(msg, root, user_id, task_id)

        # get train target column
        task_mode, model_name, metric_name, task_name, task_description, train_file_path, train_id_column, train_data_column, train_target_column = self.Database_instance.get_User_Sponsor_Table(user_id=user_id, task_id=task_id, test_indicator=self.test_indicator)
        print("train_file_path", train_file_path, train_target_column)

        # call make residual
        make_residual_multiple_paths = make_residual(root=root, self_id=user_id, task_id=task_id, round=self.initial_round, dataset_path=train_file_path, target_idx=train_target_column, skip_header=self.skip_header_default, task_mode=task_mode, metric_name=metric_name)
        # assert make_residual_multiple_paths is not None
        _, make_residual_multiple_paths = handle_Algorithm_return_value("make_residual_multiple_paths", make_residual_multiple_paths, "200", "make_residual")
        # assert make_residual_multiple_paths is not None

        msg = ["3.6 Sponsor makes residual finished\n"]
        log_helper(msg, root, user_id, task_id)

        residual_paths = make_residual_multiple_paths[2].split("?")

        assistor_random_id_to_residual_dict = {}
        for i in range(len(residual_paths)):
            cur_residual_path_data = load_file(residual_paths[i])
            # cur_residual_path_data = "\n".join(cur_residual_path_data)

            cur_path = residual_paths[i]
            path_split = os.path.split(cur_path)
            assistor_random_id = path_split[-1].split(".")[0]
            assistor_random_id_to_residual_dict[assistor_random_id] = cur_residual_path_data

        url = self.base_url + self.Network_instance.process_url(prefix='main_flow', url="/send_situation", suffix=user_id)
        data = {
            "task_id": task_id,
            "assistor_random_id_to_residual_dict": assistor_random_id_to_residual_dict
        }
        try:
            send_situation_res = requests.post(url, json=data, headers={'Authorization': 'Bearer ' + token})
            send_situation_res = load_json_data(json_data=send_situation_res, json_data_name='send_situation_res', 
                                                testing_key_value_pair=[('message', 'send situation successfully!')])
        except:
            print('send_situation_res wrong')

        msg = ["3.7 Sponsor sends all situations" + "\n", "---- 3. Unread Match ID Done\n"]
        log_helper(msg, root, user_id, task_id)

        print('Sponsor: Training task_id: ', task_id, ' is running')
        return 'unread_match_identifier_sponsor successfully'
