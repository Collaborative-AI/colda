"""
synspot
~~~~~~

The synspot package - a Python package template project that is intended
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

from .TrainRequest import TrainRequest
from .TestRequest import TestRequest
from synspot.authorization import Authorization
from .GetNotification import GetNotification
from synspot.database import Database
from synspot.network import Network
from synspot.personalinformation import PersonalInformation
# from .Database_class_helper import database_strategy_interface
# from Algorithm import log
# from .Network import Network
# from synspot import TrainRequest, PersonalInformation
# from synspot import Authorization
# from synspot import TestRequest
# from synspot import Get_Notification
# from synspot import Database_class
import threading

_default_authorization = Authorization.get_Authorization_instance()
_default_trainRequest = TrainRequest.get_TrainRequest_instance()
_default_testRequest = TestRequest.get_TestRequest_instance()
_default_getNotification = GetNotification.get_GetNotification_instance()
_default_network = Network.get_Network_instance()
_default_personalinformation = PersonalInformation.get_PersonalInformation_instance()
_default_database = Database.get_Database_instance()

def userRegister(username: str, email: str, password: str):
    return _default_authorization.userRegister(username, password)
    
    
def userLogin(username: str, password: str):
    res = _default_authorization.userLogin(username, password)
    print('ressss', res)
    return res

def userLogout():
    """
    Handle user logout

    :returns: None

    :exception OSError: Placeholder.
    """
    return _default_authorization.userLogout()

def callForTrain(maxRound: int, assistors: list, train_file_path: str, train_id_column: str, train_data_column: str, 
                            train_target_column: str, task_mode: str, model_name: str, metric_name: str, task_name: str=None, task_description: str=None):
    trainRequest_instance = _default_trainRequest.get_TrainRequest_instance()
    trainRequest_instance.handleTrainRequest(maxRound=maxRound, assistors=assistors, train_file_path=train_file_path, train_id_column=train_id_column, 
                            train_data_column=train_data_column, train_target_column=train_target_column, task_mode=task_mode, model_name=model_name, 
                            metric_name=metric_name, task_name=task_name, task_description=task_description)
    return

def callForTest(task_id: str, test_file_path: str, test_id_column: str, test_data_column: str, 
                            test_target_column: str, test_name: str=None, test_description: str=None):
    testRequest_instance = _default_testRequest.get_TestRequest_instance()
    testRequest_instance.handleTestRequest(task_id=task_id, test_file_path=test_file_path, test_id_column=test_id_column, test_data_column=test_data_column, 
                            test_target_column=test_target_column, test_name=test_name, test_description=test_description)
    return

def start_Collaboration():
    _default_getNotification.start_Collaboration()
    return

def end_Collaboration():
    return _default_getNotification.end_Collaboration()
    

def set_default_data_path(default_mode: str, default_task_mode: str, default_model_name: str, default_file_path: str=None, default_id_column: str=None, default_data_column: str=None):
    PersonalInformation_instance = PersonalInformation.get_PersonalInformation_instance()
    user_id = PersonalInformation_instance.user_id
    if user_id == None:
        return 'Please Login first'
    PersonalInformation_instance.default_mode = default_mode
    return _default_database.store_User_Default_Table(user_id=user_id, default_mode=default_mode, default_task_mode=default_task_mode, default_model_name=default_model_name,
                                                    default_file_path=default_file_path, default_id_column=default_id_column, default_data_column=default_data_column)
    
def clean_db():
    base_url = _default_network.base_url
    url = base_url + "/delete_all_rows/"
    try:
        delete_db_res = requests.get(url)
    except:
        print('delete_db_res wrong')

def get_all_task_id_as_sponsor():
    try:
        res = _default_database.get_all_task_id_as_sponsor()
        print('resff', res)
    except:
        print('get_all_task_id_as_sponsor wrong')
    else:
        return res
    
def get_all_test_id_as_sponsor():
    try:
        res = _default_database.get_all_test_id_as_sponsor()
    except:
        print('get_all_test_id_as_sponsor wrong')
    else:
        return res

def get_all_task_id_as_assistor():
    try:
        res = _default_database.get_all_task_id_as_assistor()
    except:
        print('get_all_task_id_as_assistor wrong')
    else:
        return res

def get_all_test_id_as_assistor():
    try:
        res = _default_database.get_all_test_id_as_assistor()
    except:
        print('get_all_test_id_as_assistor wrong')
    else:
        return res

def get_all_task_id():
    return get_all_task_id_as_sponsor() + get_all_task_id_as_assistor()

def get_all_test_id():
    return get_all_test_id_as_sponsor() + get_all_test_id_as_assistor()

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

def get_pending_requests():
    pass
    
def get_online_user(username: list):
    pass

def test_function():
    return 'test successfully' 
# userLogin("xie2", "Xie2@123")
# set_default_data_path("/Users/qile/Documents/data/BostonHousing/2/123/0.5/0/train/data.csv", "1", "2")
# callForTrain(2, [2], "/Users/qile/Documents/data/combine.csv", "1", "2-7", "8")



