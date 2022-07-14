from __future__ import annotations

from colda.algorithm.strategy.base import BaseAlgorithmStrategy

from colda.algorithm.strategy.abstract_algorithm_strategy import AbstractTestAlgorithmStrategy

from colda.algorithm.strategy.utils import algorithm_process

from colda.algorithm.test_stage.api import MakeTestLocal

from colda.algorithm.strategy.custom.api import GetTestFixedParameter

from typeguard import typechecked


#@typechecked
class TestAlgorithm(AbstractTestAlgorithmStrategy, BaseAlgorithmStrategy):
    '''
    Strategy pattern to manage test algorithm

    Attributes
    ----------
    train_custom

    Methods
    -------
    get_instance
    make_test_local
    make_test
    make_eval
    '''

    __TestAlgorithm_instance = None

    def __init__(self) -> None:
        self.__test_custom = GetTestFixedParameter.get_class()

    @classmethod
    def get_instance(cls) -> TestAlgorithm:
        '''
        Singleton pattern. 
        Get instance of current class.

        Returns
        -------
        TestAlgorithm
        '''
        if cls.__TestAlgorithm_instance == None:
            cls.__TestAlgorithm_instance = TestAlgorithm()

        return cls.__TestAlgorithm_instance

    @property
    def test_custom(self):
        '''
        Get strategy object

        Returns
        -------
        Any
        '''
        return self.__test_custom

    @test_custom.setter
    def test_custom(
        self, test_custom
    ) -> None:
        '''
        Set strategy object

        Returns
        -------
        Any
        '''
        self.__test_custom = test_custom

    @algorithm_process
    def make_test_local(
        self, **kwargs
    ) -> list:
        '''
        call specific function

        Parameters
        ----------
        **kwargs : Any

        Returns
        -------
        list
        '''
        return MakeTestLocal.make_test_local(**kwargs)

    @algorithm_process
    def make_test(
        self, **kwargs
    ) -> list:
        '''
        call specific function

        Parameters
        ----------
        **kwargs : Any

        Returns
        -------
        list
        '''
        return self.__test_custom.make_test(**kwargs)

    @algorithm_process
    def make_eval(
        self, **kwargs
    ) -> list:
        '''
        call specific function

        Parameters
        ----------
        **kwargs : Any

        Returns
        -------
        list
        '''
        return self.__test_custom.make_eval(**kwargs)
