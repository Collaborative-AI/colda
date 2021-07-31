import argparse
import os
import shutil

parser = argparse.ArgumentParser()
parser.add_argument('--root', default=None, type=str)
parser.add_argument('--self_id', default=None, type=str)
parser.add_argument('--task_id', default=None, type=str)
parser.add_argument('--round', default=None, type=int)
parser.add_argument('--from_id', default=None, type=str)
args = vars(parser.parse_args())


def main():
    root = args['root']
    self_id = args['self_id']
    task_id = args['task_id']
    round = args['round']
    from_id = args['from_id']
    self_residual_path = os.path.join(root, self_id, 'task', task_id, 'train', 'round', str(round), 'residual',
                                      '{}.csv'.format(self_id))
    from_residual_path = os.path.join(root, from_id, 'task', task_id, 'train', 'round', str(round), 'residual',
                                      '{}.csv'.format(self_id))
    shutil.copy(from_residual_path, self_residual_path)
    return


if __name__ == "__main__":
    main()
