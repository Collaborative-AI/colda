import os
from utils import makedir_exist_ok


def save_match_id(args):
    root = args['root']
    self_id = args['self_id']
    task_id = args['task_id']
    mode = args['mode']
    test_id = args['test_id']
    from_id = args['from_id']
    if mode == 'train':
        match_id_path = os.path.join(root, self_id, 'task', task_id, mode, 'id')
        makedir_exist_ok(match_id_path)
        open(os.path.join(match_id_path, '{}.csv'.format(from_id)), "a")

    elif mode == 'test' and test_id is not None:
        match_id_path = os.path.join(root, self_id, 'task', task_id, mode, test_id, 'id')
        makedir_exist_ok(match_id_path)
        open(os.path.join(match_id_path, '{}.csv'.format(from_id)), "a")
    else:
        raise ValueError('Not valid mode')

    match_id_path = os.path.join(match_id_path, '{}.csv'.format(from_id))
    print(match_id_path, end='')
    return
