#projectForCps500.py 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt#plots stuff
import pandas_datareader as web#extracts data off the internet
from scipy.stats import skew#is a method that lets us get the skew of data
import random
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()#This will explicitly convery date time for us
plt.ion()#makes all plots interactive instead of static so when you close out of them
            #   It doesn't just hang in the terminal

class Stock():
    def __init__(self, ticker, startDate, endDate):
        self.ticker = ticker
        self.startDate = startDate
        self.endDate = endDate
        self.data = web.get_data_yahoo(ticker, start= startDate, end = endDate)

    #Shows top of the data
    def display_head(self):
        print(self.data.head())

    #Plot of the data unmodified
    def graph_data(self):
        self.data['Adj Close'].plot()
        plt.xlabel("Date")
        plt.ylabel("Adjusted")
        plt.title(self.ticker + " Prices")
        plt.show()

    #gets the percent difference between the current and previous day
    def daily_percent_difference(self):
        #pct_change() gets the difference between the current and last value
        #   because there's nothing before the first one it will be NaN and dropna()
        #   will drop the NaN
        return self.data['Adj Close'].pct_change().dropna()

    #gets the percent difference between the current and previous month
    def monthly_percent_difference(self):
        #ffill() will fill a data frames empty slots with a previous observation
        #and pct_change() still does the same
        return self.data['Adj Close'].resample("M").ffill().pct_change()

    #Plot the daily returns
    def daily_return(self):
        fig = plt.figure()                                    #From the bottom left
        axis = fig.add_axes([0.15, 0.1, 0.8 , 0.8])#[x0, y0, width%, height%]
        axis.plot(self.daily_percent_difference())
        axis.set_xlabel('Date')
        axis.set_ylabel('% Difference')
        axis.set_title(self.ticker + ' Daily Return Data')
        plt.show()

    #Plot the monthly returns
    def monthly_return(self):
        fig = plt.figure()
        axis = fig.add_axes([0.15 ,0.1 ,0.8, 0.8])#[x0, y0, width%, height%]
        axis.plot(self.monthly_percent_difference())
        axis.set_xlabel("Date")
        axis.set_ylabel("% Difference")
        axis.set_title(self.ticker + " monthly return data")
        plt.show()

    #Plot as a histogram of how much of the data % of the data consists of a daily return vs daily returns
    def histo(self):
        fig = plt.figure()
        axis = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        self.daily_percent_difference().plot.hist(bins = 100)#bins is how many rectangles to use
        axis.set_xlabel("Daily returns %")
        axis.set_ylabel("Percent")
        axis.set_title(self.ticker + " daily returns data")
        axis.text(-0.35, 200, "Low returns")
        axis.text(0.25, 200, "High returns")
        plt.show()

    def histo_gaus(self):
        #Generate normalized data
        normalizedData = np.random.normal(self.daily_return_mean(), self.daily_return_std_dev(), size = 10000)

        #Note that alpha is opaqueness going from 0 = transparent to 1 = opaque
        #   bins is the amount of bins that something will be divided into
        #   density = true means that the area under the histogram = 1

        plt.hist(normalizedData, bins=150, alpha = 0.8, density = True, label = 'Normal Distribution')
        plt.hist(self.daily_percent_difference(), bins = 100, alpha = 0.7, density = True, label = 'Returns')
        plt.legend()
        plt.xlabel("%")
        plt.ylabel("% Difference")
        plt.show()

    #Get the stats #Note that these are all lambda functions
    #mean of the daily returns
    daily_return_mean = lambda self : np.mean(self.daily_percent_difference())

    #standard deviation of the daily returns
    daily_return_std_dev = lambda self : np.std(self.daily_percent_difference())

    #variance of the daily returns
    daily_return_variance = lambda self : self.daily_return_std_dev() ** 2

    #mean of the annualized returns
    annualized_return_mean = lambda self : ((1+ self.daily_return_mean())**252) -1

    #standard deviation of the annualized return
    annualized_return_std_dev = lambda self : self.daily_return_std_dev()  * np.sqrt(252)

    #variance of the anuualized return
    annualized_return_variance = lambda self : self.annualized_return_std_dev() ** 2

    #skew of the daily returns
    daily_skew = lambda self : skew(self.daily_percent_difference())

    #This will print out a neat list of the results
    def stats(self):
        print("-"*65)
        print("The mean of the daily returns is : {0:0.02}%".format(self.daily_return_mean()))
        print("-"*65)
        print("The standard deviation of the daily returns is : {0:0.02}%".format(self.daily_return_std_dev()))
        print("-"*65)
        print("The variance of the daily returns is : {0:0.02}%".format(self.daily_return_variance()))
        print("-"*65)
        print("The skew of the daily returns is : {0:0.02}".format(self.daily_skew()))
        print("-"*65)
        print("The mean of the anuualized returns is :  {0:0.02}%".format(self.annualized_return_mean()))
        print("-"*65)
        print("The standard deviation of the anuualized returns is  :  {0:0.02}%".format(self.annualized_return_std_dev()))
        print("-"*65)
        print("The variance of the anualized returns is :  {0:0.02}%".format(self.annualized_return_variance()))
        print("-"*65)
