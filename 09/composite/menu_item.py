from menu_component import MenuComponent
from null_iterator import NullIterator


class MenuItem(MenuComponent):

    def __init__(self, name, description, vegetarian, price):
        super().__init__()

        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price

    def is_vegetarian(self):
        return self.vegetarian

    def print(self):
        print(' ' + self.get_name(), end='')
        if self.is_vegetarian():
            print(' (V)', end='')
        print(', ' + str(self.get_price()), end='')
        print(' -- ' + self.get_description())

    def create_iterator(self):
        return NullIterator()
