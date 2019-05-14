from factory_pattern.abstract_duck_factory import AbstractDuckFactory
from mallard_duck import MallardDuck
from redhead_duck import RedheadDuck
from duck_call import DuckCall
from rubber_duck import RubberDuck
from decorator_pattern.quack_count import QuackCount


class CountingDuckFactory(AbstractDuckFactory):

    def create_mallard_duck(self):
        return QuackCount(MallardDuck())

    def create_redhead_duck(self):
        return QuackCount(RedheadDuck())

    def create_duck_call(self):
        return QuackCount(DuckCall())

    def create_rubber_duck(self):
        return QuackCount(RubberDuck())
