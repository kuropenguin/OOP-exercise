class Address:
    def method(self):
        pass  # ここにmethodのロジックを実装します

class User:
    def __init__(self, address: Address):
        self.address = address

    def get_address(self) -> Address:
        return self.address

class Rule4:
    def __init__(self, user: User):
        self.user = user

    def method(self):
        self.user.get_address().method()

# 使用例
address = Address()
user = User(address)
rule4 = Rule4(user)
print(rule4.method())
