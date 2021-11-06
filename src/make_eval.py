import numpy as np
import os
from utils import log, parse_idx


def make_eval(args):
    root = args['root']
    self_id = args['self_id']
    task_id = args['task_id']
    test_id = args['test_id']
    round = args['round']
    dataset_path = args['dataset_path']
    target_idx = args['target_idx']
    task_path = os.path.join(root, self_id, 'task', task_id)
    result = np.genfromtxt(os.path.join(task_path, 'train', 'round', '0', 'init.csv'), delimiter=',')
    result = result.reshape(-1)
    if dataset_path is not None and target_idx is not None:
        dataset = np.genfromtxt(dataset_path, delimiter=',')
        target_idx = parse_idx(target_idx)
        target = dataset[:, target_idx]
        loss = np.sqrt(((target - result) ** 2).mean())
        msg = 'Test Round: init, RMSE: {}'.format(loss)
        log(msg, root, self_id, task_id, test_id)
    result_path = []

    for i in range(round + 1):
        sponsor_test_result_path = os.path.join(task_path, 'test', test_id, 'round', str(i), 'output', '{}.csv'.format(self_id))
        if not os.path.exists(sponsor_test_result_path):
            print("300?make_eval sponsor cannot find test output file")
            return 

    for i in range(round + 1):
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
            loss = np.sqrt(((target - result) ** 2).mean())
            msg = 'Test Round: {}, RMSE: {}'.format(i, loss)
            log(msg, root, self_id, task_id, test_id)
    result_path = '?'.join(result_path)
    print('200?make_eval?{}'.format(result_path), end='')
    return
