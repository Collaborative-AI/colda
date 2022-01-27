"""
tests.test_curves.py
~~~~~~~~~~~~~~~~~~~~

Test suite for the curves.py module that handles everything to do with
supply and demand curves.
"""
import json
from typing import Any, Dict, List
from copy import deepcopy

from py_pkg.TrainRequest import TrainRequest
from py_pkg.Authorization import Authorization
import pytest

class TestTrainRequest:
    def get_instance(self):
        TrainRequest_instance = TrainRequest()
        return TrainRequest_instance

    def login(self):
        Authorization_instance = Authorization()
        testing_data = self.get_testing_data()
        userLogin_res = Authorization_instance.userLogin(username=testing_data['first_user_username'], password=testing_data['first_user_password'])
        assert userLogin_res == 'userLogin Successfully'
        return

    def get_testing_data(self):
        testing_data = {}
        testing_data['first_user_username'] = 'xie1'
        testing_data['first_user_password'] = 'Xie1@123'
        testing_data['second_user_username'] = 'xie2'
        testing_data['second_user_password'] = 'Xie2@123'

        testing_data['sponsor_mode'] = 'regression'
        data_file = 'BostonHousing'
        total_participants = '2'
        match_ratio = '1.0'
        user_id = '1'
        folder_indicator = 'train'
        if testing_data['sponsor_mode'] == 'regression':
            testing_data['train_file_path'] = "/Users/qile/Documents/Apollo_Data/data/" + data_file + "/" + data_file + "_" + total_participants + "_123_" + match_ratio + "/" + user_id + "/" + folder_indicator + "/dataset.csv"
        elif testing_data['sponsor_mode'] == 'classification':
            testing_data['train_file_path'] = "/Users/qile/Documents/Apollo_Data/data/" + data_file + "/" + data_file + "_" + total_participants + "_123_" + match_ratio + "/" + user_id + "/" + folder_indicator + "/dataset.csv"

        testing_data['maxRound'] = 2
        testing_data['assistors'] = ['xie2']
        testing_data['train_id_column'] = '1'
        testing_data['train_data_column'] = '2-8'
        testing_data['train_target_column'] = '9'
        testing_data['task_mode'] = 'regression'
        testing_data['model_name'] = 'linear'
        testing_data['metric_name'] = 'MAD_RMSE_R2'

        testing_data['task_name'] = 'ceshi111'
        testing_data['task_description'] = 'lihaideceshi'
        return testing_data

    def test_handleTrainRequest(self):
        TrainRequest_instance = self.get_instance()
        testing_data = self.get_testing_data()
        self.login()
        handleTrainRequest_res = TrainRequest_instance.handleTrainRequest(maxRound=testing_data['maxRound'], assistors=testing_data['assistors'], train_file_path=testing_data['train_file_path'],
                             train_id_column=testing_data['train_id_column'], train_data_column=testing_data['train_data_column'], train_target_column=testing_data['train_target_column'], 
                             task_mode= testing_data['task_mode'], model_name=testing_data['model_name'], metric_name=testing_data['metric_name'], 
                             task_name=testing_data['task_name'], task_description=testing_data['task_description'])
        assert handleTrainRequest_res == 'handleTrainRequest successfully'

    