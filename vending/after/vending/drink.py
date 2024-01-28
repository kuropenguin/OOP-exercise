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

