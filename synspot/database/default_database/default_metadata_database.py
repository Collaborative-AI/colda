from __future__ import annotations

import collections

from synspot.database.base import BaseDatabase

from synspot.database.abstract_database import AbstractMetadataDatabase

from synspot.utils import DictHelper


class DefaultMetadataDatabase(BaseDatabase, AbstractMetadataDatabase):
    __DefaultMetadataDatabase_instance = None

    def __init__(self):
        self.__temp_database = collections.defaultdict(dict)

    @classmethod
    def get_database_instance(cls) -> type[DefaultMetadataDatabase]:
        if cls.__DefaultMetadataDatabase_instance == None:
            cls.__DefaultMetadataDatabase_instance = DefaultMetadataDatabase()

        return cls.__DefaultMetadataDatabase_instance

    def get_all_records(self) -> list[tuple[str, str]]:
        return DictHelper.get_all_key_value_pairs(container=self.__temp_database)

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

        value = {
            'default_mode': default_mode,
            'default_task_mode': default_task_mode,
            'default_model_name': default_model_name,
            'default_file_path': default_file_path,
            'default_id_column': default_id_column,
            'default_data_column': default_data_column,
        }
        DictHelper.store_value(
            key=user_id,
            value=value,
            container=self.__temp_database
        )

        return True

    def get_record(
        self, user_id: str
    ) -> tuple[str]:
        
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

        key = user_id
        if key not in self.__temp_database:
            print(f'{self.__class__.__name__} does not contain the record')

        default_metadata = DictHelper.get_value(
            key=key,
            container=self.__temp_database
        )

        default_mode = DictHelper.get_value(
            key='default_mode',
            container=default_metadata
        )

        default_task_mode = DictHelper.get_value(
            key='default_task_mode',
            container=default_metadata
        )

        default_model_name = DictHelper.get_value(
            key='default_model_name',
            container=default_metadata
        )

        default_file_path = DictHelper.get_value(
            key='default_file_path',
            container=default_metadata
        )

        default_id_column = DictHelper.get_value(
            key='default_id_column',
            container=default_metadata
        )

        default_data_column = DictHelper.get_value(
            key='default_data_column',
            container=default_metadata
        )

        return default_mode, default_task_mode, default_model_name, default_file_path, default_id_column, default_data_column