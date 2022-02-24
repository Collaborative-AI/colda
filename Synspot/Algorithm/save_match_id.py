import os
from synspot.algorithm.utils import makedir_exist_ok


def save_match_id(root, self_id, task_id, mode, test_id, from_id):

    if mode == 'train':
        match_id_path = os.path.join(root, self_id, 'task', task_id, mode, 'id')
        makedir_exist_ok(match_id_path)
        open(os.path.join(match_id_path, '{}.csv'.format(from_id)), "a")
    elif mode == 'test' and test_id is not None:
        match_id_path = os.path.join(root, self_id, 'task', task_id, mode, test_id, 'id')
        makedir_exist_ok(match_id_path)
        open(os.path.join(match_id_path, '{}.csv'.format(from_id)), "a")
    else:
        print('300?save_match_id?not valid mode', end='')
        return
    match_id_path = os.path.join(match_id_path, '{}.csv'.format(from_id))
    return '200?save_match_id?{}'.format(match_id_path)
