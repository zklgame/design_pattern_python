####################################################
# Observer Pattern:
# 观察者模式定义了对象之间的一对多依赖。
# 这样一来，当一个对象改变状态时，它的所有依赖者都会收到通知并自动更新。
# 观察者模式提供了一种对象设计，让主题和观察者之间松耦合。
####################################################

import abc


class Subject(abc.ABC):

    @abc.abstractmethod
    def register_observer(self, observer):
        pass

    @abc.abstractmethod
    def remove_observer(self, observer):
        pass

    @abc.abstractmethod
    def notify_observers(self):
        pass
