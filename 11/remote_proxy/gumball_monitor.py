class GumballMonitor(object):

    def __init__(self):
        self.stub = None

    def set_stub(self, stub):
        self.stub = stub

    def report(self):
        data = self.stub.get_report()
        print('Gumball Machine: ', data['location'])
        print('Current inventory: ', data['count'], ' gumballs')
        print('Current state: ', data['state'])
