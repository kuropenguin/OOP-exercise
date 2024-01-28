# すべてのプリミティブ型と文字列型をラップすること
class Name:
    def __init__(self, value: str):
        self.value = value

    # 他のメソッドや操作が必要な場合、ここに追加します。

class Person:
    def __init__(self, name: Name):
        self.name = name

# 使用例
name = Name("mike")
mike = Person(name)
