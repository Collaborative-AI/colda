from __future__ import annotations

from abc import ABC, abstractmethod

class AbstractTrainMainWorkflow(ABC):
    '''
    Abstract class for train main workflow
    '''

    @classmethod
    @abstractmethod
    def get_instance(cls):
        pass

    @abstractmethod
    def find_assistor(self, **kwargs):
        pass
    
    @abstractmethod
    def train_assistor_request(self, **kwargs):
        pass

    @abstractmethod
    def train_match_identifier(self, **kwargs):
        pass

    @abstractmethod
    def train_sponsor_match_identifier(self, **kwargs):
        pass

    @abstractmethod
    def train_assistor_match_identifier(self, **kwargs):
        pass

    @abstractmethod
    def train_situation(self, **kwargs):
        pass

    @abstractmethod
    def train_sponsor_situation(self, **kwargs):
        pass
    
    @abstractmethod
    def train_assistor_situation(self, **kwargs):
        pass

    @abstractmethod
    def train_output(self, **kwargs):
        pass

    @abstractmethod
    def stop_train(self, **kwargs):
        pass

class AbstractTestMainWorkflow(ABC):
    '''
    Abstract class for test main workflow
    '''

    @classmethod
    @abstractmethod
    def get_instance(cls):
        pass

    @abstractmethod
    def find_test_assistor(self, **kwargs):
        pass
    
    @abstractmethod
    def test_assistor_request(self, **kwargs):
        pass

    @abstractmethod
    def test_match_identifier(self, **kwargs):
        pass
    
    @abstractmethod
    def test_sponsor_match_identifier(self, **kwargs):
        pass

    @abstractmethod
    def test_assistor_match_identifier(self, **kwargs):
        pass

    @abstractmethod
    def test_output(self, **kwargs):
        pass
