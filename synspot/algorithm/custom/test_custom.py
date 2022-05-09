from __future__ import annotations

from abc import ABC, abstractmethod

from synspot.algorithm.test_stage import (
    MakeTest,
    MakeEval
)


class AbstractTestCustom(ABC):

    @classmethod
    @abstractmethod
    def make_test(cls, **kwargs):
        pass

    @classmethod
    @abstractmethod
    def make_eval(cls, **kwargs):
        pass


class TestFixedParameter(AbstractTestCustom):

    @classmethod
    def make_test(cls, **kwargs):
        return MakeTest.make_test(**kwargs)
    
    @classmethod
    def make_eval(cls, **kwargs):
        return MakeEval.make_eval(**kwargs)


class TestOptimizedParameter(AbstractTestCustom):

    @classmethod
    def make_test(cls, **kwargs):
        return MakeTest.make_test(**kwargs)
    
    @classmethod
    def make_eval(cls, **kwargs):
        return MakeEval.make_eval(**kwargs)


class TestOwnFunction(AbstractTestCustom):
    
    def __init__(cls, OwnFunction):
        cls.OwnFunction = OwnFunction
    
    @classmethod
    def make_test(cls, **kwargs):
        return cls.OwnFunction['MakeTest'].make_test(**kwargs)

    @classmethod    
    def make_eval(cls, **kwargs):
        return cls.OwnFunction['MakeEval'].make_eval(**kwargs)
        