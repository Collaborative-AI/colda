from __future__ import annotations

import collections

from colda.database.base import BaseDatabase

from colda.database.abstract_database import AbstractMetadataDatabase

from colda._typing import (
    Task_Mode,
    Model_Name,
    Metric_Name
)

from colda.utils.api import DictHelper

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
        root_key = DictHelper.generate_dict_root_key(
            user_id=user_id, 
            task_id=train_id
        )  
    
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
        DictHelper.store_value(
            key=root_key,
            value=value,
            container=self.__temp_database
        )
        return
    
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
        key = DictHelper.generate_dict_root_key(
            user_id=user_id, 
            task_id=train_id
        )  

        sponsor_metadata = DictHelper.get_value(
            key=key,
            container=self.__temp_database
        )

        train_id = sponsor_metadata['train_id']
        task_mode = sponsor_metadata['task_mode']
        model_name = sponsor_metadata['model_name']
        metric_name = sponsor_metadata['metric_name']
        train_file_path = sponsor_metadata['train_file_path']
        train_id_column = sponsor_metadata['train_id_column']
        train_data_column = sponsor_metadata['train_data_column']
        train_target_column = sponsor_metadata['train_target_column']
        task_name = sponsor_metadata['task_name']
        task_description = sponsor_metadata['task_description']

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
       
    @classmethod
    def delete(cls):
        cls.__TrainSponsorMetadataDatabase_instance = None