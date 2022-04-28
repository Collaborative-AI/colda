from __future__ import annotations

from synspot.algorithm.strategy.base import BaseAlgorithm

from synspot.algorithm.strategy.abstract_algorithm import AbstractTestAlgorithmStrategy

from synspot.algorithm.test_stage import (
    MakeEval,
    MakeTestLocal,
    MakeTest,
)

from synspot.algorithm.custom.custom_factory import FixedParameterFactory

from typing import (
    Type,
    List,
    Tuple
)


class TestAlgorithm(AbstractTestAlgorithmStrategy, BaseAlgorithm):
    __TestAlgorithm_instance = None
    # strategy pattern
    # 传给他不同的行为，algo使用

    def __init__(self) -> None:
        self.__test_custom = FixedParameterFactory.create_custom()

    @classmethod
    def get_algorithm_instance(cls) -> Type[TestAlgorithm]:
        if cls.__TestAlgorithm_instance == None:
            cls.__TestAlgorithm_instance = TestAlgorithm()

        return cls.__TestAlgorithm_instance

    @property
    def test_custom(self):
        """
        The Context maintains a reference to one of the Strategy objects. The
        Context does not know the concrete class of a strategy. It should work
        with all strategies via the Strategy interface.
        """

        return self.__test_custom

    @test_custom.setter
    def test_custom(self, test_custom) -> None:
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """

        self.__test_custom = test_custom

    def make_test_local(self, *args):
        return MakeTestLocal.make_test_local(*args)

    def make_test(self, *args):
        return self.__test_custom.make_test(*args)

    def make_eval(self, *args):
        return self.__test_custom.make_eval(*args)
