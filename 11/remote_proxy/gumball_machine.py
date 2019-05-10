class GumballMachine(object):

    def __init__(self, count, location=''):
        self.count = count
        self.location = location
        self.state = 'Init'

    def get_report(self):
        report = dict()
        report['count'] = self.count
        report['location'] = self.location
        report['state'] = self.state
        return report
