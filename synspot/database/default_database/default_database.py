from __future__ import annotations

import collections

from synspot.database.base import BaseDatabase

from synspot.database.abstract_database import AbstractMetadataDatabase

from typing import (
    Type,
    List,
    Tuple
)

class DefaultMetadataDatabase(BaseDatabase, AbstractMetadataDatabase):
    __DefaultMetadataDatabase_instance = None

    def __init__(self):
        self.__temp_database = collections.defaultdict(dict)

    @classmethod
    def get_database_instance(cls) -> Type[DefaultMetadataDatabase]:
        if cls.__DefaultMetadataDatabase_instance == None:
            cls.__DefaultMetadataDatabase_instance = DefaultMetadataDatabase()

        return cls.__DefaultMetadataDatabase_instance

    def get_all_records(self) -> List[Tuple[str, str]]:

        all_records = []
        for key in self.__temp_database:
            # key is a tuple
            if len(key) >= 2:
                all_records.append(key)

        return all_records

    def store_record(
        self, 
        user_id: str, 
        default_mode: str, 
        default_task_mode: str, 
        default_model_name: str, 
        default_file_path: str = None, 
        default_id_column: str = None, 
        default_data_column: str = None
    ) -> None:

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

        if user_id not in self.__temp_database:
            self.__temp_database[user_id] = collections.defaultdict(dict)

        try:
            cur_class_name = self.__class__.__name__
            self.__temp_database[user_id]['user_id'] = user_id
            self.__temp_database[user_id]['default_mode'] = default_mode
            self.__temp_database[user_id]['default_task_mode'] = default_task_mode
            self.__temp_database[user_id]['default_model_name'] = default_model_name
            self.__temp_database[user_id]['default_file_path'] = default_file_path
            self.__temp_database[user_id]['default_id_column'] = default_id_column
            self.__temp_database[user_id]['default_data_column'] = default_data_column
        except:
            print('User_Default_Table stores false')
            return False

        return True

    def get_record(
        self, user_id: str
    ) -> None:
        
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

        cur_class_name = self.__class__.__name__
        user_id = self.__temp_database[user_id]['user_id']
        default_mode = self.__temp_database[user_id]['default_mode']
        default_task_mode = self.__temp_database[user_id]['default_task_mode']
        default_model_name = self.__temp_database[user_id]['default_model_name']
        default_file_path = self.__temp_database[user_id]['default_file_path']
        default_id_column = self.__temp_database[user_id]['default_id_column']
        default_data_column = self.__temp_database[user_id]['default_data_column'] 

        return user_id, default_mode, default_task_mode, default_model_name, default_file_path, default_id_column, default_data_column