import unittest
from waitress import Waitress
from menu import Menu
from menu_item import MenuItem


class TestWaitress(unittest.TestCase):

    def setUp(self):
        pancake_menu = Menu('Pancake house menu', 'Breakfast')
        diner_menu = Menu('Diner menu', 'Lunch')
        cafe_menu = Menu('Cafe menu', 'Dinner')
        dessert_menu = Menu('Dessert menu', 'Dessert of course!')

        all_menus = Menu('All menus', 'All menus combined')
        all_menus.add(pancake_menu)
        all_menus.add(diner_menu)
        all_menus.add(cafe_menu)

        diner_menu.add(MenuItem('Pasta', 'Pasta description', True, 3.89))
        diner_menu.add(dessert_menu)

        dessert_menu.add(MenuItem('Apple Pie', 'Apple Pie description', True, 1.59))

        self.waitress = Waitress(all_menus)


    def tearDown(self):
        print('######################')

    def test_inner_iterator(self):
        self.waitress.print_menu()

    def test_outer_iterator(self):
        self.waitress.print_vegetarian_menu()


if __name__ == '__main__':
    unittest.main()
