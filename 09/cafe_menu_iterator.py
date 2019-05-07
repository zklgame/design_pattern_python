from iterator import Iterator


class CafeMenuIterator(Iterator):

    def __init__(self, items):
        self.items = items
        self.position = 0

    def next(self):
        menu_item = self.items[self.position]
        self.position += 1
        return menu_item

    def has_next(self):
        if self.position >= len(self.items):
            return False
        else:
            return True
