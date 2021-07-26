"""
A* Search with two heuristics: Manhattan distance, Euclidean distance
"""

import numpy as np


class AStar:

    def __init__(self, start, goal):

        self.path = []
        self.expanded = []
        self.parent = {}
        self.start = start
        self.goal = goal

    def search(self, nodes, heuristic):
        """
        f(n) = g(n) + h(n)
        """
        open_list = []
        closed_list = []

        open_list.append(self.start)
        self.parent[self.start] = self.start

        while len(open_list) > 0:
            current = None

            if heuristic == "euclid":
                for node in open_list:
                    if current is None or self.euclidean_distance(node, self.goal) < self.euclidean_distance(current, self.goal):
                        current = node
            else:                           # Manhattan
                for node in open_list:
                    if current is None or self.manhattan_distance(node, self.goal) < self.manhattan_distance(current, self.goal):
                        current = node

            if current is None:
                return None                 # Path does not exist

            if current == self.goal:

                goal_node = current
                while goal_node is not self.start:
                    self.path.append(goal_node)
                    goal_node = self.parent[goal_node]

                self.path.append(self.start)
                self.path.reverse()
                return self.path

            neighbor = nodes.get(current)

            if neighbor is not None:
                for n in neighbor:

                    if n not in open_list and n not in closed_list:
                        open_list.append(n)
                        self.parent[n] = current

                    else:
                        if n in closed_list:
                            closed_list.remove(n)
                            open_list.append(n)

            open_list.remove(current)
            closed_list.append(current)
            self.expanded.append(current)

        return None         # Path does not exist

    @staticmethod
    def euclidean_distance(a, b):

        a = np.array(a)
        b = np.array(b)
        return np.linalg.norm(a - b)

    @staticmethod
    def manhattan_distance(a, b):

        return abs(a[0] - b[0]) + abs(a[1] - b[1])
