from __future__ import annotations

import collections

from pyrsistent import T

from synspot.database.base import BaseDatabase

from synspot.database.abstract_database import AbstractMetadataDatabase

from synspot.utils import DictHelper

from typing import (
    Type,
    List,
    Tuple
)


class TrainAssistorMetadataDatabase(BaseDatabase, AbstractMetadataDatabase):
    __TrainAssistorMetadataDatabase_instance = None

    def __init__(self):
        self.__temp_database = collections.defaultdict(dict)

    @classmethod
    def get_database_instance(cls) -> Type[TrainAssistorMetadataDatabase]:
        if cls.__TrainAssistorMetadataDatabase_instance == None:
            cls.__TrainAssistorMetadataDatabase_instance = TrainAssistorMetadataDatabase()

        return cls.__TrainAssistorMetadataDatabase_instance

    def get_all_records(self) -> List[Tuple[str, str]]:
        return DictHelper.get_all_key_value_pairs(container=self.__temp_database)

    def store_record(
        self, 
        user_id: str, 
        train_id: str, 
        mode: str, 
        task_mode: str, 
        model_name: str, 
        train_file_path: str, 
        train_id_column: str, 
        train_data_column: str, 
        task_name: str = None, 
        task_description: str = None,  
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


        key = DictHelper.generate_dict_key(user_id, train_id)
        if key not in self.__temp_database:
            self.__temp_database[key] = collections.defaultdict(dict)

        value = {
            'user_id': user_id,
            'train_id': train_id,
            'mode': mode,
            'task_mode': task_mode,
            'model_name': model_name,
            'train_file_path': train_file_path,
            'train_id_column': train_id_column,
            'train_data_column': train_data_column,
            'task_name': task_name,
            'task_description': task_description
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

        key = DictHelper.generate_dict_key(user_id, train_id)
        if key not in self.__temp_database:
            print(f'{self.__class__.__name__} does not contain the record')

        assistor_metadata = DictHelper.get_value(
            key=key,
            container=self.__temp_database
        )
        user_id = assistor_metadata['user_id']
        train_id = assistor_metadata['train_id']
        mode = assistor_metadata['mode']
        task_mode = assistor_metadata['task_mode']
        model_name = assistor_metadata['model_name']
        train_file_path = assistor_metadata['train_file_path']
        train_id_column = assistor_metadata['train_id_column']
        train_data_column = assistor_metadata['train_data_column']
        task_name = assistor_metadata['task_name']
        task_description = assistor_metadata['task_description']     
        
        return train_id, mode, task_mode, model_name, task_name, task_description, train_file_path, train_id_column, train_data_column
       
   