# %%
from attr import dataclass
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt # plotting
import numpy as np # linear algebra
import os # accessing directory structure
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os 
import colda

# from datetime import datetime
from datetime import datetime
# Distribution graphs (histogram/bar graph) of column data
def plotPerColumnDistribution(df, nGraphShown, nGraphPerRow):
    nunique = df.nunique()
    df = df[[col for col in df if nunique[col] > 1 and nunique[col] < 50]] # For displaying purposes, pick columns that have between 1 and 50 unique values
    nRow, nCol = df.shape
    columnNames = list(df)
    nGraphRow = (nCol + nGraphPerRow - 1) / nGraphPerRow
    nGraphRow = int(nGraphRow)
    plt.figure(num = None, figsize = (6 * nGraphPerRow, 8 * nGraphRow), dpi = 80, facecolor = 'w', edgecolor = 'k')
    for i in range(min(nCol, nGraphShown)):
        plt.subplot(nGraphRow, nGraphPerRow, i + 1)
        columnDf = df.iloc[:, i]
        if (not np.issubdtype(type(columnDf.iloc[0]), np.number)):
            valueCounts = columnDf.value_counts()
            valueCounts.plot.bar()
        else:
            columnDf.hist()
        plt.ylabel('counts')
        plt.xticks(rotation = 90)
        plt.title(f'{columnNames[i]} (column {i})')
    plt.tight_layout(pad = 1.0, w_pad = 1.0, h_pad = 1.0)
    plt.show()



# Correlation matrix
def plotCorrelationMatrix(df, graphWidth):
    filename = df.dataframeName
    df = df.dropna('columns') # drop columns with NaN
    df = df[[col for col in df if df[col].nunique() > 1]] # keep columns where there are more than 1 unique values
    if df.shape[1] < 2:
        print(f'No correlation plots shown: The number of non-NaN or constant columns ({df.shape[1]}) is less than 2')
        return
    corr = df.corr()
    plt.figure(num=None, figsize=(graphWidth, graphWidth), dpi=80, facecolor='w', edgecolor='k')
    corrMat = plt.matshow(corr, fignum = 1)
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.gca().xaxis.tick_bottom()
    plt.colorbar(corrMat)
    plt.title(f'Correlation Matrix for {filename}', fontsize=15)
    plt.show()
    
# Scatter and density plots
def plotScatterMatrix(df, plotSize, textSize):
    df = df.select_dtypes(include =[np.number]) # keep only numerical columns
    # Remove rows and columns that would lead to df being singular
    df = df.dropna('columns')
    df = df[[col for col in df if df[col].nunique() > 1]] # keep columns where there are more than 1 unique values
    columnNames = list(df)
    if len(columnNames) > 10: # reduce the number of columns for matrix inversion of kernel density plots
        columnNames = columnNames[:10]
    df = df[columnNames]
    ax = pd.plotting.scatter_matrix(df, alpha=0.75, figsize=[plotSize, plotSize], diagonal='kde')
    corrs = df.corr().values
    for i, j in zip(*plt.np.triu_indices_from(ax, k = 1)):
        ax[i, j].annotate('Corr. coef = %.3f' % corrs[i, j], (0.8, 0.2), xycoords='axes fraction', ha='center', va='center', size=textSize)
    plt.suptitle('Scatter and Density Plot')
    plt.show()

usernameSponsor = "testKaiwangke"
emailSponsor = "wangkedaily@gmail.com"
passwordSponsor = "1testWangke!"
# print(colda.test_network())
usernameAssistor = "testKaiwangkeass"
emailAssistor = "wan00802@umn.edu"
passwordAssistor = "1testWangkeass!"

# colda.login(usernameAssistor, passwordAssistor)
# test_function_res = colda.test_function()
# print(test_function_res)



print("ABOVE TESTS=========================================")


# %%
# reading files input/cab_rides.csv REMIND: CHANGE THE ROWS FOR TRAINING AND TESTING
if os.path.exists('input/cab_rides.csv'):
    print("path valid")
else:
    print("not valid")

Rows = None
Rows_sub_1000 = 1000
Rows_sub_100 = 100
# cab_rides.csv has 693071 rows in reality, but we are only loading/previewing the first 1000 rows
df_rides = pd.read_csv('input/cab_rides.csv', delimiter=',', nrows = Rows_sub_100)
df_rides.dataframeName = 'cab_rides.csv'

nRow, nCol = df_rides.shape
print(f'Price Data: There are {nRow} rows and {nCol} columns')

# %%
Rows = None
Rows_sub_1000 = 1000
if os.path.exists('input/weather.csv'):
    print("path valid")
else:
    print("not valid")
df_weather = pd.read_csv('input/weather.csv',delimiter=',',nrows=Rows)
df_weather.dataframeName = 'weather.csv'
nRow, nCol = df_weather.shape
print(f'Weather Data: There are {nRow} rows and {nCol} columns')


# %%
# Visualization

df_rides.head(5)


# %%
plotPerColumnDistribution(df_rides, 10, 5)
plotCorrelationMatrix(df_rides, 8)
plotScatterMatrix(df_rides, 12, 10)


# %%
df_weather.head(5)
plotPerColumnDistribution(df_weather, 10, 5)
plotCorrelationMatrix(df_weather, 8)
plotScatterMatrix(df_weather, 20, 10)

# %%
# df_rides['merged_date'] = df_rides['source'].astype('str') + ' - ' + df_rides['date'].dt.strftime('%Y-%m-%d').astype('str') + ' - ' + df_rides['date'].dt.hour.astype('str')
# df_weather['merged_date'] = df_weather['location'].astype('str') + ' - ' + df_weather['date'].dt.strftime('%Y-%m-%d').astype('str') + ' - ' + df_weather['date'].dt.hour.astype('str')
# %%

wthr_time_max = df_weather.time_stamp.max()
wthr_time_min = df_weather.time_stamp.min()
print(f"Max: {wthr_time_max}, Min: {wthr_time_min}")

# %%
# df_rides['time_stamp'] = round(df_rides['time_stamp'] / 1000)
pd.set_option('display.float_format', lambda x: '%.0f' % x)
df_rides.head(5)

# %%
# Try to train
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler



df_rides.isnull().sum()
# remove these rows where the price is not present
df_rides.dropna(axis = 0 , inplace = True)

df_weather.isnull().sum()
#rain not happening
df_weather.fillna(0 ,inplace = True)
# %%


df_rides.isnull().sum()
df_weather.isnull().sum()
#take average of all values  based on place /locations
# weather_avg
weather_avg = df_weather.groupby('location').mean().reset_index()
print(weather_avg)
# %%


timeseries  = df_rides['time_stamp']
price = df_rides['price']

plt.plot(timeseries,price)
# %%
import time
timeseries_converting  = df_rides['time_stamp'][0]
# unix_timestamp = float(timeseries_converting)
# readabel_time = int(str(timeseries_converting))
d = datetime.fromtimestamp(timeseries_converting / 1000.0)
# value = datetime.fromtimestamp(d)
# %%
print(d)

# print(timeseries.shape)
realtime = []

for i,d in enumerate(timeseries):
    realtime.append(datetime.fromtimestamp(d / 1000.0))
print(realtime)

plt.plot(realtime,price)

# readabel_time
# %%
