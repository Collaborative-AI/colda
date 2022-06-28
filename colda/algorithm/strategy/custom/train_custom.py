from __future__ import annotations

from abc import ABC, abstractmethod

from colda.algorithm.train_stage.api import (
    MakeTrain,
    MakeResult
)

from typing import Callable

from typeguard import typechecked


class AbstractTrainCustom(ABC):
    '''
    Abstract class for the custom part of
    train algorithm

    Parameters
    ----------
    None

    Returns
    -------
    None
    '''

    @classmethod
    @abstractmethod
    def make_train(cls, **kwargs):
        pass
    
    @classmethod
    @abstractmethod
    def make_result(cls, **kwargs):
        pass


class TrainFixedParameter(AbstractTrainCustom):
    '''
    Fix learning rate in the make_train and make_result stage

    Attributes
    ----------
    None

    Methods
    -------
    make_train
    make_result
    '''

    @classmethod
    def make_train(
        cls, **kwargs
    ) -> None:
        '''
        Call MakeTrain.make_train
        
        Parameters
        ----------
        **kwargs : Any

        Returns
        -------
        None
        '''
        return MakeTrain.make_train(**kwargs)
    
    @classmethod
    def make_result(
        cls, **kwargs
    ) -> None:
        '''
        Call MakeResult.make_result
        
        Parameters
        ----------
        **kwargs : Any

        Returns
        -------
        None
        '''
        return MakeResult.make_result(**kwargs)


class TrainOptimizedParameter(AbstractTrainCustom):
    '''
    Learnable learning rate in the make_train 
    and make_result stage

    Attributes
    ----------
    None

    Methods
    -------
    make_train
    make_result
    '''

    @classmethod
    def make_train(
        cls, **kwargs
    ) -> None:
        '''
        Call MakeTrain.make_train
        
        Parameters
        ----------
        **kwargs : Any

        Returns
        -------
        None
        '''
        return MakeTrain.make_train(**kwargs)
    
    @classmethod
    def make_result(cls, **kwargs):
        '''
        Call MakeResult.make_result
        
        Parameters
        ----------
        **kwargs : Any

        Returns
        -------
        None
        '''
        return MakeResult.make_result(**kwargs)


class TrainOwnFunction(AbstractTrainCustom):
    '''
    Custom testing algo in the make_train 
    and make_result stage

    Attributes
    ----------
    None

    Methods
    -------
    make_train
    make_result
    '''
    __OwnFunction = None

    @property
    def OwnFunction(cls):
        return cls.__OwnFunction

    @OwnFunction.setter
    def OwnFunction(
        cls, OwnFunction: dict[str, Callable]
    ) -> None:
        cls.__OwnFunction = OwnFunction

    @classmethod
    def make_train(cls, **kwargs):
        '''
        Call OwnFunction['MakeTrain']
        
        Parameters
        ----------
        **kwargs : Any

        Returns
        -------
        None
        '''
        return cls.OwnFunction['MakeTrain'](**kwargs)
    
    @classmethod
    def make_result(cls, **kwargs):
        '''
        Call OwnFunction['MakeResult']
        
        Parameters
        ----------
        **kwargs : Any

        Returns
        -------
        None
        '''
        return cls.OwnFunction['MakeResult'](**kwargs)

        