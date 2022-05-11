from __future__ import annotations

from synspot.utils.log import GetAlgorithmLog

from typing import (
    Final,
    final
)

class BaseAlgorithm:
    """
    Base class for Algorithm
    """
    __root: Final[str] = './algorithm_log'
    __log = GetAlgorithmLog.get_log()

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
    ) -> None:

        cls.__log.store_log(
            user_id=user_id,
            task_id=task_id,
            msgs=msgs,
            log_category=log_category,
        )
        return None
