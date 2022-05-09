Documentaion:
https://docutils-zh-cn.readthedocs.io/zh_CN/latest/user/rst/cheatsheet.html
1. 分Module done
2. (done) 加粗 => ** **
3. (done )红字 => `` ``
4. !Note => .. note::
5. !Warning => .. warning:: 
6. code block done :py:exc:` `
7. 文字中分小块 

1. 
The 'Synspot' package
This package aims to help various entities assist each other in supervised learning tasks without sharing data, models, and objective function. 

Available Implementations
At this time, the 'Synspot' API is available right out of the box to the general public for personal use in the following programming languages

A Quick Setup Guide
Getting Started

1. Install the 'slants' package using pip
# Installing package
python -m pip install Synspot

2. Import the Model and Experiment API classes
from Synspot import Package

Using the package
1. Register
userRegister(username, email, password)

Password Requirements:
1. At least 8 characters. At most 25 characters
2. A mixture of both uppercase and lowercase letters
3. A mixture of letters and numbers
4. Inclusion of at least one special character, e.g., ! @ # ? ]

2. Login
userLogin(username, password)

3. Set default information
set_default_data_path(default_mode: str, default_task_mode: str, default_model_name: str, default_file_path: str=None, default_id_column: str=None, default_data_column: str=None)

Parameters:
    default_mode - String. Auto or Manual
    default_task_mode - String. Classification or Regression
    default_model_name - String. Specific model, such as LinearRegression, DecisionTree.
    default_file_path - String. File position of dataset using for training and testing
    default_id_column - String. Data column of default dataset
    default_data_column - String. Target column of default dataset

3. Start Training
callForTrain(maxRound: int, assistors: list, train_file_path: str, train_id_column: str, train_data_column: str, train_target_column: str, task_mode: str, model_name: str, metric_name: str, task_name: str=None, task_description: str=None)

Parameters:
    maxRound - Integer. Maximum training round
    assistors - List. The List of assistors' usernames
    train_file_path - String. Input path address of training data path
    train_id_column - String. ID column of Input File
    train_data_column - String. Data column of Input File
    train_target_column - String. Target column of Input File
    task_mode - String. Classification or Regression
    model_name - String. Specific model, such as LinearRegression, DecisionTree.
    metric_name - String. Metric to measure the result, such as MAD, RMSE, R2.
    task_name - None or String. The name of current task.
    task_description - None or String. The description of current task

4. Start Testing
callForTest(task_id: str, test_file_path: str, test_id_column: str, test_data_column: str, 
            test_target_column: str, test_name: str=None, test_description: str=None):

Parameters:
    task_id - String. The task that the user wanted to test
    test_file_path - String. Input path address of testing data path
    test_id_column - String. ID column of Input File
    test_data_column - String. Data column of Input File
    test_target_column - String. Target column of Input File
    test_name - None or String. The name of current test
    test_description - None or String. The description of current test






import collections
from typing import List
from abc import ABC, abstractmethod

from .PI import PI
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
        PI_instance = PI.get_PI_instance()
        Database_class_instance = Database_class.get_Database_class_instance()
        user_id = self.PI_instance.user_id
        assert user_id is not None

        return self._database_strategy.search_database(user_id, Database_class_instance)



