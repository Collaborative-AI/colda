# Import the packages needed
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import time
import tushare as ts


# Try out the apple stock dataset
apple = yf.Ticker("AAPL")
df_apple = apple.history(period="max")
df_apple.tail()
df_apple.shape

# visualize the data (apple)
alt.Chart(df_apple[-200:]).mark_bar(opacity=0.45).encode(x="Low", y="High")

# Try out the tesla stock dataset
tsla = yf.Ticker("TSLA")
tsla.info

# visualize the data (tsla)
df_tsla = tsla.history(period="max")
print(df_tsla.shape)
df_tsla.tail()

# another visualization
alt.Chart(df_tsla).mark_point().encode(
    x="Open:Q", y="Close:Q", color="Volume", tooltip="Dividends"
).interactive()


# using tushare
ts.get_hist_data("600519")  # 茅台股价

# ## Web-scraping yfinance
#
# * https://github.com/vinodvidhole/yahoo-finance-scraper/blob/main/yahoo-finance-web-scraper.ipynb
import requests
from bs4 import BeautifulSoup

# pip install get-all-tickers


# from get_all_tickers import get_tickers as gt

# list_of_tickers = gt.get_tickers()
# # or if you want to save them to a CSV file
# get.save_tickers()

# check all stock symbols
bat = pd.read_csv("bats_symbols.csv")
bat.head()

# check the symbols are unique and valid
all_labels = list(bat["Name"].unique())
all_labels[:5]

# Here is the function
def get_csv(label):
    temp = yf.Ticker(label)
    df_temp = temp.history(period="max")
    return df_temp.to_csv(label + ".csv")
    # print(df_temp[1:])
    return df_temp.head()


# run the function and get the csv
for i in all_labels:
    # print(i)
    get_csv(i)


bat.head()


lst = pd.read_csv(
    "/Users/belladu/Desktop/SynSpot Project/Stock-Classifier-master/SP500_list.csv"
)
lst.head()


# join bat and lst right on Symbol and left on Name
bat_lst = pd.merge(bat, lst, how="inner", right_on="Symbol", left_on="Name")
bat_lst

# get the unique stock names
lst["Symbol"].unique()
stock_sec = lst[["Symbol", "Sector"]].rename(columns={"Symbol": "Stock_Name"})
stock_sec.shape
stock_sec.sample(3)
bat.sample(5)
stocks = bat["Name"]


# the following code is to get the industry, beta, and sector of the stocks
df = pd.DataFrame()
for stock in stocks[:5]:
    info = yf.Ticker(stock).info
    industry = info.get("industry")
    beta = info.get("beta")
    sector = info.get("sector")
    df = df.append(
        {"Stock": stock, "Industry": industry, "Beta": beta, "Sector": sector},
        ignore_index=True,
    )

df
stocks.shape
len(set(lst["Symbol"]) and set(bat["Name"]))

# url = 'https://finance.yahoo.com/topic/stock-market-news/'
# response = requests.get(my_url)


# ## Reference Links
#
# * https://blog.csdn.net/weixin_41103006/article/details/113203684?ops_request_misc=&request_id=&biz_id=102&utm_term=yfinance&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-2-113203684.142^v62^pc_search_tree,201^v3^control,213^v1^control&spm=1018.2226.3001.4187
#
# * https://blog.csdn.net/u010751000/article/details/124938370?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_utm_term~default-0-124938370-blog-113203684.pc_relevant_recovery_v2&spm=1001.2101.3001.4242.1&utm_relevant_index=3
#
# * https://www.wenvenn.com/20211215/shi-yong-python-bao-yfinance-du-qu-ya-hu-cai-jing-shang-de-gu-piao-shu-ju/
#
# * https://blog.jovian.ai/web-scraping-yahoo-finance-using-python-7c4612fab70c

# ## Reference Link for coding
# * https://www.kaggle.com/code/shwetagoyal4/beginner-s-guide-to-altair-visualization
