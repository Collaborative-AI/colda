from __future__ import annotations

from abc import ABC, abstractmethod

from algorithm.strategy.custom.train_custom import (
    TrainFixedParameter, 
    TrainOptimizedParameter, 
    TrainOwnFunction
)

from algorithm.strategy.custom.test_custom import (
    TestFixedParameter,
    TestOptimizedParameter,
    TestOwnFunction
)

from typing import Callable

from typeguard import typechecked


class AbstractCustomFactory(ABC):
    '''
    Abstract class for custom algorithm factory
    '''

    @classmethod
    @abstractmethod
    def get_class(cls):
        pass


#@typechecked
class GetTrainFixedParameter(AbstractCustomFactory) :
    
    @classmethod
    def get_class(cls) -> type[TrainFixedParameter]:
        '''
        TrainFixedParameter factory

        Returns
        -------
        TrainFixedParameter
        '''
        return TrainFixedParameter


#@typechecked
class GetTrainOptimizedParameter(AbstractCustomFactory):
    
    @classmethod
    def get_class(cls) -> type[TrainOptimizedParameter]:
        '''
        TrainOptimizedParameter factory

        Returns
        -------
        TrainOptimizedParameter
        '''

        return TrainOptimizedParameter


#@typechecked
class GetTrainOwnFunction(AbstractCustomFactory):

    @classmethod
    def get_class(cls) -> type[TrainOwnFunction]:
        '''
        TrainOwnFunction factory
        
        Parameters
        ----------
        OwnFunction : Callable
            callback custom function

        Returns
        -------
        TrainOwnFunction
        '''
        return TrainOwnFunction


#@typechecked
class GetTestFixedParameter(AbstractCustomFactory):
    
    @classmethod
    def get_class(cls) -> type[TestFixedParameter]:
        '''
        TestFixedParameter factory

        Returns
        -------
        TestFixedParameter
        '''
        return TestFixedParameter


#@typechecked
class GetTestOptimizedParameter(AbstractCustomFactory):
    
    @classmethod
    def get_class(cls) -> type[TestOptimizedParameter]:
        '''
        TestOptimizedParameter factory

        Returns
        -------
        TestOptimizedParameter
        '''
        return TestOptimizedParameter


#@typechecked
class GetTestOwnFunction(AbstractCustomFactory):

    @classmethod
    def get_class(cls) -> type[TestOwnFunction]:
        '''
        TestOwnFunction factory
        
        Parameters
        ----------
        OwnFunction : Callable
            callback custom function

        Returns
        -------
        TestOwnFunction
        '''
        return TestOwnFunction
