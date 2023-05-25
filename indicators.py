class Indicator:
    """Class used for calculating indicators based on inputted data"""

    def __init__(self, data, period):
        """Initializer

        Args:
            data(list): list of candlestick data
            period(int): period of time to calculate indicator from
        """
        self.data = data
        self.period = period

    def getRSI(self):
        """Make the initial RSI calculation

        Returns:
            rsi(int): current rsi score
        """
        ###FUNCTION WORKS WITH DATA BY THE MINUTE###
        gains = 0
        losses = 0
        last = float(self.data[0][4])
        for x in range(self.period):
            price = float(self.data[x][4])
            differencePercentage = (price - last) / last
            if differencePercentage == 0:
                continue
            if price > last:
                gains += differencePercentage
            elif price < last:
                losses += (differencePercentage * -1)
            last = price
        gains /= self.period
        losses /= self.period
        try:
            rsi = 100 - (100 / (1 + (losses / gains)))
        except ZeroDivisionError:
            rsi = 100
        return rsi

    def updateRSI(rsi):
        pass
