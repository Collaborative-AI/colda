"""
tests.test_curves.py
~~~~~~~~~~~~~~~~~~~~

Test suite for the curves.py module that handles everything to do with
supply and demand curves.
"""
import json
import os
from typing import Any, Dict, List
from copy import deepcopy
from . import testing_data
from . import _default_authentication

import pytest

# def load_test_data() -> List[Dict[str, Any]]:
#     """Load test data from JSON file.
#     :return: Test data.
#     :rtype: Dict[str, Any]
#     """

#     basedir = os.path.abspath(os.path.dirname(__file__))
#     print('zzz', basedir)
#     config_file_path = './test_data_dict.json'
#     with open(config_file_path) as file:
#         json_data = file.read()

#     data = json.loads(json_data)
#     return data['testing_data']

class TestAuthentication:

    # def test_userLogin(self):
    #     Authentication_instance = self.get_instance()
    #     testing_data = get_testing_data()        
        
    #     userLogin_res = Authentication_instance.userLogin(username=testing_data['first_user_username'], password=testing_data['first_user_password'])
    #     assert userLogin_res == 'userLogin Successfully'

    def test_userRegister(self):       
        userRegister_res = _default_authentication.userRegister(username=testing_data['test_register_username'], email=testing_data['test_register_email'], password=testing_data['test_register_password'])
        assert userRegister_res == {'password': 'please create password between 8 chars and 40 chars'}





        # // "first_user_password"
        # // "second_user_username"
        # // "second_user_password"

        # // "sponsor_mode"
        # // "maxRound"
        # // "assistors"
        # // "train_id_column"
        # // "train_data_column"
        # // "train_target_column"
        # // "task_mode"
        # // "model_name"
        # // "metric_name"
        # // "task_name"
        # // "task_description"
        # // testing_data['first_user_username'] = 'xie1'
        # // testing_data['first_user_password'] = 'Xie1@123'
        # // testing_data['second_user_username'] = 'xie2'
        # // testing_data['second_user_password'] = 'Xie2@123'

        # // testing_data['sponsor_mode'] = 'regression'
        # // data_file = 'BostonHousing'
        # // total_participants = '2'
        # // match_ratio = '1.0'
        # // user_id = '1'
        # // folder_indicator = 'train'
        # // if testing_data['sponsor_mode'] == 'regression':
        # //     testing_data['train_file_path'] = "/Users/qile/Documents/Apollo_Data/data/" + data_file + "/" + data_file + "_" + total_participants + "_123_" + match_ratio + "/" + user_id + "/" + folder_indicator + "/dataset.csv"
        # // elif testing_data['sponsor_mode'] == 'classification':
        # //     testing_data['train_file_path'] = "/Users/qile/Documents/Apollo_Data/data/" + data_file + "/" + data_file + "_" + total_participants + "_123_" + match_ratio + "/" + user_id + "/" + folder_indicator + "/dataset.csv"

        # // testing_data['maxRound'] = 2
        # // testing_data['assistors'] = ['xie2']
        # // testing_data['train_id_column'] = '1'
        # // testing_data['train_data_column'] = '2-8'
        # // testing_data['train_target_column'] = '9'
        # // testing_data['task_mode'] = 'regression'
        # // testing_data['model_name'] = 'linear'
        # // testing_data['metric_name'] = 'MAD_RMSE_R2'

        # // testing_data['task_name'] = 'ceshi111'
        # // testing_data['task_description'] = 'lihaideceshi'
        # // return testing_data