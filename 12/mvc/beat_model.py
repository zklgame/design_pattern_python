class BeatModel(object):

    def __init__(self):
        super().__init__()

        self.beat_observers = []
        self.bpm_observers = []
        self.bpm = 90

    def on(self):
        self.set_bpm(90)

    def off(self):
        self.set_bpm(0)

    def set_bpm(self, bpm):
        self.bpm = bpm
        self.notify_bpm_observers()

    def get_bpm(self):
        return self.bpm

    def register_beat_observer(self, o):
        self.beat_observers.append(o)

    def remove_beat_observer(self, o):
        self.beat_observers.remove(o)

    def notify_beat_observers(self):
        for observer in self.beat_observers:
            observer.update_beat()

    def register_bpm_observer(self, o):
        self.bpm_observers.append(o)

    def remove_bpm_observer(self, o):
        self.bpm_observers.remove(o)

    def notify_bpm_observers(self):
        for observer in self.bpm_observers:
            observer.update_bpm()
