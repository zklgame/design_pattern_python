from duck import Duck
from fly_behavior import FlyNoWay
from quack_behavior import Quack


class ModelDuck(Duck):

    def __init__(self):
        super().__init__(FlyNoWay, Quack)

    def display(self):
        print("I'm a model duck.")
