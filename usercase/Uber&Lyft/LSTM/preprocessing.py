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
import random
import numpy as np
import torch

# multivariate data preparation
from numpy import array
from numpy import hstack
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
# %%

traindata = []
testdata  = []

 
# # split a multivariate sequence into samples
# def split_sequences(sequences, n_steps):
#     X, y = list(), list()
#     for i in range(len(sequences)):
#         # find the end of this pattern
#         end_ix = i + n_steps
#         # check if we are beyond the dataset
#         if end_ix > len(sequences):
#             break
#         # gather input and output parts of the pattern
#         seq_x, seq_y = sequences[i:end_ix, :-1], sequences[end_ix-1, -1]
#         X.append(seq_x)
#         y.append(seq_y)
#     return array(X), array(y)
 
# # define input sequence
# in_seq1 = array([x for x in range(0,100,10)])
# in_seq2 = array([x for x in range(5,105,10)])
# out_seq = array([in_seq1[i]+in_seq2[i] for i in range(len(in_seq1))])
# # convert to [rows, columns] structure
# in_seq1 = in_seq1.reshape((len(in_seq1), 1))
# in_seq2 = in_seq2.reshape((len(in_seq2), 1))
# out_seq = out_seq.reshape((len(out_seq), 1))
# # horizontally stack columns
# dataset = hstack((in_seq1, in_seq2, out_seq))
# # plt.plot(dataset["price"])
# # %%
# # model
# class MV_LSTM(torch.nn.Module):
#     def __init__(self,n_features,seq_length):
#         super(MV_LSTM, self).__init__()
#         self.n_features = n_features
#         self.seq_len = seq_length
#         self.n_hidden = 20 # number of hidden states
#         self.n_layers = 1 # number of LSTM layers (stacked)
    
#         self.l_lstm = torch.nn.LSTM(input_size = n_features, 
#                                  hidden_size = self.n_hidden,
#                                  num_layers = self.n_layers, 
#                                  batch_first = True)
#         # according to pytorch docs LSTM output is 
#         # (batch_size,seq_len, num_directions * hidden_size)
#         # when considering batch_first = True
#         self.l_linear = torch.nn.Linear(self.n_hidden*self.seq_len, 1)
        
    
#     def init_hidden(self, batch_size):
#         # even with batch_first = True this remains same as docs
#         hidden_state = torch.zeros(self.n_layers,batch_size,self.n_hidden)
#         cell_state = torch.zeros(self.n_layers,batch_size,self.n_hidden)
#         self.hidden = (hidden_state, cell_state)
    
    
#     def forward(self, x):        
#         batch_size, seq_len, _ = x.size()
        
#         lstm_out, self.hidden = self.l_lstm(x,self.hidden)
#         # lstm_out(with batch_first = True) is 
#         # (batch_size,seq_len,num_directions * hidden_size)
#         # for following linear layer we want to keep batch_size dimension and merge rest       
#         # .contiguous() -> solves tensor compatibility error
#         x = lstm_out.contiguous().view(batch_size,-1)
#         return self.l_linear(x)


# n_features = 2 # this is number of parallel inputs
# n_timesteps = 3 # this is number of timesteps

# # convert dataset into input/output
# X, y = split_sequences(dataset, n_timesteps)
# print(X.shape, y.shape)

# # create NN
# mv_net = MV_LSTM(n_features,n_timesteps)
# criterion = torch.nn.MSELoss() # reduction='sum' created huge loss value
# optimizer = torch.optim.Adam(mv_net.parameters(), lr=1e-1)

# train_episodes = 500
# batch_size = 16


# mv_net.train()
# for t in range(train_episodes):
#     for b in range(0,len(X),batch_size):
#         inpt = X[b:b+batch_size,:,:]
#         target = y[b:b+batch_size]    
        
#         x_batch = torch.tensor(inpt,dtype=torch.float32)    
#         y_batch = torch.tensor(target,dtype=torch.float32)
    
#         mv_net.init_hidden(x_batch.size(0))
#     #    lstm_out, _ = mv_net.l_lstm(x_batch,nnet.hidden)    
#     #    lstm_out.contiguous().view(x_batch.size(0),-1)
#         output = mv_net(x_batch) 
#         loss = criterion(output.view(-1), y_batch)  
        
#         loss.backward()
#         optimizer.step()        
#         optimizer.zero_grad() 
#     print('step : ' , t , 'loss : ' , loss.item())
    
    
# Import Libraries and packages from Keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
from keras.optimizers import Adam

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


es = EarlyStopping(monitor='val_loss', min_delta=1e-10, patience=10, verbose=1)
rlr = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=10, verbose=1)
mcp = ModelCheckpoint(filepath='weights.h5', monitor='val_loss', verbose=1, save_best_only=True, save_weights_only=True)

tb = TensorBoard('logs')

history = model.fit(X_train, y_train, shuffle=True, epochs=30, callbacks=[es, rlr, mcp, tb], validation_split=0.2, verbose=1, batch_size=256)