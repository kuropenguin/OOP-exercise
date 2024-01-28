from vending.drink import Drink, KindOfDrink
from vending.coin import Coin, Coins

class VendingMachine:
    def __init__(self):
        self.quantity_of_coke = 5
        self.quantity_of_diet_coke = 5
        self.quantity_of_tea = 5
        self.number_of_100yen = 10
        self.refund_coins = Coins()

    def buy(self, input_coin: Coin, kind_of_drink: KindOfDrink):
        if not self.__can_use_coin(input_coin):
            self.refund_coins.add(input_coin)
            return None

        if (kind_of_drink == KindOfDrink.COKE and self.quantity_of_coke == 0) or \
           (kind_of_drink == KindOfDrink.DIET_COKE and self.quantity_of_diet_coke == 0) or \
           (kind_of_drink == KindOfDrink.TEA and self.quantity_of_tea == 0):
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

        if kind_of_drink == KindOfDrink.COKE:
            self.quantity_of_coke -= 1
            return Drink(kind_of_drink)

        if kind_of_drink == KindOfDrink.DIET_COKE:
            self.quantity_of_diet_coke -= 1
            return Drink(kind_of_drink)

        self.quantity_of_tea -= 1
        return Drink(kind_of_drink)


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
