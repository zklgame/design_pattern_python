import unittest
from fly_behavior import *
from quack_behavior import *
from mallard_duck import MallardDuck
from model_duck import ModelDuck


class TestCase(unittest.TestCase):

    def tearDown(self):
        print('##################################')


class TestFlyBehavior(TestCase):

    def test_FlyWithWings(self):
        fly_behavior = FlyWithWings()
        fly_behavior.fly()

    def test_FlyNoWay(self):
        fly_behavior = FlyNoWay()
        fly_behavior.fly()


class TestQuackBehavior(TestCase):

    def test_Quack(self):
        quack_behavior = Quack()
        quack_behavior.quack()

    def test_Squeak(self):
        quack_behavior = Squeak()
        quack_behavior.quack()

    def test_MuteQuack(self):
        quack_behavior = MuteQuack()
        quack_behavior.quack()


class TestDuck(TestCase):

    def test_MallardDuck(self):
        duck = MallardDuck()
        self.simulate(duck)

    def test_ModelDuck(self):
        duck = ModelDuck()
        self.simulate(duck)

    def test_set_fly_behavior(self):
        duck = ModelDuck()
        self.simulate(duck)
        duck.set_fly_behavior(FlyRocketPowered())
        self.simulate(duck)

    def test_set_quack_behavior(self):
        duck = ModelDuck()
        self.simulate(duck)
        duck.set_quack_behavior(MuteQuack())
        self.simulate(duck)

    def simulate(self, duck):
        duck.display()
        duck.perform_fly()
        duck.perform_quack()
        duck.swim()


if __name__ == '__main__':
    unittest.main()
