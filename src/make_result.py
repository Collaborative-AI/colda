import numpy as np
from scipy.optimize import minimize
import os
from utils import log, parse_idx


def make_result(args):
    root = args['root']
    self_id = args['self_id']
    task_id = args['task_id']
    round = args['round']
    dataset_path = args['dataset_path']
    target_idx = args['target_idx']
    dataset = np.genfromtxt(dataset_path, delimiter=',')
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
                print("300?make_result sponsor cannot find train output file")
                return 
            output_i = np.genfromtxt(os.path.join(output_path, output_files[i]), delimiter=',')
            output_i = output_i.reshape(output_i.shape[0], -1)
            self_from_idx_i = np.genfromtxt(os.path.join(matched_idx_path, '{}.csv'.format(from_id_i)),
                                            delimiter=',').astype(np.int64)
            output[self_from_idx_i,] = output[self_from_idx_i,] + output_i
            count[self_from_idx_i,] = count[self_from_idx_i,] + 1
    output = output / count
    if round == 0:
        result = np.genfromtxt(os.path.join(round_path, str(round), 'init.csv'), delimiter=',')
        result = result.reshape(-1)
    else:
        result = np.genfromtxt(os.path.join(round_path, str(round - 1), 'result.csv'), delimiter=',')
        result = result.reshape(result.shape[0], -1)
    alpha = np.ones(1)
    func_ = minimize(result_func, alpha, (result, output, target))
    alpha = func_.x
    np.savetxt(os.path.join(round_path, str(round), 'alpha.csv'), alpha, delimiter=",")
    result = result + alpha * output
    np.savetxt(os.path.join(round_path, str(round), 'result.csv'), result, delimiter=",")
    loss = np.sqrt(((target - result) ** 2).mean())
    msg = 'Train Round: {}, RMSE: {}, alpha: {}'.format(round, loss, alpha)
    log(msg, root, self_id, task_id)
    print('200?make_result?complete', end='')
    return


def result_func(alpha, history, output, target):
    new_output = history + alpha * output
    loss = ((target - new_output) ** 2).mean()
    return loss
