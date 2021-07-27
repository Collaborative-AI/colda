import argparse
import numpy as np
import os

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
    init = np.genfromtxt(os.path.join(root, data_name, client_id, task_id, 'train', '0', 'init.csv'), delimiter=',')
    target = np.genfromtxt(os.path.join(root, data_name, client_id, 'test', 'target.csv'), delimiter=',')
    if round == 0:
        loss = np.sqrt(((target - init) ** 2).mean())
    else:
        client_ids = os.listdir(os.path.join(root, '{}'.format(data_name)))
        client_ids.remove('oracle')
        history = init
        for i in range(round):
            output_i = []
            for j in range(len(client_ids)):
                output_i_j = np.genfromtxt(
                    os.path.join(root, data_name, client_id, task_id, 'test', str(i + 1), 'output',
                                 '{}.csv'.format(client_ids[j])), delimiter=',')
                output_i.append(output_i_j.reshape(-1, 1))
            output_i = np.concatenate(output_i, axis=-1)
            output_i = np.mean(output_i, axis=-1)
            alpha = np.genfromtxt(os.path.join(root, data_name, client_id, task_id, 'train', str(i + 1), 'alpha.csv'),
                                 delimiter=',')
            history = history + alpha * output_i
        loss = np.sqrt(((target - history) ** 2).mean())
    print('Round: {}, RMSE: {}'.format(round, loss))
    return


if __name__ == "__main__":
    main()
