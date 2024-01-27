# ルール2．else句を使用しないこと
# strategy パターンを利用

from abc import ABC, abstractmethod

class Type(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

class Addition(Type):
    def execute(self, a, b):
        return a + b

class Substraction(Type):
    def execute(self, a, b):
        return a - b

class Calculator:
    def __init__(self, type):
        self.type = type

    def calculate(self, a, b):
        result = self.type.execute(a, b)
        return result

# 使用例
add = Addition()
calc = Calculator(add)
print(calc.calculate(5, 3))  # 8

sub = Substraction()
calc = Calculator(sub)
print(calc.calculate(5, 3))  # 2
