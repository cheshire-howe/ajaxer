import matplotlib.dates as mdates
import matplotlib.pyplot as plt

from pandas.io.data import get_data_yahoo
from datetime import datetime, timedelta
from itertools import izip
from matplotlib.finance import candlestick_ochl


def pancan():
    symbol = "GOOG"
    # get the data on a symbol
    data = get_data_yahoo(symbol, datetime.now() - timedelta(days=90))
    close_price = data['Adj Close']
    # format time properly
    dates = data.index.to_pydatetime()
    times = mdates.date2num(dates)
    # make an array of tuples in the specific order needed
    q = izip(times, data['Open'], data['Close'],
             data['High'], data['Low'])
    # construct and show the plot
    plt.figure(figsize=(10, 4))
    ax1 = plt.gca()
    ax1.xaxis_date()
    candlestick_ochl(ax1, q, width=0.6, colorup='g', colordown='r')
    close_price.plot()
    plt.savefig("static/candle.png")
    plt.clf()


def add():
    return 2


def array():
    return ['Hey', 'You', 'There']
