# %%

import sys
sys.path.append('../../../')


from colda.algorithm.model.my_model import LSTMModel,SequenceDataset_handeler
from colda.algorithm.metric.metrics import MAD,RMSE,R2
import pandas as pd

train_data = pd.read_csv('lstm_dataset/0/sponsor_train.csv')
train_data = train_data.set_index('id')


test_data = pd.read_csv('lstm_dataset/0/sponsor_test.csv')
test_data = test_data.set_index('id')


train_data_x = train_data.drop(['price'],axis=1)
train_data_y = train_data['price']


test_data_x = test_data.drop(['price'],axis=1)
test_data_y = test_data['price']

# %%

train_data_x = train_data_x.to_numpy()
train_data_y = train_data_y.to_numpy()
train_data_loader = SequenceDataset_handeler(train_data_x,train_data_y)

test_data_x = test_data_x.to_numpy()
test_data_loader = SequenceDataset_handeler(test_data_x)



# %%
model = LSTMModel(num_sensors=57, hidden_units=8)
model.fit(train_data_loader, epochs=20, lr=0.001)

ouput = model.lstm_predict(test_data_loader)

test_data_y = test_data_y.to_numpy()
print("Sponsor Single, LSTM, Uber&Lyft")
print("MAD: ",MAD(ouput,test_data_y))
print("RMSE: ",RMSE(ouput,test_data_y))
print("R2: ",R2(ouput,test_data_y))


# %%
