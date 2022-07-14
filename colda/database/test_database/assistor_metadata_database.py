from __future__ import annotations

import collections

from colda.database.base import BaseDatabase

from colda.database.abstract_database import AbstractMetadataDatabase

from colda.utils.api import DictHelper

from colda._typing import (
    Task_Mode,
    Model_Name,
    Metric_Name
)

from typeguard import typechecked


# @typechecked
class TestAssistorMetadataDatabase(BaseDatabase, AbstractMetadataDatabase):
    '''
    Store and manage data generated from assistor test stage.

    Methods
    -------
    get_instance
    get_all_records
    store_record
    get_record
    '''

    __TestAssistorMetadataDatabase_instance = None

    def __init__(self):
        self.__temp_database = collections.defaultdict(dict)

    @classmethod
    def get_instance(cls) -> type[TestAssistorMetadataDatabase]:
        '''
        Singleton pattern. 
        Get instance of current class.

        Returns
        -------
        type[TestAssistorMetadataDatabase]
        '''
        if cls.__TestAssistorMetadataDatabase_instance == None:
            cls.__TestAssistorMetadataDatabase_instance = TestAssistorMetadataDatabase()

        return cls.__TestAssistorMetadataDatabase_instance

    def get_all_records_history(self) -> list[tuple[str, str]]:
        '''
        Return all keys of records in this database

        Returns
        -------
        list[tuple[str, str]]
        '''
        return DictHelper.get_all_key_value_pairs(
            container=self.__temp_database
        )

    def store_record(
        self, 
        user_id: str, 
        train_id: str, 
        mode: str, 
        task_mode: Task_Mode, 
        model_name: Model_Name, 
        test_id: str, 
        test_file_path: str, 
        test_id_column: str, 
        test_data_column: str,
        test_name: str=None, 
        test_description: str=None, 
    ) -> None:
        '''
        Store record

        Parameters
        ----------
        user_id : str
        train_id : str
        mode : str
        task_mode : Task_Mode
        model_name : Model_Name
        test_id : str
        test_file_path : str
        test_id_column : str 
        test_data_column : str
        test_name : str=None
        test_description : str=None 

        Returns
        -------
        None
        '''

        root_key = DictHelper.generate_dict_root_key(
            user_id=user_id, 
            task_id=test_id
        )

        value = {
            'train_id': train_id,
            'mode': mode,
            'task_mode': task_mode,
            'model_name': model_name,
            'test_id': test_id,
            'test_file_path': test_file_path,
            'test_id_column': test_id_column,
            'test_data_column': test_data_column,
            'test_name': test_name,
            'test_description': test_description
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
        test_id: str,
    ) -> None:
        '''
        Get record

        Parameters
        ----------
        user_id : str
        test_id : str 

        Returns
        -------
        None
        '''
        if not test_id:
            raise RuntimeError('Use task_id to retrieve User_Assistor_Table')

        root_key = DictHelper.generate_dict_root_key(
            user_id=user_id, 
            task_id=test_id
        )

        assistor_metadata = DictHelper.get_value(
            key=root_key,
            container=self.__temp_database
        )

        train_id = assistor_metadata['train_id']
        mode = assistor_metadata['mode']
        task_mode = assistor_metadata['task_mode']
        model_name = assistor_metadata['model_name']
        test_id = assistor_metadata['test_id']
        test_file_path = assistor_metadata['test_file_path']
        test_id_column = assistor_metadata['test_id_column']
        test_data_column = assistor_metadata['test_data_column']
        test_name = assistor_metadata['test_name']
        test_description = assistor_metadata['test_description']

        return (
            train_id, 
            mode, 
            task_mode, 
            model_name, 
            test_id,
            test_file_path, 
            test_id_column, 
            test_data_column, 
            test_name, 
            test_description
        )
    
    @classmethod
    def delete(cls):
        cls.__TestAssistorMetadataDatabase_instance = None