from sklearn import preprocessing
import numpy as np
import pandas as pd

le = preprocessing.LabelEncoder()



#####  cab rides
cab = pd.read_csv("input/cab_rides.csv")

# drop useless cols and na records
cols = ['cab_type', 'id', 'product_id']
cab.drop(cols, inplace=True, axis=1)
cab.dropna(axis = 0 , inplace = True)

# transform data to int
cols = ['destination', 'source', 'name']
cab[cols] = cab[cols].apply(le.fit_transform).astype(str)

# combine dest and src
cab['dest_src'] = cab['destination'].str.cat(cab['source'])

cab.drop('destination', inplace=True, axis=1)
cab.drop('source', inplace=True, axis=1)

cab.to_csv('input/clean_cab_new.csv')





#### weather
weather = pd.read_csv("input/weather.csv")
weather.dropna(axis=0, inplace=True)

cols = ['location']
weather[cols] = weather[cols].apply(le.fit_transform).astype(str)

weather.to_csv('input/clean_weather.csv')