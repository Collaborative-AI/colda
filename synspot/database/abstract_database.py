from __future__ import annotations

from abc import ABC, abstractmethod

class AbstractMetadataDatabase(ABC):

    @classmethod
    @abstractmethod
    def get_database_instance(cls):
        pass
    
    @abstractmethod
    def get_all_records(self, **kwargs):
        pass

    @abstractmethod
    def store_record(self, **kwargs):
        pass
    
    @abstractmethod
    def get_record(self, **kwargs):
        pass


class AbstractAlgorithmDatabase(ABC):

    @classmethod
    @abstractmethod
    def get_database_instance(cls):
        pass
    
    @abstractmethod
    def get_all_records(self, **kwargs):
        pass

    @abstractmethod
    def store_record(self, **kwargs):
        pass
    
    @abstractmethod
    def get_record(self, **kwargs):
        pass