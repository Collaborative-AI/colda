from __future__ import annotations

from synspot.workflow.abstract_workflow import AbstractTestMainWorkflow

from synspot.workflow.utils import (
    obtain_notification_information
)

from synspot.workflow.test_workflow.sponsor import (
    TestSponsorFindAssistor,
    TestSponsorMatchIdentifier,
    TestSponsorOutput
)

from synspot.workflow.test_workflow.assistor import (
    TestAssistorRequest,
    TestAssistorMatchIdentifier
)

from synspot.workflow.utils import CheckSponsor

from typing import Any


class TestMainWorkflow(AbstractTestMainWorkflow):
    __TestMainWorkflow_instance = None

    def __init__(self):
        pass

    @classmethod
    def get_instance(cls) -> type[TestMainWorkflow]:
        if cls.__TestMainWorkflow_instance == None:
            cls.__TestMainWorkflow_instance = TestMainWorkflow()

        return cls.__TestMainWorkflow_instance

    def find_test_assistor(
        self, 
        train_id: str, 
        test_file_path: str, 
        test_id_column: str, 
        test_data_column: str, 
        test_target_column: str, 
        test_name: str=None, 
        test_description: str=None
    ) -> Any:

        """
        start testing with all assistors of the task

        :param task_id: String. The task that the user wanted to test
        :param task_name: String. The name of the task that the user wanted to test
        :param task_description: String. The description of the task that the user wanted to test
        :param task_mode: String. Classification or Regression
        :param model_name: String. Specific model, such as LinearRegression, DecisionTree.
        :param metric_name: String. Metric to measure the result, such as MAD, RMSE, R2.
        :param test_file_path: String. Input path address of testing data path
        :param test_id_column: String. ID column of Input File
        :param test_data_column: String. Data column of Input File
        :param test_target_column: String. Target column of Input File
        :param test_name: None or String. The name of current test
        :param test_description: None or String. The description of current test

        :returns: None

        :exception OSError: Placeholder.
        """

        return TestSponsorFindAssistor.find_test_assistor(
            train_id=train_id,
            test_file_path=test_file_path, 
            test_id_column=test_id_column,
            test_data_column=test_data_column, 
            test_target_column=test_target_column, 
            test_name=test_name,
            test_description=test_description
        )
       

    def test_assistor_request(
        self, test_id_dicts: dict[dict[str, str]]
    ) -> bool:

        """
        Handle the unread test request for three default mode: ["passive", "active", "auto"]

        :param test_id_dict: Dictionary.

        :returns: None

        :exception OSError: Placeholder.
        """

        for test_id, test_id_dict in test_id_dicts.items():
            TestAssistorRequest.test_assistor_request(
                test_id=test_id,
                test_id_dict=test_id_dict
            )
        
        return True


    def test_match_identifier(
        self, test_id_dicts: dict[dict[str, str]]
    ) -> bool:
        """
        Handle the unread_test_match_identifier. Two situations needed to be considered: sponsor and assistor

        :param test_id_dict: Dictionary.

        :returns: None

        :exception OSError: Placeholder.
        """

        for test_id, test_id_dict in test_id_dicts.items():
            _, role, _, _ = obtain_notification_information(
                notification_dict=test_id_dict, 
                test_indicator='test'
            )

            if role == CheckSponsor.sponsor:
                self.test_sponsor_match_identifier(
                    test_id=test_id,
                    test_id_dict=test_id_dict
                )
            elif role == CheckSponsor.assistor:
                self.test_assistor_match_identifier(
                    test_id=test_id,
                    test_id_dict=test_id_dict
                )

            return True

    def test_sponsor_match_identifier(
        self, test_id: str, test_id_dict: dict[str, str]
    ) -> bool:

        """
        Handle the unread_test_match_identifier of sponsor.

        :param task_id: String.
        :param test_id: String.
        :param cur_max_round: Integer.

        :returns: None

        :exception OSError: Placeholder.
        """

        return TestSponsorMatchIdentifier.test_sponsor_match_identifier(
            test_id=test_id,
            test_id_dict=test_id_dict
        )

    def test_assistor_match_identifier(
        self, test_id: str, test_id_dict: dict[str, str]
    ) -> bool:

        """
        Handle the unread_test_match_identifier of assistor.

        :param task_id: String.
        :param test_id: String.
        :param cur_max_round: Integer.

        :returns: None

        :exception OSError: Placeholder.
        """

        return TestAssistorMatchIdentifier.test_assistor_match_identifier(
            test_id=test_id,
            test_id_dict=test_id_dict
        )


    def test_output(
        self, test_id_dicts: dict[dict[str, str]]
    ) -> bool:

        """
        Handle the unread_test_output.

        :param test_id_dict: Dictionary.

        :returns: None

        :exception OSError: Placeholder.
        """

        for test_id, test_id_dict in test_id_dicts.items():
            TestSponsorOutput.test_sponsor_output(
                test_id=test_id,
                test_id_dict=test_id_dict
            )
        
        return True

