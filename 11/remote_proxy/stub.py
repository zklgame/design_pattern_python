class Stub(object):

    def __init__(self):
        self.skeleton = None

    def set_skeleton(self, skeleton):
        self.skeleton = skeleton

    def get_report(self):
        report = self.skeleton.get_report()
        return report
