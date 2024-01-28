# ルール8．ファーストクラスコレクションを使用すること

# このルールは、ルール3と非常に似ています。
# コレクションは非常に便利ですが、単なるプリミティブな型と同じで意図を表すことができません。

# コレクションを独自のクラスでラップします。
# コレクションをラップしたクラスには、多くのインスタンス変数を持たせないようにします。
# フィルタなどのコレクションに関する振る舞いをまとめることができます。
from typing import List

class User:
    pass  # Userクラスの詳細は省略

class Users:
    def __init__(self):
        self.users: List[User] = []

    def add(self, user: User):
        self.users.append(user)

    def filter(self, func):
        return list(filter(func, self.users))
      

class Rule8:
    def __init__(self, users: Users):
        self.users: users

# 使用例
rule8 = Rule8()
