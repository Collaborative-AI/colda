import pytest

from colda.network import Network

@pytest.fixture
def network_instance():
    print('Initiate Network Instance')
    __Network_instance = Network.get_instance()
    return __Network_instance

# @pytest.fixture
# def network_error():
#     return StatusCodeError