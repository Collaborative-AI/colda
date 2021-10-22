"""
py_pkg
~~~~~~

The py_pkg package - a Python package template project that is intended
to be used as a cookie-cutter for developing new Python packages.
"""
from global_class import global_class
# import jwt
_default_apollo_system = global_class()

def callForTrain(maxRound: int, assistors: list, training_data_path: str):
    trainRequest_instance = _default_apollo_system.get_TrainRequest_instance()
    trainRequest_instance.handleTrainRequest(maxRound, assistors, training_data_path)

    return

def callForTest(task_id: str, testing_data_path: str):
    testRequest_instance = _default_apollo_system.get_TestRequest_instance()
    testRequest_instance.handleTestRequest(task_id, testing_data_path)

    return

def ceshi(aa):
    trainRequest_instance = _default_apollo_system.get_TrainRequest_instance()
    trainRequest_instance.unread_request(aa)


# Call Authorization
def userRegister(username: str, password: str):
    authorization_instance = _default_apollo_system.get_Authorization_instance()
    authorization_instance.userRegister(username, password)

    return

def userLogin(username: str, password: str):
    authorization_instance = _default_apollo_system.get_Authorization_instance()
    authorization_instance.userLogin(username, password)

    return

def userLogout():
    authorization_instance = _default_apollo_system.get_Authorization_instance()
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

# userLogin("testa", "123")
ceshi({"a": "a"})