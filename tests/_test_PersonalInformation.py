"""
tests.test_curves.py
~~~~~~~~~~~~~~~~~~~~

Test suite for the curves.py module that handles everything to do with
supply and demand curves.
"""
import json
from typing import Any, Dict, List
from copy import deepcopy

from Synspot.PersonalInformation import PersonalInformation
import pytest

class TestPersonalInformation:
    def get_instance(self):
        PersonalInformation_instance = PersonalInformation()
        return PersonalInformation_instance

    def test_set_user_id(self):
        PersonalInformation_instance = self.get_instance()
        user_id = 'ceshi'
        PersonalInformation_instance.set_user_id(user_id)
        assert PersonalInformation_instance.get_user_id() == user_id

    def test_default_mode(self):
        PersonalInformation_instance = self.get_instance()
        default_mode = PersonalInformation_instance.get_default_mode()
        assert default_mode == 'manual'

    def test_set_wrong_default_mode(self):
        PersonalInformation_instance = self.get_instance()
        with pytest.raises(Exception):
            mode = 'zz'
            PersonalInformation_instance.set_default_mode(mode)
    
    def test_set_default_mode(self):
        PersonalInformation_instance = self.get_instance()
        mode = 'auto'
        PersonalInformation_instance.set_default_mode(mode)
        assert PersonalInformation_instance.get_default_mode() == mode

    