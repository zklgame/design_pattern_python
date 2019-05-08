from state import State


class WinnerState(State):

    def insert_quarter(self):
        print("Please wait, we're already giving you a Gumball")

    def eject_quarter(self):
        print("Please wait, we're already giving you a Gumball")

    def turn_crank(self):
        print("Turning again doesn't get you another gumball!")

    def dispense(self):
        print("YOU'RE A WINNER! You got two gumballs for your quarter")
        self.machine.release_ball()
        if self.machine.get_count() == 0:
            self.machine.set_state(self.machine.get_sold_out_state())
        else:
            self.machine.release_ball()
            if self.machine.get_count() > 0:
                self.machine.set_state(self.machine.get_no_quarter_state())
            else:
                print('Oops, out of gumballs!')
                self.machine.set_state(self.machine.get_sold_out_state())
