import argparse
import numpy as np
import os
from utils import makedir_exist_ok, log

parser = argparse.ArgumentParser()
parser.add_argument('--self_id', default=None, type=str)
parser.add_argument('--task_id', default=None, type=str)
parser.add_argument('--round', default=None, type=int)
parser.add_argument('--target_path', default=None, type=str)
args = vars(parser.parse_args())


def main():
    self_id = args['self_id']
    task_id = args['task_id']
    round = args['round']
    target_path = args['target_path']
    target = np.genfromtxt(target_path, delimiter=',')
    makedir_exist_ok(os.path.join(self_id, task_id, 'train', str(round)))
    if round == 0:
        init = make_init(target).reshape(-1)
        np.savetxt(os.path.join(self_id, task_id, 'train', str(round), 'init.csv'), init, delimiter=",")
        residual = make_residual(init, target)
        loss = np.sqrt(((target - init) ** 2).mean())
        msg = 'Train Round: init, RMSE: {}'.format(loss)
        log(msg, self_id, task_id)
    else:
        result = np.genfromtxt(os.path.join(self_id, task_id, 'train', str(round - 1), 'result.csv'), delimiter=',')
        residual = make_residual(result, target)
    self_residual_path = os.path.join(self_id, task_id, 'train', str(round), 'residual', '{}.csv'.format(self_id))
    np.savetxt(self_residual_path, residual, delimiter=",")
    self_from_idx_files = os.listdir(os.path.join(self_id, task_id, 'train', 'matched_idx'))
    residual_path = []
    for i in range(len(self_from_idx_files)):
        self_from_idx_i = np.genfromtxt(
            os.path.join(self_id, task_id, 'train', 'matched_idx', str(self_from_idx_files[i])), delimiter=',')
        residual_path_i = os.path.join(self_id, task_id, 'train', str(round), 'residual', str(self_from_idx_files[i]))
        residual_path.append(residual_path_i)
        np.savetxt(residual_path[-1], residual[self_from_idx_i], delimiter=",")
    residual_path = '?'.join(residual_path)
    print(residual_path)
    return


def make_init(target):
    init = np.mean(target)
    return init


def make_residual(output, target):
    return 2 * (target - output)


if __name__ == "__main__":
    main()
