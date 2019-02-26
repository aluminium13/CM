import simpy
from task import Task
from node import Unit
from data import env, until, statistics


cpu = Unit('CPU', 1, 1)
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

cpu.queue = [Task() for _ in range(5)]

env.process(cpu.process())
env.process(ram.process())
env.process(rom.process())
env.process(nb.process())
env.process(sb.process())
env.process(dc.process())
env.process(ap.process())
env.process(vp.process())


env.run(until=until)
statistics([cpu, ram, rom, nb, sb, dc, ap, vp])