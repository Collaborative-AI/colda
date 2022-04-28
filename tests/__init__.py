"""
tests
~~~~~

Test suite for the synspot package.
"""
from typing import List
from abc import ABC, abstractmethod

from synspot.workflow.train_workflow import TrainRequest
from synspot.workflow.test_workflow import TestRequest
from synspot.authorization import Authorization
from synspot.GetNotification import GetNotification
from synspot.personalinformation import PersonalInformation
from synspot.network import Network
from synspot import set_default_data_path, get_all_task_id_as_sponsor, get_all_test_id_as_sponsor, get_all_task_id_as_assistor, get_all_test_id_as_assistor
from synspot import get_all_task_id, get_all_test_id

_default_authorization = Authorization.get_Authorization_instance()
_default_trainRequest = TrainRequest.get_TrainRequest_instance()
_default_testRequest = TestRequest.get_TestRequest_instance()
_default_getNotification = GetNotification.get_GetNotification_instance()
_default_PersonalInformation = PersonalInformation.get_PersonalInformation_instance()
_default_Network = Network.get_Network_instance()
# _default_testRequest = TestRequest.get_TestRequest_instance()
# _default_get_notification = Get_Notification.get_Get_notification_instance()

testing_data = {}
testing_data['max_round'] = 2
testing_data['first_user_username'] = 'xie1'
testing_data['first_user_password'] = 'Xie1@123'
testing_data['second_user_username'] = 'xie2'
testing_data['second_user_password'] = 'Xie2@123'

testing_data['test_register_username'] = 'leqq'
testing_data['test_register_email'] = 'lq109945190@gmail.com'
testing_data['test_register_password'] = 'leq1'

testing_data['sponsor_mode'] = 'regression'
data_file = 'BostonHousing'
total_participants = '2'
match_ratio = '1.0'
user_id = '0'
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

folder_indicator = 'test'
if testing_data['sponsor_mode'] == 'regression':
    testing_data['test_file_path'] = "/Users/qile/Documents/Apollo_Data/data/" + data_file + "/" + data_file + "_" + total_participants + "_123_" + match_ratio + "/" + user_id + "/" + folder_indicator + "/dataset.csv"
elif testing_data['sponsor_mode'] == 'classification':
    testing_data['test_file_path'] = "/Users/qile/Documents/Apollo_Data/data/" + data_file + "/" + data_file + "_" + total_participants + "_123_" + match_ratio + "/" + user_id + "/" + folder_indicator + "/dataset.csv"
testing_data['test_id_column'] = '1'
testing_data['test_data_column'] = '2-8'
testing_data['test_target_column'] = '9'
testing_data['test_name'] = 'test_ceshi111'
testing_data['test_description'] = 'wudiwudiw'

# Assistor
testing_data['default_mode'] = 'auto'
testing_data['default_task_mode'] = 'regression'
testing_data['default_model_name'] = 'linear'

data_file = 'BostonHousing'
total_participants = '2'
match_ratio = '1.0'
user_id = '1'
folder_indicator = 'all'
if testing_data['default_task_mode'] == 'regression':
    testing_data['default_file_path'] = "/Users/qile/Documents/Apollo_Data/data/" + data_file + "/" + data_file + "_" + total_participants + "_123_" + match_ratio + "/" + user_id + "/" + folder_indicator + "/dataset.csv"
elif testing_data['default_task_mode'] == 'classification':
    testing_data['default_file_path'] = "/Users/qile/Documents/Apollo_Data/data/" + data_file + "/" + data_file + "_" + total_participants + "_123_" + match_ratio + "/" + user_id + "/" + folder_indicator + "/dataset.csv"

testing_data['default_id_column'] = '1'
testing_data['default_data_column'] = '2-7'


class Strategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @abstractmethod
    def unread_test_output_test(self):
        pass
    
    @abstractmethod
    def unread_test_sponsor_match_id_test(self):
        pass
    
    @abstractmethod
    def unread_test_assistor_match_id_test(self):
        pass

"""
Concrete Strategies implement the algorithm while following the base Strategy
interface. The interface makes them interchangeable in the Context.
"""

class Regression_1s_1a(Strategy):
    def unread_test_output_test(self):
        def unread_test_output_regression_regression_1s_1a(data):
            test_dict = {
                "1": {
                    "MAD": 3.54763,
                    "RMSE": 5.21270,
                    "R2": 0.46997,
                },
                "2": {
                    "MAD": 3.54221,
                    "RMSE": 5.19744,
                    "R2": 0.45141,
                }
            }
            
            for key in data:
                cur_running_res = data[key]
                cur_testing_dict = test_dict[key]
                for sub_key in cur_running_res:
                    cur_number = cur_running_res[sub_key]
                    cur_number = float(format(cur_number, '.5f'))
                    cur_testing_number = cur_testing_dict[sub_key]
                    cur_testing_number = float(format(cur_testing_number, '.5f'))
                    print('1s_1a', cur_number, cur_testing_number)
                    if cur_number != cur_testing_number:
                        return False
            return True
        return unread_test_output_regression_regression_1s_1a
    
    def unread_test_sponsor_match_id_test(self):
        def unread_test_sponsor_match_id_regression_regression_1s_1a(data):
            test_array = [-15.62146, -7.63978, -3.17975, -3.77626, -2.13779, 1.60417, -1.76595, -0.91224]
            test_array_index = 0
            for key in data:
                cur_list = data[key]
                for j in range(len(cur_list)):
                    cur_number = cur_list[j]
                    cur_number = float(format(cur_number, '.5f'))
                    print('1s_1a', cur_number, type(cur_number), test_array[test_array_index], type(test_array[test_array_index]))
                    if cur_number != test_array[test_array_index]:
                        return False
                    test_array_index += 1
            return True
        return unread_test_sponsor_match_id_regression_regression_1s_1a

    def unread_test_assistor_match_id_test(self):
        def unread_test_assistor_match_id_regression_regression_1s_1a(data):
            test_array = [3.93492, -1.96598, -19.51288, 6.83615, -0.52504, -0.75834, -1.23748, -0.11017]
            test_array_index = 0
            for key in data:
                cur_list = data[key]
                for j in range(len(cur_list)):
                    cur_number = cur_list[j]
                    cur_number = float(format(cur_number, '.5f'))
                    print('1s_1a_assistor', cur_number, type(cur_number), test_array[test_array_index], type(test_array[test_array_index]))
                    if cur_number != test_array[test_array_index]:
                        return False
                    test_array_index += 1
            return True
        return unread_test_assistor_match_id_regression_regression_1s_1a

class unittest_strategy_interface():
    """
    The Context defines the interface of interest to clients.
    """

    def __init__(self) -> None:
        self._unittest_strategy = None

    @property
    def unittest_strategy(self) -> Strategy:
        """
        The Context maintains a reference to one of the Strategy objects. The
        Context does not know the concrete class of a strategy. It should work
        with all strategies via the Strategy interface.
        """

        return self._unittest_strategy

    @unittest_strategy.setter
    def unittest_strategy(self, unittest_strategy: Strategy) -> None:
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """

        self._unittest_strategy = unittest_strategy

    def get_unread_test_sponsor_match_id_test(self):
        return self._unittest_strategy.unread_test_sponsor_match_id_test()
    
    def get_unread_test_assistor_match_id_test(self):
        return self._unittest_strategy.unread_test_assistor_match_id_test()

    def get_unread_test_output_test(self):
        return self._unittest_strategy.unread_test_output_test()
    
    





