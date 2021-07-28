import argparse
import numpy as np
from scipy.optimize import minimize
import os
from utils import makedir_exist_ok

parser = argparse.ArgumentParser()
parser.add_argument('--data_name', default='BostonHousing', type=str)
parser.add_argument('--task_id', default=None, type=str)
parser.add_argument('--round', default=None, type=int)
args = vars(parser.parse_args())

root = 'exp'


def main():
    data_name = args['data_name']
    client_id = '0'
    task_id = args['task_id']
    round = args['round']
    target = np.genfromtxt(os.path.join(root, data_name, client_id, 'train', 'target.csv'), delimiter=',')
    makedir_exist_ok(os.path.join(root, data_name, client_id, task_id, 'train', str(round)))
    if round == 0:
        init = make_init(target).reshape(-1)
        residual = make_residual(init, target)
        np.savetxt(os.path.join(root, data_name, client_id, task_id, 'train', str(round), 'init.csv'), init,
                   delimiter=",")
        np.savetxt(os.path.join(root, data_name, client_id, task_id, 'train', str(round), 'res.csv'), residual,
                   delimiter=",")
        loss = np.sqrt(((target - init) ** 2).mean())
        print('Train Round: -1, RMSE: {}'.format(loss))
    else:
        result = np.genfromtxt(
            os.path.join(root, data_name, client_id, task_id, 'train', str(round - 1), 'result.csv'), delimiter=',')
        residual = make_residual(result, target)
        np.savetxt(os.path.join(root, data_name, client_id, task_id, 'train', str(round), 'res.csv'), residual,
                   delimiter=",")
        np.savetxt(os.path.join(root, data_name, client_id, task_id, 'train', str(round), 'history.csv'), result,
                   delimiter=",")
    return


def make_init(target):
    init = np.mean(target)
    return init


def make_residual(output, target):
    return 2 * (target - output)


if __name__ == "__main__":
    main()
