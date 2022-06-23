get_train_id_response_text = load_json_data(json_data=get_train_id_response, json_data_name='get_train_id_response', 
                                                    testing_key_value_pair=[('train_id', None)])

find_assistor_res = load_json_data(json_data=find_assistor_res, json_data_name='find_assistor_res',
                                                testing_key_value_pair=[('train_id', train_id)])

sponsor_get_match_id_file_res = load_json_data(json_data=sponsor_get_match_id_file_res, json_data_name='sponsor_get_match_id_file_res', 
                                                            testing_key_value_pair=[('assistor_random_id_to_identifier_content_dict', None)])

send_situation_res = load_json_data(json_data=send_situation_res, json_data_name='send_situation_res', 
                                            testing_key_value_pair=[('message', 'send situation successfully!')])

sponsor_get_output_res = load_json_data(json_data=sponsor_get_output_res, json_data_name='sponsor_get_output_res', 
                                                    testing_key_value_pair=[('assistor_random_id_to_output_content_dict', None)])

send_situation_res = load_json_data(json_data=send_situation_res, json_data_name='send_situation_res', 
                                                        testing_key_value_pair=[('message', 'send situation successfully!')])


assistor:

match_assistor_id_res = load_json_data(json_data=match_assistor_id_res, json_data_name='match_assistor_id_res', 
                                                        testing_key_value_pair=[('stored', 'assistor match id stored')]

assistor_get_match_id_file_res = load_json_data(json_data=assistor_get_match_id_file_res, json_data_name='assistor_get_match_id_file_res', 
                                                            testing_key_value_pair=[('sponsor_random_id_to_identifier_content_dict', None)])   

assistor_get_situation_res = load_json_data(json_data=assistor_get_situation_res, json_data_name='assistor_get_situation_res', 
                                                            testing_key_value_pair=[('situation_content', None), ('sender_random_id', None)])

assistor_send_output_res = load_json_data(json_data=assistor_send_output_res, json_data_name='assistor_send_output_res', 
                                                                testing_key_value_pair=[('send_output', 'send output successfully')])