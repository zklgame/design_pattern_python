from quackable import Quackable


class GooseAdapter(Quackable):

    def __init__(self, goose):
        super().__init__()
        self.goose = goose

    def quack(self):
        self.goose.honk()
        self.notify_observers()
