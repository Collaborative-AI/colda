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
    output = []
    client_outputs = os.listdir(os.path.join(root, data_name, client_id, task_id, 'train', str(round), 'output'))
    for i in range(len(client_outputs)):
        output_i = np.genfromtxt(
            os.path.join(root, data_name, client_id, task_id, 'train', str(round), 'output', client_outputs[i]),
            delimiter=',')
        output.append(output_i.reshape(-1, 1))
    output = np.concatenate(output, axis=-1)
    output = np.mean(output, axis=-1)
    if round == 0:
        result = np.genfromtxt(
            os.path.join(root, data_name, client_id, task_id, 'train', str(round), 'init.csv'),
            delimiter=',')
    else:
        result = np.genfromtxt(
            os.path.join(root, data_name, client_id, task_id, 'train', str(round - 1), 'result.csv'),
            delimiter=',')
    alpha = np.ones(1)
    func_ = minimize(func, alpha, (result, output, target))
    alpha = func_.x
    np.savetxt(os.path.join(root, data_name, client_id, task_id, 'train', str(round), 'alpha.csv'), alpha,
               delimiter=",")
    result = result + alpha * output
    loss = np.sqrt(((target - result) ** 2).mean())
    print('Train Round: {}, RMSE: {}'.format(round, loss))
    np.savetxt(os.path.join(root, data_name, client_id, task_id, 'train', str(round), 'result.csv'), result,
               delimiter=",")
    return


def func(alpha, history, output, target):
    new_output = history + alpha * output
    loss = ((target - new_output) ** 2).mean()
    return loss


if __name__ == "__main__":
    main()
