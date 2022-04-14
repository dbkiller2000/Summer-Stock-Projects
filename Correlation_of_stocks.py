import pandas_datareader.data as web
import pandas as pd
import numpy
#ticker = str(input("INPUT TICKER \n")).split()
#ticker = ["FB", 'AAPL', 'AMZN', 'MSFT', 'GOOG']
ticker = ["MRO","ABBV","XLF","KR","F","SPYG","GLD","BIV","SCHP","ED","SLCA","HPQ","TELL"]
#GSPC is SP500 benchmark
sp500 = "^GSPC"
ohlcv =  web.DataReader(ticker, 'yahoo', start='2020-01-01')
df = pd.DataFrame(ohlcv)
x = df["Close"].pct_change()
corr = x.corr()
print(corr)

