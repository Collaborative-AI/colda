import argparse
import os
import numpy as np
from utils import makedir_exist_ok

parser = argparse.ArgumentParser()
parser.add_argument('--root', default=None, type=str)
parser.add_argument('--self_id', default=None, type=str)
parser.add_argument('--task_id', default=None, type=str)
parser.add_argument('--run', default=None, type=str)
parser.add_argument('--test_id', default=None, type=str)
parser.add_argument('--from_id', default=None, type=str)
args = vars(parser.parse_args())


def main():
    root = args['root']
    self_id = args['self_id']
    task_id = args['task_id']
    run = args['run']
    test_id = args['test_id']
    from_id = args['from_id']
    if run == 'train':
        self_id_path = os.path.join(root, self_id, 'task', task_id, run, 'id', '{}.csv'.format(self_id))
        from_id_path = os.path.join(root, self_id, 'task', task_id, run, 'id', '{}.csv'.format(from_id))
        self_from_matched_idx_path = os.path.join(root, self_id, 'task', task_id, run, 'matched_idx')
    elif run == 'test' and test_id is not None:
        self_id_path = os.path.join(root, self_id, 'task', task_id, run, test_id, 'id', '{}.csv'.format(self_id))
        from_id_path = os.path.join(root, self_id, 'task', task_id, run, test_id, 'id', '{}.csv'.format(from_id))
        self_from_matched_idx_path = os.path.join(root, self_id, 'task', task_id, run, test_id, 'matched_idx')
    else:
        raise ValueError('Not valid run')
    self_id_data = np.genfromtxt(self_id_path, delimiter=',', dtype=np.str_)
    from_id_data = np.genfromtxt(from_id_path, delimiter=',', dtype=np.str_)
    _, self_from_matched_idx, _ = np.intersect1d(self_id_data, from_id_data, return_indices=True)
    makedir_exist_ok(self_from_matched_idx_path)
    np.savetxt(os.path.join(self_from_matched_idx_path, '{}.csv'.format(from_id)), self_from_matched_idx,
               delimiter=",")
    return


if __name__ == "__main__":
    main()
