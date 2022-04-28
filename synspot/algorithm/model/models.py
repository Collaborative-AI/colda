from sklearn.linear_model import (
    LinearRegression, 
    LogisticRegression
)

from sklearn.tree import (
    DecisionTreeRegressor, 
    DecisionTreeClassifier
)

from sklearn.svm import (
    SVR, 
    SVC
)

from sklearn.ensemble import (
    GradientBoostingRegressor, 
    GradientBoostingClassifier
)

from sklearn.neural_network import (
    MLPRegressor, 
    MLPClassifier
)

from sklearn.multioutput import MultiOutputRegressor


class Model:
    def __init__(self, task_mode, model_name, model=None):
        self.task_mode = task_mode
        self.model_name = model_name
        self.model = self.make_model(self.task_mode, self.model_name) if model is None else model

    def make_model(self, task_mode, model_name):
        model_dict = {'regression': {'linear': LinearRegression, 'decision_tree': DecisionTreeRegressor,
                                     'svm': SVR, 'gradient_boosting': GradientBoostingRegressor, 'mlp': MLPRegressor},
                      'classification': {'linear': LogisticRegression, 'decision_tree': DecisionTreeClassifier,
                                         'svm': SVC, 'gradient_boosting': GradientBoostingClassifier,
                                         'mlp': MLPClassifier}}
        if task_mode in model_dict:
            if model_name in model_dict[task_mode]:
                if task_mode == 'regression' and model_name in ['svm', 'gradient_boosting']:
                    model = MultiOutputRegressor(model_dict[task_mode][model_name]())
                else:
                    model = model_dict[task_mode][model_name]()
            else:
                raise ValueError('Not valid model name')
        else:
            raise ValueError('Not valid task mode')
        return model

    def fit(self, data, target):
        self.model.fit(data, target)
        return

    def predict(self, data):
        if self.task_mode == 'regression':
            output = self.model.predict(data)
        elif self.task_mode == 'classification':
            output = self.model.predict_log_proba(data)
        else:
            raise ValueError('Not valid task name')
        return output
