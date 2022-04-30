from __future__ import annotations

from synspot.utils.log.base import BaseLog

from synspot.utils.log.abstract_log import AbstractLog


class WorkflowLog(BaseLog, AbstractLog):
    __WorkflowLog_instance = None

    def __init__(self):
        pass

    @classmethod
    def get_WorkflowLog_instance(cls) -> type[WorkflowLog]:
        if cls.__WorkflowLog_instance == None:
            cls.__WorkflowLog_instance = WorkflowLog()

        return cls.__WorkflowLog_instance

    def store_log(self, *args):
        pass

    def get_log(self, *args):
        pass
    