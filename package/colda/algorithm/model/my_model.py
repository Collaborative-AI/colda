import torch 
import torch.nn as nn
import numpy as np
from torch.utils.data import Dataset,DataLoader


class LSTMModel(nn.Module):
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
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        # device = 'cpu'
        h0 = torch.zeros(self.num_layers, batch_size, self.hidden_units).to(device)
        c0 = torch.zeros(self.num_layers, batch_size, self.hidden_units).to(device)
        
            
        _, (hn, _) = self.lstm(x, (h0, c0))
        out = self.linear(hn[0]).flatten()  # First dim of Hn is num_layers, which is set to 1 above.

        return out
    
    
    
    # def test(self, test_loader):
    #     print("=======\ninside test function\n=======")
        
    #     device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    #     loss_function = nn.MSELoss().to(device)
        

    #     total_loss = 0
    #     # model evaluation mode
    #     self.eval()
    #     num_batches = len(test_loader)
        
    #     for X, y in test_loader:
    #         X = X.to(device)
    #         y = y.to(device)
    #         print(X.shape)
    #         output = self(X)
    #         total_loss += loss_function(output, y)

    #     avg_loss = total_loss / num_batches
    #     print(f"Train loss: {avg_loss}")
            
                
    def fit(self, train_loader, epochs=10, lr=0.1):
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        # device = 'cpu'
        self.to(device)
        
        print("=======\ninside fitting function using\n=======")
        
        loss_function = nn.MSELoss()
        optimizer = torch.optim.Adam(self.parameters(), lr=lr)

        
        num_batches = len(train_loader)
        self.train()
        for ix_epoch in range(epochs):
            print(f"Epoch {ix_epoch} ---------")
            total_loss = 0
            
            for X, y in train_loader:
                X = X.to(device)
                y = y.to(device)
                output = self(X)
                # check the shape of output
                # if output.shape == y.shape:
                #     continue
                # else:
                #     print("got messed up shape")
                #     print(output.shape)
                #     print(y.shape)
                #     output = output.view(len(output))
                #     y = y.view(len(y))
                
                loss = loss_function(output, y)

                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

                total_loss += loss.item()

            avg_loss = total_loss / num_batches
            print(f"Train loss: {avg_loss}")
    
    def lstm_predict(self, test_dataloader):
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        # device = 'cpu'
        
        
        self.eval()
        predictions = torch.tensor([])
        predictions = predictions.to(device)
        
        with torch.no_grad():
            for X in test_dataloader:
                X = X.to(device)
                y_star = self(X)
                predictions = torch.cat((predictions, y_star), 0)
        
        predictions = predictions.cpu().numpy()        
        
        
        return predictions
        
   



class SequenceDataset(Dataset):
    def __init__(self, sequence_length, dataframe_x, dataframe_y = None):

        self.sequence_length = sequence_length
        # dataframe_y = dataframe_y.to_numpy()
        # print(dataframe_x.type)/
        # print(dataframe_y.type)
        # self.y = torch.tensor(dataframe_y).float()
        if dataframe_y is not None:
            self.y = torch.tensor(dataframe_y.astype(np.float32))
        else:
            self.y = None
        self.X = torch.tensor(dataframe_x.astype(np.float32))

        # self.X = torch.tensor(dataframe_x).float()

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
        
        if self.y is not None:
            return x, self.y[i]
        else:
            return x


# class SequenceDataset(Dataset):
#     def __init__(self, dataframe_x,dataframe_y = None, sequence_length=96*5):
#         self.sequence_length = sequence_length
#         self.y = torch.tensor(dataframe_y.astype(np.float32))
#         self.X = torch.tensor(dataframe_x.astype(np.float32))

#     def __len__(self):
#         return self.X.shape[0]

#     def __getitem__(self, i): 
#         if i >= self.sequence_length - 1:
#             i_start = i - self.sequence_length + 1
#             x = self.X[i_start:(i + 1), :]
#         else:
#             padding = self.X[0].repeat(self.sequence_length - i - 1, 1)
#             x = self.X[0:(i + 1), :]
#             x = torch.cat((padding, x), 0)

#         return x, self.y[i]


def SequenceDataset_handeler(dataset,target_dataset=None):
    target = 'price'
    sequence_length = 96*5
    batch_size = 96
    if target_dataset is None:
        dataloader_pre = SequenceDataset(sequence_length,dataset)
    else:
        dataloader_pre = SequenceDataset(sequence_length,dataset,target_dataset)
        
    return DataLoader(dataloader_pre, batch_size=batch_size, shuffle=False)
    