from copy import deepcopy
from math import inf

# Task of salesman
# Number of points: 5

myPoints = [
    [inf, 5,  8,  7, 3],
    [4, inf, 6, 2, 5],
    [9, 8, inf, 7, 9],
    [3, 5, 2, inf, 4],
    [1, 2, 3, 4, inf]
]

# myPoints = [
#     [inf, 14,  8,  7, 3],
#     [4, inf, 2, 2, 5],
#     [9, 8, inf, 17, 9],
#     [31, 5, 2, inf, 4],
#     [15, 5, 3, 4, inf]
# ]


def printPoints(points):
    for i in points:
        print(i)


def getMin(row):
    try:
        return min([x for x in row if x != 0])
    except ValueError:
        return 0


def getPriceForZero(points, i, j):
    minInRow = getMin(points[i])
    col = [row[j] for row in points]
    minInCol = getMin(col)
    return minInRow + minInCol


def salesman(myPoints):

    cities = deepcopy(myPoints)
    conncs = []
    fromNodes = [i + 1 for i in range(len(cities))]
    toNodes = [i + 1 for i in range(len(cities))]

    for _ in range(len(cities)):

        points = deepcopy(cities)
        size = len(cities)

        # minimize rows
        for i in range(size):
            row = points[i]
            minInRow = getMin(row)
            points[i] = [i-minInRow if i != 0 else i for i in row]

        # minimize colomns
        for j in range(size):
            col = [row[j] for row in points]
            if col.count(0) != 0:
                minInCol = getMin(col)
                col = [i-minInCol if i != 0 else i for i in col]
                for i in range(size):
                    points[i][j] = col[i]

        minPoint = {"from": 0, "to": 0, "price": 0}
        for i in range(size):
            for j in range(size):
                if points[i][j] == 0 and i != j:
                    price = getPriceForZero(points, i, j)
                    if price > minPoint["price"] and (toNodes[j], fromNodes[i]) not in conncs:
                        minPoint["from"] = i
                        minPoint["to"] = j
                        minPoint["price"] = price
        rowNum = fromNodes.pop(minPoint["from"])
        colNum = toNodes.pop(minPoint["to"])
        conncs.append((rowNum, colNum))

        del cities[minPoint["from"]]
        for row in cities:
            del row[minPoint["to"]]

    return conncs


conncs = salesman(myPoints)

import networkx as nx
import pylab as plt

G = nx.DiGraph()
for i in range(len(myPoints)):
    G.add_node(i+1)
for i in range(len(myPoints)):
    for j in range(len(myPoints[i])):
        if myPoints[i][j] == inf:
            continue
        else:
            G.add_edge((i + 1), (j + 1), weight=myPoints[i][j])

for i in conncs:
    G.add_edge(i[0], i[1])

nx.draw(G, pos=nx.shell_layout(G), arrows=True, with_labels=True, node_size=250, width=1,
        font_size=13, font_family="Consolas")

edge_labels = dict([((u, v,), d['weight']) for u, v, d in G.edges(data=True)])
nx.draw_networkx_edge_labels(G, pos=nx.shell_layout(
    G), edge_labels=edge_labels, label_pos=0.3, font_size=9)
nx.draw_networkx_edges(G, pos=nx.shell_layout(
    G), edgelist=conncs, edge_color='r', arrows=True, with_labels=True)
plt.savefig(r"Graph1.png")
plt.show()

print("Connections: " + str(conncs))
