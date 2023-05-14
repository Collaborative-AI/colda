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
import datetime as dt
from datetime import datetime
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.callbacks import ReduceLROnPlateau
from keras.callbacks import TensorBoard
from datetime import datetime
from dateutil import parser
import time


dataset = pd.read_csv('../input/clean_cab_new.csv')

# dataset['price'].fillna(0, inplace=True)
# dataset.drop('product_id', axis=1, inplace=True) 
dataset.head(10)
# %%


# %%


# %%
dataset = dataset.sort_values('time_stamp')

timeseries_converting  = dataset['time_stamp']


# dataset.head(10)
# timeseries_converting.head(10)
# d = datetime.fromtimestamp(1543203646318 / 1000.0)
# print(d)
# %%
# unix_timestamp = float(timeseries_converting)
# readabel_time = int(str(timeseries_converting))


def convert_date(orig_date):
    # orig_date = datetime(x,y,z)
    orig_date = str(orig_date)
    d = datetime.strptime(orig_date, '%Y-%m-%d %H:%M:%S')
    d = d.strftime('%m/%d/%y')
    return d
count = 0
datelist = []
for i,date in enumerate(timeseries_converting):
    d = datetime.fromtimestamp(date / 1000.0)
    # print(d)
    d = str(d)
    if len(d) != 26:
        # print(len(d))
        d = d+'.0'
    # while d!= 26:
    #     d = d+'0'
    datelist.append(d)
datelist_train = datelist.copy()




datelist_train = [dt.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f").date() for date in datelist_train]
print('All timestamps == {}'.format(len(datelist_train)))


# dataset.drop(dataset['time_stamp'])
dataset.drop('time_stamp', axis=1, inplace=True) 

dataset.head(10)



# %%
cols = list(dataset)[0:7]

cols.remove('Unnamed: 0')
# datelist_train = list(dataset['Date'])

print('Featured selected: {}'.format(cols))
# print(cols)

# %%
# print(dataset.shape)
# dataset = dataset.head(5000)


dataset_train = dataset[cols].astype(str)

# %%
# for i in cols:
#     for j in range(0, len(dataset_train)):
#         print(dataset_train[i][j])
#         # dataset_train[i][j] = dataset_train[i][j].replace(',', '')

dataset_train = dataset_train.astype(float)

# Using multiple features (predictors)
print(dataset_train)

# %%
training_set = dataset_train.values

print('Shape of training set == {}.'.format(training_set.shape))
# Feature Scaling
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
training_set_scaled = sc.fit_transform(training_set)

sc_predict = StandardScaler()
sc_predict.fit_transform(training_set[:, 0:1])


# %%

test = set(datelist_train)
print(test)

# %%
# Creating a data structure with 90 timestamps and 1 output
X_train = []
y_train = []

n_future = 6   # Number of days we want top predict into the future
n_past = 12     # Number of past days we want to use to predict the future
# print(training_set_scaled[:][:-1])
# print("\n")
# print(training_set_scaled[:][:])
print(training_set_scaled)
print("\n")


for i in range(n_past, len(training_set_scaled) - n_future +1):
    # print(i)
    X_train.append(training_set_scaled[i - n_past:i, 0:dataset_train.shape[1] - 1])
    y_train.append(training_set_scaled[i + n_future - 1:i + n_future, 0])

X_train, y_train = np.array(X_train), np.array(y_train)

print('X_train shape == {}.'.format(X_train.shape))
print('y_train shape == {}.'.format(y_train.shape))

# print(y_train)

plt.plot(y_train)
# %%


# begin to train


es = EarlyStopping(monitor='val_loss', min_delta=1e-10, patience=10, verbose=1)
rlr = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=10, verbose=1)
mcp = ModelCheckpoint(filepath='weights.h5', monitor='val_loss', verbose=1, save_best_only=True, save_weights_only=True)

tb = TensorBoard('logs')



# Initializing the Neural Network based on LSTM
model = Sequential()

# Adding 1st LSTM layer
model.add(LSTM(units=64, return_sequences=True, input_shape=(n_past, dataset_train.shape[1]-1)))

# Adding 2nd LSTM layer
model.add(LSTM(units=10, return_sequences=False))

# Adding Dropout
model.add(Dropout(0.25))

# Output layer
model.add(Dense(units=1, activation='linear'))

# Compiling the Neural Network
model.compile(optimizer = Adam(learning_rate=0.01), loss='mean_squared_error')

# %%
history = model.fit(X_train, y_train, shuffle=True, epochs=100, callbacks=[es, rlr, mcp, tb], validation_split=0.2, verbose=1, batch_size=256)

# %%

# Generate list of sequence of days for predictions
datelist_future = pd.date_range(datelist_train[-1], periods=n_future, freq='1d').tolist()

'''
Remeber, we have datelist_train from begining.
'''

# Convert Pandas Timestamp to Datetime object (for transformation) --> FUTURE
datelist_future_ = []
for this_timestamp in datelist_future:
    datelist_future_.append(this_timestamp.date())


# Perform predictions
predictions_future = model.predict(X_train[-n_future:])

predictions_train = model.predict(X_train[n_past:])

# Inverse the predictions to original measurements

# ---> Special function: convert <datetime.date> to <Timestamp>
def datetime_to_timestamp(x):
    '''
        x : a given datetime value (datetime.date)
    '''
    return datetime.strptime(x.strftime('%Y%m%d'), '%Y%m%d')


y_pred_future = sc_predict.inverse_transform(predictions_future)
y_pred_train = sc_predict.inverse_transform(predictions_train)

PREDICTIONS_FUTURE = pd.DataFrame(y_pred_future, columns=['price']).set_index(pd.Series(datelist_future))
PREDICTION_TRAIN = pd.DataFrame(y_pred_train, columns=['price']).set_index(pd.Series(datelist_train[2 * n_past + n_future -1:]))

# Convert <datetime.date> to <Timestamp> for PREDCITION_TRAIN
PREDICTION_TRAIN.index = PREDICTION_TRAIN.index.to_series().apply(datetime_to_timestamp)


# %%


# Set plot size 
from pylab import rcParams
rcParams['figure.figsize'] = 14, 5

# Plot parameters
START_DATE_FOR_PLOTTING = '2018-11-25'

plt.plot(PREDICTIONS_FUTURE.index, PREDICTIONS_FUTURE['price'], color='r', label='Predicted Uber&Lyft Price')
plt.plot(PREDICTION_TRAIN.loc[START_DATE_FOR_PLOTTING:].index, PREDICTION_TRAIN.loc[START_DATE_FOR_PLOTTING:]['price'], color='orange', label='Training predictions')
plt.plot(dataset_train.loc[START_DATE_FOR_PLOTTING:].index, dataset_train.loc[START_DATE_FOR_PLOTTING:]['price'], color='b', label='Uber&Lyft Stock Price')

plt.axvline(x = min(PREDICTIONS_FUTURE.index), color='green', linewidth=2, linestyle='--')

plt.grid(which='major', color='#cccccc', alpha=0.5)

plt.legend(shadow=True)
plt.title('Predcitions and Acutal Uber&Lyft Prices', family='Arial', fontsize=12)
plt.xlabel('Timeline', family='Arial', fontsize=10)
plt.ylabel('Uber&Lyft Price Value', family='Arial', fontsize=10)
plt.xticks(rotation=45, fontsize=8)



# Parse training set timestamp for better visualization
dataset_train = pd.DataFrame(dataset_train, columns=cols)
dataset_train.index = datelist_train
dataset_train.index = pd.to_datetime(dataset_train.index)
# %%

dataset_train.head(10)
print(X_train)
print(y_train)
# plt.plot(X_train)
plt.plot(y_train)


plt.savefig("test.png")
# %%
