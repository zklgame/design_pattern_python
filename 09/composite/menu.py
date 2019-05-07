from menu_component import MenuComponent
from composite_iterator import CompositeIterator
from null_iterator import NullIterator
from iterator import Iterator


class Menu(MenuComponent):

        def __init__(self, name, description):
            super().__init__()

            self.menu_components = []
            self.name = name
            self.description = description
            self.visit = False

        def get_name(self):
            return self.name

        def get_description(self):
            return self.description

        def print(self):
            print(self.get_name(), end='')
            print(', ' + self.get_description())
            print('-----------------')

            # inner iterator
            for menu_component in self.menu_components:
                menu_component.print()

        def add(self, component):
            self.menu_components.append(component)

        def remove(self, component):
            self.menu_components.remove(component)

        def get_child(self, i):
            return self.menu_components[i]

        def create_iterator(self):
            if not self.visit:
                self.visit = True
                return CompositeIterator(self.iterator())
            else:
                return NullIterator()

        def iterator(self):

            class RealIterator(Iterator):

                def __init__(self, items):
                    self.items = items
                    self.position = 0

                def has_next(self):
                    if self.position >= len(self.items):
                        return False
                    else:
                        return True

                def next(self):
                    item = self.items[self.position]
                    self.position += 1
                    return item

            return RealIterator(self.menu_components)
