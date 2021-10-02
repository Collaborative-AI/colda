import os
from utils import makedir_exist_ok


def save_output(args):
    root = args['root']
    self_id = args['self_id']
    task_id = args['task_id']
    mode = args['mode']
    test_id = args['test_id']
    round = args['round']
    from_id = args['from_id']
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
    print('200?save_output?{}'.join(output_path), end='')
    return
