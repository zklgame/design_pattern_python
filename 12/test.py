import unittest
from adapter_pattern.goose import Goose
from adapter_pattern.goose_adapter import GooseAdapter
from decorator_pattern.quack_count import QuackCount
from factory_pattern.counting_duck_factory import CountingDuckFactory
from composite_pattern.flock import Flock
from observer_pattern.quack_observer import QuackObserver


class TestCase(unittest.TestCase):

    def setUp(self):
        print('#####################')

    def test_ducks(self):
        flock_of_ducks, flock_of_mallard = self.crate_ducks()

        print('Whole Flock Simulation')
        self.simulate(flock_of_ducks)
        print('Mallard Flock Simulation')
        self.simulate(flock_of_mallard)

        print('The ducks quacked %d times' % (QuackCount.get_quacks()))

    def test_observer_pattern(self):
        flock_of_ducks, flock_of_mallard = self.crate_ducks()
        quackologist = QuackObserver()
        flock_of_ducks.register_observer(quackologist)

        self.simulate(flock_of_ducks)


    def crate_ducks(self):
        duck_factory = CountingDuckFactory()

        mallard_duck = duck_factory.create_mallard_duck()
        redhead_duck = duck_factory.create_redhead_duck()
        duck_call = duck_factory.create_duck_call()
        rubber_duck = duck_factory.create_rubber_duck()
        goose_duck = GooseAdapter(Goose())

        flock_of_ducks = Flock()
        flock_of_ducks.add(mallard_duck)
        flock_of_ducks.add(redhead_duck)
        flock_of_ducks.add(duck_call)
        flock_of_ducks.add(rubber_duck)
        flock_of_ducks.add(goose_duck)

        flock_of_mallard = Flock()
        mallard_one = duck_factory.create_mallard_duck()
        mallard_two = duck_factory.create_mallard_duck()
        mallard_three = duck_factory.create_mallard_duck()
        mallard_four = duck_factory.create_mallard_duck()
        flock_of_mallard.add(mallard_one)
        flock_of_mallard.add(mallard_two)
        flock_of_mallard.add(mallard_three)
        flock_of_mallard.add(mallard_four)

        flock_of_ducks.add(flock_of_mallard)

        return flock_of_ducks, flock_of_mallard

    def simulate(self, duck):
        duck.quack()


if __name__ == '__main__':
    unittest.main()
