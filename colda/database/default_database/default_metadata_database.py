from __future__ import annotations

import collections

from colda.database.base import BaseDatabase

from colda.database.abstract_database import AbstractMetadataDatabase

from colda.utils import DictHelper

from typing import Any

from colda._typing import (
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

        Parameters
        ----------
        None

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

        Parameters
        ----------
        None

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
        key = user_id
        value = {
            'default_mode': default_mode,
            'default_task_mode': default_task_mode,
            'default_model_name': default_model_name,
            'default_file_path': default_file_path,
            'default_id_column': default_id_column,
            'default_data_column': default_data_column,
        }
        store_res = DictHelper.store_value(
            key=key,
            value=value,
            container=self.__temp_database,
            store_type='multiple_access'
        )

        if store_res == True:
            return f'{self.__class__.__name__} stores {key} successfully!' 
        else:
            return store_res

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
        key = user_id
        if key not in self.__temp_database:
            print(f'{self.__class__.__name__} does not contain the record')

        default_metadata = DictHelper.get_value(
            key=key,
            container=self.__temp_database
        )

        default_mode = DictHelper.get_value(
            key='default_mode',
            container=default_metadata
        )

        default_task_mode = DictHelper.get_value(
            key='default_task_mode',
            container=default_metadata
        )

        default_model_name = DictHelper.get_value(
            key='default_model_name',
            container=default_metadata
        )

        default_file_path = DictHelper.get_value(
            key='default_file_path',
            container=default_metadata
        )

        default_id_column = DictHelper.get_value(
            key='default_id_column',
            container=default_metadata
        )

        default_data_column = DictHelper.get_value(
            key='default_data_column',
            container=default_metadata
        )

        return (
            default_mode, 
            default_task_mode, 
            default_model_name, 
            default_file_path, 
            default_id_column, 
            default_data_column
        )