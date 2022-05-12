from __future__ import annotations

from abc import ABC, abstractmethod

from synspot.algorithm.train_stage import (
    MakeTrain,
    MakeResult
)


class AbstractTrainCustom(ABC):

    @classmethod
    @abstractmethod
    def make_train(cls, **kwargs):
        pass
    
    @classmethod
    @abstractmethod
    def make_result(cls, **kwargs):
        pass


class TrainFixedParameter(AbstractTrainCustom):
    
    @classmethod
    def make_train(cls, **kwargs):
        return MakeTrain.make_train(**kwargs)
    
    @classmethod
    def make_result(cls, **kwargs):
        return MakeResult.make_result(**kwargs)


class TrainOptimizedParameter(AbstractTrainCustom):
    
    @classmethod
    def make_train(cls, **kwargs):
        return MakeTrain.make_train(**kwargs)
    
    @classmethod
    def make_result(cls, **kwargs):
        return MakeResult.make_result(**kwargs)


class TrainOwnFunction(AbstractTrainCustom):
    
    def __init__(cls, OwnFunction):
        cls.OwnFunction = OwnFunction

    @classmethod
    def make_train(cls, **kwargs):
        return cls.OwnFunction['MakeTrain'](**kwargs)
    
    @classmethod
    def make_result(cls, **kwargs):
        return cls.OwnFunction['MakeResult'](**kwargs)

        