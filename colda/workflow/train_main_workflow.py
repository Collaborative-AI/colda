from __future__ import annotations

from colda.workflow.abstract_workflow import AbstractTrainMainWorkflow

from colda.workflow.utils import (
    obtain_notification_information
)

from colda.workflow.train_workflow.sponsor.api import (
    TrainSponsorFindAssistor,
    TrainSponsorMatchIdentifier,
    TrainSponsorSituation,
    TrainSponsorOutput
)

from colda.workflow.train_workflow.assistor.api import (
    TrainAssistorRequest,
    TrainAssistorMatchIdentifier,
    TrainAssistorSituation
)

from colda.workflow.utils import CheckSponsor

from colda._typing import (
    Task_Mode,
    Model_Name,
    Metric_Name
)
from typeguard import typechecked


#@typechecked
class TrainMainWorkflow(AbstractTrainMainWorkflow):
    '''
    Manage train workflow

    Attributes
    ----------
    None

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
    def get_class(cls) -> type[TrainMainWorkflow]:
        ''' 
        Get current class.

        Parameters
        ----------
        None

        Returns
        -------
        type[TrainMainWorkflow]
        '''
        return TrainMainWorkflow  

    @classmethod
    def find_assistor(
        cls, 
        maxRound: int, 
        assistors: list, 
        task_mode: Task_Mode, 
        model_name: Model_Name, 
        metric_name: Metric_Name, 
        train_file_path: str, 
        train_id_column: str, 
        train_data_column: str, 
        train_target_column: str, 
        task_name: str=None, 
        task_description: str=None
    ) -> str:
        ''' 
        Start training

        Parameters
        ----------
        maxRound : int 
        assistors : list 
        task_mode : Task_Mode
        model_name : Model_Name
        metric_name : Metric_Name
        train_file_path : str
        train_id_column : str
        train_data_column : str 
        train_target_column : str 
        task_name : str=None 
        task_description : str=None

        Returns
        -------
        Any
        '''
        return TrainSponsorFindAssistor.find_assistor(
            maxRound=maxRound,
            assistors=assistors,
            train_file_path=train_file_path,
            train_id_column=train_id_column,
            train_data_column=train_data_column,
            train_target_column=train_target_column,
            task_mode=task_mode,
            model_name=model_name,
            metric_name=metric_name,
            task_name=task_name,
            task_description=task_description
        )
        
    @classmethod
    def train_assistor_request(
        cls, train_id_dicts: dict[dict[str, str]]
    ) -> None:
        ''' 
        Request is fist stage of training for assistor.
        In this stage, assistor would:
            1. Encrypt the identifiers
            2. Send the identifiers to server

        Parameters
        ----------
        train_id_dicts : dict[dict[str, str]]

        Returns
        -------
        None
        '''
        for train_id, train_id_dict in train_id_dicts.items():
            TrainAssistorRequest.train_assistor_request(
                train_id=train_id, 
                train_id_dict=train_id_dict
            )
        return

    @classmethod
    def train_match_identifier(
        cls, train_id_dicts: dict[dict[str, str]]
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
        for train_id, train_id_dict in train_id_dicts.items():
            _, role, _ = obtain_notification_information(
                notification_dict=train_id_dict
            )            

            if role == CheckSponsor.sponsor:
                cls.train_sponsor_match_identifier(
                    train_id=train_id, 
                    train_id_dict=train_id_dict
                )
            elif role == CheckSponsor.assistor:
                cls.train_assistor_match_identifier(
                    train_id=train_id, 
                    train_id_dict=train_id_dict
                )
        return

    @classmethod
    def train_sponsor_match_identifier(
        cls, train_id: str, train_id_dict: dict[str, str]
    ) -> None:
        ''' 
        Match_identifier is second stage of training for sponsor.
        In this stage, sponsor would:
            1. Match the identifiers sent from all the assistors
            2. Calculate residual(training target)
            3. Send residual to all assistors

        Parameters
        ----------
        train_id : str
        train_id_dicts : dict

        Returns
        -------
        None
        '''
        TrainSponsorMatchIdentifier.train_sponsor_match_identifier(
            train_id=train_id, 
            train_id_dict=train_id_dict
        )
        return
    
    @classmethod
    def train_assistor_match_identifier(
        cls, train_id: str, train_id_dict: dict[str, str]
    ) -> None:
        ''' 
        Match_identifier is second stage of training for assistor.
        In this stage, assistor would:
            1. Match the identifiers sent from all the assistors

        Parameters
        ----------
        train_id : str
        train_id_dict : dict

        Returns
        -------
        None
        '''
        TrainAssistorMatchIdentifier.train_assistor_match_identifier(
            train_id=train_id, 
            train_id_dict=train_id_dict
        )
        return

    @classmethod
    def train_situation(
        cls, train_id_dicts: dict[dict[str, str]]
    ) -> None:
        ''' 
        Handle the unread_train_situation. 
        Two situations needed to be considered: sponsor and assistor

        Parameters
        ----------
        train_id_dicts : dict[dict[str, str]]

        Returns
        -------
        None
        '''
        for train_id, train_id_dict in train_id_dicts.items():
            _, role, _ = obtain_notification_information(
                notification_dict=train_id_dict
            )

            if role == CheckSponsor.sponsor:
                cls.train_sponsor_situation(
                    train_id=train_id, 
                    train_id_dict=train_id_dict,
                )
            elif role == CheckSponsor.assistor:
                cls.train_assistor_situation(
                    train_id=train_id, 
                    train_id_dict=train_id_dict
                )
        return True

    @classmethod
    def train_sponsor_situation(
        cls, train_id: str, train_id_dict: dict
    ) -> None:
        ''' 
        situation is third stage of training for sponsor.
        In this stage, sponsor would:
            1. Train model

        Parameters
        ----------
        train_id : str
        train_id_dicts : dict

        Returns
        -------
        None
        '''
        TrainSponsorSituation.train_sponsor_situation(train_id, train_id_dict)
        return

    @classmethod
    def train_assistor_situation(
        cls, train_id: str, train_id_dict: dict
    ) -> None:
        ''' 
        situation is third stage of training for assistor.
        In this stage, assistor would:
            1. Get the residual(training target) sent from the 
               sponsor
            2. Train model
            3. Send trained model output to sponsor

        Parameters
        ----------
        train_id : str
        train_id_dicts : dict

        Returns
        -------
        None
        '''
        TrainAssistorSituation.train_assistor_situation(
            train_id=train_id, 
            train_id_dict=train_id_dict
        )
        return

    @classmethod
    def train_output(
        cls, train_id_dicts: dict[dict[str, str]]
    ) -> None:
        ''' 
        Output is fourth stage of testing for sponsor.
        In this stage, sponsor would:
            1. Get the train outputs sent from all the assistors
            2. Evaluate train results

        Parameters
        ----------
        train_id_dicts : dict[dict[str, str]]

        Returns
        -------
        None
        '''
        for train_id, train_id_dict in train_id_dicts.items():
            TrainSponsorOutput.train_sponsor_output(
                train_id=train_id,
                train_id_dict=train_id_dict
            )
        return

    @classmethod
    def stop_train(cls, unread_train_stop_notification: dict):
        ''' 
        Stop Train and delete related files.
        Implement later
        ''' 
        return






