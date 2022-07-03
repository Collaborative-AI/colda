from __future__ import annotations

import collections

from colda.database.base import BaseDatabase

from colda.database.abstract_database import AbstractAlgorithmDatabase

from colda.utils.api import DictHelper

from colda._typing import (
    Task_Mode,
    Model_Name,
    Metric_Name
)
from typing import (
    Union,
    Any
)

from typeguard import typechecked


#@typechecked
class TrainAlgorithmDatabase(BaseDatabase, AbstractAlgorithmDatabase):
    '''
    Store and manage train_algorithm database.
    Train algorithm database mainly stores the output and log generated
    from algorithm part of train stage.

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

    __TrainAlgorithmDatabase_instance = None

    def __init__(self):
        self.__temp_database = collections.defaultdict(dict)

    @classmethod
    def get_instance(cls) -> type[TrainAlgorithmDatabase]:
        '''
        Singleton pattern. 
        Get instance of current class.

        Parameters
        ----------
        None

        Returns
        -------
        type[TrainAlgorithmDatabase]
        '''
        if cls.__TrainAlgorithmDatabase_instance == None:
            cls.__TrainAlgorithmDatabase_instance = TrainAlgorithmDatabase()

        return cls.__TrainAlgorithmDatabase_instance

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
        algorithm_data_name: str,
        algorithm_data: Union[list[str], list[list[str]], Any],
    ) -> None:
        '''
        Store record

        Parameters
        ----------
        user_id : str
        test_id : str 
        algorithm_data_name : str
        algorithm_data : Union[list[str], list[list[str]], Any]

        Returns
        -------
        None
        '''
        root_key = DictHelper.generate_dict_root_key(
            user_id=user_id, 
            task_id=train_id,
        )
        key = DictHelper.generate_dict_supplement_key(
            root_key=root_key,
            supplement_key=algorithm_data_name
        )

        DictHelper.store_value(
            key=key,
            value=algorithm_data,
            container=self.__temp_database,
            store_type='store_multiple'
        )
        return

    def get_record(
        self, 
        user_id: str, 
        train_id: str, 
        algorithm_data_name: str,
    ) -> None:
        '''
        Get record

        Parameters
        ----------
        user_id : str
        test_id : str 
        algorithm_data_name : str

        Returns
        -------
        None
        '''
        if not train_id:
            raise RuntimeError('Use train_id to retrieve User_Assistor_Table')
            
        root_key = DictHelper.generate_dict_root_key(
            user_id=user_id, 
            task_id=train_id,
        )
        key = DictHelper.generate_dict_supplement_key(
            root_key=root_key,
            supplement_key=algorithm_data_name
        )

        algorithm_data = DictHelper.get_value(
            key=key,
            container=self.__temp_database
        )
        return algorithm_data
       
    @classmethod
    def delete(cls):
        cls.__TrainAlgorithmDatabase_instance = None