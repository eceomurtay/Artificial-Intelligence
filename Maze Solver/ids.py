"""
Iterative Deepening Search
"""


class IDS:

    def __init__(self, start, goal, nodes):

        self.expanded_nodes = []
        self.start = start
        self.goal = goal
        self.nodes = nodes

    def iddfs(self, maximum_depth):       # iterative deepening depth first search

        for depth in range(0, maximum_depth):
            result = self.dls([self.start], self.goal, depth)
            if result is None:
                continue
            return result

    def dls(self, path, goal, depth):         # depth limited search

        current = path[-1]
        self.expanded_nodes.append(current)

        if current == goal:
            return path
        if depth <= 0:         # If reached the maximum depth, stop recursing
            return None

        cell_neighbors = self.nodes.get(current)
        if cell_neighbors is not None:
            for nb in cell_neighbors:
                new_path = list(path)
                new_path.append(nb)
                result = self.dls(new_path, goal, depth - 1)
                if result is not None:
                    return result

