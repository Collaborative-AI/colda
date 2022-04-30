from __future__ import annotations

from abc import ABC, abstractmethod

class AbstractMetadataDatabase(ABC):

    @classmethod
    @abstractmethod
    def get_database_instance(cls):
        pass
    
    @abstractmethod
    def get_all_records(self, *args):
        pass

    @abstractmethod
    def store_record(self, *args):
        pass
    
    @abstractmethod
    def get_record(self, *args):
        pass


class AbstractAlgorithmDatabase(ABC):

    @classmethod
    @abstractmethod
    def get_database_instance(cls):
        pass
    
    @abstractmethod
    def get_all_records(self, *args):
        pass

    @abstractmethod
    def store_record(self, *args):
        pass
    
    @abstractmethod
    def get_record(self, *args):
        pass