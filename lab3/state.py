class State:

    def __init__(self, modules: list, pvState, intense=0.0):
        self.modules = modules
        self.pvState = pvState
        self.intense = intense

    def __eq__(self, other):
        return self.modules == other.modules

    def __repr__(self):
        return str(self.modules)

    def printState(self, index):
        names = ["CPU", "RAM", "ROM", "NB", "SB", "DC", "AP", "VP"]
        string = ""
        for i in range(8):
            if self.modules[i] != 0:
                string += names[i] + ": <" + str(self.modules[i] - 1) + ",1,0>; "
            else:
                string += names[i] + ": <0,0,1>; "
        print("M" + str(index) + ": " + string)