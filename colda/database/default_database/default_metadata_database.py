from __future__ import annotations

import collections

from database.base import BaseDatabase

from database.abstract_database import AbstractMetadataDatabase

from utils.api import DictHelper

from typing import Any

from _typing import (
    Mode,
    Task_Mode,
    Model_Name,
    Metric_Name
)

from typeguard import typechecked


class DefaultMetadataDatabase(BaseDatabase, AbstractMetadataDatabase):

    '''
    Store default setting. Ex. default path,
    default mode.
    Default setting is used by assistor.

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

    __DefaultMetadataDatabase_instance = None

    def __init__(self):
        self.__temp_database = collections.defaultdict(dict)

    @classmethod
    def get_instance(cls) -> type[DefaultMetadataDatabase]:
        '''
        Singleton pattern. 
        Get instance of current class.

        Returns
        -------
        type[DefaultMetadataDatabase]
        '''
        if cls.__DefaultMetadataDatabase_instance == None:
            cls.__DefaultMetadataDatabase_instance = DefaultMetadataDatabase()

        return cls.__DefaultMetadataDatabase_instance

    def get_all_records_history(self) -> list[tuple[str]]:
        '''
        Return all records in this database

        Returns
        -------
        list[tuple[str]]
        '''
        return DictHelper.get_all_key_value_pairs(
            container=self.__temp_database
        )

    def store_record(
        self, 
        user_id: str, 
        default_mode: Mode, 
        default_task_mode: Task_Mode, 
        default_model_name: Model_Name, 
        default_file_path: str=None, 
        default_id_column: str=None, 
        default_data_column: str=None
    ) -> None:
        '''
        Store default setting

        Parameters
        ----------
        user_id : str
            unique user id get from the token
        default_mode : Default_Mode
            Must in Default_Mode
        default_task_mode : str
            Must in Default_Task_Mode
        default_model_name : str
            model_name. Ex. Decision Tree
        default_file_path : str=None
            training data file path
        default_id_column : str=None
            training data id column
        default_data_column : str=None
            training data data column

        Returns
        -------
        None
        '''
        key = DictHelper.generate_dict_root_key(
            user_id=user_id, 
        )  
        value = {
            'default_mode': default_mode,
            'default_task_mode': default_task_mode,
            'default_model_name': default_model_name,
            'default_file_path': default_file_path,
            'default_id_column': default_id_column,
            'default_data_column': default_data_column,
        }
        DictHelper.store_value(
            key=key,
            value=value,
            container=self.__temp_database,
            store_type='store_multiple'
        )
        print('store default info done')
        return

    def get_record(
        self, user_id: str
    ) -> tuple[str]:
        '''
        Store default setting

        Parameters
        ----------
        user_id : str
            current user's id
    
        Returns
        -------
        None
        '''
        root_key = DictHelper.generate_dict_root_key(
            user_id=user_id, 
        )  

        default_metadata = DictHelper.get_value(
            key=root_key,
            container=self.__temp_database
        )

        default_mode = default_metadata['default_mode']
        default_task_mode = default_metadata['default_task_mode']
        default_model_name = default_metadata['default_model_name']
        default_file_path = default_metadata['default_file_path']
        default_id_column = default_metadata['default_id_column']
        default_data_column = default_metadata['default_data_column']

        return (
            default_mode, 
            default_task_mode, 
            default_model_name, 
            default_file_path, 
            default_id_column, 
            default_data_column
        )
    
    @classmethod
    def delete(cls):
        cls.__DefaultMetadataDatabase_instance = None