import pytest
from synspot.tests.test_database.conftest import TrainAlgorithmDatabase_instance

class TestTrainAlgorithmDatabase:

    @pytest.mark.usefixtures('TrainAlgorithmDatabase_instance')
    @pytest.mark.parametrize("url, expected_url", [
        (('prefix', 'root', 'suffix'), '/prefix/root/suffix'),
        (('prefix', 'root', None), '/prefix/root')
    ])
    def test_process_url(self, network_instance, url, expected_url):
        processed_url = network_instance.process_url(
            url_prefix=url[0],
            url_root=url[1],
            url_suffix=url[2]
        )

        assert processed_url == f'{network_instance.base_url}{expected_url}'