from __future__ import annotations

from abc import ABC, abstractmethod

from colda.database.train_database.api import (
    TrainSponsorMetadataDatabase,
    TrainAssistorMetadataDatabase,
    TrainAlgorithmDatabase
)

from colda.database.test_database.api import (
    TestSponsorMetadataDatabase,
    TestAssistorMetadataDatabase,
    TestAlgorithmDatabase
)

from colda.database.default_database.api import DefaultMetadataDatabase

from typeguard import typechecked


class AbstractDatabaseFactory(ABC):
    '''
    Abstract class for database factory

    Parameters
    ----------
    None

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
        
        Parameters
        ----------
        None

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
        
        Parameters
        ----------
        None

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
        
        Parameters
        ----------
        None

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
        
        Parameters
        ----------
        None

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
        
        Parameters
        ----------
        None

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
        
        Parameters
        ----------
        None

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
        
        Parameters
        ----------
        None

        Returns
        -------
        TestAlgorithmDatabase
        '''
        return TestAlgorithmDatabase.get_instance()