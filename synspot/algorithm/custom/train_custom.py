from abc import ABC, abstractmethod

from synspot.algorithm.train_stage import (
    MakeTrain,
    MakeResult
)


class AbstractTrainCustom(ABC):

    @abstractmethod
    def make_train(self, *args):
        pass
    
    @abstractmethod
    def make_result(self, *args):
        pass


class TrainFixedParameter(AbstractTrainCustom):
    
    def make_train(self, *args):
        return MakeTrain.make_train(*args)
        
    def make_result(self, *args):
        return MakeResult.make_result(*args)


class TrainOptimizedParameter(AbstractTrainCustom):
    
    def make_train(self, *args):
        return MakeTrain.make_train(*args)
        
    def make_result(self, *args):
        return MakeResult.make_result(*args)


class TrainOwnFunction(AbstractTrainCustom):
    
    def __init__(self, OwnFunction):
        self.OwnFunction = OwnFunction

    def make_train(self, *args):
        return self.OwnFunction['MakeTrain'].make_train(*args)
        
    def make_result(self, *args):
        return self.OwnFunction['MakeResult'].make_result(*args)

        