from __future__ import annotations

from colda.workflow.abstract_workflow import AbstractTestMainWorkflow

from colda.workflow.utils import (
    obtain_notification_information
)

from colda.workflow.test_workflow.sponsor.api import (
    TestSponsorFindAssistor,
    TestSponsorMatchIdentifier,
    TestSponsorOutput
)

from colda.workflow.test_workflow.assistor.api import (
    TestAssistorRequest,
    TestAssistorMatchIdentifier
)

from colda.workflow.utils import CheckSponsor

from colda._typing import (
    Task_Mode,
    Model_Name,
    Metric_Name
)
from typing import Any

from typeguard import typechecked


#@typechecked
class TestMainWorkflow(AbstractTestMainWorkflow):
    '''
    Manage test workflow

    Methods
    -------
    get_instance
    find_test_assistor
    test_assistor_request
    test_match_identifier
    test_sponsor_match_identifier
    test_assistor_match_identifier
    test_output
    '''

    def __init__(self):
        pass

    @classmethod
    def get_class(cls) -> type[TestMainWorkflow]:
        ''' 
        Get current class.

        Returns
        -------
        type[TestMainWorkflow]
        '''
        return TestMainWorkflow
        
    @classmethod
    def find_test_assistor(
        cls, 
        train_id: str, 
        test_file_path: str, 
        test_id_column: str, 
        test_data_column: str, 
        test_target_column: str, 
        test_name: str=None, 
        test_description: str=None
    ) -> str:
        ''' 
        Start testing with all assistors of the previous train 
        task

        Parameters
        ----------
        train_id : str
        test_file_path : str
        test_id_column : str
        test_data_column : str 
        test_target_column : str 
        test_name : str=None
        test_description : str=None

        Returns
        -------
        Any
        '''
        return TestSponsorFindAssistor.find_test_assistor(
            train_id=train_id,
            test_file_path=test_file_path, 
            test_id_column=test_id_column,
            test_data_column=test_data_column, 
            test_target_column=test_target_column, 
            test_name=test_name,
            test_description=test_description
        )
       
    @classmethod
    def test_assistor_request(
        cls, test_id_dicts: dict[dict[str, str]]
    ) -> None:
        ''' 
        Request is fist stage of testing for assistor.
        In this stage, assistor would:
            1. Encrypt the identifiers
            2. Send the identifiers to server

        Parameters
        ----------
        test_id_dicts : dict[dict[str, str]]

        Returns
        -------
        None
        '''
        for test_id, test_id_dict in test_id_dicts.items():
            TestAssistorRequest.test_assistor_request(
                test_id=test_id,
                test_id_dict=test_id_dict
            )
        return

    @classmethod
    def test_match_identifier(
        cls, test_id_dicts: dict[dict[str, str]]
    ) -> None:
        ''' 
        Handle the unread_test_match_identifier. 
        Two situations needed to be considered: sponsor and assistor

        Parameters
        ----------
        test_id_dicts : dict[dict[str, str]]

        Returns
        -------
        None
        '''
        for test_id, test_id_dict in test_id_dicts.items():
            _, role, _, _ = obtain_notification_information(
                notification_dict=test_id_dict, 
                test_indicator='test'
            )

            if role == CheckSponsor.sponsor:
                cls.test_sponsor_match_identifier(
                    test_id=test_id,
                    test_id_dict=test_id_dict
                )
            elif role == CheckSponsor.assistor:
                cls.test_assistor_match_identifier(
                    test_id=test_id,
                    test_id_dict=test_id_dict
                )
        return

    @classmethod
    def test_sponsor_match_identifier(
        cls, test_id: str, test_id_dict: dict[str, str]
    ) -> None:
        ''' 
        Match_identifier is second stage of testing for sponsor.
        In this stage, sponsor would:
            1. Match the identifiers sent from all the assistors
            2. Test the trained models produced at each round of
               training stage

        Parameters
        ----------
        test_id : str
        test_id_dicts : dict[str, str]

        Returns
        -------
        None
        '''
        TestSponsorMatchIdentifier.test_sponsor_match_identifier(
            test_id=test_id,
            test_id_dict=test_id_dict
        )
        return

    @classmethod
    def test_assistor_match_identifier(
        cls, test_id: str, test_id_dict: dict[str, str]
    ) -> bool:
        ''' 
        Match_identifier is second stage of testing for assistor.
        In this stage, assistor would:
            1. Match the identifiers sent from the sponsor
            2. Test the trained models produced at each round of
               training stage using test data
            3. Send the test ouputs to sponsor

        Parameters
        ----------
        test_id : str
        test_id_dicts : dict[str, str]

        Returns
        -------
        None
        '''
        TestAssistorMatchIdentifier.test_assistor_match_identifier(
            test_id=test_id,
            test_id_dict=test_id_dict
        )
        return

    @classmethod
    def test_output(
        cls, test_id_dicts: dict[dict[str, str]]
    ) -> None:
        ''' 
        Output is third stage of testing for sponsor.
        In this stage, sponsor would:
            1. Get the test outputs sent from all the assistors
            2. Evaluate test results

        Parameters
        ----------
        test_id_dicts : dict[dict[str, str]]

        Returns
        -------
        None
        '''
        for test_id, test_id_dict in test_id_dicts.items():
            TestSponsorOutput.test_sponsor_output(
                test_id=test_id,
                test_id_dict=test_id_dict
            )
        return

