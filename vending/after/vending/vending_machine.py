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
    def __init__(self, quantity_of_coke: int, quantity_of_diet_coke: int, quantity_of_tea: int):
        self.coke_stock = Stock(quantity_of_coke, KindOfDrink.COKE)
        self.diet_coke_stock = Stock(quantity_of_diet_coke, KindOfDrink.DIET_COKE)
        self.tea_stock = Stock(quantity_of_tea, KindOfDrink.TEA)
    
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

class Accountant:
    def __init__(self, number_of_100yen: int, number_of_500yen: int):
        self.one_handread_coins = Coins([Coin.ONE_HUNDRED for _ in range(number_of_100yen)])
        self.five_handread_coins = Coins([Coin.FIVE_HUNDRED for _ in range(number_of_500yen)])
        self.charge_coins = Coins()
    
    def is_valid_coin(self, coin: Coin):
        return coin in [Coin.ONE_HUNDRED, Coin.FIVE_HUNDRED]
    
    def can_return_change(self, input_coin: Coin) -> bool:
        if input_coin == Coin.ONE_HUNDRED:
            return True
        if input_coin == Coin.FIVE_HUNDRED:
            return self.one_handread_coins.get_amount() >= 400
        return False
    
    
    def accounting(self, input_coin: Coin):
        # validation
        if not self.is_valid_coin(input_coin):
            return
        if not self.can_return_change(input_coin):
            return

        # お釣りを計算して保持
        charge_coins_num = self.calc_charge_one_handread_coins_num(input_coin)
        for _ in range(charge_coins_num):
            coin = self.one_handread_coins.pop()
            self.charge_coins.add(coin)

        # 受け取ったお金を保持
        self.add_coin(input_coin)
        return
    
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
class VendingMachine:
    def __init__(self):
        self.stocks = Stocks(5, 5, 5)
        self.accountant = Accountant(10, 10)

    def buy(self, input_coin: Coin, kind_of_drink: KindOfDrink) -> Drink:
        # 会計係がお金を受け取る・お釣りを計算する・お釣りを出す
        # 在庫管理が在庫を確認する・在庫を出す
        if not self.accountant.is_valid_coin(input_coin):
            self.accountant.add_change(input_coin)
            return None

        if not self.accountant.can_return_change(input_coin):
            self.accountant.add_change(input_coin)
            return None

        if self.stocks.get_quintity(kind_of_drink) == 0:
            self.accountant.add_change(input_coin)
            return None

        self.accountant.accounting(input_coin) 

        return self.stocks.pick(kind_of_drink)

    def refund(self) -> Coins:
        return self.accountant.refund()
    