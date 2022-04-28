
class TrainSponsorSituation:

    @classmethod
    def train_sponsor_situation(cls):
        msg = ["4.2 Cur round is: " + str(rounds) + "\n"]
        log_helper(msg, root, user_id, task_id)

        # get train_data_path from db
        task_mode, model_name, metric_name, task_name, task_description, train_file_path, train_id_column, train_data_column, train_target_column = self.Database_instance.get_User_Sponsor_Table(user_id=user_id, task_id=task_id, test_indicator=self.test_indicator)

        # call make train
        train_output = make_train(root=root, self_id=user_id, task_id=task_id, round=rounds, 
                                  dataset_path=train_file_path, data_idx=train_data_column, skip_header=self.skip_header_default, 
                                  task_mode=task_mode, model_name=model_name)
        # assert train_output is not None
        _, train_output = handle_Algorithm_return_value("train_output", train_output, "200", "make_train")
        # assert train_output is not None

        msg = ["4.3 Sponsor round " + str(rounds) + " training done." + "\n", "---- 4. Unread Situation Done\n"]
        log_helper(msg, root, user_id, task_id)

        print('Sponsor: Training task_id: ', task_id, ' is running')
        return 'unread_situation_sponsor successfully'

        pass
