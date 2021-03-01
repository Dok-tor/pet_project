from numpy import random
from scipy.spatial import distance

def closest_node(node, nodes):
    closest_index = distance.cdist([node], nodes).argmin()
    return nodes[closest_index]

a = random.randint(1000, size=(50000, 2))

some_pt = (1, 2)

closest_node(some_pt, a)