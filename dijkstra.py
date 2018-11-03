
import math


def dijkstra_algorithm(vertices, edges, source):
    """
    Dijkstra algorithm implementation, based on
    https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
    :param vertices: List of vertices
    :param edges: List of Edges, which are (u, v, weight) tuples
    :param source: From where to build a tree
    :return: (distance, predecessor) tuple
    """

    # Dictionary to store nodes preceding each node on the SPT from source
    predecessor = {}

    # 1 - Mark all nodes unvisited. Create a set of all the unvisited nodes called the unvisited set.
    unvisited = vertices.copy()

    # 2 - Assign to every node a tentative distance value: set it to zero for our initial node and
    # to infinity for all other nodes. Set the initial node as current.
    distance = {}
    for v in vertices:
        distance[v] = math.inf
    distance[source] = 0
    current = source

    while len(unvisited) != 0:
        # 3 - For the current node, consider all of its unvisited neighbors and calculate their tentative
        # distances through the current node. Compare the newly calculated tentative distance to the current
        # assigned value and assign the smaller one. For example, if the current node A is marked with a
        # distance of 6, and the edge connecting it with a neighbor B has length 2, then the distance to B
        # through A will be 6 + 2 = 8. If B was previously marked with a distance greater than 8 then change
        # it to 8. Otherwise, keep the current value.

        for (u, neighbor, weight) in edges:
            if u == current and neighbor in unvisited:
                new_distance = distance[current] + weight
                if new_distance < distance[neighbor]:
                    distance[neighbor] = new_distance
                    predecessor[neighbor] = current

        # 4 - Remove current node from the unvisited set. A visited node will never be checked again.
        unvisited.remove(current)

        # Skipping this for now (assume no disconnected parts of a graph):
        # 5 - If the destination node has been marked visited (when planning a route between two specific nodes)
        # or if the smallest tentative distance among the nodes in the unvisited set is infinity (when planning
        # a complete traversal; occurs when there is no connection between the initial node and remaining unvisited
        # nodes), then stop. The algorithm has finished.

        # 6 - Select the unvisited node that is marked with the smallest tentative distance, set it as the new current
        # node, and go back to step 3.
        smallest_dist = math.inf

        for node in unvisited:
            if distance[node] < smallest_dist:
                smallest_dist = distance[node]
                node_smallest_dist = node

        current = node_smallest_dist

    return distance, predecessor

if __name__ == "__main__":
    vert = [1, 2, 3, 4, 5, 6, 7, 8]
    edg = [(6, 7, 1), (5, 8, 1), (4, 8, 2), (4, 5, 1), (2, 6, 1), (2, 5, 2), (3, 4, 1), (1, 2, 2), (1, 3, 1)]

    print(dijkstra_algorithm(vert, edg, 1))


"""
Result:
({1: 0, 2: 2, 3: 1, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4}, {2: 1, 3: 1, 4: 3, 6: 2, 5: 4, 8: 4, 7: 6})
"""
