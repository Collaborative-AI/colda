from __future__ import annotations

import collections

from synspot.database.base import BaseDatabase

from synspot.database.abstract_database import AbstractMetadataDatabase

from synspot.database.utils import (
    generate_database_key
)

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
        task_id: str, 
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

        try:
            key = generate_database_key(user_id, test_id)
            if key not in self.__temp_database:
                self.__temp_database[key] = collections.defaultdict(dict)

            cur_class_name = self.__class__.__name__
            self.__temp_database[key]['user_id'] = user_id
            self.__temp_database[key]['task_id'] = task_id
            self.__temp_database[key]['mode'] = mode
            self.__temp_database[key]['task_mode'] = task_mode
            self.__temp_database[key]['model_name'] = model_name
            self.__temp_database[key]['test_id'] = test_id
            self.__temp_database[key]['test_file_path'] = test_file_path
            self.__temp_database[key]['test_id_column'] = test_id_column
            self.__temp_database[key]['test_data_column'] = test_data_column
            self.__temp_database[key]['test_name'] = test_name
            self.__temp_database[key]['test_description'] = test_description
            
        except:
            print('User_Assistor_Table stores false')
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

        if not task_id and not test_id:
            raise RuntimeError('Use task_id or test_id to retrieve User_Assistor_Table')

        key = generate_database_key(user_id, test_id)
        cur_class_name = self.__class__.__name__
        if key not in self.__temp_database:
            print(f'{cur_class_name} does not contain the record')

        try:

            user_id = self.__temp_database[key]['user_id']
            task_id = self.__temp_database[key]['task_id']
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

        return mode, task_mode, model_name, test_name, test_description, test_file_path, test_id_column, test_data_column
    