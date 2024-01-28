from vending.drink import Drink,KindOfDrink
from vending.coin import Coin, Coins
from vending.stock import Stocks
from vending.accountant import Accountant
class VendingMachine:
    def __init__(self):
        self.stocks = Stocks(5, 5, 5)
        self.accountant = Accountant(10, 10)

    def buy(self, input_coin: Coin, kind_of_drink: KindOfDrink) -> Drink:
        # 使えないお金は、受け取ったお金をそのままお釣りにして終了
        if not self.accountant.is_valid_coin(input_coin):
            self.accountant.add_change(input_coin)
            return None

        # お釣りがない場合は、受け取ったお金をそのままお釣りにして終了
        if not self.accountant.can_return_change(input_coin):
            self.accountant.add_change(input_coin)
            return None

        # 在庫がない場合は、受け取ったお金をそのままお釣りにして終了
        if self.stocks.is_empty(kind_of_drink):
            self.accountant.add_change(input_coin)
            return None

        # お釣りを計算して保持
        charge_coins = self.accountant.get_charge_coins(input_coin)
        for coin in charge_coins:
            self.accountant.add_change(coin)

        # お金を受け取る
        self.accountant.add_coin(input_coin)

        return self.stocks.pick(kind_of_drink)

    def refund(self) -> Coins:
        return self.accountant.refund()
    