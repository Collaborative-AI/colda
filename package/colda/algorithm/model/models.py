from __future__ import annotations

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
from colda.algorithm.model.base import BaseModel
from typeguard import typechecked

from sklearn.multioutput import MultiOutputRegressor
from colda._typing import (
    Task_Mode,
    Metric_Name,
    Model_Name
)


import pandas as pd
import torch
import numpy as np
from .my_model import LSTMModel
from .my_model import SequenceDataset_handeler





class Model(BaseModel):
    def __init__(
        self, 
        task_mode: Task_Mode, 
        model_name: Model_Name
    ) -> None:
        self.task_mode = task_mode
        self.model_name = model_name
        self.model = self.make_model(self.task_mode, self.model_name)
        
    def make_model(
        self, 
        task_mode: Task_Mode, 
        model_name: Model_Name
    ) -> object:
        model_dict = {
            'regression': {
                'linear': LinearRegression, 
                'decision_tree': DecisionTreeRegressor,
                'svm': SVR, 
                'gradient_boosting': GradientBoostingRegressor, 
                'mlp': MLPRegressor,
                'lstm': LSTMModel
            },
            'classification': {
                'linear': LogisticRegression, 
                'decision_tree': DecisionTreeClassifier,
                'svm': SVC, 
                'gradient_boosting': GradientBoostingClassifier,
                'mlp': MLPClassifier
            }
        }
        print("stage of making model")
        if task_mode in model_dict:
            if model_name in model_dict[task_mode]:
                if task_mode == "regression":
                    if model_name == "lstm":
                        print("current model is LSTM")
                        model = LSTMModel(num_sensors=57, hidden_units=8)
                    elif model_name in ['svm', 'gradient_boosting']:
                        model = MultiOutputRegressor(model_dict[task_mode][model_name]())
                    else:
                        model = model_dict[task_mode][model_name]()
                else:
                    model = model_dict[task_mode][model_name]()
            else:
                raise ValueError('Not valid model name')
        else:
            raise ValueError('Not valid task mode')
        return model

    def fit(
        self, 
        data, 
        target
    ) -> None:
        if self.model_name == 'lstm':
            print("=======\n LSTM fitting begined\n=======")
            train_loader = SequenceDataset_handeler(data,target)
            self.model.fit(train_loader, epochs=10, lr=0.001)

            return
        else:
            self.model.fit(data, target)
        return
    
    '''
    situation 1:
        predict(data) invoke in the ski-learn package model.predict
    
    situation 2:
        predict(data,target) invoke LSTM_self_defined
    '''
    def predict(
        self, 
        data,
        target = None
    ) -> None:
        if self.task_mode == 'regression':
            if self.model_name == 'lstm':
                test_dataloader = SequenceDataset_handeler(data)
                output_lstm = self.model.lstm_predict(test_dataloader)                                
                return output_lstm
            '''
            Here'model.predict' and 'model.predict_log_proba' 
                is not model.predict in the other package place
                predict is a method available in most scikit-learn models, 
                both for regression and classification tasks. This method 
                returns the predicted output for a given input dataset. 
                The output depends on the type of problem:
                
                y_pred_c = classifier.predict(X_test_c)
                
                For regression tasks, it returns the predicted continuous values.
                For classification tasks, it returns the predicted class labels.
            '''
            if target is None:
                output = self.model.predict(data)
        elif self.task_mode == 'classification' and (target is None):
            output = self.model.predict_log_proba(data)
        else:
            raise ValueError('Not valid task name')
        return output
