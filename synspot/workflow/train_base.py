from __future__ import annotations

from synspot.workflow.base import BaseWorkflow

from synspot.algorithm.strategy import TrainAlgorithm

from typing import (
    final,
    Any
)


class TrainBaseWorkflow(BaseWorkflow):    
    __TrainAlgorithm_instance = TrainAlgorithm.get_instance()

    @final
    @classmethod
    def _calculate_residual(
        cls, **kwargs
    ) -> None:
        return cls.__TrainAlgorithm_instance.make_residual(**kwargs)

    @final
    @classmethod
    def _calculate_result(
        cls, **kwargs
    ) -> None:
        return cls.__TrainAlgorithm_instance.make_result(**kwargs)

    @final
    @classmethod
    def _train_cooperative_model(
        cls, **kwargs
    ) -> None:
        return cls.__TrainAlgorithm_instance.make_train(**kwargs)

    @final
    @classmethod
    def _train_local_model(
        cls, **kwargs
    ) -> None:
        return cls.__TrainAlgorithm_instance.make_train_local(**kwargs)


