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


class DatabaseAbstractFactory(ABC):
    """
    Abstract Factory
    """
    @classmethod
    @abstractmethod
    def get_database(cls):
        pass


class GetDefaultMetadataDatabase(DatabaseAbstractFactory):
    """
    Concrete Factory
    """
    @classmethod
    def get_database(cls):
        return DefaultMetadataDatabase.get_database_instance()


class GetTrainSponsorMetadataDatabase(DatabaseAbstractFactory):
    """
    Concrete Factory
    """
    @classmethod
    def get_database(cls):
        return TrainSponsorMetadataDatabase.get_database_instance()


class GetTrainAssistorMetadataDatabase(DatabaseAbstractFactory):
    """
    Concrete Factory
    """
    @classmethod
    def get_database(cls):
        return TrainAssistorMetadataDatabase.get_database_instance()


class GetTrainAlgorithmDatabase(DatabaseAbstractFactory):
    """
    Concrete Factory
    """
    @classmethod
    def get_database(cls):
        return TrainAlgorithmDatabase.get_database_instance()


class GetTestSponsorMetadataDatabase(DatabaseAbstractFactory):
    """
    Concrete Factory
    """
    @classmethod
    def get_database(cls):
        return TestSponsorMetadataDatabase.get_database_instance()


class GetTestAssistorMetadataDatabase(DatabaseAbstractFactory):
    """
    Concrete Factory
    """
    @classmethod
    def get_database(cls):
        return TestAssistorMetadataDatabase.get_database_instance()


class GetTestAlgorithmDatabase(DatabaseAbstractFactory):
    """
    Concrete Factory
    """
    @classmethod
    def get_database(cls):
        return TestAlgorithmDatabase.get_database_instance()