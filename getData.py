import requests


class Data:
    """Class for Crpyto Data Collection from Binance"""
    key = "<Key Here>"
    secret_key = "<Secret Key Here>"
    api_url = "https://api.binance.us"

    def __init__(self, symbol):
        """Initializer Function."""
        self.symbol = symbol

    def getCandles(self):
        """Gathers live candlestick data for a given ticker.

        Args:
            symbol(str): Ticker symbol

        Returns:
            (list): candlestick data
        """
        ###Last entry in the list is the most recent, so I flipped it so that the return value places
        ###the first most recent value at index 0
        resp = requests.get(f"{Data.api_url}/api/v3/klines?symbol={self.symbol}&interval=1s")
        return resp.json()[::-1]

    def getPrice(self):
        """Returns most recent trade price"""
        resp = requests.get(f"{Data.api_url}/api/v3/ticker/price?symbol={self.symbol}")
        return resp.json()

if __name__ == "__main__":
    test = Data("BTCUSD")
    print(test.getCandles())
