


class TrainAssistorMatchIdentifier:

    @classmethod
    def train_assistor_match_identifier(cls):
        # initiate a request
        url = self.base_url + self.Network_instance.process_url(prefix='main_flow', url="/get_identifier_content", suffix=user_id)
        data = {
            "task_id": task_id,
        }
        try:
            assistor_get_match_id_file_res = requests.post(url, json=data, headers={'Authorization': 'Bearer ' + token})
            assistor_get_match_id_file_res = load_json_data(json_data=assistor_get_match_id_file_res, json_data_name='assistor_get_match_id_file_res', 
                                                            testing_key_value_pair=[('sponsor_random_id_to_identifier_content_dict', None)])
        except:
            print('assistor_get_match_id_file_res wrong')

        msg = ["3.3 Assistor gets matched id file\n"]
        log_helper(msg, root, user_id, task_id)

        # handle the response from request, assistor only has one match_id_file. 
        sponsor_random_id_to_identifier_content_dict = load_json_data(assistor_get_match_id_file_res['sponsor_random_id_to_identifier_content_dict'])

        sponsor_random_id = next(iter(sponsor_random_id_to_identifier_content_dict))
        identifier_content = sponsor_random_id_to_identifier_content_dict[sponsor_random_id]
        # call save_match_id to get the designated position to save the match_id file
        save_match_id_file_pos = save_match_id(root=root, self_id=user_id, task_id=task_id, mode=self.test_indicator, test_id=None, from_id=sponsor_random_id)
        # assert save_match_id_file_pos is not None
        _, save_match_id_file_pos = handle_Algorithm_return_value("save_match_id_file_pos", save_match_id_file_pos,
                                                                "200", "save_match_id")
        # assert save_match_id_file_pos is not None

        # save match id file to designated position
        save_file(save_match_id_file_pos[2], identifier_content)

        msg = ["3.4 Assistor Saved Matched id File at " + save_match_id_file_pos[2] + "\n"]
        log_helper(msg, root, user_id, task_id)

        # call make_match_idx
        make_match_idx_done = make_match_idx(root=root, self_id=user_id, task_id=task_id, mode=self.test_indicator, test_id=None, from_id=sponsor_random_id)
        # assert make_match_idx_done is not None
        _, make_match_idx_done = handle_Algorithm_return_value("make_match_idx_done", make_match_idx_done, "200", "make_match_idx")
        # assert make_match_idx_done is not None

        msg = ["3.5 Assistor matches id to index\n", "---- 3. Unread Match ID Done\n"]
        log_helper(msg, root, user_id, task_id)

        print('Assistor: Training task_id: ', task_id, ' is running')
        return 'unread_match_identifier_assistor successfully'
    pass
