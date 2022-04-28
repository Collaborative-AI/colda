from abc import ABC, abstractmethod

from synspot.algorithm.test_stage import (
    MakeTest,
    MakeEval
)


class AbstractTestCustom(ABC):

    @abstractmethod
    def make_test(self, *args):
        pass

    @abstractmethod
    def make_eval(self, *args):
        pass


class TestFixedParameter(AbstractTestCustom):

    def make_test(self, *args):
        return MakeTest.make_test(*args)
    
    def make_eval(self, *args):
        return MakeEval.make_eval(*args)


class TestOptimizedParameter(AbstractTestCustom):

    def make_test(self, *args):
        return MakeTest.make_test(*args)
        
    def make_eval(self, *args):
        return MakeEval.make_eval(*args)


class TestOwnFunction(AbstractTestCustom):
    
    def __init__(self, OwnFunction):
        self.OwnFunction = OwnFunction
        
    def make_test(self, *args):
        return self.OwnFunction['MakeTest'].make_test(*args)
        
    def make_eval(self, *args):
        return self.OwnFunction['MakeEval'].make_eval(*args)
        