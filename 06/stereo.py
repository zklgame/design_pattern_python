class Stereo(object):

    def __init__(self, name=''):
        self.name = name

    def on(self):
        print(self.name + ' stereo on!')

    def off(self):
        print(self.name + ' stereo off!')

    def set_CD(self):
        print(self.name + ' stereo set_CD.')

    def set_volume(self, volume):
        print(self.name + ' setreo set_volume to %d.' % volume)
