from state import State
from copy import deepcopy
import networkx as nx


def generateTree(system, units):

    G = nx.DiGraph()
    unique_states = []
    unchecked_states = [State(system, None)]

    while len(unchecked_states) != 0:
        current = unchecked_states.pop()
        if current not in unique_states:
            G.add_node(len(unique_states), state=current)
            if current.pvState:
                G.add_weighted_edges_from(
                    [(unique_states.index(current.pvState), len(unique_states), current.intense)])
            unique_states.append(current)
            next_states = get_possible_states(current, units)
            unchecked_states.extend(next_states)
        else:
            G.add_weighted_edges_from([(unique_states.index(
                current.pvState), unique_states.index(current), current.intense)])

    return G, unique_states


def get_possible_states(current, units):
    states = []
    for i in range(8):
        currUnit = units[i]
        numOfTasks = current.modules[i]
        if numOfTasks != 0:
            for newUnit, prob in currUnit.transitions():
                system = deepcopy(current.modules)
                system[i] -= 1
                system[units.index(newUnit)] += 1
                states.append(
                    State(system, current, intense=units[i].intens * prob))
    return states
