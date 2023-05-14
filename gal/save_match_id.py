import argparse
import os
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
        match_id_path = os.path.join(root, self_id, 'task', task_id, run, 'id')
        makedir_exist_ok(match_id_path)
        open(os.path.join(match_id_path, '{}.csv'.format(from_id)),"a")

    elif run == 'test' and test_id is not None:
        match_id_path = os.path.join(root, self_id, 'task', task_id, run, test_id, 'id')
        makedir_exist_ok(match_id_path)
        open(os.path.join(match_id_path, '{}.csv'.format(from_id)),"a")
    else:
        raise ValueError('Not valid run')

    match_id_path = os.path.join(match_id_path, '{}.csv'.format(from_id))
    print(match_id_path)
    return


if __name__ == "__main__":
    main()
