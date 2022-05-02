from __future__ import annotations

from abc import ABC, abstractmethod

from synspot.utils.log.algorithm_log import AlgorithmLog

from synspot.utils.log.workflow_log import WorkflowLog


class AbstractLogFactory(ABC):
    """
    Abstract Factory
    """
    @classmethod
    @abstractmethod
    def get_log(cls):
        pass


class GetAlgorithmLog(AbstractLogFactory):
    @classmethod
    def get_log(cls):
        return AlgorithmLog.get_instance()


class GetWorkflowLog(AbstractLogFactory):
    @classmethod
    def get_log(cls):
        return WorkflowLog.get_instance()