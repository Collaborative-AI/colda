
from abc import ABC, abstractmethod

class AbstractTrainMainWorkflow(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @classmethod
    @abstractmethod
    def get_TrainRequest_instance(cls):
        pass

    @abstractmethod
    def handleTrainRequest(self, *args):
        pass
    
    @abstractmethod
    def unread_request(self, *args):
        pass

    @abstractmethod
    def unread_match_identifier(self, *args):
        pass

    @abstractmethod
    def unread_match_identifier_sponsor(self, *args):
        pass

    @abstractmethod
    def unread_match_identifier_assistor(self, *args):
        pass

    @abstractmethod
    def unread_situation(self, *args):
        pass

    @abstractmethod
    def unread_situation_sponsor(self, *args):
        pass
    
    @abstractmethod
    def unread_situation_assistor_train_part(self, *args):
        pass

    @abstractmethod
    def unread_situation_assistor(self, *args):
        pass

    @abstractmethod
    def unread_output(self, *args):
        pass

    @abstractmethod
    def unread_output_singleTask(self, *args):
        pass

    @abstractmethod
    def unread_output_make_result_helper(self, *args):
        pass

    @abstractmethod
    def unread_train_stop(self, *args):
        pass

class AbstractTestMainWorkflow(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @classmethod
    @abstractmethod
    def get_TestRequest_instance(cls):
        pass

    @abstractmethod
    def handleTestRequest(self, *args):
        pass
    
    @abstractmethod
    def unread_test_request(self, *args):
        pass

    @abstractmethod
    def unread_test_match_identifier(self, *args):
        pass

    @abstractmethod
    def unread_test_match_identifier_sponsor(self, *args):
        pass

    @abstractmethod
    def unread_test_match_identifier_assistor(self, *args):
        pass

    @abstractmethod
    def unread_test_output(self, *args):
        pass

    @abstractmethod
    def unread_test_output_singleTask(self, *args):
        pass
    
    @abstractmethod
    def unread_test_output_make_eval_helper(self, *args):
        pass