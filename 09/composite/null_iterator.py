from iterator import Iterator


class NullIterator(Iterator):

    def has_next(self):
        return False

    def next(self):
        return None
