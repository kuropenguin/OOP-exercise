#ルール4．1行につきドットは1つまでにすること(クラスが直接関連しない他のクラスのメソッドを呼び出さないようにする)
# 操作できるオブジェクトは、
# ・オブジェクト自身
# ・インスタンス変数のオブジェクト
# ・引数で渡されたオブジェクト
# ・メソッド内でインスタンス化したオブジェクト
# デメテルの法則(最小知識の原則)に従いましょう。

class Address:
    def get_zip_code(self):
        return "123-4567"

class User:
    def __init__(self, address: Address):
        self.address = address

    def get_zip_code(self) -> Address:
        return self.address.get_zip_code()

class Rule4:
    def __init__(self, user: User):
        self.user = user

    def get_user_zip_code(self):
        self.user.get_zip_code()

# 使用例
address = Address()
user = User(address)
rule4 = Rule4(user)
print(rule4.get_user_zip_code())
