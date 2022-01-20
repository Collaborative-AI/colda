import os
import numpy as np
from utils import makedir_exist_ok


def make_match_idx(root, self_id, task_id, mode, test_id, from_id):

    if mode == 'train':
        self_id_path = os.path.join(root, self_id, 'task', task_id, mode, 'id', '{}.csv'.format(self_id))
        from_id_path = os.path.join(root, self_id, 'task', task_id, mode, 'id', '{}.csv'.format(from_id))
        self_from_matched_idx_path = os.path.join(root, self_id, 'task', task_id, mode, 'matched_idx')
    elif mode == 'test' and test_id is not None:
        self_id_path = os.path.join(root, self_id, 'task', task_id, mode, test_id, 'id', '{}.csv'.format(self_id))
        from_id_path = os.path.join(root, self_id, 'task', task_id, mode, test_id, 'id', '{}.csv'.format(from_id))
        self_from_matched_idx_path = os.path.join(root, self_id, 'task', task_id, mode, test_id, 'matched_idx')
    else:
        print('300?make_match_idx?not valid mode', end='')
        return
    self_id_data = np.genfromtxt(self_id_path, delimiter=',', dtype=np.str_)
    from_id_data = np.genfromtxt(from_id_path, delimiter=',', dtype=np.str_)
    _, self_from_matched_idx, _ = np.intersect1d(self_id_data, from_id_data, return_indices=True)
    makedir_exist_ok(self_from_matched_idx_path)
    np.savetxt(os.path.join(self_from_matched_idx_path, '{}.csv'.format(from_id)), self_from_matched_idx,
               delimiter=",")
    print('200?make_match_idx?complete', end='')
    return
