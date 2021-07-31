import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--root', default=None, type=str)
parser.add_argument('--self_id', default=None, type=str)
parser.add_argument('--task_id', default=None, type=str)
parser.add_argument('--run', default=None, type=str)
parser.add_argument('--test_id', default=None, type=str)
parser.add_argument('--round', default=None, type=int)
parser.add_argument('--from_id', default=None, type=str)
args = vars(parser.parse_args())


def main():
    root = args['root']
    self_id = args['self_id']
    task_id = args['task_id']
    run = args['run']
    test_id = args['test_id']
    round = args['round']
    from_id = args['from_id']
    if run == 'train':
        output_path = os.path.join(root, self_id, 'task', task_id, run, 'round', str(round), 'output',
                                   '{}.csv'.format(from_id))
    elif run == 'test' and test_id is not None:
        output_path = os.path.join(root, self_id, 'task', task_id, run, test_id, 'round', str(round), 'output',
                                   '{}.csv'.format(from_id))
    else:
        raise ValueError('Not valid run')
    print(output_path)
    return


if __name__ == "__main__":
    main()
