import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--self_id', default=None, type=str)
parser.add_argument('--task_id', default=None, type=str)
parser.add_argument('--from_id', default=None, type=str)
parser.add_argument('--round', default=None, type=int)
args = vars(parser.parse_args())


def main():
    self_id = args['self_id']
    task_id = args['task_id']
    from_id = args['from_id']
    round = args['round']
    match_id_path = os.path.join(self_id, task_id, 'train', str(round), 'residual', '{}.csv.'.format(from_id))
    print(match_id_path)
    return


if __name__ == "__main__":
    main()
