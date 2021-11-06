import argparse
import numpy as np
from utils import parse_idx

# parser = argparse.ArgumentParser()
# parser.add_argument('--root', default=None, type=str)
# parser.add_argument('--data_name', default=None, type=str)
# parser.add_argument('--num_users', default=None, type=int)
# parser.add_argument('--task_id', default=None, type=int)
# parser.add_argument('--match_rate', default=None, type=float)
# args = vars(parser.parse_args())
#
# ./dist/run/run
# def main():
#     root = args['root']
#     arr = np.arange(12)
#     print('Hello World')
#     print(root)
#     print(arr)
#
#
# if __name__ == '__main__':
#     main()


# def main():
#     idx = '1, 2-4, 20-43'
#     parsed_idx = parse_idx(idx)
#     print(parsed_idx)
#
#
# if __name__ == '__main__':
#     main()