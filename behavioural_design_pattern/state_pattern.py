class ComputerState:
    name = 'state'
    allowed = []

    def switch(self, state):
        if state.name in self.allowed:
            print("Current: ", self, " => switched to new state", state.name)
            self.__class__ = state
        else:
            print("Current: ", self, " +> switched to ", state.name, "not possible.")

    def __str__(self):
        return self.name


class Off(ComputerState):
    name = "off"
    allowed = ["on"]


class On(ComputerState):
    name = "on"
    allowed = ["off", "suspend", "hibernate"]


class Suspend(ComputerState):
    name = "suspend"
    allowed = ["on"]


class Hibernate(ComputerState):
    name = "hibernate"
    allowed = ["om"]

class Computer:
    def __init__(self):
        self.state = Off()

    def change(self, state):
        self.state.switch(state)