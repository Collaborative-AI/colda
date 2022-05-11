from __future__ import annotations

import numpy as np
from scipy.optimize import minimize
import os
from synspot.algorithm.base import BaseAlgorithm
from synspot.algorithm.utils import log, parse_idx
from synspot.algorithm.metric.metrics import Metric


class MakeResult(BaseAlgorithm):

    '''
    Combine the sponsor's trained model and assistors' trained models to a better sponsor model
    '''

    @classmethod
    def make_result(
        cls, 
        # root, 
        # self_id, 
        # task_id, 
        rounds, 
        dataset_path, 
        target_idx, 
        skip_header, 
        task_mode, 
        metric_name,
        sponsor_trained_cooperative_model_output,
        assistor_trained_cooperative_model_outputs,
        sponsor_matched_identifers,
        last_round_result,
    ) -> None:

        dataset = np.genfromtxt(dataset_path, delimiter=',', skip_header=skip_header)
        target_idx = parse_idx(target_idx)
        target = dataset[:, target_idx]
        # output_path = os.path.join(root, self_id, 'task', task_id, 'train', 'round', str(round), 'output')
        # matched_idx_path = os.path.join(root, self_id, 'task', task_id, 'train', 'matched_idx')
        # round_path = os.path.join(root, self_id, 'task', task_id, 'train', 'round')
        # output = np.genfromtxt(os.path.join(output_path, '{}.csv'.format(self_id)), delimiter=',')
        # output = sponsor_trained_cooperative_model_output
        cooperative_model_output = sponsor_trained_cooperative_model_output.reshape(
            sponsor_trained_cooperative_model_output.shape[0], -1
        )
        count = np.ones((cooperative_model_output.shape[0], 1))
        # output_files = os.listdir(output_path)
        
        # for i in range(len(output_files)):
        #     from_id_i = os.path.splitext(output_files[i])[0]
        #     if from_id_i != self_id:
        #         output_i_path = os.path.join(output_path, output_files[i])
        #         if not os.path.exists(output_i_path):
        #             return "300?make_result sponsor cannot find train output file"
                    
        #         output_i = np.genfromtxt(os.path.join(output_path, output_files[i]), delimiter=',')
        #         output_i = output_i.reshape(output_i.shape[0], -1)
        #         self_from_idx_i = np.genfromtxt(os.path.join(matched_idx_path, '{}.csv'.format(from_id_i)),
        #                                         delimiter=',').astype(np.int64)
        #         output[self_from_idx_i,] = output[self_from_idx_i,] + output_i
        #         count[self_from_idx_i,] = count[self_from_idx_i,] + 1
        print('!!!assistor_trained_cooperative_model_outputs', assistor_trained_cooperative_model_outputs, type(assistor_trained_cooperative_model_outputs))
        for assistor_random_id, assistor_trained_cooperative_model_output in assistor_trained_cooperative_model_outputs.items():
            # output_i = np.genfromtxt(os.path.join(output_path, output_files[i]), delimiter=',')
            assistor_trained_cooperative_model_output = assistor_trained_cooperative_model_output.reshape(
                assistor_trained_cooperative_model_output.shape[0], -1
            )
            # self_from_idx_i = np.genfromtxt(os.path.join(matched_idx_path, '{}.csv'.format(from_id_i)),
            #                                 delimiter=',').astype(np.int64)
            self_from_idx_id = sponsor_matched_identifers[assistor_random_id]
            cooperative_model_output[self_from_idx_id,] = cooperative_model_output[self_from_idx_id,] + assistor_trained_cooperative_model_output
            count[self_from_idx_id,] = count[self_from_idx_id,] + 1
        cooperative_model_output = cooperative_model_output / count
        # result = np.genfromtxt(os.path.join(round_path, str(round - 1), 'result.csv'), delimiter=',')
        
        # result = last_round_result
        if round == 1:
            if len(last_round_result.shape) == 0:
                last_round_result = last_round_result.reshape(-1)
            if len(last_round_result.shape) == 1:
                last_round_result = last_round_result.reshape(1, -1)
        last_round_result = last_round_result.reshape(last_round_result.shape[0], -1)
        alpha = np.ones(1)
        func_ = minimize(cls.result_func, alpha, (task_mode, last_round_result, cooperative_model_output, target))
        alpha = func_.x
        # np.savetxt(os.path.join(round_path, str(round), 'alpha.csv'), alpha, delimiter=",")
        cur_round_result = last_round_result + alpha * cooperative_model_output
        # np.savetxt(os.path.join(round_path, str(round), 'result.csv'), result, delimiter=",")
        metric = Metric(task_mode, metric_name)
        eval = metric.eval(cur_round_result, target)
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
