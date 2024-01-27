class Calculator:
    ADDITION = 1
    SUBSTRACTION = 2

    def __init__(self, type):
        self.type = type

    def calculate(self, a, b):
        result = 0
        if self.type == self.ADDITION:
            result = a + b
        elif self.type == self.SUBSTRACTION:
            result = a - b
        return result

# 使用例
calc = Calculator(Calculator.ADDITION)
print(calc.calculate(5, 3))  # 8

calc = Calculator(Calculator.SUBSTRACTION)
print(calc.calculate(5, 3))  # 2
