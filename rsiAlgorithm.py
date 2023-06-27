"""
THIS IS A PAPER TRADING PROGRAM BASED ON THE RSI ALGORITHM
BUY AT RSI = 30
SELL AT RSI = 70
"""

from getData import Data
from indicators import Indicator
from algorithms import Algorithm
from graph import Graph
import keyboard

def main():
    """Main function to handle the algorithm."""
    print("RSI Trading Algorithm Started. Press 'Q' to Close")
    run = True
    money = 100000
    shares = 0
    x = []
    y = []
    index = 0
    graph = Graph()
    buys = []
    sells = []
    avBuyPrice = 0
    avSellPrice = 0
    percentage = 0
    while run:
        if keyboard.is_pressed("q"):
            run = False
        ticker = "BTCUSD"
        data = Data(ticker)
        #the longer the interval, the slower the RSI calculation
        indicator = Indicator(data.getCandles(), 120)
        rsi = indicator.getRSI()
        currentPrice = data.getPrice()
        x.append(index)
        y.append(float(currentPrice.get("price")))
        if len(x) > 120:
            x.remove(x[0])
            graph.clear()
        if len(y) > 120:
            y.remove(y[0])
            graph.clear()
        index += 1
        algo = Algorithm(rsi)
        rsiAlgo = algo.RSI(70, 30, float(currentPrice.get("price")), money, shares)
        orderType = rsiAlgo[0]
        money = rsiAlgo[1]
        shares = rsiAlgo[2]
        price = rsiAlgo[3]
        percentage = (money - 100000) / 100000
        graph.liveGraph(x, y, buys, avBuyPrice, avSellPrice, percentage, money)
        if orderType == "B":
            buys.append(price)
        if orderType == "S":
            sells.append(price)
        if len(buys) > 0:
            avBuyPrice = sum(buys) / len(buys)
        if len(sells) > 0:
            avSellPrice = sum(sells) / len(sells)
    graph.show()

if __name__ == "__main__":
    main()
