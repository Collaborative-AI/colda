from __future__ import annotations

from abc import ABC, abstractmethod

from database.train_database.api import (
    TrainSponsorMetadataDatabase,
    TrainAssistorMetadataDatabase,
    TrainAlgorithmDatabase
)

from database.test_database.api import (
    TestSponsorMetadataDatabase,
    TestAssistorMetadataDatabase,
    TestAlgorithmDatabase
)

from database.default_database.api import DefaultMetadataDatabase

from typeguard import typechecked


class AbstractDatabaseFactory(ABC):
    '''
    Abstract class for database factory

    Returns
    -------
    None
    '''

    @classmethod
    @abstractmethod
    def get_instance(cls):
        pass


class GetDefaultMetadataDatabase(AbstractDatabaseFactory):

    @classmethod
    def get_instance(cls) -> DefaultMetadataDatabase:
        '''
        DefaultMetadataDatabase factory

        Returns
        -------
        DefaultMetadataDatabase
        '''
        return DefaultMetadataDatabase.get_instance()


class GetTrainSponsorMetadataDatabase(AbstractDatabaseFactory):

    @classmethod
    def get_instance(cls) -> TrainSponsorMetadataDatabase:
        '''
        TrainSponsorMetadataDatabase factory

        Returns
        -------
        TrainSponsorMetadataDatabase
        '''
        return TrainSponsorMetadataDatabase.get_instance()


class GetTrainAssistorMetadataDatabase(AbstractDatabaseFactory):

    @classmethod
    def get_instance(cls) -> TrainAssistorMetadataDatabase:
        '''
        TrainAssistorMetadataDatabase factory

        Returns
        -------
        TrainAssistorMetadataDatabase
        '''
        return TrainAssistorMetadataDatabase.get_instance()


class GetTrainAlgorithmDatabase(AbstractDatabaseFactory):

    @classmethod
    def get_instance(cls) -> TrainAlgorithmDatabase:
        '''
        TrainAlgorithmDatabase factory

        Returns
        -------
        TrainAlgorithmDatabase
        '''
        return TrainAlgorithmDatabase.get_instance()


class GetTestSponsorMetadataDatabase(AbstractDatabaseFactory):

    @classmethod
    def get_instance(cls) -> TestSponsorMetadataDatabase:
        '''
        TestSponsorMetadataDatabase factory

        Returns
        -------
        TestSponsorMetadataDatabase
        '''
        return TestSponsorMetadataDatabase.get_instance()


class GetTestAssistorMetadataDatabase(AbstractDatabaseFactory):

    @classmethod
    def get_instance(cls) -> TestAssistorMetadataDatabase:
        '''
        TestAssistorMetadataDatabase factory

        Returns
        -------
        TestAssistorMetadataDatabase
        '''
        return TestAssistorMetadataDatabase.get_instance()


class GetTestAlgorithmDatabase(AbstractDatabaseFactory):

    @classmethod
    def get_instance(cls) -> TestAlgorithmDatabase:
        '''
        TestAlgorithmDatabase factory

        Returns
        -------
        TestAlgorithmDatabase
        '''
        return TestAlgorithmDatabase.get_instance()