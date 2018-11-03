import math


def bprint(vertices, distance, predecessor):
    for vertex in vertices:
        print(vertex, ":", predecessor[vertex], distance[vertex], end="    ")
    print()


def bellman_ford(vertices, edges, source):
    """
    Takes in a graph, represented as lists of vertices and edges, and fills two arrays
    (distance and predecessor) about the shortest path from the source to each vertex.
    Based on https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm
     :param vertices: List of vertices
     :param edges: List of Edges, which are (u, v, weight) tuples
     :param source: From where to build a tree
     :return: (distance, predecessor) tuple
    """

    distance = {}
    predecessor = {}

    # 1 - Initialize graph
    for vertex in vertices:
        distance[vertex] = math.inf
        predecessor[vertex] = None

    distance[source] = 0

    # 2 - Relax edges repeatedly
    for i in range(len(vertices) - 1):
        for (u, v, weight) in edges:
            if distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                predecessor[v] = u
        print("Cycle {}".format(i+1))
        bprint(vertices, distance, predecessor)

    # 3 - Check for negative-weight cycles
    for (u, v, weight) in edges:
        if distance[u] + weight < distance[v]:
            print("Graph contains a negative-weight cycle")
            return None

    return distance, predecessor


if __name__ == "__main__":

    vert = [1, 2, 3, 4, 5, 6, 7, 8]
    edg = [(6, 7, 1), (5, 8, 1), (4, 8, 2), (4, 5, 1), (2, 6, 1), (2, 5, 2), (3, 4, 1), (1, 2, 2), (1, 3, 1)]

    bellman_ford(vert, edg, 1)


"""
Result run:
~~~~~~~~~~
Cycle 1
1 : None 0    2 : 1 2    3 : 1 1    4 : None inf    5 : None inf    6 : None inf    7 : None inf    8 : None inf    
Cycle 2
1 : None 0    2 : 1 2    3 : 1 1    4 : 3 2    5 : 2 4    6 : 2 3    7 : None inf    8 : None inf    
Cycle 3
1 : None 0    2 : 1 2    3 : 1 1    4 : 3 2    5 : 4 3    6 : 2 3    7 : 6 4    8 : 4 4    
Cycle 4
1 : None 0    2 : 1 2    3 : 1 1    4 : 3 2    5 : 4 3    6 : 2 3    7 : 6 4    8 : 4 4    
Cycle 5
1 : None 0    2 : 1 2    3 : 1 1    4 : 3 2    5 : 4 3    6 : 2 3    7 : 6 4    8 : 4 4    
Cycle 6
1 : None 0    2 : 1 2    3 : 1 1    4 : 3 2    5 : 4 3    6 : 2 3    7 : 6 4    8 : 4 4    
Cycle 7
1 : None 0    2 : 1 2    3 : 1 1    4 : 3 2    5 : 4 3    6 : 2 3    7 : 6 4    8 : 4 4    
"""
