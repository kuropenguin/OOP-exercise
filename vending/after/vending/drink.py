from enum import Enum

class KindOfDrink(Enum):
    COKE = 0
    DIET_COKE = 1
    TEA = 2

class Drink:
    def __init__(self, kind: KindOfDrink):
        self.kind = kind

    def get_kind(self):
        return self.kind

class Drinks:
    def __init__(self):
        self.drinks = []

    def add(self, drink: Drink):
        self.drinks.append(drink)
    
    def pick(self) -> Drink:
        if self.get_quantity() == 0:
            return None
        return self.drinks.pop()

    def get_quantity(self) -> int:
        return len(self.drinks)
