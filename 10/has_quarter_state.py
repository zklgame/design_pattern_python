from state import State
import random


class HasQuarterState(State):

    def insert_quarter(self):
        print("You can't insert another quarter")

    def eject_quarter(self):
        print("Quarter returned")
        self.machine.set_state(self.machine.get_no_quarter_state())

    def turn_crank(self):
        print("You turned ...")
        winner = random.randint(0, 9)
        if winner == 0 and self.machine.get_count() > 1:
            self.machine.set_state(self.machine.get_winner_state())
        else:
            self.machine.set_state(self.machine.get_sold_state())

    def dispense(self):
        print("No gumball dispensed")
