import argparse
import numpy as np
import os

parser = argparse.ArgumentParser()
parser.add_argument('--data_name', default='BostonHousing', type=str)
parser.add_argument('--task_id', default=None, type=str)
parser.add_argument('--round', default=None, type=int)
args = vars(parser.parse_args())


def main():
    data_name = args['data_name']
    client_id = '0'
    task_id = args['task_id']
    round = args['task_id']
    init = np.genfromtxt(os.path.join(data_name, client_id, task_id, 'train', '0', 'init.csv'), delimiter=',')
    client_ids = os.listdir(os.path.join('.', '{}'.format(data_name)))
    target = np.genfromtxt(os.path.join(data_name, client_id, 'train', 'target.csv'), delimiter=',')
    output = []
    for i in range(round):
        output_i = []
        for j in range(len(client_ids)):
            output_i_j = np.genfromtxt(os.path.join(data_name, client_id, task_id, 'test', str(i + 1), 'output',
                                                    '{}.csv'.format(client_ids[j])), delimiter=',')
            output_i.append(output_i_j.reshape(-1, 1))
        output_i = np.concatenate(output_i, axis=-1)
        output_i = np.mean(output_i, axis=-1)
        output.append(output_i.reshape(-1, 1))
    output = np.concatenate(output, axis=-1)
    output = init + np.sum(output, axis=-1)
    loss = ((target - output) ** 2).mean(axis=0)
    print('Loss: {}'.format(loss))
    return


def make_init(target):
    init = np.mean(target)
    return init


def make_res(output, target):
    return 2 * (target - output)


if __name__ == "__main__":
    main()
