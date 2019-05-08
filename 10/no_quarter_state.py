from state import State


class NoQuarterState(State):

    def insert_quarter(self):
        print("You inserted a quarter")
        self.machine.set_state(self.machine.get_has_quarter_state())

    def eject_quarter(self):
        print("You haven't inserted a quarter")

    def turn_crank(self):
        print("You turned, but there's no quarter")

    def dispense(self):
        print('You need to pay first')
