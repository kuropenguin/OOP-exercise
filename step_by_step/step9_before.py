class Item:
    def __init__(self):
        self.amount = 0

    def set_amount(self, amount):
        self.amount = amount

    def get_amount(self):
        return self.amount

class Rule9:
    def method(self, item: Item):
        value = item.get_amount()
        item.set_amount(value + 1)

# 使用例
item = Item()
rule9 = Rule9()
rule9.method(item)
print(item.get_amount())  # 1
