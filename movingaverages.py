import pandas as pd
import matplotlib.pyplot as plt
import pandas_ta as pta
import pandas_datareader.data as web
#Keeps Code Running
while True:
    #Input for stock Upper Case only
    ticker = str(input("INPUT TICKER \n"))
    #Capture Data through Yahoo
    ohlcv = web.DataReader(ticker, 'yahoo', start='2018-01-01')
    pd.DataFrame(ohlcv)
    close = ohlcv["Close"]
#close.index = pd.to_datetime(close.index)
    #Simple moving Averages
    sma50  = pta.sma(ohlcv["Close"], length=50)
    sma200 = pta.sma(ohlcv["Close"], length=200)
    #RSI Calculator
    rsi = pta.rsi(ohlcv["Close"], length = 20)
    #OUTPUT
    print("200d Moving Average is " + str(sma200.tail(1)))
    print("50d Moving Average is " + str(sma50.tail(1)))
    print("The RSI is " + str(rsi.tail(1)))
    print("The Sharpe Ratio is " + str(pta.sharpe_ratio(ohlcv["Close"])))
    #Decision Maker
    if float(sma50.tail(1)) > float(sma200.tail(1)):
        print("BUY")
    elif float(sma50.tail(1)) < float(sma200.tail(1)):
        print("Sell")
    elif float(sma50.tail(1)) == float(sma200.tail(1)):
        print("Check Chart")
    #PLOTS
    plt.plot(close,label = "close")
    plt.plot(sma50,label = "sma50")
    plt.plot(sma200, label = "sma200")
    plt.legend()
    plt.show()
    #Restarts Code
    restart = str(input("Do you want to enter another ticker? \n"))
    if restart == "Y" or "y":
        continue
    print("Analysis Done")
    break
    #Not sure how to close without creating error






