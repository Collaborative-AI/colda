from abc import ABC, abstractmethod

from synspot.algorithm.algoAPI import make_train, make_result, make_test, make_eval

class CustomAbstract(ABC):

    @abstractmethod
    def make_train(self, *args):
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

class CustomConcrete_FixedParameter(CustomAbstract):
    
    def make_train(self, *args):
        return make_train(*args)
        
    def make_result(self, *args):
        return make_result(*args)

    def make_test(self, *args):
        return make_test(*args)
    
    def make_eval(self, *args):
        return make_eval(*args)

class CustomConcrete_OptimizerTrainedParameter(CustomAbstract):
    
    def make_train(self, *args):
        return make_train(*args)
        
    def make_result(self, *args):
        return make_result(*args)

    def make_test(self, *args):
        return make_test(*args)
        
    def make_eval(self, *args):
        return make_eval(*args)

class CustomConcrete_OwnFunction(CustomAbstract):
    
    def __init__(self, OwnFunction):
        self.OwnFunction = OwnFunction

    def make_train(self, *args):
        return self.OwnFunction['make_train'](*args)
        
    def make_result(self, *args):
        return self.OwnFunction['make_result'](*args)
        
    def make_test(self, *args):
        return self.OwnFunction['make_test'](*args)
        
    def make_eval(self, *args):
        return self.OwnFunction['make_eval'](*args)
        