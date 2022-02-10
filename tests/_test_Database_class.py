"""
tests.test_curves.py
~~~~~~~~~~~~~~~~~~~~

Test suite for the curves.py module that handles everything to do with
supply and demand curves.
"""
import json
from typing import Any, Dict, List
from copy import deepcopy

from py_pkg.Database_class import Database_class
import pytest

class TestDatabase_class:
    def get_instance(self):
        Database_class_instance = Database_class()
        return Database_class_instance

    def test_User_Default_Table(self):
        Database_class_instance = self.get_instance()
        user_id = 'xie1'
        default_mode = 'manual'
        default_model_name = 'linear'
        res = Database_class_instance.store_User_Default_Table(user_id=user_id, default_mode=default_mode, default_model_name=default_model_name)
        assert res == 'User_Default_Table stores successfully'

        res = Database_class_instance.get_User_Default_Table(user_id)
        assert res[0] == user_id
        assert res[1] == default_mode
        assert res[2] == default_model_name

    def test_User_Sponsor_Table(self):
        Database_class_instance = self.get_instance()
        user_id = 'xie1'
        task_id = 'zzz'
        test_indicator = 'train'
        task_mode = 'regression'
        model_name = 'linear'
        metric_name = 'MAD_RMSE_R2'
        res = Database_class_instance.store_User_Sponsor_Table(user_id=user_id, task_id=task_id, test_indicator=test_indicator,
                                                                task_mode=task_mode, model_name=model_name, metric_name=metric_name)
        assert res == 'User_Sponsor_Table stores successfully'

        res = Database_class_instance.get_User_Sponsor_Table(user_id=user_id, task_id=task_id, test_indicator=test_indicator)
        assert res[0] == task_mode
        assert res[1] == model_name
        assert res[2] == metric_name


    def test_User_Assistor_Table(self):
        Database_class_instance = self.get_instance()
        user_id = 'xie1'
        task_id = 'zzz'
        test_indicator = 'train'
        mode = 'auto'
        model_name = 'linear'
        
        res = Database_class_instance.store_User_Assistor_Table(user_id=user_id, task_id=task_id, test_indicator=test_indicator, 
                                                                mode=mode, model_name=model_name)
        assert res == 'User_Assistor_Table stores successfully'

        res = Database_class_instance.get_User_Assistor_Table(user_id=user_id, task_id=task_id, test_indicator=test_indicator)
        assert res[0] == mode
        assert res[1] == model_name
    
   
    