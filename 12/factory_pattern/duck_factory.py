from factory_pattern.abstract_duck_factory import AbstractDuckFactory
from mallard_duck import MallardDuck
from redhead_duck import RedheadDuck
from duck_call import DuckCall
from rubber_duck import RubberDuck


class DuckFactory(AbstractDuckFactory):

    def create_mallard_duck(self):
        return MallardDuck()

    def create_redhead_duck(self):
        return RedheadDuck()

    def create_duck_call(self):
        return DuckCall()

    def create_rubber_duck(self):
        return RubberDuck()
