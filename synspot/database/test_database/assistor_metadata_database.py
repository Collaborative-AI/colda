from __future__ import annotations

import collections

from synspot.database.base import BaseDatabase

from synspot.database.abstract_database import AbstractMetadataDatabase

from synspot.utils.dict_helper import DictHelper

from typing import (
    Type,
    List,
    Tuple
)


class TestAssistorMetadataDatabase(BaseDatabase, AbstractMetadataDatabase):
    __TestAssistorMetadataDatabase_instance = None

    def __init__(self):
        self.__temp_database = collections.defaultdict(dict)

    @classmethod
    def get_instance(cls) -> Type[TestAssistorMetadataDatabase]:
        if cls.__TestAssistorMetadataDatabase_instance == None:
            cls.__TestAssistorMetadataDatabase_instance = TestAssistorMetadataDatabase()

        return cls.__TestAssistorMetadataDatabase_instance

    def store_record(
        self, 
        user_id: str, 
        train_id: str, 
        mode: str, 
        task_mode: str, 
        model_name: str, 
        test_id: str, 
        test_file_path: str, 
        test_id_column: str, 
        test_data_column: str,
        test_name: str=None, 
        test_description: str=None, 
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

        
        key = DictHelper.generate_dict_key(user_id, test_id)
        if key not in self.__temp_database:
            self.__temp_database[key] = collections.defaultdict(dict)

        value = {
            'user_id': user_id,
            'train_id': train_id,
            'mode': mode,
            'task_mode': task_mode,
            'model_name': model_name,
            'test_id': test_id,
            'test_file_path': test_file_path,
            'test_id_column': test_id_column,
            'test_data_column': test_data_column,
            'test_name': test_name,
            'test_description': test_description
        }
        DictHelper.store_value(
            key=key,
            value=value,
            container=self.__temp_database
        )
            
        return 'User_Assistor_Table stores successfully'
    
    def get_all_records(self) -> List[Tuple[str, str]]:

        all_records = []
        for key in self.__temp_database:
            # key is a tuple
            if len(key) >= 2:
                all_records.append(key)

        return all_records

    def get_record(
        self, 
        user_id: str, 
        test_id: str,
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

        if not not test_id:
            raise RuntimeError('Use task_id or test_id to retrieve User_Assistor_Table')

        key = DictHelper.generate_dict_key(user_id, test_id)
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
        test_id = assistor_metadata['test_id']
        test_file_path = assistor_metadata['test_file_path']
        test_id_column = assistor_metadata['test_id_column']
        test_data_column = assistor_metadata['test_data_column']
        test_name = assistor_metadata['test_name']
        test_description = assistor_metadata['test_description'] 

        return train_id, mode, task_mode, model_name, test_name, test_description, test_file_path, test_id_column, test_data_column
    