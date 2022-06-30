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


#@typecheckd
class TestSponsorMetadataDatabase(BaseDatabase, AbstractMetadataDatabase):
    '''
    Store and manage data generated from sponsor test stage.

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

    __TestSponsorMetadataDatabase_instance = None

    def __init__(self):
        self.__temp_database = collections.defaultdict(dict)

    @classmethod
    def get_instance(cls) -> type[TestSponsorMetadataDatabase]:
        '''
        Singleton pattern. 
        Get instance of current class.

        Parameters
        ----------
        None

        Returns
        -------
        type[TestAssistorMetadataDatabase]
        '''
        if cls.__TestSponsorMetadataDatabase_instance == None:
            cls.__TestSponsorMetadataDatabase_instance = TestSponsorMetadataDatabase()

        return cls.__TestSponsorMetadataDatabase_instance

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
        test_id: str, 
        test_file_path: str, 
        test_id_column: str, 
        test_data_column: str,
        test_target_column: str,
        test_name: str=None, 
        test_description: str=None, 
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
        test_id : str
        test_file_path : str
        test_id_column : str
        test_data_column : str
        test_target_column : str
        test_name : str=None
        test_description : str=None

        Returns
        -------
        None
        '''
        key = DictHelper.generate_dict_root_key(
            user_id=user_id, 
            task_id=test_id
        )
        temp_key = str(key)

        value = {
            'train_id': train_id,
            'task_mode': task_mode,
            'model_name': model_name,
            'metric_name': metric_name,
            'test_id': test_id,
            'test_file_path': test_file_path,
            'test_id_column': test_id_column,
            'test_data_column': test_data_column,
            'test_target_column': test_target_column,
            'test_name': test_name,
            'test_description': test_description
        }
        DictHelper.store_value(
            key=key,
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
            raise RuntimeError('Use test_id to retrieve User_Assistor_Table')

        root_key = DictHelper.generate_dict_root_key(
            user_id=user_id, 
            task_id=test_id
        )

        sponsor_metadata = DictHelper.get_value(
            key=root_key,
            container=self.__temp_database
        )

        train_id = sponsor_metadata['train_id']
        task_mode = sponsor_metadata['task_mode']
        model_name = sponsor_metadata['model_name']
        metric_name = sponsor_metadata['metric_name']
        test_id = sponsor_metadata['test_id']
        test_file_path = sponsor_metadata['test_file_path']
        test_id_column = sponsor_metadata['test_id_column']
        test_data_column = sponsor_metadata['test_data_column']
        test_target_column = sponsor_metadata['test_target_column']
        test_name = sponsor_metadata['test_name']
        test_description = sponsor_metadata['test_description']

        return ( 
            train_id,
            task_mode, 
            model_name,
            metric_name, 
            test_id,
            test_file_path, 
            test_id_column, 
            test_data_column, 
            test_target_column,
            test_name, 
            test_description
        )
    