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
    if round == -1:
        loss = np.sqrt(((target - init) ** 2).mean())
    else:
        client_ids = os.listdir(os.path.join(root, '{}'.format(data_name)))
        client_ids.remove('oracle')
        result = init
        for i in range(round + 1):
            output_i = np.genfromtxt(os.path.join(root, data_name, client_id, task_id, 'test', str(i), 'output',
                                                  '{}.csv'.format(client_id)), delimiter=',')
            count_i = np.ones(output_i.shape[0])
            for j in range(len(client_ids)):
                if client_ids[j] != client_id:
                    sponsor_idx_j = np.genfromtxt(
                        os.path.join(root, data_name, client_id, task_id, 'test', 'matched_idx',
                                     '{}.csv'.format(client_ids[j])), delimiter=',').astype(np.int64)
                    output_i_j = np.genfromtxt(
                        os.path.join(root, data_name, client_id, task_id, 'test', str(i), 'output',
                                     '{}.csv'.format(client_ids[j])), delimiter=',')
                    output_i[sponsor_idx_j] = output_i[sponsor_idx_j] + output_i_j
                    count_i[sponsor_idx_j] = count_i[sponsor_idx_j] + 1
            output_i = output_i / count_i
            alpha = np.genfromtxt(os.path.join(root, data_name, client_id, task_id, 'train', str(i), 'alpha.csv'),
                                  delimiter=',')
            result = result + alpha * output_i
        loss = np.sqrt(((target - result) ** 2).mean())
        np.savetxt(os.path.join(root, data_name, client_id, task_id, 'test', str(round), 'result.csv'), result,
                   delimiter=",")
    print('Test Round: {}, RMSE: {}'.format(round, loss))
    return


if __name__ == "__main__":
    main()
