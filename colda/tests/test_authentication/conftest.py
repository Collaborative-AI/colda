import pytest
from authentication.api import Authentication

from network.api import Network

@pytest.fixture
def Network_instance():
    print('Unittest: Initiate Network Instance')
    instance = Network.get_instance()
    return instance

@pytest.fixture
def Authentication_instance():
    print('Unittest: Initiate Authentication Instance')
    instance = Authentication.get_instance()
    return instance