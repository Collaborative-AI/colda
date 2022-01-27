import numpy as np
import os
import json
import collections
from utils import log, parse_idx
from metrics import Metric

def make_eval(root, self_id, task_id, test_id, round, dataset_path, target_idx, skip_header, task_mode, metric_name, task_path):

    task_path = os.path.join(root, self_id, 'task', task_id)
    result = np.genfromtxt(os.path.join(task_path, 'train', 'round', '0', 'result.csv'), delimiter=',')
    if len(result.shape) == 0:
        result = result.reshape(-1)
    if len(result.shape) == 1:
        result = result.reshape(1, -1)
    if dataset_path is not None and target_idx is not None:
        dataset = np.genfromtxt(dataset_path, delimiter=',', skip_header=skip_header)
        target_idx = parse_idx(target_idx)
        target = dataset[:, target_idx]
        metric = Metric(task_mode, metric_name)
        result = result.repeat(target.shape[0], axis=0)
        eval = metric.eval(result, target)
        msg = 'Test Round: 0, {}'.format(eval)
        log(msg, root, self_id, task_id, test_id)
    result_path = []
    for i in range(1, round + 1):
        sponsor_test_result_path = os.path.join(task_path, 'test', test_id, 'round', str(i), 'output',
                                                '{}.csv'.format(self_id))
        if not os.path.exists(sponsor_test_result_path):
            return "300?make_eval sponsor cannot find test output file"
    
    make_eval_res = collections.defaultdict(dict)
    for i in range(1, round + 1):
        output_path_i = os.path.join(task_path, 'test', test_id, 'round', str(i), 'output')
        output_i = np.genfromtxt(os.path.join(output_path_i, '{}.csv'.format(self_id)), delimiter=',')
        output_i = output_i.reshape(output_i.shape[0], -1)
        count_i = np.ones((output_i.shape[0], 1))
        output_files = os.listdir(output_path_i)
        for j in range(len(output_files)):
            from_id_j = os.path.splitext(output_files[j])[0]
            if from_id_j != self_id:
                output_i_j = np.genfromtxt(os.path.join(output_path_i, output_files[j]), delimiter=',')
                output_i_j = output_i_j.reshape(output_i_j.shape[0], -1)
                self_from_idx_j = np.genfromtxt(
                    os.path.join(task_path, 'test', test_id, 'matched_idx', '{}.csv'.format(from_id_j)),
                    delimiter=',').astype(np.int64)
                output_i[self_from_idx_j,] = output_i[self_from_idx_j,] + output_i_j
                count_i[self_from_idx_j,] = count_i[self_from_idx_j,] + 1
        output_i = output_i / count_i
        alpha = np.genfromtxt(os.path.join(task_path, 'train', 'round', str(i), 'alpha.csv'), delimiter=',')
        result = result + alpha * output_i
        result_path_i = os.path.join(task_path, 'test', test_id, 'round', str(i), 'result.csv')
        result_path.append(result_path_i)
        np.savetxt(result_path_i, result, delimiter=",")
        if dataset_path is not None and target_idx is not None:
            metric = Metric(task_mode, metric_name)
            eval, eval_dict = metric.eval(result, target)
            make_eval_res[i] = eval_dict
            msg = 'Test Round: {}, {}'.format(i, eval)
            log(msg, root, self_id, task_id, test_id)

    result_path = '?'.join(result_path)
    make_eval_res = json.dumps(make_eval_res)
    return '200?make_eval?{make_eval_res}?{result_path}'.format(make_eval_res = make_eval_res, result_path = result_path)
