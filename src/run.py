import argparse
from make_train_local import make_train_local
from make_test_local import make_test_local
from make_hash import make_hash
from save_match_id import save_match_id
from make_match_idx import make_match_idx
from make_residual import make_residual
from save_residual import save_residual
from make_train import make_train
from save_output import save_output
from make_result import make_result
from make_test import make_test
from make_eval import make_eval

parser = argparse.ArgumentParser()
parser.add_argument('func', type=str)
parser.add_argument('--root', default=None, type=str)
parser.add_argument('--self_id', default=None, type=str)
parser.add_argument('--task_id', default=None, type=str)
parser.add_argument('--mode', default=None, type=str)
parser.add_argument('--round', default=None, type=int)
parser.add_argument('--test_id', default=None, type=str)
parser.add_argument('--from_id', default=None, type=str)
parser.add_argument('--dataset_path', default=None, type=str)
parser.add_argument('--id_idx', default=None, type=str)
parser.add_argument('--data_idx', default=None, type=str)
parser.add_argument('--target_idx', default=None, type=str)
parser.add_argument('--skip_header', default=1, type=int)
args = vars(parser.parse_args())


def main():
    func = args['func']
    if func == 'make_train_local':
        make_train_local(args)
    elif func == 'make_test_local':
        make_test_local(args)
    elif func == 'make_hash':
        make_hash(args)
    elif func == 'save_match_id':
        save_match_id(args)
    elif func == 'make_match_idx':
        make_match_idx(args)
    elif func == 'make_residual':
        make_residual(args)
    elif func == 'save_residual':
        save_residual(args)
    elif func == 'make_train':
        make_train(args)
    elif func == 'save_output':
        save_output(args)
    elif func == 'make_result':
        make_result(args)
    elif func == 'make_test':
        make_test(args)
    elif func == 'make_eval':
        make_eval(args)
    else:
        raise ValueError('Not valid func')


if __name__ == '__main__':
    main()
