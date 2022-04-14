from abc import ABC, abstractmethod

from synspot.algorithm.custom import CustomConcrete_FixedParameter, CustomConcrete_OptimizerTrainedParameter, CustomConcrete_OwnFunction
class CustomAbstractFactory(ABC):
    """抽象工厂
    """

    @classmethod
    @abstractmethod
    def create_custom(cls):
        pass

class FixedParameterFactory(CustomAbstractFactory):
    """具体工厂
    """
    @classmethod
    def create_custom(cls):
        return CustomConcrete_FixedParameter()

class OptimizerTrainedParameteFactory(CustomAbstractFactory):
    """具体工厂
    """
    @classmethod
    def create_custom(cls):
        return CustomConcrete_OptimizerTrainedParameter()

class OwnFunctionFactory(CustomAbstractFactory):
    """具体工厂
    """
    @classmethod
    def create_custom(cls, OwnFunction=None):
        return CustomConcrete_OwnFunction(OwnFunction)

