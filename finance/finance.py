import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
plt.style.use('seaborn')


import yfinance as yf

twtr = yf.Ticker('twtr')

stockInfo = twtr.info



for key,value in stockInfo.items():
    print(key, ":", value)




print(twtr._institutional_holders)


df = twtr.dividends


data = df.resample('Y').sum()

data = data.reset_index()

plt.figure()
plt.bar(data['Year'], data['Dividends'])
plt.ylabel('Dividend Yield ($)')
plt.xlabel('Year')
plt.title('Plot')
plt.xlim(2002,2020)
plt.show()