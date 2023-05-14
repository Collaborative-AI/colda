from __future__ import annotations

from abc import ABC, abstractmethod

from utils.log.algorithm_log import AlgorithmLog

from utils.log.workflow_log import WorkflowLog

from typeguard import typechecked

class AbstractLogFactory(ABC):
    """
    Abstract Factory
    """
    @classmethod
    @abstractmethod
    def get_log(cls):
        pass


#@typechecked
class GetAlgorithmLog(AbstractLogFactory):

    @classmethod
    def get_instance(cls) -> AlgorithmLog:
        '''
        AlgorithmLog factory

        Returns
        -------
        AlgorithmLog
        '''
        return AlgorithmLog.get_instance()


#@typechecked
class GetWorkflowLog(AbstractLogFactory):

    @classmethod
    def get_instance(cls) -> WorkflowLog:
        '''
        WorkflowLog factory

        Returns
        -------
        WorkflowLog
        '''
        return WorkflowLog.get_instance()