from random import random as r
from math import log
from data import lmbda, mu, relevance


class Task():
    
    def __init__(self, t):
        self.t_in = t                               # час входу до системи
        self.t_new = t - (1/lmbda) * log(r())       # час коли з'явиться нова задача
        self.t_solve = - (1/mu) * log(r())          # час рішення 
        self.t_inQueque = 0                         # час в черзі (записується пізніше)
        self.t_out = 0                              # час виходу з системи (записується при виході)
        self.marker = 0                             # для FB: номер черги в котру повертається
        self.t_firstComp = 0                        # час від входу до першого потрапляння на процесор
        