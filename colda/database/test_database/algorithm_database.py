from __future__ import annotations

import collections

from colda.database.base import BaseDatabase

from colda.database.abstract_database import AbstractAlgorithmDatabase

from colda.utils.api import DictHelper

from typing import (
    Union,
    Any
)

from typeguard import typechecked


#@typechecked
class TestAlgorithmDatabase(BaseDatabase, AbstractAlgorithmDatabase):
    '''
    Store and manage test_algorithm database.
    Test algorithm database mainly stores the output and log generated
    from algorithm part of test stage.

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

    __TestAlgorithmDatabase_instance = None

    def __init__(self):
        self.__temp_database = collections.defaultdict(dict)

    @classmethod
    def get_instance(cls) -> type[TestAlgorithmDatabase]:
        '''
        Singleton pattern. 
        Get instance of current class.

        Parameters
        ----------
        None

        Returns
        -------
        type[TestAlgorithmDatabase]
        '''
        if cls.__TestAlgorithmDatabase_instance == None:
            cls.__TestAlgorithmDatabase_instance = TestAlgorithmDatabase()

        return cls.__TestAlgorithmDatabase_instance

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
        return DictHelper.get_all_key_value_pairs(
            container=self.__temp_database
        )

    def store_record(
        self, 
        user_id: str, 
        test_id: str, 
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
            task_id=test_id,
        )
        key = DictHelper.generate_dict_supplement_key(
            root_key=root_key,
            supplement_key=algorithm_data_name
        )

        DictHelper.store_value(
            key=key,
            value=algorithm_data,
            container=self.__temp_database,
            store_type='append'
        )
        return

    def get_record(
        self, 
        user_id: str, 
        test_id: str, 
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
        if not test_id:
            raise RuntimeError('Use test_id to retrieve User_Assistor_Table')
            
        root_key = DictHelper.generate_dict_root_key(
            user_id=user_id, 
            task_id=test_id,
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
       
   