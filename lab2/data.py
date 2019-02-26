import simpy

global env
env = simpy.Environment()
global until
until = 100000


def statistics(modules):
    for module in modules:
        print("%3s: tasks: %4i; time loaded: %-f" %
              (module.name, module.taskComputed, module.t_used/until))
