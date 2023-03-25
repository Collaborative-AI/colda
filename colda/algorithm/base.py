from __future__ import annotations

from utils.log.api import GetAlgorithmLog

from typing import (
    Final,
    final,
    Any
)

from typeguard import typechecked


class BaseAlgorithm:
    '''
    Base class for algorithm

    Methods
    -------
    _store_log
    '''

    __root: Final[str] = './algorithm_log'
    # __log = GetAlgorithmLog.get_instance()
    
    # print('BaseAlgorithm初始化algo log', id(__log))
    # TODO: implement methods
    @final
    def placeholder(self):
        pass

    @final
    @classmethod
    def _store_log(
        cls,
        user_id: str,
        task_id: str,
        msgs: list[str],
        log_category: str,
    ) -> list[dict[str, Any]]:
        '''
        Store msgs to the corresponding
        log

        Parameters
        ----------
        user_id : str
        task_id : str
        msgs : list[str]
        log_category : str

        Returns
        -------
        list
        '''
        print('algo log address', id(GetAlgorithmLog.get_instance()))
        GetAlgorithmLog.get_instance().store_log(
            user_id=user_id,
            task_id=task_id,
            msgs=msgs,
            log_category=log_category,
        )
        return None
