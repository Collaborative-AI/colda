import pytest
from colda.tests.test_database.conftest import DatabaseOperator_instance

from colda.error import DuplicateKeyError


class TestTrainSponsorMetadataDatabase:

    @pytest.mark.usefixtures('DatabaseOperator_instance')
    @pytest.mark.parametrize("test_record, expected", [
        (
            ('test', 'test', 'test', 'test', 'test', 'test', 'test', 'test', 'test'), 
            None
        ),
    ])
    def test_store_record(self, DatabaseOperator_instance, test_record, expected):
        DatabaseOperator_instance.set_database(database_type='train_assistor_metadata')
        response = DatabaseOperator_instance.store_record(
            user_id=test_record[0], 
            train_id=test_record[1], 
            mode=test_record[2], 
            task_mode=test_record[3],
            model_name=test_record[4], 
            train_file_path=test_record[5], 
            train_id_column=test_record[6], 
            train_data_column=test_record[7]
        )
        assert response == expected

    
    @pytest.mark.usefixtures('DatabaseOperator_instance')
    @pytest.mark.parametrize("test_record, expected", [
        (
            ('test', 'test'), 
            ('test', 'test', 'test', 'test', 'test', 'test', 'test', None, None)
        ),
    ])
    def test_get_record(self, DatabaseOperator_instance, test_record, expected):
        DatabaseOperator_instance.set_database(database_type='train_assistor_metadata')
        response = DatabaseOperator_instance.get_record(
            user_id=test_record[0], 
            train_id=test_record[1], 
        )
        assert response == expected