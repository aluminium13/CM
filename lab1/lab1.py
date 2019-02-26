from smoFIFO import sys_FIFO
from smoFB import sys_FB
from data import mu, lmbda, n

print("lambda = " + str(lmbda))
print("mu = " + str(mu))
print("n = " + str(n))
print("====================== FIFO =========================")

fifo = sys_FIFO(n)
fifo.start()

print("======================= FB ==========================")
fb = sys_FB(n, 0.01)
fb.start()

print("=====================================================")
