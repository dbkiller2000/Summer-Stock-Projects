import matplotlib.pyplot as plt
from pandas_ta import sma, rsi,sharpe_ratio, ema
from pandas_datareader.data import DataReader
import time
ticker = str(input("INPUT TICKER \n"))
start = str(input("Date Input \n"))
beg_time = time.time()
ohlcv = DataReader(ticker, 'yahoo', start)
close, volume = ohlcv["Close"], ohlcv["Volume"]
sma50 = sma(close, length=50)
sma200 = sma(close, length=200)
rsi = rsi(close, length = 50)
def momentum(sma50, sma200, rsi):
    print(" ".join(["50d Moving Average is",str(sma50.tail(1))]))
    print(" ".join(["200d Moving Average is", str(sma200.tail(1))]))
    print(" ".join(["The RSI is", str(rsi.tail(1))]))
    print(" ".join(["The Sharpe Ratio is", str(sharpe_ratio(close))]))
def decision_maker(sma50, sma200, rsi, volume):
    if float(sma50.tail(1)) > float(sma200.tail(1)):
        print("BUY")
    elif float(sma50.tail(1)) < float(sma200.tail(1)):
        print("Sell")
    if float(rsi.tail(1)) > 70:
        print("Overbought")
    elif float(rsi.tail(1)) < 30:
        print("Oversold")
    else:
        print("Neutral Trend Strength")
    if sum(volume.tail(50))/50 > sum(volume.tail(200))/200 and float(sma50.tail(1)) > float(sma200.tail(1)):
        print("Break Out Likely")
    else:
        print("Not Likely or False Break Out")
momentum(sma50, sma200, rsi)
decision_maker(sma50, sma200, rsi, volume)
end_time = time.time()
print(end_time-beg_time)
plt.plot(close, label = "close")
plt.plot(sma50,label = "sma50")
plt.plot(sma200, label = "sma200")
plt.legend()
plt.show()