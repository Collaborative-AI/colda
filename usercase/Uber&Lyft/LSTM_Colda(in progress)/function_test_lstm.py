# %%
from operator import index
from random import shuffle
import torch
from torch.utils.data import Dataset,DataLoader
import pandas as pd
from sklearn.model_selection import train_test_split
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import os
import numpy as np
from torchmetrics import R2Score
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import torch
from torch.autograd import Variable
from torch import nn
from sklearn.metrics import mean_squared_error



from my_model_test import LSTMModel
from my_model_test import SequenceDataset


print("import success")
data = pd.read_csv('sponsor_train.csv')
target_sensor= 'price'
features = list(data.columns.difference([target_sensor]))
target = data['price']

print("target.shape")
print(target.shape)


data = data.loc[:, features]
print("data.shape")
print(data.shape)


train_dataset = SequenceDataset(data,target)
print("SequenceDataset success")

train_loader = DataLoader(train_dataset, batch_size=96*5, shuffle=False)
print("DataLoader success")
# exit()
# test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
sample = torch.randn(data.shape[1])  # Create a random input sample



# %%
learning_rate = 0.01
num_hidden_units = 265

model = LSTMModel(num_sensors=58, hidden_units=num_hidden_units)
model.fit(train_loader, epochs=10, lr=0.01)

sample = torch.randn(data.shape[1])  # Create a random input sample
prediction = model.predict(sample)
print(f"Predicted price: {prediction:.2f}")

# %%
