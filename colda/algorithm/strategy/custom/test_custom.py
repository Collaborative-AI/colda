from __future__ import annotations

from abc import ABC, abstractmethod

from colda.algorithm.test_stage.api import (
    MakeTest,
    MakeEval
)

from typing import Callable

from typeguard import typechecked


class AbstractTestCustom(ABC):
    '''
    Abstract class for the custom part of
    test algorithm

    Parameters
    ----------
    None

    Returns
    -------
    None
    '''

    @classmethod
    @abstractmethod
    def make_test(cls, **kwargs):
        pass

    @classmethod
    @abstractmethod
    def make_eval(cls, **kwargs):
        pass


class TestFixedParameter(AbstractTestCustom):
    '''
    Fix learning rate in the make_test and make_eval stage

    Attributes
    ----------
    None

    Methods
    -------
    make_test
    make_eval
    '''

    @classmethod
    def make_test(
        cls, **kwargs
    ) -> None:
        '''
        Call MakeTest.make_test
        
        Parameters
        ----------
        **kwargs : Any

        Returns
        -------
        None
        '''
        return MakeTest.make_test(**kwargs)
    
    @classmethod
    def make_eval(
        cls, **kwargs
    ) -> None:
        '''
        Call MakeEval.make_eval
        
        Parameters
        ----------
        **kwargs : Any

        Returns
        -------
        None
        '''
        return MakeEval.make_eval(**kwargs)


class TestOptimizedParameter(AbstractTestCustom):
    '''
    Learnable learning rate in the make_test 
    and make_eval stage

    Attributes
    ----------
    None

    Methods
    -------
    make_test
    make_eval
    '''

    @classmethod
    def make_test(
        cls, **kwargs
    ) -> None:
        '''
        Call MakeTest.make_test
        
        Parameters
        ----------
        **kwargs : Any

        Returns
        -------
        None
        '''
        return MakeTest.make_test(**kwargs)
    
    @classmethod
    def make_eval(
        cls, **kwargs
    ) -> None:
        '''
        Call MakeEval.make_eval
        
        Parameters
        ----------
        **kwargs : Any

        Returns
        -------
        None
        '''
        return MakeEval.make_eval(**kwargs)


class TestOwnFunction(AbstractTestCustom):
    '''
    Custom testing algo in the make_test 
    and make_eval stage

    Attributes
    ----------
    None

    Methods
    -------
    make_test
    make_eval
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
    def make_test(
        cls, **kwargs
    ) -> None:
        '''
        Call OwnFunction['MakeTest']
        
        Parameters
        ----------
        **kwargs : Any

        Returns
        -------
        None
        '''
        return cls.OwnFunction['MakeTest'](**kwargs)

    @classmethod    
    def make_eval(
        cls, **kwargs
    ) -> None:
        '''
        Call OwnFunction['MakeEval']
        
        Parameters
        ----------
        **kwargs : Any

        Returns
        -------
        None
        '''
        return cls.OwnFunction['MakeEval'](**kwargs)
        