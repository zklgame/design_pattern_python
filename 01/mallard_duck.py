from duck import Duck
from fly_behavior import FlyWithWings
from quack_behavior import Quack


class MallardDuck(Duck):

    def __init__(self):
        super().__init__(FlyWithWings, Quack)

    def display(self):
        print("I'm a real Mallard duck.")
