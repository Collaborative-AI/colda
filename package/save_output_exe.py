import argparse
import os
import shutil

parser = argparse.ArgumentParser()
parser.add_argument('--root', default=None, type=str)
parser.add_argument('--self_id', default=None, type=str)
parser.add_argument('--task_id', default=None, type=str)
parser.add_argument('--mode', default=None, type=str)
parser.add_argument('--test_id', default=None, type=str)
parser.add_argument('--round', default=None, type=int)
parser.add_argument('--from_id', default=None, type=str)
args = vars(parser.parse_args())


def main():
    root = args['root']
    self_id = args['self_id']
    task_id = args['task_id']
    mode = args['mode']
    test_id = args['test_id']
    round = args['round']
    from_id = args['from_id']
    if mode == 'train':
        from_output_path = os.path.join(root, from_id, 'task', task_id, mode, 'round', str(round), 'output',
                                   '{}.csv'.format(from_id))
        self_output_path = os.path.join(root, self_id, 'task', task_id, mode, 'round', str(round), 'output',
                                   '{}.csv'.format(from_id))
    elif mode == 'test' and test_id is not None:
        from_output_path = os.path.join(root, from_id, 'task', task_id, mode, test_id, 'round', str(round), 'output',
                                   '{}.csv'.format(from_id))
        self_output_path = os.path.join(root, self_id, 'task', task_id, mode, test_id, 'round', str(round), 'output',
                                   '{}.csv'.format(from_id))
    else:
        raise ValueError('Not valid mode')
    shutil.copy(from_output_path, self_output_path)
    return


if __name__ == "__main__":
    main()
