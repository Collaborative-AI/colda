import pytest
from colda.authentication.api import Authentication

from colda.network.api import Network

@pytest.fixture
def Network_instance():
    print('Initiate Network Instance')
    instance = Network.get_instance()
    return instance

@pytest.fixture
def Authentication_instance():
    instance = Authentication.get_instance()
    return instance