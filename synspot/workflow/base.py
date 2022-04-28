from synspot.network import Network
from synspot.personalinformation import PersonalInformation

from synspot.algorithm.strategy import (
    TrainAlgorithm,
    TestAlgorithm
)

from synspot.database import (
    GetDefaultMetadataDatabase,
    GetTrainSponsorMetadataDatabase,
    GetTrainAssistorMetadataDatabase,
    GetTrainAlgorithmDatabase,
)

from synspot.database import (
    GetDefaultMetadataDatabase,
    GetTrainSponsorMetadataDatabase,
    GetTrainAssistorMetadataDatabase,
    GetTrainAlgorithmDatabase,
    GetTestSponsorMetadataDatabase,
    GetTestAssistorMetadataDatabase,
    GetTestAlgorithmDatabase
)

from typing import (
    final,
    Tuple
)


class BaseWorkflow:
    __Network_instance = Network.get_Network_instance()
    __PersonalInformation_instance = PersonalInformation.get_PersonalInformation_instance()

    __DefaultMetadataDatabase_instance = GetDefaultMetadataDatabase.get_database()
    __TrainSponsorMetadataDatabase_instance = GetTrainSponsorMetadataDatabase.get_database()
    __TrainAssistorMetadataDatabase_instance = GetTrainAssistorMetadataDatabase.get_database()
    __TrainAlgorithmDatabase_instance = GetTrainAlgorithmDatabase.get_database()
    __TestSponsorMetadataDatabase_instance = GetTestSponsorMetadataDatabase.get_database()
    __TestAssistorMetadataDatabase_instance = GetTestAssistorMetadataDatabase.get_database()
    __TestAlgorithmDatabase_instance = GetTestAlgorithmDatabase.get_database()

    __TrainAlgorithm_instance = TrainAlgorithm.get_algorithm_instance()
    __TestAlgorithm_instance = TestAlgorithm.get_algorithm_instance()

    @final
    @classmethod
    def _get_important_information(cls) -> Tuple[str, str, str]:
        """
        Obtain the information we need: user_id, root, token, task_id

        :param get_train_id: Boolean. Indicate if we need to get the new train id

        :returns: A tuple of ``(user_id, root, token, task_id)``

        :exception OSError: Placeholder.
        """
        user_id = cls.__PersonalInformation_instance.user_id
        # assert user_id is not None
        root = cls.__PersonalInformation_instance.root
        # assert root is not None
        token = cls.__Network_instance.token
        # assert token is not None
        return user_id, root, token
    
    @final
    @classmethod
    def _get_base_url(cls) -> str:
        base_url = cls.__Network_instance.base_url
        return base_url
    
    @final
    @classmethod
    def _process_url(
        cls,
        prefix: str,
        url: str,
        suffix: str = None
    ) -> str:
        return cls.__Network_instance.process_url(prefix=prefix, url=url)



