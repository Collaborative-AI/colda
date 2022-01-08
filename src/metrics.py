import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, accuracy_score, f1_score


class Metric():
    def __init__(self, task_mode, metric_name, metric=None):
        self.task_mode = task_mode
        self.metric_name = metric_name.split('_')
        self.metric = self.make_metric(self.task_mode, self.metric_name) if metric is None else metric

    def make_metric(self, task_mode, metric_name):
        metric_dict = {'regression': {'MAD': MAD, 'RMSE': RMSE, 'R2': R2},
                       'classification': {'Accuracy': Accuracy, 'F1': F1}}
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
        if self.task_mode == 'regression':
            pass
        elif self.task_mode == 'classification':
            output = np.argmax(output, axis=1)
        else:
            raise ValueError('Not valid task name')
        for i in range(len(self.metric)):
            evaluation_i = self.metric[i](output, target)
            evaluation.append('{}: {:.4f}'.format(self.metric_name[i], evaluation_i))
            evaluation_dict[self.metric_name[i]] = evaluation_i
        evaluation = ', '.join(evaluation)
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
    accuracy = accuracy_score(output, target).item()
    return accuracy


def F1(output, target):
    f1 = f1_score(output, target, average='macro').item()
    return f1
