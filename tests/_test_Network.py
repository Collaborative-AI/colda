"""
tests.test_curves.py
~~~~~~~~~~~~~~~~~~~~

Test suite for the curves.py module that handles everything to do with
supply and demand curves.
"""
import json
from typing import Any, Dict, List
from copy import deepcopy

from Synspot.Network import Network
import pytest

class TestNetwork:
    def get_instance(self):
        Network_instance = Network()
        return Network_instance

    def test_set_token(self):
        Network_instance = self.get_instance()
        token = 'ceshi'
        Network_instance.set_token(token)
        assert Network_instance.get_token() == token



    