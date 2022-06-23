"""
tests
~~~~~

Test suite for the colda package.
"""
from typing import List
from abc import ABC, abstractmethod

from colda.workflow import (
    TrainMainWorkflow,
    TestMainWorkflow
)
    
from colda.authentication.api import Authentication
from colda.short_polling.api import ShortPolling
from colda.pi.api import PI
from colda.network.api import Network
from colda.utils.log import GetAlgorithmLog
# from colda import set_default_data_path, get_all_task_id_as_sponsor, get_all_test_id_as_sponsor, get_all_task_id_as_assistor, get_all_test_id_as_assistor
# from colda import get_all_task_id, get_all_test_id

_default_authentication = Authentication.get_instance()
_default_trainMainWorkflow = TrainMainWorkflow.get_instance()
_default_testMainWorkflow = TestMainWorkflow.get_instance()
_default_ShortPolling = ShortPolling.get_instance()
_default_PI = PI.get_instance()
_default_Network = Network.get_instance()
# _default_algorithm_log = GetAlgorithmLog.get_instance()
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
    testing_data['train_file_path'] = "/Users/qile/Documents/colda_all/colda_Data/data/" + data_file + "/" + data_file + "_" + total_participants + "_123_" + match_ratio + "/" + user_id + "/" + folder_indicator + "/dataset.csv"
elif testing_data['sponsor_mode'] == 'classification':
    testing_data['train_file_path'] = "/Users/qile/Documents/colda_all/colda_Data/data/" + data_file + "/" + data_file + "_" + total_participants + "_123_" + match_ratio + "/" + user_id + "/" + folder_indicator + "/dataset.csv"

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
    testing_data['test_file_path'] = "/Users/qile/Documents/colda_all/colda_Data/data/" + data_file + "/" + data_file + "_" + total_participants + "_123_" + match_ratio + "/" + user_id + "/" + folder_indicator + "/dataset.csv"
elif testing_data['sponsor_mode'] == 'classification':
    testing_data['test_file_path'] = "/Users/qile/Documents/colda_all/colda_Data/data/" + data_file + "/" + data_file + "_" + total_participants + "_123_" + match_ratio + "/" + user_id + "/" + folder_indicator + "/dataset.csv"
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
    testing_data['default_file_path'] = "/Users/qile/Documents/colda_all/colda_Data/data/" + data_file + "/" + data_file + "_" + total_participants + "_123_" + match_ratio + "/" + user_id + "/" + folder_indicator + "/dataset.csv"
elif testing_data['default_task_mode'] == 'classification':
    testing_data['default_file_path'] = "/Users/qile/Documents/colda_all/colda_Data/data/" + data_file + "/" + data_file + "_" + total_participants + "_123_" + match_ratio + "/" + user_id + "/" + folder_indicator + "/dataset.csv"

testing_data['default_id_column'] = '1'
testing_data['default_data_column'] = '2-7'


class Strategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @classmethod
    @abstractmethod
    def alpha(cls):
        pass

    @classmethod
    @abstractmethod
    def sponsor_trained_cooperative_model_output(cls):
        pass

    @classmethod
    @abstractmethod
    def assistor_trained_cooperative_model_output(cls):
        pass

    @classmethod
    @abstractmethod
    def unread_test_make_result(cls):
        pass

    @classmethod
    @abstractmethod
    def unread_test_output_test(cls):
        pass
    
    @classmethod
    @abstractmethod
    def unread_test_sponsor_match_id_test(cls):
        pass
    
    @classmethod
    @abstractmethod
    def unread_test_assistor_match_id_test(cls):
        pass

"""
Concrete Strategies implement the algorithm while following the base Strategy
interface. The interface makes them interchangeable in the Context.
"""

class Regression_1s_1a(Strategy):
    
    @classmethod
    def alpha(cls):
        def alpha_callback(data):
            test_dict = {
                "rounds_1": [0.57166346],
                "rounds_2": [0.802418863],
            }
            
            for key in data:
                cur_running_res = data[key]
                cur_testing_res = test_dict[key]
                # print('cur_running_res', cur_running_res, cur_running_res[0])
                # print(cur_testing_res, cur_testing_res[0])
                # for i in range(len(cur_running_res)):
                cur_number = cur_running_res[0]
                cur_number = float(format(cur_number, '.5f'))
                cur_testing_number = cur_testing_res[0]
                cur_testing_number = float(format(cur_testing_number, '.5f'))
                print('1s_1a', cur_testing_number, cur_number)
                if cur_number != cur_testing_number:
                    return False
            return True
        return alpha_callback

    # @classmethod
    # def make_result_cooperative_model_output(cls):
    #     def make_result_cooperative_model_output_callback(data):
    #         test_dict = {
    #             "rounds_1": [
    #                 [-8.29007],
    #                 [-1.670738],
    #                 [-13.95130964],
    #                 [12.425088]
    #             ],
    #             "rounds_2": [
    #                 [0.0506641812],
    #                 [-3.080867],
    #                 [0.5027218],
    #                 [-0.942036042]
    #             ]
    #         }
            
    #         for key in data:
    #             cur_running_res = data[key]
    #             cur_testing_res = test_dict[key]
    #             for i in range(len(cur_running_res)):
    #                 cur_number = cur_running_res[i][0]
    #                 cur_number = float(format(cur_number, '.5f'))
    #                 cur_testing_number = cur_testing_res[i][0]
    #                 cur_testing_number = float(format(cur_testing_number, '.5f'))
    #                 print('1s_1a', cur_testing_number, cur_number)
    #                 if cur_number != cur_testing_number:
    #                     return False
    #         return True
    #     return make_result_cooperative_model_output_callback

    @classmethod
    def sponsor_trained_cooperative_model_output(cls):
        def sponsor_trained_cooperative_model_output_callback(data):
            test_dict = {
                "rounds_1": [
                    [-8.29007],
                    [-1.670738],
                    [-13.95130964],
                    [12.425088]
                ],
                "rounds_2": [
                    [0.0506641812],
                    [-3.080867],
                    [0.5027218],
                    [-0.942036042]
                ]
            }
            
            for key in data:
                cur_running_res = data[key]
                cur_testing_res = test_dict[key]
                for i in range(len(cur_running_res)):
                    cur_number = cur_running_res[i][0]
                    cur_number = float(format(cur_number, '.5f'))
                    cur_testing_number = cur_testing_res[i][0]
                    cur_testing_number = float(format(cur_testing_number, '.5f'))
                    print('1s_1a', cur_testing_number, cur_number)
                    if cur_number != cur_testing_number:
                        return False
            return True
        return sponsor_trained_cooperative_model_output_callback

    @classmethod
    def assistor_trained_cooperative_model_output(cls):
        def assistor_trained_cooperative_model_output_callback(data):
            test_dict = {
                "rounds_1": [
                    [13.47092],
                    [-7.71771],
                    [2.183919],
                    [11.85157]
                ],
                "rounds_2": [
                    [-1.74752106],
                    [-1.19497534],
                    [-0.87041926],
                    [-0.23935089]
                ]
            }
            
            for key in data:
                cur_running_res = data[key]
                cur_testing_res = test_dict[key]
                for i in range(len(cur_running_res)):
                    cur_number = cur_running_res[i][0]
                    cur_number = float(format(cur_number, '.5f'))
                    cur_testing_number = cur_testing_res[i][0]
                    cur_testing_number = float(format(cur_testing_number, '.5f'))
                    print('1s_1a', cur_testing_number, cur_number)
                    if cur_number != cur_testing_number:
                        return False
            return True
        return assistor_trained_cooperative_model_output_callback

    @classmethod
    def unread_test_make_result(cls):
        def unread_test_make_result_regression_regression_1s_1a(data):
            test_dict = {
                "rounds_1": [
                    [21.28509384],
                    [22.65005942],
                    [13.2916661],
                    [28.7824146]
                ],
                "rounds_2": [
                    [22.036252],
                    [21.005467],
                    [13.064913],
                    [28.00325766]
                ]
            }
            
            for key in data:
                cur_running_res = data[key]
                cur_testing_res = test_dict[key]
                for i in range(len(cur_running_res)):
                    cur_number = cur_running_res[i][0]
                    cur_number = float(format(cur_number, '.5f'))
                    cur_testing_number = cur_testing_res[i][0]
                    cur_testing_number = float(format(cur_testing_number, '.5f'))
                    print('1s_1a', cur_testing_number, cur_number)
                    if cur_number != cur_testing_number:
                        return False
            return True
        return unread_test_make_result_regression_regression_1s_1a

    @classmethod
    def unread_test_output_test(cls):
        def unread_test_output_regression_regression_1s_1a(data):
            test_dict = {
                "rounds_1": {
                    "MAD": 3.54763,
                    "RMSE": 5.21270,
                    "R2": 0.46997,
                },
                "rounds_2": {
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
                    print('1s_1a', cur_testing_number, cur_number)
                    if cur_number != cur_testing_number:
                        return False
            return True
        return unread_test_output_regression_regression_1s_1a
    
    @classmethod
    def unread_test_sponsor_match_id_test(cls):
        def unread_test_sponsor_match_id_regression_regression_1s_1a(data):
            test_dict = {
                "rounds_1": [
                    -15.62146, 
                    -7.63978, 
                    -3.17975, 
                    -3.77626
                ],
                "rounds_2": [
                    -2.13779, 
                    1.60417, 
                    -1.76595, 
                    -0.91224
                ]
            } 
            
            for key in data:
                cur_running_res = data[key]
                cur_testing_res = test_dict[key]
                for i in range(len(cur_running_res)):
                    cur_number = cur_running_res[i]
                    cur_number = float(format(cur_number, '.5f'))
                    cur_testing_number = cur_testing_res[i]
                    cur_testing_number = float(format(cur_testing_number, '.5f'))
                    print('1s_1a', cur_testing_number, cur_number)
                    if cur_number != cur_testing_number:
                        return False
            return True
        return unread_test_sponsor_match_id_regression_regression_1s_1a

    @classmethod
    def unread_test_assistor_match_id_test(cls):
        def unread_test_assistor_match_id_regression_regression_1s_1a(data):
            test_dict = {
                "rounds_1": [
                    3.93492, 
                    -1.96598, 
                    -19.51288, 
                    6.83615
                ],
                "rounds_2": [
                    -0.52504, 
                    -0.75834, 
                    -1.23748, 
                    -0.11017
                ]
            }

            for key in data:
                cur_running_res = data[key]
                cur_testing_res = test_dict[key]
                for i in range(len(cur_running_res)):
                    cur_number = cur_running_res[i]
                    cur_number = float(format(cur_number, '.5f'))
                    cur_testing_number = cur_testing_res[i]
                    cur_testing_number = float(format(cur_testing_number, '.5f'))
                    print('1s_1a', cur_testing_number, cur_number)
                    if cur_number != cur_testing_number:
                        return False
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

    def alpha(self):
        return self._unittest_strategy.alpha()

    def sponsor_trained_cooperative_model_output(self):
        return self._unittest_strategy.sponsor_trained_cooperative_model_output()

    def assistor_trained_cooperative_model_output(self):
        return self._unittest_strategy.assistor_trained_cooperative_model_output()

    def get_unread_test_make_result(self):
        return self._unittest_strategy.unread_test_make_result()

    def get_unread_test_sponsor_match_id_test(self):
        print('strategy', self._unittest_strategy)
        return self._unittest_strategy.unread_test_sponsor_match_id_test()
    
    def get_unread_test_assistor_match_id_test(self):
        return self._unittest_strategy.unread_test_assistor_match_id_test()

    def get_unread_test_output_test(self):
        return self._unittest_strategy.unread_test_output_test()
    

_default_unittest_strategy = unittest_strategy_interface()





