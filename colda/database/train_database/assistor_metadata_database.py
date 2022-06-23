from __future__ import annotations

import collections

from colda.database.base import BaseDatabase

from colda.database.abstract_database import AbstractMetadataDatabase
from colda._typing import (
    Mode,
    Task_Mode,
    Model_Name,
    Metric_Name
)
from colda.utils import DictHelper

from typeguard import typechecked


class TrainAssistorMetadataDatabase(BaseDatabase, AbstractMetadataDatabase):
    '''
    Store and manage data generated from assistor train stage.

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

    __TrainAssistorMetadataDatabase_instance = None

    def __init__(self):
        self.__temp_database = collections.defaultdict(dict)

    @classmethod
    def get_instance(cls) -> type[TrainAssistorMetadataDatabase]:
        '''
        Singleton pattern. 
        Get instance of current class.

        Parameters
        ----------
        None

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
        key = DictHelper.generate_unique_dict_key(user_id, train_id)
        temp_key = str(key)
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
            raise RuntimeError('Use train_id to retrieve User_Assistor_Table')

        key = DictHelper.generate_unique_dict_key(user_id, train_id)            

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
       
   