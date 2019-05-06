import unittest
from mallard_duck import MallardDuck
from wild_turkey import WildTurkey
from turkey_adapter import TurkeyAdapter


class TestDdapter(unittest.TestCase):

    def test_turkey_adapter(self):
        duck = MallardDuck()
        turkey = WildTurkey()
        turkey_adapter = TurkeyAdapter(turkey)

        print('The Turkey says ...')
        turkey.gobble()
        turkey.fly()

        print('The Duck says ...')
        self.simulate(duck)

        print('The TurkeyAdapter says ...')
        self.simulate(turkey_adapter)

    def simulate(self, duck):
        duck.quack()
        duck.fly()


if __name__ == '__main__':
    unittest.main()
