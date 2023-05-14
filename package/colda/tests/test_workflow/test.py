import argparse
import numpy as np
from colda.algorithm.utils import parse_idx

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

if __name__ == '__main__':
    import torch

    # output = torch.randn(10, 5)
    # output.requires_grad = True
    # target = torch.randn(10, 5)
    # mse_c = torch.nn.MSELoss(reduction='sum')(output, target)
    # mse_c.backward()
    # print(output.grad)
    # de = - 2 * (target - output)
    # print(de)
    #
    # output = torch.randn(10, 5)
    # output.requires_grad = True
    # target = torch.randn(10, 5)
    # mse_c = torch.nn.L1Loss(reduction='sum')(output, target)
    # mse_c.backward()
    # print(output.grad)
    # de = - torch.sign(target - output)
    # print(de)

    # output = torch.randn(10, 5)
    # # output.requires_grad = True
    # target = torch.randint(0, 5, (10,))
    # softmax_output = torch.softmax(output, dim=-1)
    # softmax_output.requires_grad = True
    # logsoftmax_output = torch.log(softmax_output)
    # # logsoftmax_output.requires_grad = True
    # nll_c = torch.nn.NLLLoss(reduction='sum')(logsoftmax_output, target)
    # nll_c.backward()
    # print(softmax_output.grad)
    # one_hot_target = torch.eye(5)[target]
    # de = - one_hot_target / softmax_output
    # print(de)

    # output = torch.randn(10, 5)
    # output.requires_grad = True
    # target = torch.randint(0, 5, (10,))
    # softmax_output = torch.softmax(output, dim=-1)
    # # softmax_output.requires_grad = True
    # logsoftmax_output = torch.log(softmax_output)
    # # logsoftmax_output.requires_grad = True
    # nll_c = torch.nn.NLLLoss(reduction='sum')(logsoftmax_output, target)
    # nll_c.backward()
    # print(output.grad)
    # one_hot_target = torch.eye(5)[target]
    # de = softmax_output - one_hot_target
    # print(de)
