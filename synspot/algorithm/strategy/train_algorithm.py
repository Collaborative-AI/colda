from __future__ import annotations

from synspot.algorithm.strategy.base import BaseAlgorithmStrategy

from synspot.algorithm.strategy.abstract_algorithm_strategy import AbstractTrainAlgorithmStrategy

from synspot.algorithm.train_stage import (
    MakeResidual,
    MakeResult,
    MakeTrainLocal,
    MakeTrain,
    SaveResidual,
)

from synspot.algorithm.custom.custom_factory import GetTrainFixedParameter


class TrainAlgorithm(AbstractTrainAlgorithmStrategy, BaseAlgorithmStrategy):
    __TrainAlgorithm_instance = None
    # strategy pattern
    # 传给他不同的行为，algo使用

    def __init__(self) -> None:
        self.__train_custom = GetTrainFixedParameter.create_custom()

    @classmethod
    def get_instance(cls) -> type[TrainAlgorithm]:
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

    def make_train_local(self, **kwargs):
        return MakeTrainLocal.make_train_local(**kwargs)
    
    def make_residual(self, **kwargs):
        return MakeResidual.make_residual(**kwargs)
    
    def save_residual(self, **kwargs):
        return SaveResidual.save_residual(**kwargs)
    
    def make_train(self, **kwargs):
        return self.__train_custom.make_train(**kwargs)

    def make_result(self, **kwargs):
        return self.__train_custom.make_result(**kwargs)

