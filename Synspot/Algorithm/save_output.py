import os
from synspot.algorithm.utils import makedir_exist_ok


def save_output(root, self_id, task_id, mode, test_id, round, from_id):

    if mode == 'train':
        output_path = os.path.join(root, self_id, 'task', task_id, mode, 'round', str(round), 'output')
        makedir_exist_ok(output_path)
        open(os.path.join(output_path, '{}.csv'.format(from_id)), "a")
    elif mode == 'test' and test_id is not None:
        output_path = os.path.join(root, self_id, 'task', task_id, mode, test_id, 'round', str(round), 'output')
        makedir_exist_ok(output_path)
        open(os.path.join(output_path, '{}.csv'.format(from_id)), "a")
    else:
        print('300?save_output?not valid mode', end='')
        return
    output_path = os.path.join(output_path, '{}.csv'.format(from_id))
    return '200?save_output?{}'.format(output_path)
