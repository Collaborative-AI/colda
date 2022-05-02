from __future__ import annotations

from abc import ABC, abstractmethod

from synspot.database.train_database import (
    TrainSponsorMetadataDatabase,
    TrainAssistorMetadataDatabase,
    TrainAlgorithmDatabase
)

from synspot.database.test_database import (
    TestSponsorMetadataDatabase,
    TestAssistorMetadataDatabase,
    TestAlgorithmDatabase
)

from synspot.database.default_database import DefaultMetadataDatabase


class AbstractDatabaseFactory(ABC):
    """
    Abstract Factory
    """
    @classmethod
    @abstractmethod
    def get_database(cls):
        pass


class GetDefaultMetadataDatabase(AbstractDatabaseFactory):
    """
    Concrete Factory
    """
    @classmethod
    def get_database(cls):
        return DefaultMetadataDatabase.get_database_instance()


class GetTrainSponsorMetadataDatabase(AbstractDatabaseFactory):
    """
    Concrete Factory
    """
    @classmethod
    def get_database(cls):
        return TrainSponsorMetadataDatabase.get_database_instance()


class GetTrainAssistorMetadataDatabase(AbstractDatabaseFactory):
    """
    Concrete Factory
    """
    @classmethod
    def get_database(cls):
        return TrainAssistorMetadataDatabase.get_database_instance()


class GetTrainAlgorithmDatabase(AbstractDatabaseFactory):
    """
    Concrete Factory
    """
    @classmethod
    def get_database(cls):
        return TrainAlgorithmDatabase.get_database_instance()


class GetTestSponsorMetadataDatabase(AbstractDatabaseFactory):
    """
    Concrete Factory
    """
    @classmethod
    def get_database(cls):
        return TestSponsorMetadataDatabase.get_database_instance()


class GetTestAssistorMetadataDatabase(AbstractDatabaseFactory):
    """
    Concrete Factory
    """
    @classmethod
    def get_database(cls):
        return TestAssistorMetadataDatabase.get_database_instance()


class GetTestAlgorithmDatabase(AbstractDatabaseFactory):
    """
    Concrete Factory
    """
    @classmethod
    def get_database(cls):
        return TestAlgorithmDatabase.get_database_instance()