
from vending.coin import Coin, Coins
class Accountant:
    def __init__(self, quantity_of_100yen: int, quantity_of_500yen: int):
        self.one_handread_coins = Coins([Coin.ONE_HUNDRED for _ in range(quantity_of_100yen)])
        self.five_handread_coins = Coins([Coin.FIVE_HUNDRED for _ in range(quantity_of_500yen)])
        self.charge_coins = Coins()
    
    def is_valid_coin(self, coin: Coin):
        return coin in [Coin.ONE_HUNDRED, Coin.FIVE_HUNDRED]
    
    def can_return_change(self, input_coin: Coin) -> bool:
        if input_coin == Coin.ONE_HUNDRED:
            return True
        if input_coin == Coin.FIVE_HUNDRED:
            return self.one_handread_coins.get_amount() >= 400
        return False
    
    def get_charge_coins(self, input_coin: Coin):
        # お釣りを計算して保持
        charge_coins_num = self.calc_charge_one_handread_coins_num(input_coin)
        charge_coins = Coins()
        for _ in range(charge_coins_num):
            coin = self.one_handread_coins.pop()
            charge_coins.add(coin)
        return charge_coins
    
    def calc_charge_one_handread_coins_num(self, input_coin: Coin) -> int:
        return (input_coin.value - Coin.ONE_HUNDRED.value) // 100
    
    def add_change(self, coin: Coin):
        self.charge_coins.add(coin)
    
    def refund(self) -> Coins:
        charge_coins = self.charge_coins
        self.charge_coins = Coins()
        return charge_coins

    def add_coin(self, coin: Coin):
        if coin == Coin.ONE_HUNDRED:
            self.one_handread_coins.add(coin)
        if coin == Coin.FIVE_HUNDRED:
            self.five_handread_coins.add(coin)
            
    def pop_coin(self, coin: Coin):
        if coin == Coin.ONE_HUNDRED:
            self.one_handread_coins.pop()
        if coin == Coin.FIVE_HUNDRED:
            self.five_handread_coins.pop()
