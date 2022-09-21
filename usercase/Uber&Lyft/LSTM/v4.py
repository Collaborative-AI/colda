# %%

import torch
from torch.utils.data import Dataset,DataLoader
import pandas as pd
from sklearn.model_selection import train_test_split
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio


df = pd.read_csv("data.csv", index_col="time_stamp")

df_train, df_test = train_test_split(df, test_size=0.2,shuffle=False)

# %%
# handle target split point
# datelist = df_test.values.tolist()
test_start = '1544894109125'
# 2018-12-15 11:15:09.125000
# %%

print("Test set fraction:", len(df_test) / len(df))

# create the window for the shifting 

target_sensor = "price"
features = list(df.columns.difference([target_sensor]))
print(features)
forecast_lead = 5000
target = f"{target_sensor}"

df[target] = df[target_sensor].shift(-forecast_lead)
print(df.shape)
df = df.iloc[:-forecast_lead]
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
    def __init__(self, dataframe, target, features, sequence_length=2000):
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





# %%
torch.manual_seed(101)

batch_size = 6000
sequence_length = 500

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
learning_rate = 0.0001
num_hidden_units = 265
testround = 1
model = LSTM(num_sensors=len(features), hidden_units=num_hidden_units)
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
        print(loss)

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

for ix_epoch in range(testround):
    print(f"Epoch {ix_epoch}\n---------")
    train_model(train_loader, model, loss_function, optimizer=optimizer)
    test_model(test_loader, model, loss_function)
    print()
# %%
def predict(data_loader, model):
    output = torch.tensor([])
    output = output.to('cuda')
    # model.eval()
    with torch.no_grad():
        for X, _ in data_loader:
            X = X.to('cuda')
            y_star = model(X)
            print(y_star)
            output = torch.cat((output, y_star), 0)
    
    return output
# %%
train_eval_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=False)
model.eval()


ystar_col = "Model forecast"
model = model.to("cuda")
df_train[ystar_col] = predict(train_eval_loader, model).detach().cpu().numpy()
df_test[ystar_col] = predict(test_loader, model).detach().cpu().numpy()

df_out = pd.concat((df_train, df_test))[[target, ystar_col]]

for c in df_out.columns:
    df_out[c] = df_out[c] * target_stdev + target_mean

print(df_out)
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