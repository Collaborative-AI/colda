from __future__ import annotations

import collections

from database.base import BaseDatabase

from database.abstract_database import AbstractMetadataDatabase
from _typing import (
    Mode,
    Task_Mode,
    Model_Name,
    Metric_Name
)
from utils.api import DictHelper

from typeguard import typechecked


class TrainAssistorMetadataDatabase(BaseDatabase, AbstractMetadataDatabase):
    '''
    Store and manage data generated from assistor train stage.

    Methods
    -------
    get_instance
    get_all_records
    store_record
    get_record
    '''

    __TrainAssistorMetadataDatabase_instance = None

    def __init__(self):
        self.__temp_database = collections.defaultdict(dict)

    @classmethod
    def get_instance(cls) -> type[TrainAssistorMetadataDatabase]:
        '''
        Singleton pattern. 
        Get instance of current class.

        Returns
        -------
        type[TrainAssistorMetadataDatabase]
        '''
        if cls.__TrainAssistorMetadataDatabase_instance == None:
            cls.__TrainAssistorMetadataDatabase_instance = TrainAssistorMetadataDatabase()

        return cls.__TrainAssistorMetadataDatabase_instance

    def get_all_records_history(self) -> list[tuple[str, str]]:
        '''
        Return all keys of records in this database

        Returns
        -------
        list[tuple[str, str]]
        '''
        return DictHelper.get_all_key_value_pairs(container=self.__temp_database)

    def store_record(
        self, 
        user_id: str, 
        train_id: str, 
        mode: Mode, 
        task_mode: Task_Mode, 
        model_name: Model_Name, 
        train_file_path: str, 
        train_id_column: str, 
        train_data_column: str, 
        task_name: str=None, 
        task_description: str=None,  
    ) -> None:
        '''
        Store record

        Parameters
        ----------
        user_id : str
        train_id : str 
        mode : Mode
        task_mode : Task_Mode
        model_name : Model_Name 
        train_file_path : str
        train_id_column : str 
        train_data_column : str 
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
        root_key = DictHelper.generate_dict_root_key(
            user_id=user_id, 
            task_id=train_id
        )            

        assistor_metadata = DictHelper.get_value(
            key=root_key,
            container=self.__temp_database
        )

        train_id = assistor_metadata['train_id']
        mode = assistor_metadata['mode']
        task_mode = assistor_metadata['task_mode']
        model_name = assistor_metadata['model_name']
        train_file_path = assistor_metadata['train_file_path']
        train_id_column = assistor_metadata['train_id_column']
        train_data_column = assistor_metadata['train_data_column']
        task_name = assistor_metadata['task_name']
        task_description = assistor_metadata['task_description']

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
       
    @classmethod
    def delete(cls):
        cls.__TrainAssistorMetadataDatabase_instance = None