from __future__ import annotations

import numpy as np
import os

from pyrsistent import b
from synspot.algorithm.base import BaseAlgorithm
from synspot.algorithm.utils import makedir_exist_ok, log, parse_idx
from synspot.algorithm.metric.metrics import Metric

from typing import (
    Any,
    Union,
    overload,
)


class MakeResidual(BaseAlgorithm):
    '''
    Calculate Residual.
    Residual is used as target for the following training step.
    '''
    
    @overload
    @classmethod
    def make_residual(
        cls, 
        self_id: str, 
        task_id: str, 
        round: str, 
        dataset_path: str, 
        target_idx: str, 
        skip_header: str, 
        task_mode: str, 
        metric_name: str,
        last_round_result: None
    ) -> np.ndarray:
        ...

    @overload
    @classmethod
    def make_residual(
        cls, 
        self_id: str, 
        task_id: str, 
        round: str, 
        dataset_path: str, 
        target_idx: str, 
        skip_header: str, 
        task_mode: str, 
        metric_name: str,
        last_round_result: Any
    ) -> np.ndarray:
        ...
    
    @classmethod
    def make_residual(
        cls, 
        self_id: str, 
        train_id: str, 
        round: str, 
        dataset_path: str, 
        target_idx: str, 
        skip_header: str, 
        task_mode: str, 
        metric_name: str,
        last_round_result: Union[Any, None] = None
    ) -> tuple[np.ndarray[Any], np.ndarray[Any]]:

        dataset = np.genfromtxt(dataset_path, delimiter=',', skip_header=skip_header)
        target_idx = parse_idx(target_idx)
        target = dataset[:, target_idx]
        
        init_round_result = None
        if round == 1:
            init_round_result = cls.make_init(task_mode, target)
            # round_path = os.path.join(root, self_id, 'task', task_id, 'train', 'round', str(round - 1))
            # makedir_exist_ok(round_path)
            # np.savetxt(os.path.join(round_path, 'result.csv'), output, delimiter=",")
            init_round_result = init_round_result.repeat(target.shape[0], axis=0)

            residual = cls.compute_residual(task_mode, init_round_result, target)
            metric = Metric(task_mode, metric_name)
            eval = metric.eval(init_round_result, target)
            # log(msg, cls.__root, self_id, train_id)
        else:
            # round_path = os.path.join(root, self_id, 'task', task_id, 'train', 'round', str(round - 1))
            '''
            需要传入参数
            '''
            # result = np.genfromtxt(os.path.join(round_path, 'result.csv'), delimiter=',')
            last_round_result = last_round_result.reshape(last_round_result.shape[0], -1)
            residual = cls.compute_residual(task_mode, last_round_result, target)
        # residual_path = os.path.join(root, self_id, 'task', task_id, 'train', 'round', str(round), 'residual')
        # makedir_exist_ok(residual_path)
        # np.savetxt(os.path.join(residual_path, '{}.csv'.format(self_id)), residual, delimiter=",")
        # matched_idx_path = os.path.join(root, self_id, 'task', task_id, 'train', 'matched_idx')
        # self_from_idx_files = os.listdir(matched_idx_path)
        # assistor_residual_path = []
        # for i in range(len(self_from_idx_files)):
        #     self_from_idx_i = np.genfromtxt(os.path.join(matched_idx_path, str(self_from_idx_files[i])),
        #                                     delimiter=',').astype(np.int64)
        #     assistor_residual_path_i = os.path.join(residual_path, str(self_from_idx_files[i]))
        #     # np.savetxt(assistor_residual_path_i, residual[self_from_idx_i,], delimiter=",")
        #     assistor_residual_path.append(assistor_residual_path_i)
        # assistor_residual_path = '?'.join(assistor_residual_path)
        # return '200?make_residual?{}'.format(assistor_residual_path)             
        return init_round_result, residual

    @classmethod
    def make_init(
        cls, task_mode: str, target: list[str]
    ) -> np.ndarray:

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
        task_mode: str, 
        output: np.ndarray, 
        target: np.ndarray,
    ) -> np.ndarray:

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
