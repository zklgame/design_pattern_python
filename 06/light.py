class Light(object):

    def __init__(self, name=''):
        self.name = name

    def on(self):
        print(self.name + ' light on!')

    def off(self):
        print(self.name + ' light off!')
