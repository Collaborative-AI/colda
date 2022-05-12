from __future__ import annotations

import collections

from synspot.database.utils import get_user_id

from typing import(
    List
)

from synspot.database.strategy import DatabaseOperator


def get_all_train_id():
    return get_all_train_id_as_sponsor() + get_all_train_id_as_assistor()

def get_all_test_id():
    return get_all_test_id_as_sponsor() + get_all_test_id_as_assistor()

def get_all_train_id_as_sponsor() -> List[str]:

    """
    start task with all assistors

    :param maxRound: Integer. Maximum training round
    :param assistors: List. The List of assistors' usernames
    :param train_file_path: String. Input path address of training data path
    :param train_id_column: String. ID column of Input File
    :param train_data_column: String. Data column of Input File
    :param train_target_column: String. Target column of Input File
    :param task_mode: String. Classification or Regression
    :param model_name: String. Specific model, such as LinearRegression, DecisionTree.
    :param metric_name: String. Metric to measure the result, such as MAD, RMSE, R2.
    :param task_name: None or String. The name of current task.
    :param task_description: None or String. The description of current task

    :returns: Tuple. Contains a string 'handleTrainRequest successfully' and the task id

    :exception OSError: Placeholder.
    """

    user_id = get_user_id()
    all_train_ids = []
    DatabaseOperator.set_database(database_type='train_sponsor_metadata')
    for record_key, record_val in DatabaseOperator.get_all_records().items():
        if user_id == record_key[0]:
            all_train_ids.append(record_val['train_id'])

    return all_train_ids

def get_all_test_id_as_sponsor() -> List[str]:

    """
    start task with all assistors

    :param maxRound: Integer. Maximum training round
    :param assistors: List. The List of assistors' usernames
    :param train_file_path: String. Input path address of training data path
    :param train_id_column: String. ID column of Input File
    :param train_data_column: String. Data column of Input File
    :param train_target_column: String. Target column of Input File
    :param task_mode: String. Classification or Regression
    :param model_name: String. Specific model, such as LinearRegression, DecisionTree.
    :param metric_name: String. Metric to measure the result, such as MAD, RMSE, R2.
    :param task_name: None or String. The name of current task.
    :param task_description: None or String. The description of current task

    :returns: Tuple. Contains a string 'handleTrainRequest successfully' and the task id

    :exception OSError: Placeholder.
    """

    user_id = get_user_id()
    all_test_ids = []
    DatabaseOperator.set_database(database_type='test_sponsor_metadata')
    for record_key, record_val in DatabaseOperator.get_all_records().items():
        if user_id == record_key[0]:
            all_test_ids.append(record_val['test_id'])

    return all_test_ids


def get_all_train_id_as_assistor() -> List[str]:

    """
    start task with all assistors

    :param maxRound: Integer. Maximum training round
    :param assistors: List. The List of assistors' usernames
    :param train_file_path: String. Input path address of training data path
    :param train_id_column: String. ID column of Input File
    :param train_data_column: String. Data column of Input File
    :param train_target_column: String. Target column of Input File
    :param task_mode: String. Classification or Regression
    :param model_name: String. Specific model, such as LinearRegression, DecisionTree.
    :param metric_name: String. Metric to measure the result, such as MAD, RMSE, R2.
    :param task_name: None or String. The name of current task.
    :param task_description: None or String. The description of current task

    :returns: Tuple. Contains a string 'handleTrainRequest successfully' and the task id

    :exception OSError: Placeholder.
    """

    user_id = get_user_id()
    all_train_ids = []
    DatabaseOperator.set_database(database_type='train_assistor_metadata')
    for record_key, record_val in DatabaseOperator.get_all_records().items():
        if user_id == record_key[0]:
            all_train_ids.append(record_val['train_id'])

    return all_train_ids

def get_all_test_id_as_assistor() -> List[str]:

    """
    start task with all assistors

    :param maxRound: Integer. Maximum training round
    :param assistors: List. The List of assistors' usernames
    :param train_file_path: String. Input path address of training data path
    :param train_id_column: String. ID column of Input File
    :param train_data_column: String. Data column of Input File
    :param train_target_column: String. Target column of Input File
    :param task_mode: String. Classification or Regression
    :param model_name: String. Specific model, such as LinearRegression, DecisionTree.
    :param metric_name: String. Metric to measure the result, such as MAD, RMSE, R2.
    :param task_name: None or String. The name of current task.
    :param task_description: None or String. The description of current task

    :returns: Tuple. Contains a string 'handleTrainRequest successfully' and the task id

    :exception OSError: Placeholder.
    """

    user_id = get_user_id()
    all_test_ids = []
    DatabaseOperator.set_database(database_type='test_assistor_metadata')
    for record_key, record_val in DatabaseOperator.get_all_records().items():
        if user_id == record_key[0]:
            all_test_ids.append(record_val['test_id'])

    return all_test_ids

def logout():
    """
    Handle user logout by setting the __temp_database to collections.defaultdict(dict)

    :returns: None

    :exception OSError: Placeholder.
    """
    try:
        self.__temp_database = collections.defaultdict(dict)
    except:
        print('Logout procedure wrong')
