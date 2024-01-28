import unittest
from vending.vending_machine import VendingMachine, Stocks , Accountant
from vending.drink import KindOfDrink
from vending.coin import Coin

class TestVendingMachine(unittest.TestCase):

    def test_normal_purchase(self):
        vm = VendingMachine()
        drink = vm.buy(Coin.FIVE_HUNDRED, KindOfDrink.COKE)
        charge = vm.refund()
        self.assertIsNotNone(drink)
        self.assertEqual(drink.get_kind(), KindOfDrink.COKE)
        self.assertEqual(charge.get_amount(), 400)

    def test_out_of_stock(self):
        vm = VendingMachine()
        # コーラの在庫を0に設定
        vm.stocks = Stocks(0, 10, 10)
        drink = vm.buy(Coin.ONE_HUNDRED, KindOfDrink.COKE)
        self.assertIsNone(drink)

    def test_insufficient_change(self):
        vm = VendingMachine()
        # 100円玉の在庫を0に設定
        vm.accountant = Accountant(0, 10)
        drink = vm.buy(Coin.FIVE_HUNDRED, KindOfDrink.COKE)
        self.assertIsNone(drink)

    def test_invalid_amount(self):
        vm = VendingMachine()
        drink = vm.buy(Coin.FIFTY, KindOfDrink.COKE)  # 50円は不正な金額
        self.assertIsNone(drink)

if __name__ == '__main__':
    unittest.main()
