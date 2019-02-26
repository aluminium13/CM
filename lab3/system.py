import random
import math


class Unit:

    """
    class that defines a unit in modeling system
    """

    def __init__(self, name, tau):
        self.name = name
        self.intens = 1/tau
        self.conns = []
        self.probs = []

    def add_conn(self, module, probability):
        self.conns.append(module)
        self.probs.append(probability)

    def transitions(self):
        return zip(self.conns, self.probs)


# create system with all connections
def createSystem(numberOfTasks=5):

    cpu = Unit('CPU', 1)
    ram = Unit('RAM', 3)
    rom = Unit('ROM', 4)
    nb = Unit('NB', 2)
    sb = Unit('SB', 4)
    dc = Unit('DC', 30.0)
    ap = Unit('AP', 20.0)
    vp = Unit('VP', 25.0)

    # cpu connections
    cpu.add_conn(nb, 1)
    # RAM connections
    ram.add_conn(nb, 1.0)
    # ROM connections
    rom.add_conn(nb, 1.0)
    # North Bridge connections
    nb.add_conn(sb, 0.2)
    nb.add_conn(ram, 0.28)
    nb.add_conn(rom, 0.2)
    nb.add_conn(cpu, 0.32)
    # South Bridge connections
    sb.add_conn(nb, 0.2)
    sb.add_conn(ap, 0.29)
    sb.add_conn(vp, 0.29)
    sb.add_conn(dc, 0.22)
    # Disk Control connections
    dc.add_conn(sb, 1.0)
    # Audio Prossesor connections
    ap.add_conn(cpu, 1.0)
    # Video Prossesor connections
    vp.add_conn(cpu, 1.0)

    system = [0 for _ in range(8)]
    system[0] = numberOfTasks
    return system,  [cpu, ram, rom, nb, sb, dc, ap, vp]
