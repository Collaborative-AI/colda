from __future__ import annotations

from colda.workflow.base import BaseWorkflow

from colda.algorithm.strategy import TestAlgorithm

from typing import (
    final
)

from typeguard import typechecked


#@typechecked
class TestBaseWorkflow(BaseWorkflow):
    '''
    Base class for test workflow

    Attributes
    ----------
    None

    Methods
    -------
    _evaluate_results
    _test_cooperative_model
    _test_local_model
    '''

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

