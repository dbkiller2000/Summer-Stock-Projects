import yfinance as yf
import numpy as np
import pandas as pd

stocks = ["MRO","ABBV","XLF","KR","F","GLD","BIV","SCHP","ED","SLCA","HPQ","TELL"]
data = yf.download(stocks, start='2020-01-01')

#daily returns
data = data['Close']
x = data.pct_change()

p_weights = []
p_returns = []
p_risk = []
p_sharpe = []

count = 2000
for k in range(0, count):
    wts = np.random.uniform(size = len(x.columns))
    wts = wts/np.sum(wts)
    p_weights.append(wts)

    #returns
    mean_ret = (x.mean() * wts).sum()*252
    p_returns.append(mean_ret)

    #volatility
    ret = (x * wts).sum(axis = 1)
    annual_std = np.std(ret) * np.sqrt(252)
    p_risk.append(annual_std)
    
    #Sharpe ratio
    sharpe = (np.mean(ret) / np.std(ret))*np.sqrt(252)
    p_sharpe.append(sharpe)


max_ind = np.argmax(p_sharpe)

#Max Sharpe ratio
print(p_sharpe[max_ind])

#weights
print(p_weights[max_ind])