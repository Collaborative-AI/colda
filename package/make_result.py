import numpy as np
from scipy.optimize import minimize
import os
from utils import log


def make_result(args):
    target_path = args['target_path']
    root = args['root']
    self_id = args['self_id']
    task_id = args['task_id']
    round = args['round']
    target = np.genfromtxt(target_path, delimiter=',')
    output_path = os.path.join(root, self_id, 'task', task_id, 'train', 'round', str(round), 'output')
    matched_idx_path = os.path.join(root, self_id, 'task', task_id, 'train', 'matched_idx')
    round_path = os.path.join(root, self_id, 'task', task_id, 'train', 'round')
    output = np.genfromtxt(os.path.join(output_path, '{}.csv'.format(self_id)), delimiter=',')
    count = np.ones(output.shape[0])
    output_files = os.listdir(output_path)
    for i in range(len(output_files)):
        from_id_i = os.path.splitext(output_files[i])[0]
        if from_id_i != self_id:
            cur_output_file_position = os.path.join(output_path, output_files[i])
            if not os.path.exists(cur_output_file_position):
                print('sponsor cannot find train output file', end='')
                return 
            output_i = np.genfromtxt(os.path.join(output_path, output_files[i]), delimiter=',')
            self_from_idx_i = np.genfromtxt(os.path.join(matched_idx_path, '{}.csv'.format(from_id_i)),
                                            delimiter=',').astype(np.int64)
            output[self_from_idx_i] = output[self_from_idx_i] + output_i
            count[self_from_idx_i] = count[self_from_idx_i] + 1
    output = output / count
    if round == 0:
        result = np.genfromtxt(os.path.join(round_path, str(round), 'init.csv'), delimiter=',')
    else:
        result = np.genfromtxt(os.path.join(round_path, str(round - 1), 'result.csv'), delimiter=',')
    alpha = np.ones(1)
    func_ = minimize(result_func, alpha, (result, output, target))
    alpha = func_.x
    np.savetxt(os.path.join(round_path, str(round), 'alpha.csv'), alpha, delimiter=",")
    result = result + alpha * output
    np.savetxt(os.path.join(round_path, str(round), 'result.csv'), result, delimiter=",")
    loss = np.sqrt(((target - result) ** 2).mean())
    msg = 'Train Round: {}, RMSE: {}, alpha: {}'.format(round, loss, alpha)
    log(msg, root, self_id, task_id)
    return


def result_func(alpha, history, output, target):
    new_output = history + alpha * output
    loss = ((target - new_output) ** 2).mean()
    return loss
