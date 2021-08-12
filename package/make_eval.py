import numpy as np
import os
from utils import log


def make_eval(args):
    target_path = args['target_path']
    root = args['root']
    self_id = args['self_id']
    task_id = args['task_id']
    test_id = args['test_id']
    round = args['round']
    task_path = os.path.join(root, self_id, 'task', task_id)
    result = np.genfromtxt(os.path.join(task_path, 'train', 'round', '0', 'init.csv'), delimiter=',')
    if target_path is not None:
        target = np.genfromtxt(target_path, delimiter=',')
        loss = np.sqrt(((target - result) ** 2).mean())
        msg = 'Test Round: init, RMSE: {}'.format(loss)
        log(msg, root, self_id, task_id, test_id)
    result_path = []
    for i in range(round + 1):
        output_path_i = os.path.join(task_path, 'test', test_id, 'round', str(i), 'output')
        output_i = np.genfromtxt(os.path.join(output_path_i, '{}.csv'.format(self_id)), delimiter=',')
        count_i = np.ones(output_i.shape[0])
        output_files = os.listdir(output_path_i)
        for j in range(len(output_files)):
            from_id_j = os.path.splitext(output_files[j])[0]
            if from_id_j != self_id:
                output_i_j = np.genfromtxt(os.path.join(output_path_i, output_files[j]), delimiter=',')
                self_from_idx_j = np.genfromtxt(
                    os.path.join(task_path, 'test', test_id, 'matched_idx', '{}.csv'.format(from_id_j)),
                    delimiter=',').astype(np.int64)
                output_i[self_from_idx_j] = output_i[self_from_idx_j] + output_i_j
                count_i[self_from_idx_j] = count_i[self_from_idx_j] + 1
        output_i = output_i / count_i
        alpha = np.genfromtxt(os.path.join(task_path, 'train', 'round', str(i), 'alpha.csv'), delimiter=',')
        result = result + alpha * output_i
        result_path_i = os.path.join(task_path, 'test', test_id, 'round', str(i), 'result.csv')
        result_path.append(result_path_i)
        np.savetxt(result_path_i, result, delimiter=",")
        if target_path is not None:
            loss = np.sqrt(((target - result) ** 2).mean())
            msg = 'Test Round: {}, RMSE: {}'.format(i, loss)
            log(msg, root, self_id, task_id, test_id)
    print('?'.join(result_path))
    return
