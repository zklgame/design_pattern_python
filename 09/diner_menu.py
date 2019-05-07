from menu import Menu
from menu_item import MenuItem
from diner_menu_iterator import DinerMenuIterator


class DinerMenu(Menu):

    def __init__(self):
        self.max_items = 6
        self.menu_items = [None, ] * self.max_items
        self.number_of_items = 0

        self.add_item('Vegetarian BLT',
                      "(Fakin') Bacon with lettuce & tomato on whole wheat",
                      True,
                      2.99)
        self.add_item('BLT',
                      'Bacon with lettuce & tomato on whole wheat',
                      False,
                      2.99)
        self.add_item('Soup of the day',
                      'Soup of the day, with a side of potato salad',
                      False,
                      3.29)
        self.add_item('Hotdog',
                      'A hot dog, with saurkraut, relish, onions, topped with cheese',
                      False,
                      3.05)

    def add_item(self, name, description, vegetarian, price):
        if self.number_of_items >= self.max_items:
            print("Sorry, menu is full! Can't add item to menu")
        else:
            menu_item = MenuItem(name, description, vegetarian, price)
            self.menu_items[self.number_of_items] = menu_item
            self.number_of_items += 1

    def create_iterator(self):
        return DinerMenuIterator(self.menu_items)
