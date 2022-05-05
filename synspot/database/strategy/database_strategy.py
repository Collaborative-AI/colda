from __future__ import annotations

from synspot.database.strategy.abstract_database_strategy import AbstractDatabaseStrategy

from synspot.database.strategy.base import BaseDatabaseStrategy

from synspot.database.database_factory import (
    GetDefaultMetadataDatabase,
    GetTrainSponsorMetadataDatabase,
    GetTrainAssistorMetadataDatabase,
    GetTrainAlgorithmDatabase,
    GetTestSponsorMetadataDatabase,
    GetTestAssistorMetadataDatabase,
    GetTestAlgorithmDatabase
)

from typing import Union

from synspot._typing import (
    Train_Database_Type,
    Test_Database_Type
)


class DatabaseOperator(AbstractDatabaseStrategy, BaseDatabaseStrategy):
    __DatabaseOperator_instance = None
    # strategy pattern
    # 传给他不同的行为，algo使用

    def __init__(self) -> None:
        self.__database_operator = GetDefaultMetadataDatabase.get_database()

    @classmethod
    def get_instance(cls) -> type[DatabaseOperator]:
        if cls.__DatabaseOperator_instance == None:
            cls.__DatabaseOperator_instance = DatabaseOperator()

        return cls.__DatabaseOperator_instance

    @property
    def database(self):
        """
        The Context maintains a reference to one of the Strategy objects. The
        Context does not know the concrete class of a strategy. It should work
        with all strategies via the Strategy interface.
        """

        return self.__database_operator

    @database.setter
    def database(self, database) -> None:
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """

        self.__database_operator = database

    def set_database(
        self, database_type: Union(Train_Database_Type, Test_Database_Type)
    ) -> None:
        if database_type == 'default_metadata':
            self.__database_operator = GetDefaultMetadataDatabase.get_database()
        elif database_type == 'train_sponsor_metadata':
            self.__database_operator = GetTrainSponsorMetadataDatabase.get_database()
        elif database_type == 'train_assistor_metadata':
            self.__database_operator = GetTrainAssistorMetadataDatabase.get_database()
        elif database_type == 'train_algorithm':
            self.__database_operator = GetTrainAlgorithmDatabase.get_database()
        elif database_type == 'test_sponsor_metadata':
            self.__database_operator = GetTestSponsorMetadataDatabase.get_database()
        elif database_type == 'test_assistor_metadata':
            self.__database_operator = GetTestAssistorMetadataDatabase.get_database()
        elif database_type == 'test_algorithm':
            self.__database_operator = GetTestAlgorithmDatabase.get_database()

    def get_all_records(self, **kwargs):
        return self.__database_operator.get_all_records(**kwargs)
    
    def store_record(self, **kwargs):
        return self.__database_operator.store_record(**kwargs)
    
    def get_record(self, **kwargs):
        return self.__database_operator.get_record(**kwargs)