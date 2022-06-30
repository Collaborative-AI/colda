import pytest

from colda.network.api import Network

@pytest.fixture
def network_instance():
    print('Unittest: Initiate Network Instance')
    __Network_instance = Network.get_instance()
    return __Network_instance
