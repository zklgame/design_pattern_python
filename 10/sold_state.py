from state import State


class SoldState(State):

    def insert_quarter(self):
        print("please wait, we're already giving you a gumball")

    def eject_quarter(self):
        print("Sorry, you already turned the crank")

    def turn_crank(self):
        print("Turning twice doesn't get you another gumball!")

    def dispense(self):
        self.machine.release_ball()
        if self.machine.get_count() > 0:
            self.machine.set_state(self.machine.get_no_quarter_state())
        else:
            print('Oops, out of gumballs!')
            self.machine.set_state(self.machine.get_sold_out_state())
