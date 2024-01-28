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
