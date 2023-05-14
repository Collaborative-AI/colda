# Data-Collection
![Yahoo Finance logo](https://www.arborcrowd.com/wp-content/uploads/2021/06/Yahoo-Finance-logo.png)

## Introduction
In this Repo, we have collected daily stock data from yahoo fiance with the package `yfiance`. We have collected over 500 MB stocks including its open, high,low prices across each stock's time span. The S&P 500 stocks are all included. The data is stored in the `data.zip` file in this Repo.

Daily stock data for the S&P 500 and a selection of other stocks were successfully obtained from the `yfiance` package through web scraping. The data was collected on a daily basis, yielding a significant amount of information over time. The collected data included daily open, high, low, and close prices for each stock, as well as volume, dividends, and stock splits information. This data allowed for a detailed analysis of the stock market and the performance of individual stocks. Various web scraping techniques and tools in Python were used to extract the data from the Yahoo Finance website and store it in a suitable format for further analysis. The success of the effort provided valuable insights into the stock market and the performance of different stocks.

## Usage
It is important to note that the stock data has been grouped by sector. Not all stocks have sector information available, so there may be null values in the dataset for certain stocks. This should be taken into consideration when analyzing the data, as it may affect the accuracy and completeness of the results. It is also worth mentioning that grouping the data by sector allows for a more detailed and nuanced analysis of the stock market, as it allows for comparison and analysis within specific industries.

Check Folder `10_Dateset_Samples` for more details to replicate and get the most up-to-date CSVs.

## Discussion
The process of obtaining data from an API, such as `yfinance`, can be replicated for use with other APIs. This involves making a request to the API using a predetermined set of parameters, such as a specific stock ticker or time period. Once the API responds, the data must be processed in order to extract the relevant information. This method can be applied to any API that offers the ability to retrieve data through requests and responses, providing a versatile means of accessing and analyzing a wide range of data.
