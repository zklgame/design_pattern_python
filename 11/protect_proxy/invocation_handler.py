import abc


class InvocationHandler(abc.ABC):

    @abc.abstractmethod
    def invoke(self, proxy, method, *kwargs):
        pass
