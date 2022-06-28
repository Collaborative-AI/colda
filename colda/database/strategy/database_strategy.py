from __future__ import annotations

from colda.database.strategy.abstract_database_strategy import AbstractDatabaseStrategy

from colda.database.strategy.base import BaseDatabaseStrategy

from colda.database.database_factory import (
    GetDefaultMetadataDatabase,
    GetTrainSponsorMetadataDatabase,
    GetTrainAssistorMetadataDatabase,
    GetTrainAlgorithmDatabase,
    GetTestSponsorMetadataDatabase,
    GetTestAssistorMetadataDatabase,
    GetTestAlgorithmDatabase
)

from typing import Union

from colda._typing import (
    Train_Database_Type,
    Test_Database_Type
)

from typeguard import typechecked


#@typechecked
class DatabaseOperator(AbstractDatabaseStrategy, BaseDatabaseStrategy):
    '''
    Strategy pattern to manage db

    Attributes
    ----------
    database

    Methods
    -------
    set_database
    get_all_records_history
    store_record
    get_record
    '''

    __DatabaseOperator_instance = None

    def __init__(self) -> None:
        self.__database_operator = GetDefaultMetadataDatabase.get_instance()

    @classmethod
    def get_instance(cls) -> DatabaseOperator:
        '''
        Singleton pattern. 
        Get instance of current class.

        Parameters
        ----------
        None

        Returns
        -------
        DatabaseOperator
        '''
        if cls.__DatabaseOperator_instance == None:
            cls.__DatabaseOperator_instance = DatabaseOperator()

        return cls.__DatabaseOperator_instance

    @property
    def database(self):
        '''
        Get strategy object

        Parameters
        ----------
        None

        Returns
        -------
        Any
        '''
        return self.__database_operator

    @database.setter
    def database(self, database) -> None:
        '''
        Set strategy object

        Parameters
        ----------
        None

        Returns
        -------
        Any
        '''
        self.__database_operator = database

    def set_database(
        self, database_type: Union[Train_Database_Type, Test_Database_Type]
    ) -> None:
        '''
        Helper function to set strategy object 

        Parameters
        ----------
        database_type : Union[Train_Database_Type, Test_Database_Type]

        Returns
        -------
        None
        '''
        if database_type == 'default_metadata':
            self.__database_operator = GetDefaultMetadataDatabase.get_instance()
        elif database_type == 'train_sponsor_metadata':
            self.__database_operator = GetTrainSponsorMetadataDatabase.get_instance()
        elif database_type == 'train_assistor_metadata':
            self.__database_operator = GetTrainAssistorMetadataDatabase.get_instance()
        elif database_type == 'train_algorithm':
            self.__database_operator = GetTrainAlgorithmDatabase.get_instance()
        elif database_type == 'test_sponsor_metadata':
            self.__database_operator = GetTestSponsorMetadataDatabase.get_instance()
        elif database_type == 'test_assistor_metadata':
            self.__database_operator = GetTestAssistorMetadataDatabase.get_instance()
        elif database_type == 'test_algorithm':
            self.__database_operator = GetTestAlgorithmDatabase.get_instance()
        else:
            raise ValueError('wrong database name')

    def get_all_records_history(
        self, **kwargs
    ) -> list:
        '''
        call specific function

        Parameters
        ----------
        **kwargs : Any

        Returns
        -------
        list
        '''
        return self.__database_operator.get_all_records_history(**kwargs)
    
    def store_record(
        self, **kwargs
    ) -> list:
        '''
        call specific function

        Parameters
        ----------
        **kwargs : Any

        Returns
        -------
        list
        '''
        return self.__database_operator.store_record(**kwargs)
    
    def get_record(
        self, **kwargs
    ) -> list:
        '''
        call specific function

        Parameters
        ----------
        **kwargs : Any

        Returns
        -------
        list
        '''
        return self.__database_operator.get_record(**kwargs)