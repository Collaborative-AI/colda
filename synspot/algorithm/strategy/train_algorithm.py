from __future__ import annotations

from synspot.algorithm.strategy.base import BaseAlgorithm

from synspot.algorithm.strategy.abstract_algorithm import AbstractTrainAlgorithmStrategy

from synspot.algorithm.train_stage import (
    MakeResidual,
    MakeResult,
    MakeTrainLocal,
    MakeTrain,
    SaveResidual,
)

from synspot.algorithm.custom.custom_factory import FixedParameterFactory

from typing import (
    Type,
    List,
    Tuple
)


class TrainAlgorithm(AbstractTrainAlgorithmStrategy, BaseAlgorithm):
    __TrainAlgorithm_instance = None
    # strategy pattern
    # 传给他不同的行为，algo使用

    def __init__(self) -> None:
        self.__train_custom = FixedParameterFactory.create_custom()

    @classmethod
    def get_algorithm_instance(cls) -> Type[TrainAlgorithm]:
        if cls.__TrainAlgorithm_instance == None:
            cls.__TrainAlgorithm_instance = TrainAlgorithm()

        return cls.__TrainAlgorithm_instance

    @property
    def train_custom(self):
        """
        The Context maintains a reference to one of the Strategy objects. The
        Context does not know the concrete class of a strategy. It should work
        with all strategies via the Strategy interface.
        """

        return self.__train_custom

    @train_custom.setter
    def train_custom(self, train_custom) -> None:
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """

        self.__train_custom = train_custom

    def make_train_local(self, *args):
        return MakeTrainLocal.make_train_local(*args)
    
    def make_residual(self, *args):
        return MakeResidual.make_residual(*args)
    
    def save_residual(self, *args):
        return SaveResidual.save_residual(*args)
    
    def make_train(self, *args):
        return self.__train_custom.make_train(*args)

    def make_result(self, *args):
        return self.__train_custom.make_result(*args)

