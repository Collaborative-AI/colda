import collections
from typing import List
from abc import ABC, abstractmethod

from .PersonalInformation import PersonalInformation
from .Database_class import Database_class

class Strategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """
    @abstractmethod
    def search_database(self, user_id, Database_class_instance):
        pass

class get_all_task_id_as_sponsor(Strategy):
    def search_database(self, user_id, Database_class_instance):   
        pass

class get_all_test_id_as_sponsor(Strategy):
    def search_database(self, user_id, Database_class_instance):
        pass

class get_all_task_id_as_assistor(Strategy):
    def search_database(self, user_id, Database_class_instance):
        pass

class get_all_test_id_as_sponsor(Strategy):
    def search_database(self, user_id, Database_class_instance):
        pass

class database_strategy_interface():
    """
    The Context defines the interface of interest to clients.
    """

    def __init__(self, database_strategy: Strategy) -> None:
        """
        Usually, the Context accepts a strategy through the constructor, but
        also provides a setter to change it at runtime.
        """

        self._database_strategy = database_strategy

    @property
    def database_strategy(self) -> Strategy:
        """
        The Context maintains a reference to one of the Strategy objects. The
        Context does not know the concrete class of a strategy. It should work
        with all strategies via the Strategy interface.
        """

        return self._database_strategy

    @database_strategy.setter
    def database_strategy(self, database_strategy: Strategy) -> None:
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """
        self._database_strategy = database_strategy

    def execute_strategy(self):
        PersonalInformation_instance = PersonalInformation.get_PersonalInformation_instance()
        Database_class_instance = Database_class.get_Database_class_instance()
        user_id = self.PersonalInformation_instance.user_id
        assert user_id is not None

        return self._database_strategy.search_database(user_id, Database_class_instance)



