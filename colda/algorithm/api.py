from __future__ import annotations

from colda.utils.log import GetAlgorithmLog

from typing import Any
from typeguard import typechecked

class AlgorithmAPI:
    '''
    Some api for Algorithm part

    Attributes
    ----------
    None

    Methods
    -------
    get_log
    get_all_logs
    '''

    @classmethod
    def get_log(
        cls,
        user_id: str,
        task_id: str,
        log_category: str
    ) -> list[str]:
        '''
        Return unique log determined
        by user_id, task_id and log_category

        Parameters
        ----------
        user_id : str
        task_id : str
        log_category : str

        Returns
        -------
        list
        '''
        return GetAlgorithmLog.get_instance().get_log(
            user_id=user_id,
            task_id=task_id,
            log_category=log_category
        )
    
    @classmethod
    def get_all_logs(
        cls
    ) -> dict[str, Any]:
        '''
        Return all logs

        Parameters
        ----------
        None

        Returns
        -------
        dict[str, Any]
        '''
        return GetAlgorithmLog.get_instance().get_all_logs()
