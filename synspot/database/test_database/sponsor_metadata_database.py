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


class TestSponsorMetadataDatabase(BaseDatabase, AbstractMetadataDatabase):
    __TestSponsorMetadataDatabase_instance = None

    def __init__(self):
        self.__temp_database = collections.defaultdict(dict)

    @classmethod
    def get_database_instance(cls) -> Type[TestSponsorMetadataDatabase]:
        if cls.__TestSponsorMetadataDatabase_instance == None:
            cls.__TestSponsorMetadataDatabase_instance = TestSponsorMetadataDatabase()

        return cls.__TestSponsorMetadataDatabase_instance

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

        
        self.__temp_database[key]['user_id'] = user_id
        self.__temp_database[key]['train_id'] = train_id
        self.__temp_database[key]['mode'] = mode
        self.__temp_database[key]['task_mode'] = task_mode
        self.__temp_database[key]['model_name'] = model_name
        self.__temp_database[key]['test_id'] = test_id
        self.__temp_database[key]['test_file_path'] = test_file_path
        self.__temp_database[key]['test_id_column'] = test_id_column
        self.__temp_database[key]['test_data_column'] = test_data_column
        self.__temp_database[key]['test_name'] = test_name
        self.__temp_database[key]['test_description'] = test_description
        value = {
            'user_id': user_id,
            'train_id': train_id,
            'task_mode': task_mode,
            'model_name': model_name,
            'metric_name': metric_name,
            'train_file_path': train_file_path,
            'train_id_column': train_id_column,
            'train_data_column': train_data_column,
            'train_target_column': train_target_column,
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

        if not test_id:
            raise RuntimeError('Use test_id to retrieve User_Assistor_Table')

        key = generate_database_key(user_id, test_id)
        cur_class_name = self.__class__.__name__
        if key not in self.__temp_database:
            print(f'{cur_class_name} does not contain the record')

        try:

            user_id = self.__temp_database[key]['user_id']
            train_id = self.__temp_database[key]['train_id']
            mode = self.__temp_database[key]['mode']
            task_mode = self.__temp_database[key]['task_mode']
            model_name = self.__temp_database[key]['model_name']
            test_id = self.__temp_database[key]['test_id']
            test_file_path = self.__temp_database[key]['test_file_path']
            test_id_column = self.__temp_database[key]['test_id_column']
            test_data_column = self.__temp_database[key]['test_data_column']
            test_name = self.__temp_database[key]['test_name']
            test_description = self.__temp_database[key]['test_description']
            
        except:
            print('get User_Assistor_Table false')

        return train_id, mode, task_mode, model_name, test_name, test_description, test_file_path, test_id_column, test_data_column
    