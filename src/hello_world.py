import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--root', default=None, type=str)
parser.add_argument('--data_name', default=None, type=str)
parser.add_argument('--num_users', default=None, type=int)
parser.add_argument('--task_id', default=None, type=int)
parser.add_argument('--match_rate', default=None, type=float)
args = vars(parser.parse_args())


def main():
    root = args['root']
    arr = np.arange(12)
    print('Hello World')
    print(root)
    print(arr)


if __name__ == '__main__':
    main()
