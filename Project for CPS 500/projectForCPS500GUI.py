#projectForCps500GUI.py

from projectForCPS500 import *
from graphics import *

class GUI():
    def __init__(self,):
        self.stock = Stock('NFLX', '2009-01-01', '2018-01-1')
        self.win = GraphWin("Stocks", 400, 400)
        self.win.setBackground('#ca4b32')
        self.win.setCoords(0,0,10,10)



    #For now this will be a static, in the future an implementation will be made
    #   to make it a dynamic stock handling allowing multiple comparisons of stocks
    #   and removal of other stocks
    def wait(self):
        while True:
            key = self.win.getKey()
            if key == 'q':
                break

    def handle_enter(self):
        #draw the date text
        date = Text(Point(4.5,7),"(yyyy-mm-dd)").draw(self.win)
        #draw the text at the bottom
        bottom = Text(Point(5,2),"hit enter once you're finished").draw(self.win)

        #the ticker entry and label to the left of it
        tickerText = Text(Point(1.2,8), "Ticker : ").draw(self.win)
        tickerEntry = Entry(Point(4, 8),11).draw(self.win)

        #the start date entry and
        startText =Text (Point(1.5,6), "Start date : ").draw(self.win)
        startEntry = Entry(Point(4.5,6), 11).draw(self.win)

        endText = Text(Point(1.5,4), "End date   : ").draw(self.win)
        endEntry = Entry(Point(4.5,4), 11).draw(self.win)

        while True:
            key = self.win.getKey()
            if key == "Return":
                break
        #undraw everything
        date.undraw()
        bottom.undraw()
        tickerText.undraw()
        tickerEntry.undraw()
        startText.undraw()
        startEntry.undraw()
        endText.undraw()
        endEntry.undraw()

        #set the stock
        self.stock = Stock(tickerEntry.getText(), startEntry.getText(), endEntry.getText())


    def prompt(self):
        #tell them what they can press to get data
        Text(Point(5,9),"Press q to quit").draw(self.win)
        Text(Point(5,8),"Press d to get a graph of the data").draw(self.win)
        Text(Point(5,7),"Press a to get a graph of the daily returns").draw(self.win)
        Text(Point(5,6),"Press m for a graph of the monthly returns").draw(self.win)
        Text(Point(5,5),"Press h for a histogram of percent vs daily returns").draw(self.win)
        Text(Point(5,4),"Press g for a histogram vs a gaussian distribution").draw(self.win)
        Text(Point(5,3),"Press s for statistics").draw(self.win)

    def handle_key(self, key):
        if key  == 'd':
            #graph the data
            try:
                self.stock.graph_data()
            except Exception as e:
                print("An exception occured in handle key at d")

        elif key == 'a':
            #graph the daily returns
            try:
                self.stock.daily_return()
            except Exception as e:
                print("An exception occured in handle key at a")

        elif key == 'm':
            #graph the monthly returns
            try:
                self.stock.monthly_return()
            except Exception as e:
                print("An exception occured in handle key at m")

        elif key == 'h':
           #plot a histogram
           try:
               self.stock.histo()
           except Exception as e:
               print("An exception occured in handle key at h")

        elif key == 'g':
            #graph the histogram and gaussian distribution
            try:
                self.stock.histo_gaus()
            except Exception as e:
                print("An exception occured in handle key at g")

        elif key == 's':
            #display the stats
            try:
                self.stock.stats()
            except Exception as e:
                print("An exception occured in handle key at s")

        else:
            print("You did nothing")


def main():
    gui = GUI()
    #get the stock
    gui.handle_enter()
    gui.prompt()
    while True:
        #get their key
        key = gui.win.getKey()
        if key == 'q':
            break
        gui.handle_key(key)

    gui.win.close()



main()
