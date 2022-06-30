from __future__ import annotations
from asyncio import Task

import copy
import numpy as np

from colda.algorithm.base import BaseAlgorithm

from colda.algorithm.utils import makedir_exist_ok, log, parse_idx

from colda.algorithm.metric.metrics import Metric

from colda._typing import Task_Mode

from typing import (
    Any,
    Union,
    overload,
)

from colda._typing import (
    Task_Mode,
    Model_Name,
    Metric_Name
)

from typeguard import typechecked


class MakeResidual(BaseAlgorithm):
    '''
    Calculate Residual.
    Residual is used as target for the 
    following training step.

    Attributes
    ----------
    None

    Methods
    -------
    make_residual
    '''

    @overload
    @classmethod
    def make_residual(
        cls,  
        round: str, 
        dataset_path: str, 
        target_idx: str, 
        skip_header: str, 
        task_mode: Task_Mode, 
        metric_name: Metric_Name,
        sponsor_matched_identifers: dict[str, Any],
        last_round_result: None
    ) -> np.ndarray:
        ...

    @overload
    @classmethod
    def make_residual(
        cls, 
        round: str, 
        dataset_path: str, 
        target_idx: str, 
        skip_header: str, 
        task_mode: Task_Mode, 
        metric_name: Metric_Name,
        sponsor_matched_identifers: dict[str, Any],
        last_round_result: Any
    ) -> np.ndarray:
        ...
    
    @classmethod
    def make_residual(
        cls, 
        round: str, 
        dataset_path: str, 
        target_idx: str, 
        skip_header: str, 
        task_mode: Task_Mode, 
        metric_name: Metric_Name,
        sponsor_matched_identifers: dict[str, Any],
        last_round_result: Union[Any, None]=None
    ) -> tuple[np.ndarray[Any], dict[str, Any]]:
        '''
        Calculate Residual. 

        Parameters
        ----------
        round : str
        dataset_path : str
        target_idx : str
        skip_header : str
        task_mode : str
        metric_name : str
        sponsor_matched_identifers : dict[str, Any]
        last_round_result : Union[Any, None]=None

        Returns
        -------
        tuple[np.ndarray[Any], dict[str, Any]]
        '''
        dataset = np.genfromtxt(dataset_path, delimiter=',', skip_header=skip_header)
        target_idx = parse_idx(target_idx)
        target = dataset[:, target_idx]
        
        init_round_result = None
        if round == 1:
            init_round_result = cls.make_init(task_mode, target)

            temp_init_round_result = copy.deepcopy(init_round_result)
            temp_init_round_result = temp_init_round_result.repeat(target.shape[0], axis=0)

            residual = cls.compute_residual(task_mode, temp_init_round_result, target)
            metric = Metric(task_mode, metric_name)
            eval = metric.eval(temp_init_round_result, target)
            # log(msg, cls.__root, self_id, train_id)
        else:
            last_round_result = last_round_result.reshape(last_round_result.shape[0], -1)
            residual = cls.compute_residual(task_mode, last_round_result, target)
    
        residual_dict = {}
        residual_dict['sponsor'] = copy.deepcopy(residual)
        for assistor_random_id, sponsor_matched_identifer in sponsor_matched_identifers.items():
            self_from_idx_i = sponsor_matched_identifer
            residual_dict[assistor_random_id] = copy.deepcopy(residual[self_from_idx_i,])           
        return init_round_result, residual_dict

    @classmethod
    def make_init(
        cls, task_mode: Task_Mode, target: list[str]
    ) -> np.ndarray:
        '''
        Create initial residual at round 1 

        Parameters
        ----------
        task_mode : str
        target : list[str]

        Returns
        -------
        np.ndarray
        '''
        if task_mode == 'regression':
            init = np.mean(target, axis=0, keepdims=True)
        elif task_mode == 'classification':
            target = target.astype(np.int64).reshape(-1)
            one_hot_target = np.eye(np.max(target) + 1)[target]
            init = np.log(np.mean(one_hot_target, axis=0, keepdims=True))
        else:
            raise ValueError('Not valid task mode')
        return init

    @classmethod
    def compute_residual(
        cls,
        task_mode: Task_Mode, 
        output: np.ndarray, 
        target: np.ndarray,
    ) -> np.ndarray:
        '''
        Compute residual based on
        task mode, output and target

        Parameters
        ----------
        task_mode : str
        target : list[str]

        Returns
        -------
        np.ndarray
        '''
        if task_mode == 'regression':
            residual = - 2 * (output - target)
        elif task_mode == 'classification':
            target = target.astype(np.int64).reshape(-1)
            one_hot_target = np.eye(np.max(target) + 1)[target]
            exp_output = np.exp(output - np.max(output, axis=-1, keepdims=True))
            softmax_output = exp_output / np.sum(exp_output, axis=-1, keepdims=True)
            residual = -(softmax_output - one_hot_target)
        else:
            raise ValueError('Not valid task mode')
        return residual
