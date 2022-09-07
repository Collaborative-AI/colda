# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt # plotting
import sys
import os
import numpy as np
from random import sample
import torch
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, f1_score, accuracy_score, classification_report
from torch.utils.data.dataset import Dataset
import time
import glob
import pandas as pd

dataset = pd.read_csv('../input/clean_cab.csv')
# dataset['price'].fillna(0, inplace=True)
# dataset.drop('product_id', axis=1, inplace=True) 
dataset.head(10)
# %%
hitmapTemp = dataset[list(dataset.columns)]
hitmapData = hitmapTemp.corr()
sns.heatmap(hitmapData, vmax=1, square=True, annot=True)

plt.xticks(rotation=-70)
plt.yticks(rotation=20)
plt.show()






# %%
dataset = dataset.sort_values('time_stamp')
# dataset.drop(dataset['time_stamp'])
dataset.drop('time_stamp', axis=1, inplace=True) 

dataset.head(10)
# dataset.set_index('time_stamp', inplace=True)?

dataset.head(10)


df_id = dataset.id
df = dataset.drop('id',axis=1)
df.insert(0,'id',df_id)

# %%
cols = list(dataset)[0:6]

# cols.remove("time_stamp")
# datelist_train = list(dataset['Date'])

print('Featured selected: {}'.format(cols))
# print(cols)

# %%
print(dataset.shape)
dataset = dataset.head(5000)


dataset_train = dataset[cols].astype(str)

print(dataset_train['name'])
# %%
# for i in cols:
#     for j in range(0, len(dataset_train)):
#         print(dataset_train[i][j])
#         # dataset_train[i][j] = dataset_train[i][j].replace(',', '')

dataset_train = dataset_train.astype(float)

# Using multiple features (predictors)
# print(dataset_train)
training_set = dataset_train.values

print('Shape of training set == {}.'.format(training_set.shape))
# Feature Scaling
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
training_set_scaled = sc.fit_transform(training_set)

sc_predict = StandardScaler()
sc_predict.fit_transform(training_set[:, 0:1])


# %%


# Creating a data structure with 90 timestamps and 1 output
X_train = []
y_train = []

n_future = 60   # Number of days we want top predict into the future
n_past = 90     # Number of past days we want to use to predict the future
# print(training_set_scaled[:][:-1])
# print("\n")
# print(training_set_scaled[:][:])
print(training_set_scaled)
print("\n")
print(training_set_scaled[1:3, 0:4])


for i in range(n_past, len(training_set_scaled) - n_future +1):
    # print(i)
    X_train.append(training_set_scaled[i - n_past:i, 0:dataset_train.shape[1] - 1])
    y_train.append(training_set_scaled[i + n_future - 1:i + n_future, 0])

X_train, y_train = np.array(X_train), np.array(y_train)

print('X_train shape == {}.'.format(X_train.shape))
print('y_train shape == {}.'.format(y_train.shape))

print(y_train)
