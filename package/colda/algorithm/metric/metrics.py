from __future__ import annotations
# from lib2to3.pytree import Base

import numpy as np

from sklearn.metrics import (
    mean_absolute_error, 
    mean_squared_error, 
    r2_score, 
    accuracy_score, 
    f1_score, 
    roc_auc_score
)

from algorithm.utils import softmax

from algorithm.metric.base import BaseMetric

from typeguard import typechecked


class Metric(BaseMetric):
    '''
    Metrics used to measure the performance of
    the model

    Methods
    -------
    make_metric
    eval
    MAD
    RMSE
    R2
    Accuracy
    F1
    AUCROC
    '''

    def __init__(self, task_mode, metric_name, metric=None):
        self.task_mode = task_mode
        self.metric_name = metric_name.split('_')
        self.metric = self.make_metric(self.task_mode, self.metric_name) if metric is None else metric

    def make_metric(self, task_mode, metric_name):
        metric_dict = {'regression': {'MAD': MAD, 'RMSE': RMSE, 'R2': R2},
                       'classification': {'Accuracy': Accuracy, 'F1': F1, 'AUCROC': AUCROC}}
        metric = []
        for i in range(len(metric_name)):
            if task_mode in metric_dict:
                if metric_name[i] in metric_dict[task_mode]:
                    metric.append(metric_dict[task_mode][metric_name[i]])
                else:
                    raise ValueError('Not valid metric name')
            else:
                raise ValueError('Not valid task mode')
        return metric

    def eval(self, output, target):
        evaluation = []
        evaluation_dict = {}
        for i in range(len(self.metric)):
            if self.task_mode == 'regression':
                output_ = output
                target_ = target
            elif self.task_mode == 'classification':
                target_ = target.reshape(-1)
                if self.metric_name[i] in ['Accuracy', 'F1']:
                    output_ = np.argmax(output, axis=1)
                elif self.metric_name[i] in ['AUCROC']:
                    output_ = softmax(output, axis=-1)
                    if output.shape[1] == 2:
                        output_ = output_[:, 1]
                    else:
                        output_ = output_
                else:
                    output_ = output
            else:
                raise ValueError('Not valid task name')
            evaluation_i = self.metric[i](output_, target_)
            evaluation.append('{}: {:.4f}'.format(self.metric_name[i], evaluation_i))
            evaluation_dict[self.metric_name[i]] = evaluation_i
        return evaluation, evaluation_dict


def MAD(output, target):
    mad = mean_absolute_error(output, target).item()
    return mad


def RMSE(output, target):
    rmse = np.sqrt(mean_squared_error(output, target)).item()
    return rmse


def R2(output, target):
    r2 = r2_score(output, target).item()
    return r2


def Accuracy(output, target):
    accuracy = accuracy_score(target, output).item()
    return accuracy


def F1(output, target):
    f1 = f1_score(target, output, average='macro').item()
    return f1


def AUCROC(output, target):
    rocauc = roc_auc_score(target, output, multi_class='ovr').item()
    return rocauc
