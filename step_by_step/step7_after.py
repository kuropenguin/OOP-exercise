# ルール7．1つのクラスにつきインスタンス変数は2つまでにすること

class Contact:
    def __init__(self, phone: str, email: str):
        self.phone = phone
        self.email = email

class User:
    def __init__(self, name: str, contact: Contact):
        self.name = name
        self.contact = contact


