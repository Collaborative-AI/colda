from abc import ABC, abstractmethod

from synspot.algorithm.custom.train_custom import (
    TrainFixedParameter, 
    TrainOptimizedParameter, 
    TrainOwnFunction
)

from synspot.algorithm.custom.test_custom import (
    TestFixedParameter,
    TestOptimizedParameter,
    TestOwnFunction
)

class AbstractCustomFactory(ABC):
    """
    Abstract Factory
    """
    @classmethod
    @abstractmethod
    def create_custom(cls):
        pass


class GetTrainFixedParameter(AbstractCustomFactory):
    """
    Concrete Factory
    """
    @classmethod
    def create_custom(cls):
        return TrainFixedParameter


class GetTrainOptimizedParameter(AbstractCustomFactory):
    """
    Concrete Factory
    """
    @classmethod
    def create_custom(cls):
        return TrainOptimizedParameter


class GetTrainOwnFunction(AbstractCustomFactory):
    """
    Concrete Factory
    """
    @classmethod
    def create_custom(cls, OwnFunction=None):
        return TrainOwnFunction(OwnFunction)


class GetTestFixedParameter(AbstractCustomFactory):
    """
    Concrete Factory
    """
    @classmethod
    def create_custom(cls):
        return TestFixedParameter


class GetTestOptimizedParameter(AbstractCustomFactory):
    """
    Concrete Factory
    """
    @classmethod
    def create_custom(cls):
        return TestOptimizedParameter


class GetTestOwnFunction(AbstractCustomFactory):
    """
    Concrete Factory
    """
    @classmethod
    def create_custom(cls, OwnFunction=None):
        return TestOwnFunction(OwnFunction)
