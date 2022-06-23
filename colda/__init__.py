from __future__ import annotations
from asyncio import Task

"""
colda
~~~~~~

The colda package - a Python package template project that is intended
to be used as a cookie-cutter for developing new Python packages.
"""
# import os
# basedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Algorithm')
# print("--", basedir)
# import sys
# sys.path.append(basedir)
import os
import time
import errno
import pickle
import requests
# import Algorithm

# import colda

from colda.authentication.api import Authentication
from colda.short_polling.polling import ShortPolling
from colda.database.strategy.api import DatabaseOperator
from colda.network.api import Network
from colda.pi.api import PI

from colda.algorithm.custom.api import (
    GetTrainFixedParameter,
    GetTrainOptimizedParameter,
    GetTrainOwnFunction,
    GetTestFixedParameter,
    GetTestOptimizedParameter,
    GetTestOwnFunction
)

from colda.algorithm.strategy.api import (
    TrainAlgorithm,
    TestAlgorithm
)

from colda.workflow import (
    TrainMainWorkflow,
    TestMainWorkflow
)

from colda.utils.log import (
    GetAlgorithmLog,
    GetWorkflowLog
)

from typing import (
    Callable
)

from colda._typing import (
    Mode,
    Task_Mode,
    Model_Name,
    Metric_Name
)
    
_default_train_algo = TrainAlgorithm.get_instance()
_default_test_algo = TestAlgorithm.get_instance()
_default_network = Network.get_instance()
_default_PI = PI.get_instance()
_default_DatabaseOperator = DatabaseOperator.get_instance()
_default_authentication = Authentication.get_instance()
_default_TrainMainWorkflow = TrainMainWorkflow.get_instance()
_default_TestMainWorkflow = TestMainWorkflow.get_instance()
_default_ShortPolling = ShortPolling.get_instance()
_default_network = Network.get_instance()
_default_PI = PI.get_instance()
_default_algo_log = GetAlgorithmLog.get_log()
_default_workflow_log = GetWorkflowLog.get_log()

from colda.database.api import (
    get_all_train_id_as_sponsor,
    get_all_test_id_as_sponsor,
    get_all_train_id_as_assistor,
    get_all_test_id_as_assistor,
    get_all_train_id,
    get_all_test_id
)


def userRegister(
    username: str, 
    email: str, 
    password: str
) -> bool:

    return _default_authentication.userRegister(
        username=username, 
        email=email,
        password=password)
    
def userLogin(
    username: str, 
    password: str
) -> bool:
    return _default_authentication.userLogin(
        username=username, 
        password=password)

def userLogout():
    """
    Handle user logout

    :returns: None

    :exception OSError: Placeholder.
    """
    return _default_authentication.userLogout()

def callForTrain(
    maxRound: int, 
    assistors: list, 
    task_mode: Task_Mode, 
    model_name: Model_Name, 
    metric_name: Metric_Name,
    train_file_path: str, 
    train_id_column: str, 
    train_data_column: str, 
    train_target_column: str, 
    task_name: str = None, 
    task_description: str = None
) -> bool:

    return _default_TrainMainWorkflow.find_assistor(
        maxRound=maxRound, 
        assistors=assistors, 
        task_mode=task_mode, 
        model_name=model_name, 
        metric_name=metric_name, 
        train_file_path=train_file_path, 
        train_id_column=train_id_column, 
        train_data_column=train_data_column, 
        train_target_column=train_target_column, 
        task_name=task_name, 
        task_description=task_description
    )
    

def callForTest(
    train_id: str, 
    test_file_path: str, 
    test_id_column: str, 
    test_data_column: str, 
    test_target_column: str, 
    test_name: str = None, 
    test_description: str = None
) -> bool:

    _default_TestMainWorkflow.find_test_assistor(
        train_id=train_id, 
        test_file_path=test_file_path, 
        test_id_column=test_id_column, 
        test_data_column=test_data_column, 
        test_target_column=test_target_column, 
        test_name=test_name, 
        test_description=test_description
    )
    return

def start_Collaboration():
    _default_ShortPolling.start_cooperation()
    return

def end_Collaboration():
    return _default_ShortPolling.end_cooperation()

def set_default_data_path(
    default_mode: Mode, 
    default_task_mode: Task_Mode, 
    default_model_name: Model_Name, 
    default_file_path: str = None, 
    default_id_column: str = None, 
    default_data_column: str = None
) -> None:

    PI_instance = PI.get_instance()
    user_id = PI_instance.user_id
    if user_id == None:
        return 'Please Login first'
    PI_instance.default_mode = default_mode
    _default_DatabaseOperator.set_database(database_type='default_metadata')
    return _default_DatabaseOperator.store_record(
        user_id=user_id, 
        default_mode=default_mode, 
        default_task_mode=default_task_mode, 
        default_model_name=default_model_name,
        default_file_path=default_file_path, 
        default_id_column=default_id_column, 
        default_data_column=default_data_column
    )

def store_database(path, mode='pickle'):
    dirname = os.path.dirname(path)
    input = _default_database
    try:
        os.makedirs(path)
    except OSError as e:
        if e.errno == errno.EEXIST:
            pass
        else:
            raise
    if mode == 'pickle':
        pickle.dump(input, open(path, 'wb'))
    else:
        raise ValueError('Not valid save mode')
    return True




# https://juejin.cn/post/6844903503660335112
def set_train_stage_custom_handler(
    handler_type: str = 'fixedParameter',
    OwnFunction: dict[str, Callable] = None
):

    if handler_type == 'fixedParameter':
        custom = GetTrainFixedParameter.get_class()
    elif handler_type == 'optimizerTrainedParameter':
        custom = GetTrainOptimizedParameter.get_class()
    elif handler_type == 'ownFunctionParameter':
        GetTrainOwnFunction.get_class().OwnFunction = OwnFunction
        custom = GetTrainOwnFunction.get_class()

    _default_train_algo.train_custom = custom
    return


def set_test_stage_custom_handler(
    handler_type: str = 'fixedParameter', 
    OwnFunction: dict[str, Callable] = None
):

    if handler_type == 'fixedParameter':
        custom = GetTestFixedParameter.get_instance()
    elif handler_type == 'optimizerTrainedParameter':
        custom = GetTestOptimizedParameter.get_instance()
    elif handler_type == 'ownFunctionParameter':
        GetTestOwnFunction.get_class().OwnFunction = OwnFunction
        custom = GetTestOwnFunction.get_class()
    
    _default_test_algo.test_custom = custom
    return


def get_pending_requests():
    pass
    
def get_online_user(username: list):
    pass

# def test_function():
#     return 'test successfully' 
# # userLogin("xie2", "Xie2@123")
# # set_default_data_path("/Users/qile/Documents/data/BostonHousing/2/123/0.5/0/train/data.csv", "1", "2")
# # callForTrain(2, [2], "/Users/qile/Documents/data/combine.csv", "1", "2-7", "8")



