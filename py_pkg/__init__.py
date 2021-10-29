"""
py_pkg
~~~~~~

The py_pkg package - a Python package template project that is intended
to be used as a cookie-cutter for developing new Python packages.
"""
# import os
# basedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Algorithm')
# print("--", basedir)
# import sys
# sys.path.append(basedir)

import numpy as np
from Authorization import Authorization
from TrainRequest import TrainRequest
from TestRequest import TestRequest
from Get_Notification import Get_Notification

import threading

# import jwt
_default_authorization = Authorization.get_Authorization_instance()
_default_trainRequest = TrainRequest.get_TrainRequest_instance()
_default_testRequest = TestRequest.get_TestRequest_instance()
_default_get_notification = Get_Notification.get_Get_notification_instance()

def callForTrain(maxRound: int, assistors: list, train_file_path: str, train_id_column: str, train_data_column: str, train_target_column: str, task_name: str=None, task_description: str=None):
    trainRequest_instance = _default_trainRequest.get_TrainRequest_instance()
    trainRequest_instance.handleTrainRequest(maxRound, assistors, train_file_path, train_id_column, train_data_column, train_target_column)

    return

def callForTest(task_id: str, testing_data_path: str):
    testRequest_instance = _default_testRequest.get_TestRequest_instance()
    testRequest_instance.handleTestRequest(task_id, testing_data_path)

    return

# def ceshi(aa):
#     trainRequest_instance = _default_apollo_system.get_TrainRequest_instance()
#     trainRequest_instance.unread_request(aa)


# Call Authorization
def userRegister(username: str, password: str):
    _default_authorization.userRegister(username, password)

    return

def userLogin(username: str, password: str):
    _default_authorization.userLogin(username, password)
    # _default_get_notification.getNotification()
    # timer = threading.Timer(2, _default_get_notification.getNotification())
    # timer.start()

    return

def userLogout():
    authorization_instance = _default_authorization.get_Authorization_instance()
    authorization_instance.userLogout()

    return

def get_online_user(username: list):
    pass


def get_all_training_tasks():
    pass


def get_all_testing_tasks():
    pass


def get_pending_requests():
    pass
#

userLogin("testa", "123")
callForTrain(1, [2], "/Users/qile/Documents/data/BostonHousing/1/123/1.0/0/train/data.csv", "1", "2", "3")
# callForTrain(3,[2], '/Users/qile/Documents/data/BostonHousing/1/123/1.0/0/train/data.csv',"1","2","3")
# address = '/Users/qile/Documents/data/BostonHousing/1/123/1.0/0/train/data.csv'
# a = np.genfromtxt(address, delimiter=',')
# print(a, type(a))


