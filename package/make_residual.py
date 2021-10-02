import numpy as np
import os
from utils import makedir_exist_ok, log


def make_residual(args):
    target_path = args['target_path']
    root = args['root']
    self_id = args['self_id']
    task_id = args['task_id']
    round = args['round']
    target = np.genfromtxt(target_path, delimiter=',')
    if round == 0:
        init = make_init(target).reshape(-1)
        round_path = os.path.join(root, self_id, 'task', task_id, 'train', 'round', str(round))
        makedir_exist_ok(round_path)
        np.savetxt(os.path.join(round_path, 'init.csv'), init, delimiter=",")
        residual = compute_residual(init, target)
        loss = np.sqrt(((target - init) ** 2).mean())
        msg = 'Train Round: init, RMSE: {}'.format(loss)
        log(msg, root, self_id, task_id)
        print('200?make_residual?complete', end='')
    else:
        round_path = os.path.join(root, self_id, 'task', task_id, 'train', 'round', str(round - 1))
        result = np.genfromtxt(os.path.join(round_path, 'result.csv'), delimiter=',')
        residual = compute_residual(result, target)
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
        np.savetxt(assistor_residual_path_i, residual[self_from_idx_i], delimiter=",")
        assistor_residual_path.append(assistor_residual_path_i)
    assistor_residual_path = '?'.join(assistor_residual_path)
    print('200?make_residual?{}'.format(assistor_residual_path), end='')
    return


def make_init(target):
    init = np.mean(target)
    return init


def compute_residual(output, target):
    return 2 * (target - output)
