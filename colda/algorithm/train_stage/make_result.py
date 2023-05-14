from __future__ import annotations

import numpy as np
from scipy.optimize import minimize
import os
import copy
from algorithm.base import BaseAlgorithm
from algorithm.utils import log, parse_idx
from algorithm.metric.metrics import Metric

from _typing import (
    Task_Mode,
    Model_Name,
    Metric_Name
)

from typeguard import typechecked


class MakeResult(BaseAlgorithm):
    '''
    Combine the sponsor's trained model and assistors' trained 
    models to a better sponsor model

    Methods
    -------
    make_result
    '''

    @classmethod
    def make_result(
        cls, 
        user_id: str,
        train_id: str,
        rounds, 
        dataset_path, 
        target_idx, 
        skip_header, 
        task_mode: Task_Mode, 
        metric_name: Metric_Name,
        sponsor_trained_cooperative_model_output,
        assistor_trained_cooperative_model_outputs,
        sponsor_matched_identifers,
        last_round_result,
    ) -> None:

        dataset = np.genfromtxt(dataset_path, delimiter=',', skip_header=skip_header)
        target_idx = parse_idx(target_idx)
        target = dataset[:, target_idx]

        cooperative_model_output = copy.deepcopy(sponsor_trained_cooperative_model_output)
        cooperative_model_output = cooperative_model_output.reshape(
            cooperative_model_output.shape[0], -1
        )
        print('------------daozhelile')
        super()._store_log(
            user_id=user_id,
            task_id=train_id,
            msgs=sponsor_trained_cooperative_model_output[:4],
            log_category=['sponsor_trained_cooperative_model_output', f'rounds_{rounds}'],
        )
        
        count = np.ones((cooperative_model_output.shape[0], 1))
        
        for assistor_random_id, assistor_trained_cooperative_model_output in assistor_trained_cooperative_model_outputs.items():
            # output_i = np.genfromtxt(os.path.join(output_path, output_files[i]), delimiter=',')
            assistor_trained_cooperative_model_output = assistor_trained_cooperative_model_output.reshape(
                assistor_trained_cooperative_model_output.shape[0], -1
            )
            # print('assistor_trained_cooperative_model_output', assistor_trained_cooperative_model_output)
            super()._store_log(
                user_id=user_id,
                task_id=train_id,
                msgs=assistor_trained_cooperative_model_output[:4],
                log_category=['assistor_trained_cooperative_model_output', f'rounds_{rounds}'],
            )
            # self_from_idx_i = np.genfromtxt(os.path.join(matched_idx_path, '{}.csv'.format(from_id_i)),
            #                                 delimiter=',').astype(np.int64)
            self_from_idx_id = sponsor_matched_identifers[assistor_random_id]
            cooperative_model_output[self_from_idx_id,] = cooperative_model_output[self_from_idx_id,] + assistor_trained_cooperative_model_output
            count[self_from_idx_id,] = count[self_from_idx_id,] + 1
        
        cooperative_model_output = cooperative_model_output / count

        if round == 1:
            if len(last_round_result.shape) == 0:
                last_round_result = last_round_result.reshape(-1)
            if len(last_round_result.shape) == 1:
                last_round_result = last_round_result.reshape(1, -1)
        last_round_result = last_round_result.reshape(last_round_result.shape[0], -1)
        # print('resultyy', last_round_result)
        alpha = np.ones(1)
        func_ = minimize(cls.result_func, alpha, (task_mode, last_round_result, cooperative_model_output, target))
        alpha = func_.x
       
        cur_round_result = last_round_result + alpha * cooperative_model_output

        super()._store_log(
            user_id=user_id,
            task_id=train_id,
            msgs=alpha,
            log_category=['make_result_alpha', f'rounds_{rounds}'],
        )
        super()._store_log(
            user_id=user_id,
            task_id=train_id,
            msgs=cooperative_model_output[:4],
            log_category=['make_result_cooperative_model_output', f'rounds_{rounds}'],
        )
        super()._store_log(
            user_id=user_id,
            task_id=train_id,
            msgs=cur_round_result[:4],
            log_category=['make_result', f'rounds_{rounds}'],
        )
        # np.savetxt(os.path.join(round_path, str(round), 'result.csv'), result, delimiter=",")
        metric = Metric(task_mode, metric_name)
        eval = metric.eval(copy.deepcopy(cur_round_result), target)
        msg = 'Train Round: {}, {}, Alpha: {}'.format(round, eval, alpha.item())
        # log(msg, root, self_id, task_id)
        return alpha, cur_round_result

    @classmethod
    def result_func(
        cls,
        alpha, 
        task_mode, 
        history, 
        output, 
        target
    ) -> None:
        output = history + alpha * output
        if task_mode == 'regression':
            loss = ((target - output) ** 2).mean()
        elif task_mode == 'classification':
            exp_output = np.exp(output - np.max(output, axis=-1, keepdims=True))
            softmax_output = exp_output / np.sum(exp_output, axis=-1, keepdims=True)
            nll = -np.log(softmax_output[range(target.shape[0]), target.astype(np.int64).reshape(-1)])
            loss = np.mean(nll)
        else:
            raise ValueError('Not valid task mode')
        return loss
