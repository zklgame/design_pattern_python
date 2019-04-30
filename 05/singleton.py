class Singleton(object):

    _instance = None

    cid = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def set_id(self, cid):
        self.cid = cid

