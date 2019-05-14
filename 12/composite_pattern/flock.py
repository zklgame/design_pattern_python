from quackable import Quackable


class Iterator(object):

    def __init__(self, quackers):
        self.quackers = quackers
        self.position = 0

    def has_next(self):
        if self.position >= len(self.quackers):
            return False
        return True

    def next(self):
        quacker = self.quackers[self.position]
        self.position += 1
        return quacker


class Flock(Quackable):

    def __init__(self):
        super().__init__()
        self.quackers = []

    def add(self, quacker):
        self.quackers.append(quacker)

    def quack(self):
        iterator = Iterator(self.quackers)
        while iterator.has_next():
            quacker = iterator.next()
            quacker.quack()

    def register_observer(self, observer):
        iterator = Iterator(self.quackers)
        while iterator.has_next():
            quacker = iterator.next()
            quacker.register_observer(observer)
