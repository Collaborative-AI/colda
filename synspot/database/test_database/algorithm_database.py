from __future__ import annotations

import collections

from synspot.database.base import BaseDatabase

from synspot.database.abstract_database import AbstractAlgorithmDatabase

from synspot.database.utils import (
    generate_database_key
)

from typing import (
    Type,
    List,
    Tuple,
    Union,
    Any
)


class TestAlgorithmDatabase(BaseDatabase, AbstractAlgorithmDatabase):
    __TestAlgorithmDatabase_instance = None

    def __init__(self):
        self.__temp_database = collections.defaultdict(dict)

    @classmethod
    def get_database_instance(cls) -> Type[TestAlgorithmDatabase]:
        if cls.__TestAlgorithmDatabase_instance == None:
            cls.__TestAlgorithmDatabase_instance = TestAlgorithmDatabase()

        return cls.__TestAlgorithmDatabase_instance

    def store_record(
        self, 
        user_id: str, 
        task_id: str, 
        algorithm_data_name: str,
        algorithm_data: Union(List[str], List[List[str]], Any),
    ) -> None:
        
        """
        start task with all assistors

        :param maxRound: Integer. Maximum training round
        :param assistors: List. The List of assistors' usernames

        :returns: Tuple. Contains a string 'handleTrainRequest successfully' and the task id

        :exception OSError: Placeholder.
        """

        try:
            key = generate_database_key(user_id, task_id)
            if key not in self.__temp_database:
                self.__temp_database[key] = collections.defaultdict(dict)

            self.__temp_database[key][algorithm_data_name] = algorithm_data
        except:
            print('User_Assistor_Table stores false')
        return 'User_Assistor_Table stores successfully'
    
    def get_record(
        self, 
        user_id: str, 
        task_id: str, 
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

        if not task_id:
            raise RuntimeError('Use task_id or test_id to retrieve User_Assistor_Table')
        if not algorithm_data_name:
            print('placeholder')
            
        key = generate_database_key(user_id, task_id)
        if key not in self.__temp_database:
            print(f'{self.__class__.__name__} does not contain the record')

        try:
            algorithm_data = self.__temp_database[key][algorithm_data_name]
        except:
            print('get User_Assistor_Table false')

        return algorithm_data
       
   