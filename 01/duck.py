import abc


class Duck(abc.ABC):

    def __init__(self, fly_behavior_class, quack_behavior_class):
        self.fly_behavior = fly_behavior_class()
        self.quack_behavior = quack_behavior_class()

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()

    def set_fly_behavior(self, fly_behavior):
        self.fly_behavior = fly_behavior

    def set_quack_behavior(self, quack_behavior):
        self.quack_behavior = quack_behavior

    def swim(self):
        print('All ducks float, even decoys!')

    @abc.abstractmethod
    def display(self):
        pass
