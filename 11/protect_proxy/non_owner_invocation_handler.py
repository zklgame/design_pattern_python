from invocation_handler import InvocationHandler


class NonOwnerInvocationHandler(InvocationHandler):

    def __init__(self, person):
        super().__init__()

        self.person = person

    def invoke(self, proxy, method_name, **kwargs):
        method = getattr(self.person, method_name, None)
        if method.__name__.startswith('get'):
            return method()
        elif method.__name__ == 'set_hot_or_not_rating':
            method(**kwargs)
        elif method.__name__.startswith('set'):
            raise RuntimeError('Non-Owner Illegal Access!')
