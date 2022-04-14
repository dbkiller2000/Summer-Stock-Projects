import pandas_datareader.data as web
#ticker = ["FB", 'AAPL', 'AMZN', 'MSFT', 'GOOG']
ticker = ["MRO","ABBV","XLF","KR","F","GLD","BIV","SCHP","ED","SLCA","HPQ","TELL"]
ohlcv = web.DataReader(ticker, 'yahoo', start='2020-01-01')
#weights = [0.56175074, 0.0164289, 0.033521, 0.08098456, 0.30731479]
weights = [0.18023427, 0.02067968, 0.04167486, 0.10530452, 0.10146469, 0.03777824,
 0.17667466, 0.00526995, 0.14790009, 0.11280747, 0.02681949, 0.04339208]
x = ohlcv['Close'].pct_change()
ret = (x * weights).sum(axis = 1)
cum = (ret + 1).cumprod()*100
print(cum)