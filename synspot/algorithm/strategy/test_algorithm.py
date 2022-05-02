from __future__ import annotations

from synspot.algorithm.strategy.base import BaseAlgorithmStrategy

from synspot.algorithm.strategy.abstract_algorithm_strategy import AbstractTestAlgorithmStrategy

from synspot.algorithm.test_stage import (
    MakeEval,
    MakeTestLocal,
    MakeTest,
)

from synspot.algorithm.custom.custom_factory import GetTestFixedParameter


class TestAlgorithm(AbstractTestAlgorithmStrategy, BaseAlgorithmStrategy):
    __TestAlgorithm_instance = None
    # strategy pattern
    # 传给他不同的行为，algo使用

    def __init__(self) -> None:
        self.__test_custom = GetTestFixedParameter.create_custom()

    @classmethod
    def get_instance(cls) -> type[TestAlgorithm]:
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

    def make_test_local(self, **kwargs):
        return MakeTestLocal.make_test_local(**kwargs)

    def make_test(self, **kwargs):
        return self.__test_custom.make_test(**kwargs)

    def make_eval(self, **kwargs):
        return self.__test_custom.make_eval(**kwargs)
