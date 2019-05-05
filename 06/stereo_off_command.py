from command import Command


class StereoOffCommand(Command):

    def __init__(self, stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.off()

    def undo(self):
        self.stereo.on()
        self.stereo.set_CD()
        self.stereo.set_volume(11)
