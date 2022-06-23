from __future__ import annotations

from colda.algorithm.strategy.base import BaseAlgorithmStrategy

from colda.algorithm.strategy.abstract_algorithm_strategy import AbstractTrainAlgorithmStrategy

from colda.algorithm.train_stage.api import (
    MakeResidual,
    MakeTrainLocal,
)

from colda.algorithm.custom.api import GetTrainFixedParameter

from typing import Any

from typeguard import typechecked


#@typechecked
class TrainAlgorithm(AbstractTrainAlgorithmStrategy, BaseAlgorithmStrategy):
    '''
    Strategy pattern to manage train algorithm

    Attributes
    ----------
    train_custom

    Methods
    -------
    get_instance
    make_train_local
    make_train
    make_result
    '''

    __TrainAlgorithm_instance = None

    def __init__(self) -> None:
        self.__train_custom = GetTrainFixedParameter.get_class()

    @classmethod
    def get_instance(cls) -> TrainAlgorithm:
        '''
        Singleton pattern. 
        Get instance of current class.

        Parameters
        ----------
        None

        Returns
        -------
        type[TrainAlgorithm]
        '''
        if cls.__TrainAlgorithm_instance == None:
            cls.__TrainAlgorithm_instance = TrainAlgorithm()

        return cls.__TrainAlgorithm_instance

    @property
    def train_custom(self):
        '''
        Get strategy object

        Parameters
        ----------
        None

        Returns
        -------
        Any
        '''
        return self.__train_custom

    @train_custom.setter
    def train_custom(
        self, train_custom: Any
    ) -> None:
        '''
        Set strategy object

        Parameters
        ----------
        None

        Returns
        -------
        Any
        '''
        self.__train_custom = train_custom

    def make_train_local(
        self, **kwargs
    ) -> None:
        '''
        strategy interface
        '''
        return self.algorithm_process(MakeTrainLocal.make_train_local, **kwargs)
    
    def make_residual(
        self, **kwargs
    ) -> None:
        '''
        strategy interface
        '''
        return self.algorithm_process(MakeResidual.make_residual, **kwargs)
    
    def make_train(
        self, **kwargs
    ) -> None:
        '''
        strategy interface
        '''
        return self.algorithm_process(self.__train_custom.make_train, **kwargs)

    def make_result(
        self, **kwargs
    ) -> None:
        '''
        strategy interface
        '''
        return self.algorithm_process(self.__train_custom.make_result, **kwargs)

