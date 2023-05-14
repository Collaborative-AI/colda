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
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

indicator = 1

rides_df = pd.read_csv('input/cab_rides.csv')
weather_df = pd.read_csv('input/weather.csv')

rides_df.isnull().sum()
# remove these rows where the price is not present
rides_df.dropna(axis = 0 , inplace = True)
rides_df.isnull().sum()
weather_df.isnull().sum()


#rain not happening
weather_df.fillna(0 ,inplace = True)
weather_df.isnull().sum()
#take average of all values  based on place /locations
# %%
weather_avg = weather_df.groupby('location').mean().reset_index()

#no need for time stamp here as it does not tell anything 
weather_avg.drop(columns = 'time_stamp' , inplace = True)

weather_source = weather_avg.rename(columns =(lambda x :x+'_source'))       
weather_source.rename(columns= {'location_source' :'source'} ,inplace = True)

weather_destination = weather_avg.rename(columns =(lambda x :x+'_destination'))       
weather_destination.rename(columns= {'location_destination' :'destination'} ,inplace = True)


# %%
data = rides_df\
       .merge(weather_source ,on ='source')\
       .merge(weather_destination ,on = 'destination')
       

# %%
cat_data =data.select_dtypes('object').columns.tolist()
for cat in cat_data:
    print('category : ' ,cat)
    print(data[cat].value_counts())
    print('\n')
 #removing id columns as it is useless 
data = data.drop('id'  , axis =1)

#binary encoding to cab_type

data['cab_type'] =data['cab_type'].replace({'Uber':1,'Lyft':0})
data['cab_type'].value_counts()

def one_hot_encode(df , column , prefix):
    dummy = pd.get_dummies(df[column] ,prefix = prefix)
    df = pd.concat([df , dummy] ,axis =1)
    df =df.drop(column , axis =1)
    
    return df

data = one_hot_encode(data ,column =  'destination' , prefix = 'desti')
data = one_hot_encode(data ,column =  'source' , prefix = 'src')
data = one_hot_encode(data ,column =  'product_id' , prefix = 'pid')
data = one_hot_encode(data ,column =  'name' , prefix = 'nm')



# %%
data.select_dtypes('object').columns
data.shape
x = data.drop('price',axis =1)
y = data['price']
data = data.drop('pid_55c66225-fbe7-4fd5-9072-eab1ece5e23e',axis=1)
data = data.drop('pid_6c84fd89-3f11-4782-9b50-97c468b19529',axis=1)
data = data.drop('pid_6d318bcc-22a3-4af6-bddd-b409bfce1546',axis=1)
data = data.drop( 'pid_6f72dfc5-27f1-42e8-84db-ccc7a75f6969',axis=1)
data = data.drop('pid_997acbb5-e102-41e1-b155-9df7de0a73f2',axis=1)
data = data.drop('pid_9a0e7b09-b92b-4c41-9779-2ad22b4d779d', axis=1)
print(data.columns)
print(x.shape ,y.shape)

# %%
data = data.sort_values(by='time_stamp', ascending=True)
df_train, df_test = train_test_split(data, test_size=0.2,shuffle=False)
data = data.set_index('time_stamp')
test_start = '2018-12-15 17:10:05.354'

df_test['time_stamp'] = pd.to_datetime(df_test['time_stamp'], unit='ms')
df_train['time_stamp'] = pd.to_datetime(df_train['time_stamp'], unit='ms')
# cab_rides['timestamp'] = pd.to_datetime(cab_rides['time_stamp'], unit='ms')


# 2018-12-15 11:15:09.125000
# %%

print("Test set fraction:", len(df_test) / len(data))

# create the window for the shifting 

target_sensor = "price"
features = list(data.columns.difference([target_sensor]))
print(features)
forecast_lead = 96*2*2
target = f"{target_sensor}"

data[target] = data[target_sensor].shift(-forecast_lead)
print(data.shape)
df = data.iloc[:-forecast_lead]
print(df.shape)



target_mean = df_train[target].mean()
target_stdev = df_train[target].std()

for c in df_train.columns:
    if c != 'price':
    
        print(c)
        mean = df_train[c].mean()
        stdev = df_train[c].std()
        df_train[c] = (df_train[c] - mean) / stdev
        df_test[c] = (df_test[c] - mean) / stdev
        
print(df_train)
print(df_test)
# One elegant way to do this is to create a PyTorch Dataset class, which is simpler than you might think. This strategy lets us lean on PyTorch's nice DataLoader class to keep the model training and evaluation code super clean.

# Our custom Dataset just needs to specify what happens when somebody requests the i'th element of the dataset. In a tabular dataset, this would be the i'th row of the table, but here we need to retrieve a sequence of rows.



class SequenceDataset(Dataset):
    def __init__(self, dataframe, target, features, sequence_length=96*5):
        self.features = features
        self.target = target
        self.sequence_length = sequence_length
        self.y = torch.tensor(dataframe[target].values).float()
        self.X = torch.tensor(dataframe[features].values).float()

    def __len__(self):
        return self.X.shape[0]

    def __getitem__(self, i): 
        if i >= self.sequence_length - 1:
            i_start = i - self.sequence_length + 1
            x = self.X[i_start:(i + 1), :]
        else:
            padding = self.X[0].repeat(self.sequence_length - i - 1, 1)
            x = self.X[0:(i + 1), :]
            x = torch.cat((padding, x), 0)

        return x, self.y[i]

torch.manual_seed(101)

batch_size = 96*5
sequence_length = 96

train_dataset = SequenceDataset(
    df_train,
    target=target,
    features=features,
    sequence_length=sequence_length
)
test_dataset = SequenceDataset(
    df_test,
    target=target,
    features=features,
    sequence_length=sequence_length
)


train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=False)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

X, y = next(iter(train_loader))

print("Features shape:", X.shape)
print("Target shape:", y.shape)
# %%

from torch import nn

class LSTM(nn.Module):
    def __init__(self, num_sensors, hidden_units):
        super().__init__()
        self.num_sensors = num_sensors  # this is the number of features
        self.hidden_units = hidden_units
        self.num_layers = 1

        self.lstm = nn.LSTM(
            input_size=num_sensors,
            hidden_size=hidden_units,
            batch_first=True,
            num_layers=self.num_layers
        )

        self.linear = nn.Linear(in_features=self.hidden_units, out_features=1)

    def forward(self, x):
        batch_size = x.shape[0]
        h0 = torch.zeros(self.num_layers, batch_size, self.hidden_units).to('cuda')
        c0 = torch.zeros(self.num_layers, batch_size, self.hidden_units).to('cuda')
        
        _, (hn, _) = self.lstm(x, (h0, c0))
        out = self.linear(hn[0]).flatten()  # First dim of Hn is num_layers, which is set to 1 above.

        return out


# %%
learning_rate = 0.01
num_hidden_units = 265

model = LSTM(num_sensors=len(features), hidden_units=num_hidden_units)
# loss_function = nn.CrossEntropyLoss().to('cuda')
loss_function = nn.MSELoss().to('cuda')

optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
# %%
model = model.to('cuda')


def train_model(data_loader, model, loss_function, optimizer):
    num_batches = len(data_loader)
    print(num_batches)
    total_loss = 0
    model.train()
    
    for X, y in data_loader:
        X = X.to('cuda')
        y = y.to('cuda')
        output = model(X)
        loss = loss_function(output, y)
        # print(loss)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    avg_loss = total_loss / num_batches
    print(f"Train loss: {avg_loss}")

def test_model(data_loader, model, loss_function):
    
    num_batches = len(data_loader)
    total_loss = 0

    model.eval()
    with torch.no_grad():
        for X, y in data_loader:
            X = X.to('cuda')
            y = y.to('cuda')            
            output = model(X)
            # output = output.detach().cpu().numpy()
            total_loss += loss_function(output, y).item()

    avg_loss = total_loss / num_batches
    print(f"Test loss: {avg_loss}")
# %%



print("Untrained test\n--------")
# modle = model.cuda()
# test_loader = test_loader.cuda()
# test_model(test_loader, model, loss_function)
print()
model = model.to('cuda')
Model_Dir = 'models/'
experiment_id = 'Oct6th_firsttimeTransferLRtoLSTM'
if indicator == 1:
    for ix_epoch in range(50):
        print(f"Epoch {ix_epoch}\n---------")
        train_model(train_loader, model, loss_function, optimizer=optimizer)
        test_model(test_loader, model, loss_function)
        torch.save(model.state_dict(), os.path.join(Model_Dir,str(experiment_id)+'.pt'))
        print()
# %%

model.load_state_dict(torch.load(os.path.join(Model_Dir, str(experiment_id)+".pt")))


def predict(data_loader, model):
    output = torch.tensor([])
    output = output.to('cuda')
    # model.eval()
    with torch.no_grad():
        for X, _ in data_loader:
            X = X.to('cuda')
            y_star = model(X)
            output = torch.cat((output, y_star), 0)
    
    return output
train_eval_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=False)
model.eval()


ystar_col = "Model forecast"
model = model.to("cuda")
df_train[ystar_col] = predict(train_eval_loader, model).detach().cpu().numpy()
df_test[ystar_col] = predict(test_loader, model).detach().cpu().numpy()

df_out = pd.concat((df_train, df_test))[[target, ystar_col]]

# for c in df_out.columns:
#     df_out[c] = df_out[c] * target_stdev + target_mean

print(df_out) 
preds = df_out['price']
target = df_out[ystar_col]
preds = preds.tolist()
preds = torch.tensor(preds)
target = target.tolist()
target = torch.tensor(target)
r2score = R2Score()
print(r2score(preds, target))
df_out.to_csv(experiment_id+'.csv')

# %%

pio.templates.default = "plotly_white"

plot_template = dict(
    layout=go.Layout({
        "font_size": 18,
        "xaxis_title_font_size": 24,
        "yaxis_title_font_size": 24})
)
fig = px.line(df_out, labels={'price', 'time_stamp'})
fig.add_vline(x=test_start, line_width=4, line_dash="dash")
fig.add_annotation(xref="paper", x=0.75, yref="paper", y=0.8, text="Test set start", showarrow=False)
fig.update_layout(
  template=plot_template, legend=dict(orientation='h', y=1.02, title_text="")
)
fig.show()
fig.write_image("forecast.png", width=1200, height=600)