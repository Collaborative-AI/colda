from __future__ import annotations

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
    def get_instance(cls):
        pass

    @abstractmethod
    def find_assistor(self, *args):
        pass
    
    @abstractmethod
    def train_assistor_request(self, *args):
        pass

    @abstractmethod
    def train_match_identifier(self, *args):
        pass

    @abstractmethod
    def train_sponsor_match_identifier(self, *args):
        pass

    @abstractmethod
    def train_assistor_match_identifier(self, *args):
        pass

    @abstractmethod
    def train_situation(self, *args):
        pass

    @abstractmethod
    def train_sponsor_situation(self, *args):
        pass
    
    @abstractmethod
    def train_assistor_situation(self, *args):
        pass

    @abstractmethod
    def train_output(self, *args):
        pass

    @abstractmethod
    def stop_train(self, *args):
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
    def get_instance(cls):
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