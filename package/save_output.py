import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--self_id', default=None, type=str)
parser.add_argument('--task_id', default=None, type=str)
parser.add_argument('--from_id', default=None, type=str)
parser.add_argument('--run', default=None, type=str)
parser.add_argument('--test_id', default=None, type=str)
parser.add_argument('--round', default=None, type=int)
args = vars(parser.parse_args())


def main():
    self_id = args['self_id']
    task_id = args['task_id']
    from_id = args['from_id']
    round = args['round']
    run = args['run']
    test_id =args['test_id']
    if test_id is not None and run == 'test':
        match_id_path = os.path.join(self_id, task_id, run, test_id, str(round), 'output', '{}.csv'.format(from_id))
    else:
        match_id_path = os.path.join(self_id, task_id, run, str(round), 'output', '{}.csv'.format(from_id))

    print(match_id_path)
    return


if __name__ == "__main__":
    main()
