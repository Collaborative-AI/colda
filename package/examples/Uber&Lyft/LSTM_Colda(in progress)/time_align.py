# algin time series data
# if time same, then check if current time have data for lyft and uber

# %%
import pandas as pd
from sklearn.model_selection import train_test_split

import numpy as np
import pandas as pd 
from sklearn.preprocessing import StandardScaler

# run train with indicator of 1
indicator = 0

rides_df = pd.read_csv('../../Uber&Lyft/input/cab_rides.csv')
weather_df = pd.read_csv('../../Uber&Lyft/input/weather.csv')

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
# for cat in cat_data:
#     print('category : ' ,cat)
#     print(data[cat].value_counts())
#     print('\n')
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

data = data.drop('pid_55c66225-fbe7-4fd5-9072-eab1ece5e23e',axis=1)
data = data.drop('pid_6c84fd89-3f11-4782-9b50-97c468b19529',axis=1)
data = data.drop('pid_6d318bcc-22a3-4af6-bddd-b409bfce1546',axis=1)
data = data.drop( 'pid_6f72dfc5-27f1-42e8-84db-ccc7a75f6969',axis=1)
data = data.drop('pid_997acbb5-e102-41e1-b155-9df7de0a73f2',axis=1)
data = data.drop('pid_9a0e7b09-b92b-4c41-9779-2ad22b4d779d', axis=1)


# uberdata = data['cab_type'=='1']
# lyftdata = data['cab_type'=='0']

# uberdata.to_csv('uberdata.csv')
# lyftdata.to_csv('lyftdata.csv')


# %%
data = data.sort_values(by='time_stamp', ascending=True)
data['time_stamp'] = pd.to_datetime(data['time_stamp'], unit='ms')

# %%

# result_df = pd.DataFrame(columns=data.columns)

# result_df = data.groupby('time_stamp').apply(lambda x: x[:2])

# result_df = data.groupby('time_stamp').filter(lambda x: x['cab_type'].nunique() == 1)
# print the result dataframe
# print(result_df.head(10))

# %%


data = data.set_index('time_stamp')
test_start = '2018-12-15 17:10:05.354'

x = data.drop('price',axis =1)
# print(x)
y = data['price']
# print(y)

# print(x.shape ,y.shape)

x_train , x_test , y_train ,y_test = train_test_split(x,y ,test_size = 0.2 , random_state = 52,shuffle=False)

# %%


target_sensor = "price"
features = list(data.columns.difference([target_sensor]))
# print(features)
# forecast_lead = 96*2*2
forecast_lead = 96*2
target = f"{target_sensor}"

data[target] = data[target_sensor].shift(-forecast_lead)
# print(data.shape)
df = data.iloc[:-forecast_lead]
# print(df.shape)


sc = StandardScaler()
sc.fit(x_train)
x_train = pd.DataFrame(sc.transform(x_train) ,columns =x.columns)
# y_train = y_train.values.reshape(-1, 1)
sc.fit(y_train)
y_train = pd.DataFrame(sc.transform(y_train) ,columns =['price'])
y_train = y_train.reset_index(drop=True)  # 重置索引
# concate x_train and y_train
train_df = pd.concat([x_train , y_train] ,axis =1)

unique_ids = np.random.choice(range(1, 99999999), size=len(train_df), replace=False)

# insert the random unique IDs as the first column of the dataframe
train_df.insert(0, 'id', unique_ids)

# train_df.reset_index(drop=True)
train_df = train_df.set_index('id')


# x_test =  pd.DataFrame(sc.transform(x_test) ,columns = x.columns)
# y_test = y_test.reset_index(drop=True)  # 重置索引
# concate x_test and y_test
# test_df = pd.concat([x_test , y_test] ,axis =1)


train_df.to_csv('train.csv')
# test_df.to_csv('test.csv')
print("saved")
