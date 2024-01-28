#参考 https://qiita.com/opengl-8080/items/6f0a458df9c34eccf76c

from vending.drink import Drink
from vending.vending_machine import VendingMachine

def main():
    vm = VendingMachine()
    drink = vm.buy(500, Drink.COKE)
    charge = vm.refund()

    if drink is not None and drink.get_kind() == Drink.COKE:
        print("コーラを購入しました。")
        print(f"おつりは {charge} 円です。")
    else:
        raise Exception("コーラ買えんかった(´ﾟдﾟ｀)")

if __name__ == "__main__":
    main()
