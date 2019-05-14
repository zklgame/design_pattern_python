class DJView(object):

    def __init__(self, controller, model):
        self.controller = controller
        self.model = model
        model.register_beat_observer(self)
        model.register_bpm_observer(self)

    def update_bpm(self):
        bpm = self.model.get_bpm()
        if 0 == bpm:
            print('BPM offline')
        else:
            print('Current BPM: %d' % (bpm,))

    def update_beat(self):
        print('DJView beat: %d' % (100, ))
