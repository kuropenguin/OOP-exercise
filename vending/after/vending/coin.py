from enum import Enum

class Coin(Enum):
    One = 1
    FIVE = 5
    TEN = 10
    FIFTY = 50
    ONE_HUNDRED = 100
    FIVE_HUNDRED = 500

class Coins:
    def __init__(self, initial_coins=None):
        if initial_coins is None:
            initial_coins = []
        self.coins = initial_coins

    def add(self, coin: Coin):
        self.coins.append(coin)
      
    def pop(self) -> Coin:
        return self.coins.pop()

    def get_amount(self):
        return sum([coin.value for coin in self.coins])

    def get_quintity(self):
        return len(self.coins)
