from __future__ import annotations

import collections

from synspot.database.base import BaseDatabase

from synspot.database.abstract_database import AbstractMetadataDatabase

from synspot.utils import DictHelper


class TrainAssistorMetadataDatabase(BaseDatabase, AbstractMetadataDatabase):
    __TrainAssistorMetadataDatabase_instance = None

    def __init__(self):
        self.__temp_database = collections.defaultdict(dict)

    @classmethod
    def get_instance(cls) -> type[TrainAssistorMetadataDatabase]:
        if cls.__TrainAssistorMetadataDatabase_instance == None:
            cls.__TrainAssistorMetadataDatabase_instance = TrainAssistorMetadataDatabase()

        return cls.__TrainAssistorMetadataDatabase_instance

    def get_all_records(self) -> list[tuple[str, str]]:
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
        # if key not in self.__temp_database:
        #     self.__temp_database[key] = collections.defaultdict(dict)

        value = {
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

        store_res = DictHelper.store_value(
            key=key,
            value=value,
            container=self.__temp_database
        )
        if store_res == True:
            return f'{self.__class__.__name__} stores {key} successfully!' 
        else:
            return f'{self.__class__.__name__} failed to stores {key}'
    
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
            raise RuntimeError('Use train_id to retrieve User_Assistor_Table')

        key = DictHelper.generate_dict_key(user_id, train_id)            

        assistor_metadata = DictHelper.get_value(
            key=key,
            container=self.__temp_database
        )

        train_id = DictHelper.get_value(
            key='train_id',
            container=assistor_metadata
        )

        mode = DictHelper.get_value(
            key='mode',
            container=assistor_metadata
        )

        task_mode = DictHelper.get_value(
            key='task_mode',
            container=assistor_metadata
        )

        model_name = DictHelper.get_value(
            key='model_name',
            container=assistor_metadata
        )

        train_file_path = DictHelper.get_value(
            key='train_file_path',
            container=assistor_metadata
        )

        train_id_column = DictHelper.get_value(
            key='train_id_column',
            container=assistor_metadata
        )

        train_data_column = DictHelper.get_value(
            key='train_data_column',
            container=assistor_metadata
        )

        task_name = DictHelper.get_value(
            key='task_name',
            container=assistor_metadata
        )

        task_description = DictHelper.get_value(
            key='task_description',
            container=assistor_metadata
        )  
        
        if not super().if_db_response_valid(
            train_id, 
            mode, 
            task_mode, 
            model_name, 
            train_file_path, 
            train_id_column, 
            train_data_column, 
            task_name, 
            task_description
        ):
            print(f'{self.__class__.__name__} does not contain the record')
            return super().dict_value_not_found()
        
        return (
            train_id, 
            mode, 
            task_mode,
            model_name, 
            train_file_path, 
            train_id_column, 
            train_data_column, 
            task_name, 
            task_description
        )
       
   