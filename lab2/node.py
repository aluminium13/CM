import simpy
import random
import math
from data import env


class Unit:

    def __init__(self, name, tau, cores=1):
        self.name = name
        self.tau = tau
        self.processing_unit = simpy.Resource(env, capacity=cores)
        self.queue = []
        self.conns = []
        self.probs = []
        self.timesInQueue = 0

        # stats
        self.t_used = 0
        self.taskComputed = 0

    def add_conn(self, module, probability):
        self.conns.append(module)
        self.probs.append(probability)

    def add_task(self, task):
        self.queue.append(task)

    def moveTaskTo(self, task):
        r = random.uniform(0, 1)
        movProb = 0
        if len(self.probs) == 0:
            return
        for i in range(len(self.probs)):
            movProb += self.probs[i]
            if movProb > r:
                self.conns[i].add_task(task)
                self.conns[i].timesInQueue += 1
                return

    def process(self):
        while True:
            if len(self.queue) != 0:
                with self.processing_unit.request() as req:
                    yield req
                    task = self.queue.pop(0)
                    yield env.timeout(self.tau)
                    self.t_used += self.tau
                    self.taskComputed += 1
                    self.moveTaskTo(task)
                    # if self.name == 'CPU' and self.taskComputed == 100:
                    #     env.exit()
            else:
                yield env.timeout(1)
