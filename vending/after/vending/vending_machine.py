from vending.drink import Drink

class VendingMachine:
    def __init__(self):
        self.quantity_of_coke = 5
        self.quantity_of_diet_coke = 5
        self.quantity_of_tea = 5
        self.number_of_100yen = 10
        self.charge = 0

    def buy(self, input_coin, kind_of_drink):
        if not self.__can_use_coin(input_coin):
            self.charge += input_coin
            return None

        if (kind_of_drink == Drink.COKE and self.quantity_of_coke == 0) or \
           (kind_of_drink == Drink.DIET_COKE and self.quantity_of_diet_coke == 0) or \
           (kind_of_drink == Drink.TEA and self.quantity_of_tea == 0):
            self.charge += input_coin
            return None

        if input_coin == 500 and self.number_of_100yen < 4:
            self.charge += input_coin
            return None

        if input_coin == 100:
            self.number_of_100yen += 1
        elif input_coin == 500:
            self.charge += (input_coin - 100)
            self.number_of_100yen -= (input_coin - 100) // 100

        if kind_of_drink == Drink.COKE:
            self.quantity_of_coke -= 1
        elif kind_of_drink == Drink.DIET_COKE:
            self.quantity_of_diet_coke -= 1
        else:
            self.quantity_of_tea -= 1

        return Drink(kind_of_drink)

    def refund(self):
        result = self.charge
        self.charge = 0
        return result
    
    def __can_use_coin(self, coin):
        return coin in [100, 500]
