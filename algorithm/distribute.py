import argparse
import os
import numpy as np
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
    client_ids = os.listdir(os.path.join(root, '{}'.format(data_name)))
    client_ids.remove('oracle')
    residual = np.genfromtxt(os.path.join(root, data_name, client_id, task_id, 'train', str(round), 'residual.csv'),
                             delimiter=',')
    for i in range(len(client_ids)):
        if client_ids[i] != client_id:
            sponsor_idx_i = np.genfromtxt(os.path.join(root, data_name, client_id, task_id, 'train', 'matched_idx',
                                                    '{}.csv'.format(client_ids[i])), delimiter=',').astype(np.int64)
            residual_i = residual[sponsor_idx_i]
            makedir_exist_ok(os.path.join(root, data_name, client_ids[i], task_id, 'train', str(round)))
            np.savetxt(os.path.join(root, data_name, client_ids[i], task_id, 'train', str(round), 'residual.csv'),
                       residual_i, delimiter=",")
    return


if __name__ == "__main__":
    main()
