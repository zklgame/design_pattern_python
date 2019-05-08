from sold_out_state import SoldOutState
from no_quarter_state import NoQuarterState
from has_quarter_state import HasQuarterState
from sold_state import SoldState
from winner_state import WinnerState


class GumballMachine(object):

    def __init__(self, count):
        self.sold_out_state = SoldOutState(self)
        self.no_quarter_state = NoQuarterState(self)
        self.has_quarter_state = HasQuarterState(self)
        self.sold_state = SoldState(self)
        self.winner_state = WinnerState(self)

        self.state = self.sold_out_state
        self.count = count
        if self.count > 0:
            self.state = self.no_quarter_state

    def insert_quarter(self):
        self.state.insert_quarter()

    def eject_quarter(self):
        self.state.eject_quarter()

    def turn_crank(self):
        self.state.turn_crank()
        self.state.dispense()

    def set_state(self, state):
        self.state = state

    def get_sold_out_state(self):
        return self.sold_out_state

    def get_no_quarter_state(self):
        return self.no_quarter_state

    def get_has_quarter_state(self):
        return self.has_quarter_state

    def get_sold_state(self):
        return self.sold_state

    def get_winner_state(self):
        return self.winner_state

    def release_ball(self):
        print('A gumball comes rolling out the slot ...')
        if self.count:
            self.count -= 1

    def get_count(self):
        return self.count

    def __str__(self):
        res = []
        res.append('Inventory: %d gumball%s.' % (self.count, 's' if self.count > 1 else ''))
        res.append('\nMachine is ')
        if self.state == self.has_quarter_state:
            res.append('waiting for turn of crank')
        elif self.state == self.no_quarter_state:
            res.append('waiting for quarter')
        elif self.state == self.sold_out_state:
            res.append('sold out')
        elif self.state == self.sold_state:
            res.append('delivering a gumball')
        res.append('\n')

        return ''.join(res)
