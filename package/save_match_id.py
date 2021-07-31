import argparse
import os

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
        match_id_path = os.path.join(root, self_id, 'task', task_id, run, 'id', '{}.csv'.format(from_id))
    elif run == 'test' and test_id is not None:
        match_id_path = os.path.join(root, self_id, 'task', task_id, run, test_id, 'id', '{}.csv'.format(from_id))
    else:
        raise ValueError('Not valid run')
    print(match_id_path)
    return


if __name__ == "__main__":
    main()
