from __future__ import annotations

from utils.log.api import GetAlgorithmLog

from typing import Any
from typeguard import typechecked



def get_algo_log(
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
    # for key, val in GetAlgorithmLog.get_instance().items():
    #     print('key', key)
    #     print('val', val)
    #     print('\n')
    return GetAlgorithmLog.get_instance().get_log(
        user_id=user_id,
        task_id=task_id,
        log_category=log_category
    )


def get_all_algo_logs() -> dict[str, Any]:
    '''
    Return all logs

    Returns
    -------
    dict[str, Any]
    '''
    return GetAlgorithmLog.get_instance().get_all_logs()
