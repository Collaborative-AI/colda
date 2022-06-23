from __future__ import annotations

from abc import ABC, abstractmethod


class AbstractTrainAlgorithmStrategy(ABC):

    @classmethod
    @abstractmethod
    def get_instance(cls):
        pass
    
    @abstractmethod
    def make_train_local(self, **kwargs):
        pass
    
    @abstractmethod
    def make_residual(self, **kwargs):
        pass
    
    @abstractmethod
    def save_residual(self, **kwargs):
        pass
    
    @abstractmethod
    def make_train(self, **kwargs):
        pass
    
    @abstractmethod
    def make_result(self, **kwargs):
        pass


class AbstractTestAlgorithmStrategy(ABC):

    @classmethod
    @abstractmethod
    def get_instance(cls):
        pass

    @abstractmethod
    def make_test_local(self, **kwargs):
        pass

    @abstractmethod
    def make_test(self, **kwargs):
        pass

    @abstractmethod
    def make_eval(self, **kwargs):
        pass