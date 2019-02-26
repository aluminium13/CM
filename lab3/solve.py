from state import State
from copy import deepcopy
import networkx as nx
from numpy import transpose
from numpy.linalg import solve


def solveGraph(graph, unique_states):
    markof_m = nx.adjacency_matrix(graph).toarray()

    p = probabilities(markof_m)

    devices = [0. for _ in range(8)]
    for i, prob in enumerate(p):
        for j in range(8):
            if unique_states[i].modules[j] != 0:
                devices[j] += prob

    els = ["CPU", "RAM", "ROM", "NB", "SB", "DC", "AP", "VP"]
    for i in range(8):
        print("%3s: %-f" % (els[i], devices[i]))


def probabilities(matrix: list):
    l = len(matrix)
    m = transpose(matrix)
    for i in range(l):
        outgoing = 0
        for j in range(l):
            if i != j:
                outgoing -= matrix[i][j]
            m[i][i] = outgoing
    m[0] = [1. for _ in range(l)]
    b = [0. for _ in range(l)]
    b[0] = 1.
    return solve(m, b)
