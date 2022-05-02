from __future__ import annotations

from synspot.workflow.base import BaseWorkflow

from synspot.algorithm.strategy import TestAlgorithm

from typing import (
    final
)


class TestBaseWorkflow(BaseWorkflow):
    __TestAlgorithm_instance = TestAlgorithm.get_instance()

    @final
    @classmethod
    def _evaluate_results(
        cls, **kwargs
    ) -> None:
        return cls.__TestAlgorithm_instance.make_eval(**kwargs)

    @final
    @classmethod
    def _test_cooperative_model(
        cls, **kwargs
    ) -> None:
        return cls.__TestAlgorithm_instance.make_test(**kwargs)

    @final
    @classmethod
    def _test_local_model(
        cls, **kwargs
    ) -> None:
        return cls.__TestAlgorithm_instance.make_test_local(**kwargs)

