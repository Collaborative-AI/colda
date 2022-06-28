import pytest

from colda.database.strategy.api import DatabaseOperator

@pytest.fixture
def DatabaseOperator_instance():
    instance = DatabaseOperator.get_instance()
    return instance