
from vending.drink import Drink,Drinks, KindOfDrink

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
        if self.get_quantity() == 0:
            return None
        return self.drinks.pick()

    def get_quantity(self):
        return self.drinks.get_quantity()
    
    def __is_same_kind(self, kind_of_drink: KindOfDrink):
        if self.get_quantity() == 0:
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
    
    def get_quantity(self, kind_of_drink: KindOfDrink):
        if kind_of_drink == KindOfDrink.COKE:
            return self.coke_stock.get_quantity()
        if kind_of_drink == KindOfDrink.DIET_COKE:
            return self.diet_coke_stock.get_quantity()
        return self.tea_stock.get_quantity()
    
    def is_empty(self, kind_of_drink: KindOfDrink):
        return self.get_quantity(kind_of_drink) == 0
