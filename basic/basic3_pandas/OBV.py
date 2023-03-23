#https://superhky.tistory.com/136
#OBV 계산기 (주식거래량)

import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import pandas_datareader.data as web
import datetime
from dateutil.relativedelta import relativedelta

plt.style.use('fivethirtyeight')

krCode = "055550"
krCodeKs = krCode+".ks"

start = datetime.datetime.now()-relativedelta(months=1)
end = datetime.datetime.now()
StockData = web.DataReader(krCodeKs, "yahoo", start, end)

plt.figure(figsize=(12, 5))
plt.plot(StockData['Adj Close'], label = 'Close')
plt.title('Close Price')
plt.xlabel('Date', fontsize = 18)
plt.ylabel('Price(Won)', fontsize = 18)
plt.show()

OBV = []
OBV.append(0)

for i in range(1, len(StockData.Close)):
    if StockData.Close[i] > StockData.close[i-1]:
        OBV.append(OBV[-1]+StockData.Volume[i])
    elif StockData.Close[i] < StockData.close[i-1]:
        OBV.append(OBV[-1]+StockData.Volume[i])
    else:
        OBV.append(OBV[-1])

StockData['OBV'] = OBV
StockData['OBV_EMA'] = StockData['OBV'].ewm(span=20).mean()