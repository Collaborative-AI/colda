from __future__ import annotations

from colda.workflow.base import BaseWorkflow

from colda.algorithm.strategy import TrainAlgorithm

from typing import (
    final,
    Any,
    Final
)

from typeguard import typechecked
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


