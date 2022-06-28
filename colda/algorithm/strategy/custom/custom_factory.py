from __future__ import annotations

from abc import ABC, abstractmethod

from colda.algorithm.strategy.custom.train_custom import (
    TrainFixedParameter, 
    TrainOptimizedParameter, 
    TrainOwnFunction
)

from colda.algorithm.strategy.custom.test_custom import (
    TestFixedParameter,
    TestOptimizedParameter,
    TestOwnFunction
)

from typing import Callable

from typeguard import typechecked


class AbstractCustomFactory(ABC):
    '''
    Abstract class for custom algorithm factory

    Parameters
    ----------
    None

    Returns
    -------
    None
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
        
        Parameters
        ----------
        None

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
        
        Parameters
        ----------
        None

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
        
        Parameters
        ----------
        None

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
        
        Parameters
        ----------
        None

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
