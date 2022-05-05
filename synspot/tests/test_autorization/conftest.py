import pytest
from synspot.authorization import Authorization

from synspot.network import Network

@pytest.fixture
def Network_instance():
    print('Initiate Network Instance')
    instance = Network.get_instance()
    return instance

@pytest.fixture
def Authorization_instance():
    instance = Authorization.get_instance()
    return instance