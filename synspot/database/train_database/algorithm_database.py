from __future__ import annotations

import collections

from synspot.database.base import BaseDatabase

from synspot.database.abstract_database import AbstractAlgorithmDatabase

from synspot.utils import DictHelper

from typing import (
    Union,
    Any
)


class TrainAlgorithmDatabase(BaseDatabase, AbstractAlgorithmDatabase):
    __TrainAlgorithmDatabase_instance = None

    def __init__(self):
        self.__temp_database = collections.defaultdict(dict)

    @classmethod
    def get_database_instance(cls) -> type[TrainAlgorithmDatabase]:
        if cls.__TrainAlgorithmDatabase_instance == None:
            cls.__TrainAlgorithmDatabase_instance = TrainAlgorithmDatabase()

        return cls.__TrainAlgorithmDatabase_instance

    def store_record(
        self, 
        user_id: str, 
        train_id: str, 
        algorithm_data_name: str,
        algorithm_data: Union(list[str], list[list[str]], Any),
    ) -> None:
        
        """
        start task with all assistors

        :param maxRound: Integer. Maximum training round
        :param assistors: List. The List of assistors' usernames

        :returns: Tuple. Contains a string 'handleTrainRequest successfully' and the task id

        :exception OSError: Placeholder.
        """

        key = DictHelper.generate_dict_key(user_id, train_id)
        if key not in self.__temp_database:
            self.__temp_database[key] = collections.defaultdict(dict)
        
        value = {
            algorithm_data_name: algorithm_data
        }
        DictHelper.store_value(
            key=key,
            value=value,
            container=self.__temp_database
        )
            
        return 'User_Assistor_Table stores successfully'
    
    def get_record(
        self, 
        user_id: str, 
        train_id: str, 
        algorithm_data_name: str,
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

        if not train_id:
            raise RuntimeError('Use train_id or test_id to retrieve User_Assistor_Table')
        if not algorithm_data_name:
            print('placeholder')
            
        key = DictHelper.generate_dict_key(user_id, train_id)
        if key not in self.__temp_database:
            print(f'{self.__class__.__name__} does not contain the record')

        algorithm_data = DictHelper.get_value(
            key=algorithm_data_name,
            container=self.__temp_database[key]
        )

        return algorithm_data
       
   