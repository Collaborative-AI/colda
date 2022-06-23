from __future__ import annotations

import collections

from colda.database.base import BaseDatabase

from colda.database.abstract_database import AbstractMetadataDatabase
from colda._typing import (
    Task_Mode,
    Model_Name,
    Metric_Name
)
from colda.utils import DictHelper

from typeguard import typechecked


#@typechecked
class TrainSponsorMetadataDatabase(BaseDatabase, AbstractMetadataDatabase):
    '''
    Store and manage data generated from sponsor train stage.

    Attributes
    ----------
    None

    Methods
    -------
    get_instance
    get_all_records
    store_record
    get_record
    '''

    __TrainSponsorMetadataDatabase_instance = None

    def __init__(self):
        self.__temp_database = collections.defaultdict(dict)

    @classmethod
    def get_instance(cls) -> type[TrainSponsorMetadataDatabase]:
        '''
        Singleton pattern. 
        Get instance of current class.

        Parameters
        ----------
        None

        Returns
        -------
        type[TrainSponsorMetadataDatabase]
        '''
        if cls.__TrainSponsorMetadataDatabase_instance == None:
            cls.__TrainSponsorMetadataDatabase_instance = TrainSponsorMetadataDatabase()

        return cls.__TrainSponsorMetadataDatabase_instance

    def get_all_records_history(self) -> list[tuple[str, str]]:
        '''
        Return all keys of records in this database

        Parameters
        ----------
        None

        Returns
        -------
        list[tuple[str, str]]
        '''
        return DictHelper.get_all_key_value_pairs(container=self.__temp_database)
        
    def store_record(
        self, 
        user_id: str, 
        train_id: str, 
        task_mode: Task_Mode, 
        model_name: Model_Name, 
        metric_name: Metric_Name,
        train_file_path: str, 
        train_id_column: str, 
        train_data_column: str, 
        train_target_column: str,
        task_name: str=None, 
        task_description: str=None,  
    ) -> None:
        '''
        Store record

        Parameters
        ----------
        user_id : str
        train_id : str 
        task_mode : Task_Mode
        model_name : Model_Name 
        metric_name : Metric_Name
        train_file_path : str
        train_id_column : str 
        train_data_column : str 
        train_target_column : str
        task_name : str=None 
        task_description : str=None  

        Returns
        -------
        None
        '''
        key = DictHelper.generate_unique_dict_key(user_id, train_id)
        temp_key = str(key)
    
        value = {
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
        store_res = DictHelper.store_value(
            key=key,
            value=value,
            container=self.__temp_database
        )
        if store_res == True:
            return f'{self.__class__.__name__} stores {temp_key} successfully!' 
        else:
            return store_res
    
    def get_record(
        self, 
        user_id: str, 
        train_id: str, 
    ) -> None:
        '''
        Get record

        Parameters
        ----------
        user_id : str
        train_id : str 

        Returns
        -------
        None
        '''
        if not train_id:
            raise RuntimeError('Use train_id or test_id to retrieve User_Assistor_Table')

        key = DictHelper.generate_unique_dict_key(user_id, train_id)
        cur_class_name = self.__class__.__name__
        # if key not in self.__temp_database:
        #     print(f'{cur_class_name} does not contain the record')

        sponsor_metadata = DictHelper.get_value(
            key=key,
            container=self.__temp_database
        )

        train_id = DictHelper.get_value(
            key='train_id',
            container=sponsor_metadata
        )

        task_mode = DictHelper.get_value(
            key='task_mode',
            container=sponsor_metadata
        )

        model_name = DictHelper.get_value(
            key='model_name',
            container=sponsor_metadata
        )

        metric_name = DictHelper.get_value(
            key='metric_name',
            container=sponsor_metadata
        )

        train_file_path = DictHelper.get_value(
            key='train_file_path',
            container=sponsor_metadata
        )

        train_id_column = DictHelper.get_value(
            key='train_id_column',
            container=sponsor_metadata
        )

        train_data_column = DictHelper.get_value(
            key='train_data_column',
            container=sponsor_metadata
        )

        train_target_column = DictHelper.get_value(
            key='train_target_column',
            container=sponsor_metadata
        )

        task_name = DictHelper.get_value(
            key='task_name',
            container=sponsor_metadata
        )

        task_description = DictHelper.get_value(
            key='task_description',
            container=sponsor_metadata
        )

        if not super().if_db_response_valid(
            train_id,
            task_mode, 
            model_name, 
            metric_name, 
            train_file_path, 
            train_id_column, 
            train_data_column, 
            train_target_column, 
            task_name, 
            task_description
        ):
            print(f'{cur_class_name} does not contain the record')
            return super().dict_value_not_found()

        return (
            train_id,
            task_mode, 
            model_name, 
            metric_name, 
            train_file_path, 
            train_id_column, 
            train_data_column, 
            train_target_column, 
            task_name, 
            task_description
        )
       
   