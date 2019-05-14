from dj_view import DJView


class BeatController(object):

    def __init__(self, model):
        self.model = model
        self.view = DJView(self, self.model)

    def start(self):
        self.model.on()

    def stop(self):
        self.model.off()

    def increase_bpm(self):
        bpm = self.model.get_bpm()
        self.model.set_bpm(bpm + 1)

    def decrease_bpm(self):
        bpm = self.model.get_bpm()
        self.model.set_bpm(bpm - 1)

    def set_bpm(self, bpm):
        self.model.set_bpm(bpm)
