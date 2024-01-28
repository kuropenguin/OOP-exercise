# ルール9．Getter、Setter、プロパティを使用しないこと

class Item:
    def __init__(self):
        self.amount = 0

    def add_amount(self, amount):
        self.amount += amount

class Rule9:
    def method(self, item: Item):
      self.item.add_amount(1)

# 使用例
item = Item()
rule9 = Rule9()
rule9.method(item)
print(item.get_amount())  # 1
