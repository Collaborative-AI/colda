from __future__ import annotations

from colda.workflow.base import BaseWorkflow

from colda.algorithm.strategy.api import TrainAlgorithm

from typing import (
    final,
    Any,
    Final
)

from typeguard import typechecked


#@typechecked
class TrainBaseWorkflow(BaseWorkflow):
    '''
    1. Wrap the algorithm part
    2. Implement some common methods

    Methods
    -------
    _calculate_residual
    _calculate_result
    _train_cooperative_model
    _train_local_model
    '''

    __TrainAlgorithm_instance = TrainAlgorithm.get_instance()
    

    @final
    @classmethod
    def _calculate_residual(
        cls, **kwargs
    ) -> None:
        ''' 
        Calculate residual.
        Residual is used as training target for assistors

        Parameters
        ----------
        **kwargs : Any

        Returns
        -------
        None
        '''
        return cls.__TrainAlgorithm_instance.make_residual(**kwargs)

    @final
    @classmethod
    def _calculate_result(
        cls, **kwargs
    ) -> None:
        ''' 
        Calculate result
        Combine the sponsor's trained model and assistors' trained 
        models to a better sponsor model

        Parameters
        ----------
        **kwargs : Any

        Returns
        -------
        None
        '''
        return cls.__TrainAlgorithm_instance.make_result(**kwargs)

    @final
    @classmethod
    def _train_cooperative_model(
        cls, **kwargs
    ) -> None:
        ''' 
        Train the model

        Parameters
        ----------
        **kwargs : Any

        Returns
        -------
        None
        '''
        return cls.__TrainAlgorithm_instance.make_train(**kwargs)

    @final
    @classmethod
    def _train_local_model(
        cls, **kwargs
    ) -> None:
        ''' 
        Sponsor train model locally(only use its dataset) 

        Parameters
        ----------
        **kwargs : Any

        Returns
        -------
        None
        '''
        return cls.__TrainAlgorithm_instance.make_train_local(**kwargs)


