from __future__ import annotations

from abc import ABC, abstractmethod

from colda.utils.log.algorithm_log import AlgorithmLog

from colda.utils.log.workflow_log import WorkflowLog

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
        
        Parameters
        ----------
        None

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
        
        Parameters
        ----------
        None

        Returns
        -------
        WorkflowLog
        '''
        return WorkflowLog.get_instance()