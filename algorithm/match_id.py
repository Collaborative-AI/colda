import argparse
import os
import numpy as np
from utils import makedir_exist_ok

parser = argparse.ArgumentParser()
parser.add_argument('--data_name', default='BostonHousing', type=str)
parser.add_argument('--task_id', default=None, type=str)
parser.add_argument('--run', default='train', type=str)
args = vars(parser.parse_args())

root = 'exp'


def main():
    data_name = args['data_name']
    task_id = args['task_id']
    client_id = '0'
    run = args['run']
    client_ids = os.listdir(os.path.join(root, '{}'.format(data_name)))
    client_ids.remove('oracle')
    makedir_exist_ok(os.path.join(root, data_name, client_id, task_id, run, 'matched_idx'))
    sponsor_id = np.genfromtxt(os.path.join(root, data_name, client_id, run, 'id.csv'), delimiter=',')
    for i in range(len(client_ids)):
        if client_ids[i] != client_id:
            assistor_id_i = np.genfromtxt(os.path.join(root, data_name, client_ids[i], run, 'id.csv'), delimiter=',')
            _, sponsor_idx_i, assistor_idx_i = np.intersect1d(sponsor_id, assistor_id_i, return_indices=True)
            makedir_exist_ok(os.path.join(root, data_name, client_ids[i], task_id, run, 'matched_idx'))
            np.savetxt(
                os.path.join(root, data_name, client_id, task_id, run, 'matched_idx', '{}.csv'.format(client_ids[i])),
                sponsor_idx_i, delimiter=",")
            np.savetxt(
                os.path.join(root, data_name, client_ids[i], task_id, run, 'matched_idx', '{}.csv'.format(client_id)),
                assistor_idx_i, delimiter=",")
    return


if __name__ == "__main__":
    main()
