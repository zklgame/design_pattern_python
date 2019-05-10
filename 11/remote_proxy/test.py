import unittest
from gumball_machine import GumballMachine
from skeleton import Skeleton
from stub import Stub
from gumball_monitor import GumballMonitor

class TestCase(unittest.TestCase):

    def test_remote_proxy(self):
        machine = GumballMachine(3, 'HZ')
        skeleton = Skeleton(machine)
        monitor = GumballMonitor()
        stub = Stub()

        monitor.set_stub(stub)
        stub.set_skeleton(skeleton)

        monitor.report()


if __name__ == '__main__':
    unittest.main()
