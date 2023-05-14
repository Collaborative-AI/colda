# %%
import numpy as np

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
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
################################total

# %%
x_train , x_test , y_train ,y_test = train_test_split(x,y ,test_size = 0.2 , random_state = 52)
print(x_train.shape , x_test.shape , y_train.shape , y_test.shape)

sc = StandardScaler()
sc.fit(x_train)


x_train = pd.DataFrame(sc.transform(x_train) ,columns =x.columns)
x_test =  pd.DataFrame(sc.transform(x_test) ,columns = x.columns)
# %%
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
lr = LinearRegression()
lr.fit(x_train ,y_train)
print("r2 test score is : ",(lr.score(x_test ,y_test)))
prediction = lr.predict(x_test)




# # The coefficients
# print("Coefficients: \n", lr.coef_) 
# # The mean squared error

# print("Mean squared error: %.2f" % mean_squared_error(y_test, prediction))
# # The coefficient of determination: 1 is perfect prediction
# print("Coefficient of determination: %.2f" % r2_score(y_test, prediction))


################################Uber

# %%

uberdata = data[data.cab_type == 1]
uberdata.select_dtypes('object').columns
uberdata.shape
x = uberdata.drop('price',axis =1)
y = uberdata['price']

print(x.shape ,y.shape)
# %%
x_train , x_test , y_train ,y_test = train_test_split(x,y ,test_size = 0.2 , random_state = 52)
print(x_train.shape , x_test.shape , y_train.shape , y_test.shape)

sc = StandardScaler()
sc.fit(x_train)


x_train = pd.DataFrame(sc.transform(x_train) ,columns =x.columns)
x_test =  pd.DataFrame(sc.transform(x_test) ,columns = x.columns)
# %%
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(x_train ,y_train)
print("ONLY uber test score is : ",(lr.score(x_test ,y_test)))

################################Lyft

# %%
lyftdata = data[data.cab_type == 0]
lyftdata.select_dtypes('object').columns
lyftdata.shape
x = lyftdata.drop('price',axis =1)
y = lyftdata['price']

print(x.shape ,y.shape)
# %%
x_train , x_test , y_train ,y_test = train_test_split(x,y ,test_size = 0.2 , random_state = 52)
print(x_train.shape , x_test.shape , y_train.shape , y_test.shape)

sc = StandardScaler()
sc.fit(x_train)


x_train = pd.DataFrame(sc.transform(x_train) ,columns =x.columns)
x_test =  pd.DataFrame(sc.transform(x_test) ,columns = x.columns)
# %%
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(x_train ,y_train)
print("ONLY lyft test score is : ",(lr.score(x_test ,y_test)))


