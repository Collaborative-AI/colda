import numpy as np
from scipy.optimize import minimize
import os
from synspot.algorithm.base import BaseAlgorithm
from synspot.algorithm.utils import log, parse_idx
from synspot.algorithm.metric.metrics import Metric


class MakeResult(BaseAlgorithm):

    def make_result(
        self, 
        root, 
        self_id, 
        task_id, 
        round, 
        dataset_path, 
        target_idx, 
        skip_header, 
        task_mode, 
        metric_name
    ) -> None:

        dataset = np.genfromtxt(dataset_path, delimiter=',', skip_header=skip_header)
        target_idx = parse_idx(target_idx)
        target = dataset[:, target_idx]
        output_path = os.path.join(root, self_id, 'task', task_id, 'train', 'round', str(round), 'output')
        matched_idx_path = os.path.join(root, self_id, 'task', task_id, 'train', 'matched_idx')
        round_path = os.path.join(root, self_id, 'task', task_id, 'train', 'round')
        output = np.genfromtxt(os.path.join(output_path, '{}.csv'.format(self_id)), delimiter=',')
        output = output.reshape(output.shape[0], -1)
        count = np.ones((output.shape[0], 1))
        output_files = os.listdir(output_path)
        for i in range(len(output_files)):
            from_id_i = os.path.splitext(output_files[i])[0]
            if from_id_i != self_id:
                output_i_path = os.path.join(output_path, output_files[i])
                if not os.path.exists(output_i_path):
                    return "300?make_result sponsor cannot find train output file"
                    
                output_i = np.genfromtxt(os.path.join(output_path, output_files[i]), delimiter=',')
                output_i = output_i.reshape(output_i.shape[0], -1)
                self_from_idx_i = np.genfromtxt(os.path.join(matched_idx_path, '{}.csv'.format(from_id_i)),
                                                delimiter=',').astype(np.int64)
                output[self_from_idx_i,] = output[self_from_idx_i,] + output_i
                count[self_from_idx_i,] = count[self_from_idx_i,] + 1
        output = output / count
        result = np.genfromtxt(os.path.join(round_path, str(round - 1), 'result.csv'), delimiter=',')
        if round == 1:
            if len(result.shape) == 0:
                result = result.reshape(-1)
            if len(result.shape) == 1:
                result = result.reshape(1, -1)
        result = result.reshape(result.shape[0], -1)
        alpha = np.ones(1)
        func_ = minimize(result_func, alpha, (task_mode, result, output, target))
        alpha = func_.x
        np.savetxt(os.path.join(round_path, str(round), 'alpha.csv'), alpha, delimiter=",")
        result = result + alpha * output
        np.savetxt(os.path.join(round_path, str(round), 'result.csv'), result, delimiter=",")
        metric = Metric(task_mode, metric_name)
        eval = metric.eval(result, target)
        msg = 'Train Round: {}, {}, Alpha: {}'.format(round, eval, alpha.item())
        log(msg, root, self_id, task_id)
        return '200?make_result?complete'


    def result_func(
        self,
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
