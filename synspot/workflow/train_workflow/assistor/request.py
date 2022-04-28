
class TrainAssistorRequest:

    @classmethod
    def unread_assistor_request(cls):
        default_mode = self.PersonalInformation_instance.default_mode
        print('default_mode', default_mode)
        for task_id in task_id_dict:

            sender_random_id, role, cur_rounds_num = obtain_notification_information(notification_dict_value=task_id_dict[task_id])
            
            if default_mode == "auto":
                
                user_id, default_mode, default_task_mode, default_model_name, default_file_path, default_id_column, default_data_column = self.Database_instance.get_User_Default_Table(user_id)
                store_User_Assistor_Table_res = self.Database_instance.store_User_Assistor_Table(user_id=user_id, task_id=task_id, test_indicator=self.test_indicator, mode=default_mode, task_mode=default_task_mode, model_name=default_model_name, 
                                                            test_id=None, task_name=None, task_description=None, test_name=None, test_description=None, train_file_path=default_file_path, 
                                                            train_id_column=default_id_column, train_data_column=default_data_column, test_file_path=None, test_id_column=None, test_data_column=None)
                # assert store_User_Assistor_Table_res == 'User_Assistor_Table stores successfully'

                hash_id_file_address = make_hash(root=root, self_id=user_id, task_id=task_id, mode=self.test_indicator, 
                                                test_id=None, dataset_path=default_file_path, id_idx=default_id_column, skip_header=self.skip_header_default)
                # assert hash_id_file_address is not None
                _, hash_id_file_address = handle_Algorithm_return_value("hash_id_file_address", hash_id_file_address, "200", "make_hash")
                print('hash_id_file_address', hash_id_file_address)
                # assert hash_id_file_address is not None

                hash_id_file_data = load_file(hash_id_file_address[2])

                # add log
                msg = ["\n You are Assistor\n", "Task ID: " + task_id + "\n", "---- 2. Unread Request\n", "2.1 Update the request notification\n"]
                log_helper(msg, root, user_id, task_id)
                
                url = self.base_url + self.Network_instance.process_url(prefix='main_flow', url="/match_identifier_content", suffix=user_id)
                data = {
                    "task_id": task_id,
                    "identifier_content": hash_id_file_data
                }
                try:
                    match_assistor_id_res = requests.post(url, json=data, headers={'Authorization': 'Bearer ' + token})
                    match_assistor_id_res = load_json_data(json_data=match_assistor_id_res, json_data_name='match_assistor_id_res', 
                                                            testing_key_value_pair=[('stored', 'assistor match id stored')])
                except:
                    print('match_assistor_id_res wrong')

                # add log
                msg = ["2.2 assistor uploads id file\n", "---- 2. Unread Request Done\n"]
                log_helper(msg, root, user_id, task_id)
            elif default_mode == "manual":
                pass
            else:
                print('unread request: wrong mode')

        print('Assistor: Training task_id: ', task_id, ' is running')
        return 'unread_request successfully'
