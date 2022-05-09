"""
tests.test_curves.py
~~~~~~~~~~~~~~~~~~~~

Test suite for the curves.py module that handles everything to do with
supply and demand curves.
"""
import json
from typing import Any, Dict, List
from copy import deepcopy

from Synspot.PI import PI
import pytest

class TestPI:
    def get_instance(self):
        PI_instance = PI()
        return PI_instance

    def test_set_user_id(self):
        PI_instance = self.get_instance()
        user_id = 'ceshi'
        PI_instance.user_id = user_id
        assert PI_instance.user_id == user_id

    def test_default_mode(self):
        PI_instance = self.get_instance()
        default_mode = PI_instance.default_mode
        assert default_mode == 'manual'

    def test_set_wrong_default_mode(self):
        PI_instance = self.get_instance()
        with pytest.raises(Exception):
            default_mode = 'zz'
            PI_instance.default_mode = default_mode
    
    def test_set_default_mode(self):
        PI_instance = self.get_instance()
        default_mode = 'auto'
        PI_instance.default_mode = default_mode
        assert PI_instance.default_mode == default_mode

    