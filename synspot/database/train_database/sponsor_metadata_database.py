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


class TrainSponsorMetadataDatabase(BaseDatabase, AbstractMetadataDatabase):
    __TrainSponsorMetadataDatabase_instance = None

    def __init__(self):
        self.__temp_database = collections.defaultdict(dict)

    @classmethod
    def get_database_instance(cls) -> Type[TrainSponsorMetadataDatabase]:
        if cls.__TrainSponsorMetadataDatabase_instance == None:
            cls.__TrainSponsorMetadataDatabase_instance = TrainSponsorMetadataDatabase()

        return cls.__TrainSponsorMetadataDatabase_instance

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
        task_mode: str, 
        model_name: str, 
        metric_name: str,
        train_file_path: str, 
        train_id_column: str, 
        train_data_column: str, 
        train_target_column: str,
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

        try:
            key = generate_database_key(user_id, task_id)
            if key not in self.__temp_database:
                self.__temp_database[key] = collections.defaultdict(dict)

            self.__temp_database[key]['user_id'] = user_id
            self.__temp_database[key]['task_id'] = task_id
            self.__temp_database[key]['task_mode'] = task_mode
            self.__temp_database[key]['model_name'] = model_name
            self.__temp_database[key]['metric_name'] = metric_name

            self.__temp_database[key]['train_file_path'] = train_file_path
            self.__temp_database[key]['train_id_column'] = train_id_column
            self.__temp_database[key]['train_data_column'] = train_data_column
            self.__temp_database[key]['train_target_column'] = train_target_column

            self.__temp_database[key]['task_name'] = task_name
            self.__temp_database[key]['task_description'] = task_description
            
        except:
            print('User_Assistor_Table stores false')
        return 'User_Assistor_Table stores successfully'
    
    def get_record(
        self, 
        user_id: str, 
        task_id: str, 
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

        key = generate_database_key(user_id, task_id)
        cur_class_name = self.__class__.__name__
        if key not in self.__temp_database:
            print(f'{cur_class_name} does not contain the record')

        try:
            user_id = self.__temp_database[key]['user_id']
            task_id = self.__temp_database[key]['task_id']
            task_mode = self.__temp_database[key]['task_mode']
            model_name = self.__temp_database[key]['model_name']
            metric_name = self.__temp_database[key]['metric_name']

            train_file_path = self.__temp_database[key]['train_file_path']
            train_id_column = self.__temp_database[key]['train_id_column']
            train_data_column = self.__temp_database[key]['train_data_column']
            train_target_column = self.__temp_database[key]['train_target_column']

            task_name = self.__temp_database[key]['task_name']
            task_description = self.__temp_database[key]['task_description']     
        except:
            print('get User_Assistor_Table false')

        return task_mode, model_name, metric_name, train_file_path, train_id_column, train_data_column, train_target_column, task_name, task_description, 
       
   