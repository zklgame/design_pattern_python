from iterator import Iterator


class DinerMenuIterator(Iterator):

    def __init__(self, items):
        self.items = items
        self.position = 0

    def next(self):
        menu_item = self.items[self.position]
        self.position += 1
        return menu_item

    def has_next(self):
        if self.position >= len(self.items) or self.items[self.position] is None:
            return False
        else:
            return True
