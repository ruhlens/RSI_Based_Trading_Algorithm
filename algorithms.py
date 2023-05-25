class Algorithm:

    def __init__(self, indicator):
        self.indicator = indicator

    def RSI(self, sellTrigger, buyTrigger, price, money, shares):
        """RSI based algorithm that triggers when RSI reaches indicated points

        Args:
            sellTrigger(float): selling point in terms of rsi
            buyTrigger(float): selling point in terms of rsi
            price(float): current price
            money(float): user's current cash
            shares(int): total number of shares

        Returns:
            (list): containing the user's current amount of money and the shares
        """
        price = float(price)
        #print(f"RSI: {self.indicator}")
        if price <= money:
            if self.indicator <= buyTrigger:
                money -= price
                #print("B")
                shares += 1
                return ['B', money, shares, price]
        if shares > 0:
            if self.indicator >= sellTrigger:
                money += price
                #print("S")
                shares -= 1
                return ['S', money, shares, price]
        return ['n', money, shares, price]

    def RSI_RealMoney(self, sellTrigger, buyTrigger, price, money, shares):
        """RSI based algorithm that triggers when RSI reaches indicated points
        THIS BITCH USES REAL MONEY
        IT GOES ALL IN ON BITCOIN EVERYTIME THAT IT HAS THE CHANCE

        Args:
            sellTrigger(float): selling point in terms of rsi
            buyTrigger(float): selling point in terms of rsi
            price(float): current price
            money(float): user's current cash
            shares(int): total number of shares

        Returns:
            (list): containing the user's current amount of money and the shares
        """
        price = float(price)
        #print(f"RSI: {self.indicator}")
        if price <= money:
            if self.indicator <= buyTrigger:
                money -= price
                #print("B")
                shares += 1
                return ['B', money, shares, price]
        if shares > 0:
            if self.indicator >= sellTrigger:
                money += price
                #print("S")
                shares -= 1
                return ['S', money, shares, price]
        return ['n', money, shares, price]
