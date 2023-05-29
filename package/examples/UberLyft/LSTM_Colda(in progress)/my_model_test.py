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
        h0 = torch.zeros(self.num_layers, batch_size, self.hidden_units).to(device)
        c0 = torch.zeros(self.num_layers, batch_size, self.hidden_units).to(device)

        _, (hn, _) = self.lstm(x, (h0, c0))
        out = self.linear(hn[0]).flatten()  # First dim of Hn is num_layers, which is set to 1 above.

        return out
    
    def fit(self, train_loader, epochs=1, lr=0.01):
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        loss_function = nn.MSELoss().to(device)
        optimizer = torch.optim.Adam(self.parameters(), lr=lr)
        
        for ix_epoch in range(epochs):
            print(f"Epoch {ix_epoch}\n---------")
            self.train()
            num_batches = len(train_loader)
            total_loss = 0
            
            for X, y in train_loader:
                X = X.to(device)
                y = y.to(device)
                output = self(X)
                loss = loss_function(output, y)

                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

                total_loss += loss.item()

            avg_loss = total_loss / num_batches
            print(f"Train loss: {avg_loss}")
    
    def predict(self, x):
        # Validate input data
        if not isinstance(x, (np.ndarray, torch.Tensor)):
            raise TypeError("Input must be either a NumPy array or a PyTorch Tensor.")
        
        # Convert NumPy arrays to PyTorch tensors
        if isinstance(x, np.ndarray): 
            x = torch.from_numpy(x)
            
        # Move the input data to the correct device, either CPU or GPU
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.eval()
        # Turn off gradient calculation to speed up computation
        with torch.no_grad():
            # Reshape input to include batch size
            x = x.unsqueeze(0).unsqueeze(0)
            x = x.to(device)
            output = self(x)
            return output.item()



class SequenceDataset(Dataset):
    def __init__(self, dataframe_x,dataframe_y, sequence_length=96*5):

        self.sequence_length = sequence_length
        self.y = torch.tensor(dataframe_y.values).float()
        self.X = torch.tensor(dataframe_x.values).float()

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