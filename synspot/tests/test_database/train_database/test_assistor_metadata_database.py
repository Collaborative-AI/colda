import pytest
from synspot.tests.test_database.conftest import DatabaseOperator_instance

from synspot.error import DuplicateKeyError


class TestTrainSponsorMetadataDatabase:

    @pytest.mark.usefixtures('DatabaseOperator_instance')
    @pytest.mark.parametrize("test_record, expected_res", [
        (('test', 'test', 'test', 'test', 'test', 'test', 'test', 'test', 'test'), 
        "TrainAssistorMetadataDatabase stores ('test', 'test') successfully!"),
        (('test', 'test', 'test', 'test', 'test', 'test', 'test', 'test', 'test'), 
        DuplicateKeyError)
    ])
    def test_store_record(self, DatabaseOperator_instance, test_record, expected_res):
        DatabaseOperator_instance.set_database(database_type='train_assistor_metadata')
        response = DatabaseOperator_instance.store_record(
            user_id=test_record[0], 
            train_id=test_record[1], 
            mode=test_record[2], 
            task_mode=test_record[3],
            model_name=test_record[4], 
            train_file_path=test_record[5], 
            train_id_column=test_record[6], 
            train_data_column=test_record[7],
        )
        assert response == expected_res

    
    @pytest.mark.usefixtures('DatabaseOperator_instance')
    @pytest.mark.parametrize("test_record, expected_res", [
        (('test', 'test'), ('test', 'test', 'test', 'test', 'test', 'test', 'test', None, None)),
    ])
    def test_get_record(self, DatabaseOperator_instance, test_record, expected_res):
        DatabaseOperator_instance.set_database(database_type='train_assistor_metadata')
        response = DatabaseOperator_instance.get_record(
            user_id=test_record[0], 
            train_id=test_record[1], 
        )
        assert response == expected_res