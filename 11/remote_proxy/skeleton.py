class Skeleton(object):

    def __init__(self, machine):
        self.machine = machine

    def get_report(self):
        report = self.machine.get_report()
        return report
