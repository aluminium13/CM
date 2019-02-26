from system import createSystem
from tree import generateTree
from solve import solveGraph

def printStates(states):
    for i in range(len(states)):
        states[i].printState(i)

def printConnections(edges, states, typeOut = "all"):
    if typeOut == "all":
        print(edges)
    elif isinstance(typeOut, int):
        for i in edges:
            if i[0] == typeOut:
                print(i[0], "->", i[1])

def graphOut(G):
    import matplotlib.pyplot as plt
    import networkx as nx
    #T = nx.dfs_tree(G, source=0)
    #nx.draw(T,  with_labels=True)
    nx.draw_shell(G, with_labels=True)
    plt.savefig('tree.png')
    plt.show()


# cpu, ram, rom, nb, sb, dc, ap, vp
# create a system that contains current states + list of units that matches states by indexes
system, units = createSystem(3)

# create graph & get list of states
graph, unique_states = generateTree(system, units)

print("Number of states: ", len(unique_states))
#printConnections(graph.edges,unique_states, 0)
#graphOut(graph)
# printStates(unique_states)
#print(unique_states)
# solve graph, get stationary probabilities for each state & time loaded for each device
solveGraph(graph, unique_states)

