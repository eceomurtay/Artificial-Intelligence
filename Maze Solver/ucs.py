"""
Uniform Cost Search
step cost = 1 and all equal so, ~bfs
"""
from collections import deque


class UCS:

    def __init__(self, start, goal):

        self.path = []
        self.start = start
        self.goal = goal
        self.expanded = []
        self.parent = {}

    def search(self, nodes):

        frontier = deque()
        frontier.append(self.start)

        while len(frontier) != 0:

            current = frontier.popleft()
            self.expanded.append(current)

            if current == self.goal:
                return
            else:
                neighbors = nodes.get(current)
                if neighbors is not None:
                    for n in neighbors:
                        frontier.append(n)
                        self.parent[n] = current

    def find_path(self):

        goal_node = self.goal
        while goal_node is not self.start:
            self.path.append(goal_node)
            goal_node = self.parent[goal_node]

        self.path.append(self.start)
        self.path.reverse()
        return self.path
