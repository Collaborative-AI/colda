import argparse
import os
import numpy as np
from utils import makedir_exist_ok

parser = argparse.ArgumentParser()
parser.add_argument('--self_id', default=None, type=str)
parser.add_argument('--task_id', default=None, type=str)
parser.add_argument('--from_id', default=None, type=str)
parser.add_argument('--run', default=None, type=str)
parser.add_argument('--test_id', default=None, type=str)
args = vars(parser.parse_args())


def main():
    self_id = args['self_id']
    task_id = args['task_id']
    test_id = args['test_id']
    from_id = args['from_id']
    run = args['run']
    if test_id is not None and run == 'test':
        self_id_data = np.genfromtxt(os.path.join(self_id, task_id, run, test_id, 'id', '{}.csv'.format(self_id)),
                                     delimiter=',')
        from_id_data = np.genfromtxt(os.path.join(self_id, task_id, run, test_id, 'id', '{}.csv'.format(from_id)),
                                     delimiter=',')
        _, self_from_matched_idx, _ = np.intersect1d(self_id_data, from_id_data, return_indices=True)
        np.savetxt(os.path.join(self_id, task_id, run, test_id, 'matched_idx', '{}.csv'.format(from_id)),
                   self_from_matched_idx, delimiter=",")
    else:
        self_id_data = np.genfromtxt(os.path.join(self_id, task_id, run, 'id', '{}.csv'.format(self_id)), delimiter=',')
        from_id_data = np.genfromtxt(os.path.join(self_id, task_id, run, 'id', '{}.csv'.format(from_id)), delimiter=',')
        _, self_from_matched_idx, _ = np.intersect1d(self_id_data, from_id_data, return_indices=True)
        np.savetxt(os.path.join(self_id, task_id, run, 'matched_idx', '{}.csv'.format(from_id)), self_from_matched_idx,
                   delimiter=",")

    return


if __name__ == "__main__":
    main()
