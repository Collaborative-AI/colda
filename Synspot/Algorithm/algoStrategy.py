from abc import ABC, abstractmethod

from synspot.algorithm.algoAPI import make_train_local, make_test_local, make_hash, save_match_id, \
                                      make_match_idx, make_residual, save_residual, save_output

from synspot.algorithm.customFactory import FixedParameterFactory

class AlgoAbstractStrategy(ABC):

    @abstractmethod
    def make_train_local(self, *args):
        pass
    
    @abstractmethod
    def make_test_local(self, *args):
        pass
    
    @abstractmethod
    def make_hash(self, *args):
        pass
    
    @abstractmethod
    def save_match_id(self, *args):
        pass
    
    @abstractmethod
    def make_match_idx(self, *args):
        pass
    
    @abstractmethod
    def make_residual(self, *args):
        pass
    
    @abstractmethod
    def save_residual(self, *args):
        pass
    
    @abstractmethod
    def make_train(self, *args):
        pass
    
    @abstractmethod
    def save_output(self, *args):
        pass

    @abstractmethod
    def make_result(self, *args):
        pass

    @abstractmethod
    def make_test(self, *args):
        pass

    @abstractmethod
    def make_eval(self, *args):
        pass


class AlgoConcreteStategy(AlgoAbstractStrategy):
    # strategy pattern
    # 传给他不同的行为，algo使用

    def __init__(self) -> None:
        self._train_custom = FixedParameterFactory.create_custom()
        self._test_custom = FixedParameterFactory.create_custom()

    @property
    def train_custom(self):
        """
        The Context maintains a reference to one of the Strategy objects. The
        Context does not know the concrete class of a strategy. It should work
        with all strategies via the Strategy interface.
        """

        return self._train_custom

    @train_custom.setter
    def train_custom(self, train_custom) -> None:
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """

        self._train_custom = train_custom

    @property
    def test_custom(self):
        """
        The Context maintains a reference to one of the Strategy objects. The
        Context does not know the concrete class of a strategy. It should work
        with all strategies via the Strategy interface.
        """

        return self._test_custom

    @test_custom.setter
    def test_custom(self, test_custom) -> None:
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """

        self._test_custom = test_custom

    def make_train_local(self, *args):
        return make_train_local(*args)
    
    def make_test_local(self, *args):
        return make_test_local(*args)
    
    def make_hash(self, *args):
        return make_hash(*args)
    
    def save_match_id(self, *args):
        return save_match_id(*args)
    
    def make_match_idx(self, *args):
        return make_match_idx(*args)
    
    def make_residual(self, *args):
        return make_residual(*args)
    
    def save_residual(self, *args):
        return save_residual(*args)
    
    def save_output(self, *args):
        return save_output(*args)
    
    def make_train(self, *args):
        return self._train_custom.make_train(*args)

    def make_result(self, *args):
        return self._train_custom.make_result(*args)

    def make_test(self, *args):
        return self._test_custom.make_test(*args)

    def make_eval(self, *args):
        return self._test_custom.make_eval(*args)
