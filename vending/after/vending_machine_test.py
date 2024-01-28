import unittest
from vending.vending_machine import VendingMachine
from vending.drink import Drink,KindOfDrink

class TestVendingMachine(unittest.TestCase):

    def test_normal_purchase(self):
        vm = VendingMachine()
        drink = vm.buy(500, KindOfDrink.COKE)
        charge = vm.refund()
        self.assertIsNotNone(drink)
        self.assertEqual(drink.get_kind(), KindOfDrink.COKE)
        self.assertEqual(charge, 400)

    def test_out_of_stock(self):
        vm = VendingMachine()
        vm.quantity_of_coke = 0  # コーラの在庫を0に設定
        drink = vm.buy(100, KindOfDrink.COKE)
        self.assertIsNone(drink)

    def test_insufficient_change(self):
        vm = VendingMachine()
        vm.number_of_100yen = 0  # 100円玉の在庫を0に設定
        drink = vm.buy(500, KindOfDrink.COKE)
        self.assertIsNone(drink)

    def test_invalid_amount(self):
        vm = VendingMachine()
        drink = vm.buy(50, KindOfDrink.COKE)  # 50円は不正な金額
        self.assertIsNone(drink)

if __name__ == '__main__':
    unittest.main()
