from vending.drink import Drink,Drinks, KindOfDrink
from vending.coin import Coin, Coins

class Stock:
    def __init__(self, quantity: int, kind_of_drink: KindOfDrink):
        self.drinks = Drinks()
        for _ in range(quantity):
            self.drinks.add(Drink(kind_of_drink))

    def add(self, drink: Drink):
        if self.__is_same_kind(drink.get_kind()):
            self.drinks.append(drink)
        return None
    
    def pick(self) -> Drink:
        if self.get_quintity() == 0:
            return None
        return self.drinks.pick()

    def get_quintity(self):
        return self.drinks.get_quintity()
    
    def __is_same_kind(self, kind_of_drink: KindOfDrink):
        if self.get_quintity() == 0:
            return True
        return self.drinks[0].get_kind() == kind_of_drink

class Stocks:
    def __init__(self):
        self.coke_stock = Stock(5, KindOfDrink.COKE)
        self.diet_coke_stock = Stock(5, KindOfDrink.DIET_COKE)
        self.tea_stock = Stock(5, KindOfDrink.TEA)
    
    def pick(self, kind_of_drink: KindOfDrink) -> Drink:
        if kind_of_drink == KindOfDrink.COKE:
            return self.coke_stock.pick()
        if kind_of_drink == KindOfDrink.DIET_COKE:
            return self.diet_coke_stock.pick()
        return self.tea_stock.pick()
    
    def get_quintity(self, kind_of_drink: KindOfDrink):
        if kind_of_drink == KindOfDrink.COKE:
            return self.coke_stock.get_quintity()
        if kind_of_drink == KindOfDrink.DIET_COKE:
            return self.diet_coke_stock.get_quintity()
        return self.tea_stock.get_quintity()

class VendingMachine:
    def __init__(self):
        self.stocks = Stocks()
        self.number_of_100yen = 10
        self.refund_coins = Coins()

    def buy(self, input_coin: Coin, kind_of_drink: KindOfDrink) -> Drink:
        # 会計係がお金を受け取る・お釣りを計算する・お釣りを出す
        # 在庫管理が在庫を確認する・在庫を出す
        if not self.__can_use_coin(input_coin):
            self.refund_coins.add(input_coin)
            return None

        if self.stocks.get_quintity(kind_of_drink) == 0:
            self.refund_coins.add(input_coin)
            return None

        if input_coin == Coin.FIVE_HUNDRED and self.number_of_100yen < 4:
            self.refund_coins.add(input_coin)
            return None

        if input_coin == Coin.ONE_HUNDRED:
            self.number_of_100yen += 1
        if input_coin == Coin.FIVE_HUNDRED:
            self.__add_refund_coins(input_coin)
            self.number_of_100yen -= self.__calc_refund_coins_num(input_coin)

        return self.stocks.pick(kind_of_drink)



    def refund(self) -> Coins:
        refund_coins = self.refund_coins
        self.refund_coins = Coins()
        return refund_coins
    
    def __can_use_coin(self, coin):
        return coin in [Coin.ONE_HUNDRED, Coin.FIVE_HUNDRED]
    
    def __calc_refund_coins_num(self,input_coin: Coin) -> int:
        return (input_coin.value - Coin.ONE_HUNDRED.value) // 100

    def __add_refund_coins(self,input_coin: Coin):
        refund_coins_num = self.__calc_refund_coins_num(input_coin)
        for _ in range(refund_coins_num):
            self.refund_coins.add(Coin.ONE_HUNDRED)
