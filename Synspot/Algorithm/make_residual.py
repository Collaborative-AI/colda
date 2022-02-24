import numpy as np
import os
from synspot.algorithm.utils import makedir_exist_ok, log, parse_idx
from synspot.algorithm.metrics import Metric


def make_residual(root, self_id, task_id, round, dataset_path, target_idx, skip_header, task_mode, metric_name):

    dataset = np.genfromtxt(dataset_path, delimiter=',', skip_header=skip_header)
    target_idx = parse_idx(target_idx)
    target = dataset[:, target_idx]
    if round == 1:
        output = make_init(task_mode, target)
        round_path = os.path.join(root, self_id, 'task', task_id, 'train', 'round', str(round - 1))
        makedir_exist_ok(round_path)
        np.savetxt(os.path.join(round_path, 'result.csv'), output, delimiter=",")
        output = output.repeat(target.shape[0], axis=0)
        residual = compute_residual(task_mode, output, target)
        metric = Metric(task_mode, metric_name)
        eval = metric.eval(output, target)
        msg = 'Train Round: 0, {}'.format(eval)
        log(msg, root, self_id, task_id)
    else:
        round_path = os.path.join(root, self_id, 'task', task_id, 'train', 'round', str(round - 1))
        result = np.genfromtxt(os.path.join(round_path, 'result.csv'), delimiter=',')
        result = result.reshape(result.shape[0], -1)
        residual = compute_residual(task_mode, result, target)
    residual_path = os.path.join(root, self_id, 'task', task_id, 'train', 'round', str(round), 'residual')
    makedir_exist_ok(residual_path)
    np.savetxt(os.path.join(residual_path, '{}.csv'.format(self_id)), residual, delimiter=",")
    matched_idx_path = os.path.join(root, self_id, 'task', task_id, 'train', 'matched_idx')
    self_from_idx_files = os.listdir(matched_idx_path)
    assistor_residual_path = []
    for i in range(len(self_from_idx_files)):
        self_from_idx_i = np.genfromtxt(os.path.join(matched_idx_path, str(self_from_idx_files[i])),
                                        delimiter=',').astype(np.int64)
        assistor_residual_path_i = os.path.join(residual_path, str(self_from_idx_files[i]))
        np.savetxt(assistor_residual_path_i, residual[self_from_idx_i,], delimiter=",")
        assistor_residual_path.append(assistor_residual_path_i)
    assistor_residual_path = '?'.join(assistor_residual_path)
    return '200?make_residual?{}'.format(assistor_residual_path)


def make_init(task_mode, target):
    if task_mode == 'regression':
        init = np.mean(target, axis=0, keepdims=True)
    elif task_mode == 'classification':
        target = target.astype(np.int64).reshape(-1)
        one_hot_target = np.eye(np.max(target) + 1)[target]
        init = np.log(np.mean(one_hot_target, axis=0, keepdims=True))
    else:
        raise ValueError('Not valid task mode')
    return init


def compute_residual(task_mode, output, target):
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
