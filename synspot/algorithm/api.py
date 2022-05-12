from __future__ import annotations

from synspot.utils.log import GetAlgorithmLog

from typing import Any


class AlgorithmAPI:

    @classmethod
    def get_log(
        cls,
        user_id: str,
        task_id: str,
        log_category: str
    ) -> list[str]:

        return GetAlgorithmLog.get_log().get_log(
            user_id=user_id,
            task_id=task_id,
            log_category=log_category
        )
    
    @classmethod
    def get_all_logs(
        cls
    ) -> dict[str, Any]:
        return GetAlgorithmLog.get_log().get_all_logs()
