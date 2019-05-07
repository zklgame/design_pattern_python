from iterator import Iterator


class CompositeIterator(Iterator):

    def __init__(self, iterator):
        super().__init__()
        self.stack = [iterator, ]

    def has_next(self):
        if len(self.stack) == 0:
            return False

        iterator = self.stack[-1]
        if iterator.has_next():
            return True
        else:
            self.stack.pop()
            return self.has_next()

    def next(self):
        iterator = self.stack[-1]
        item = iterator.next()
        next_iterator = item.create_iterator()
        if next_iterator.has_next():
            self.stack.append(next_iterator)
        return item
