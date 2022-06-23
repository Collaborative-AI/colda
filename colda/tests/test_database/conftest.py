import pytest

# from colda.database.database_factory import (
#     GetDefaultMetadataDatabase,
#     GetTrainSponsorMetadataDatabase,
#     GetTrainAssistorMetadataDatabase,
#     GetTrainAlgorithmDatabase,
#     GetTestSponsorMetadataDatabase,
#     GetTestAssistorMetadataDatabase,
#     GetTestAlgorithmDatabase
# )

from colda.database.strategy import DatabaseOperator

@pytest.fixture
def DatabaseOperator_instance():
    instance = DatabaseOperator.get_instance()
    return instance

# @pytest.fixture
# def DefaultMetadataDatabase_instance():
#     instance = GetDefaultMetadataDatabase.get_database()
#     return instance

# @pytest.fixture
# def TrainSponsorMetadataDatabase_instance():
#     instance = GetTrainSponsorMetadataDatabase.get_database()
#     return instance

# @pytest.fixture
# def TrainAssistorMetadataDatabase_instance():
#     instance = GetTrainAssistorMetadataDatabase.get_database()
#     return instance

# @pytest.fixture
# def TrainAlgorithmDatabase_instance():
#     instance = GetTrainAlgorithmDatabase.get_database()
#     return instance

# @pytest.fixture
# def TestSponsorMetadataDatabase_instance():
#     instance = GetTestSponsorMetadataDatabase.get_database()
#     return instance

# @pytest.fixture
# def TestAssistorMetadataDatabase_instance():
#     instance = GetTestAssistorMetadataDatabase.get_database()
#     return instance

# @pytest.fixture
# def TestAlgorithmDatabase_instance():
#     instance = GetTestAlgorithmDatabase.get_database()
#     return instance