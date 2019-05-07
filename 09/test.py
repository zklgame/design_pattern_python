import unittest
from pancake_house_menu import PancakeHouseMenu
from diner_menu import DinerMenu
from cafe_menu import CafeMenu
from waitress import Waitress


class TestWaitress(unittest.TestCase):

    def test_Waitress(self):
        pancake_menu = PancakeHouseMenu()
        diner_menu = DinerMenu()
        cafe_menu = CafeMenu()
        waitress = Waitress([pancake_menu, diner_menu, cafe_menu])

        waitress.print_menu()


if __name__ == '__main__':
    unittest.main()
