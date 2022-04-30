from __future__ import annotations

from abc import ABC, abstractmethod


class AbstractTrainAlgorithmStrategy(ABC):

    @abstractmethod
    def make_train_local(self, *args):
        pass
    
    @abstractmethod
    def make_residual(self, *args):
        pass
    
    @abstractmethod
    def save_residual(self, *args):
        pass
    
    @abstractmethod
    def make_train(self, *args):
        pass
    
    @abstractmethod
    def make_result(self, *args):
        pass


class AbstractTestAlgorithmStrategy(ABC):

    @abstractmethod
    def make_test_local(self, *args):
        pass

    @abstractmethod
    def make_test(self, *args):
        pass

    @abstractmethod
    def make_eval(self, *args):
        pass