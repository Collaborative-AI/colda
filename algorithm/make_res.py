import argparse
import numpy as np
import os
from utils import makedir_exist_ok

parser = argparse.ArgumentParser()
parser.add_argument('--data_name', default='BostonHousing', type=str)
parser.add_argument('--task_id', default=None, type=str)
parser.add_argument('--round', default=None, type=int)
args = vars(parser.parse_args())


def main():
    data_name = args['data_name']
    client_id = '0'
    task_id = args['task_id']
    round = args['round']
    makedir_exist_ok(os.path.join('.', '{}_{}'.format(data_name, client_id, task_id, round)))
    target = np.genfromtxt(os.path.join(data_name, client_id, 'train', 'target.csv'), delimiter=',')
    if round == 0:
        init = make_init(target)
        res = make_res(init, target)
        history = init
        np.savetxt(os.path.join(data_name, client_id, task_id, 'train', round, 'init.csv'), init, delimiter=",")
        np.savetxt(os.path.join(data_name, client_id, task_id, 'train', round, 'res.csv'), res, delimiter=",")
        np.savetxt(os.path.join(data_name, client_id, task_id, 'train', 'history.csv'), history, delimiter=",")
    else:
        output = []
        client_ids = os.listdir(
            os.path.join('.', '{}_{}'.format(data_name, client_id, task_id, 'train', round - 1, 'output')))
        for i in range(len(client_ids)):
            output_i = np.genfromtxt(os.path.join('.', '{}_{}'.format(
                data_name, client_id, task_id, round - 1, 'output',
                '{}.csv'.format(client_ids[i]))), delimiter=',')
            output.append(output_i.reshape(-1, 1))
        output = np.concatenate(output, axis=1)
        output = np.mean(output, dim=-1)
        history = np.genfromtxt(os.path.join(data_name, client_id, task_id, 'train', 'history.csv'), delimiter=',')
        history = history + output
        res = make_res(output, target)
        np.savetxt(os.path.join(data_name, client_id, task_id, 'train', round, 'res.csv'), res, delimiter=",")
        np.savetxt(os.path.join(data_name, client_id, task_id, 'train', 'history.csv'), history, delimiter=",")
    return


def make_init(target):
    init = np.mean(target)
    return init


def make_res(output, target):
    return 2 * (target - output)


if __name__ == "__main__":
    main()
