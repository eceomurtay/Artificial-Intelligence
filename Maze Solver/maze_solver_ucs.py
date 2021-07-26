import random
import pygame
from timeit import default_timer as timer
import ucs

# n x n maze specifications

ms = input("Enter the maze size: ")
print("*******************")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WINDOW_HEIGHT = 701
WINDOW_WIDTH = 701
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
SCREEN.fill(BLACK)
pygame.display.set_caption("Maze")

maze_size = int(ms)
cell_width = WINDOW_WIDTH // maze_size

start = (0, 0)
goal = (maze_size - 1, maze_size - 1)


def neighbors(x, y, visited):               # find unvisited neighbors of given cell
    return [(r, c) for r in range(x - 1, x + 2) for c in range(y - 1, y + 2)
            if (-1 < r < maze_size and -1 < c < maze_size) and ((r == x - 1 and c == y) or
                                                                (r == x + 1 and c == y) or (r == x and c == y - 1)
                                                                or (r == x and c == y + 1)) and (r, c) not in visited]


def direction(current, next_node):          # determine the direction of next cell

    x = current[0]
    y = current[1]
    nx = next_node[0]
    ny = next_node[1]

    if nx == x + 1 and ny == y:
        return "down"
    if nx == x - 1 and ny == y:
        return "up"
    if nx == x and ny == y + 1:
        return "right"
    if nx == x and ny == y - 1:
        return "left"


def remove_walls(cell, next_cell):          # remove the wall between two adjacent cells, then update the maze

    way = direction(cell, next_cell)

    if way == "up":
        pygame.draw.line(SCREEN, BLACK, (cell_width * cell[1], cell_width * cell[0]),
                         (cell_width * cell[1] + cell_width, cell_width * cell[0]))

    elif way == "down":
        pygame.draw.line(SCREEN, BLACK, (cell_width * cell[1], cell_width * cell[0] + cell_width),
                         (cell_width * cell[1] + cell_width, cell_width * cell[0] + cell_width))

    elif way == "right":
        pygame.draw.line(SCREEN, BLACK, (cell_width * cell[1] + cell_width, cell_width * cell[0]),
                         (cell_width * cell[1] + cell_width, cell_width * cell[0] + cell_width))

    elif way == "left":
        pygame.draw.line(SCREEN, BLACK, (cell_width * cell[1], cell_width * cell[0]),
                         (cell_width * cell[1], cell_width * cell[0] + cell_width))

    pygame.display.update()


def dfs_iterative(cell, maze_graph, visited):           # generate the maze using randomized depth first search

    stack = []

    visited.append(cell)                                # add start node to stack and visited list
    stack.append(cell)

    while len(stack) != 0:

        current = stack.pop()
        neighs = neighbors(current[0], current[1], visited)

        if len(neighs) != 0:
            stack.append(current)
            idx = random.randint(0, len(neighs) - 1)        # index of random neighbor
            next_cell = neighs[idx]                         # pick it
            remove_walls(current, next_cell)                # remove the walls between them
            visited.append(next_cell)
            stack.append(next_cell)

            if current not in maze_graph.keys():
                maze_graph[current] = [next_cell]
            else:
                maze_graph[current] = [*maze_graph.get(current), next_cell]


def draw_map():

    for x in range(0, maze_size + 2):
        for y in range(0, maze_size + 2):
            pygame.draw.line(SCREEN, WHITE, [x, y * cell_width], [WINDOW_WIDTH, y * cell_width])
            pygame.draw.line(SCREEN, WHITE, [x * cell_width, y], [x * cell_width, WINDOW_HEIGHT])

    pygame.display.update()


def run_program():

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


def draw_solution(solution_path):                # draw the green solution line in the middle of cell

    for s in range(len(solution_path) - 1):
        node = solution_path[s]
        next_node = solution_path[s + 1]
        pygame.draw.line(SCREEN, (0, 255, 0),
                         (cell_width * node[1] + cell_width / 2, cell_width * node[0] + cell_width / 2),
                         (cell_width * next_node[1] + cell_width / 2, cell_width * next_node[0] + cell_width / 2))

    pygame.display.update()


def delete(solution_path):                      # delete previous one to draw other maze's solution to the screen
    for c in range(len(solution_path) - 1):
        node = solution_path[c]
        next_node = solution_path[c + 1]
        pygame.draw.line(SCREEN, BLACK,
                         (cell_width * node[1] + cell_width / 2, cell_width * node[0] + cell_width / 2),
                         (cell_width * next_node[1] + cell_width / 2, cell_width * next_node[0] + cell_width / 2))

    pygame.display.update()


def generate(num):

    visited = []
    maze_graph = {}

    pygame.init()
    draw_map()

    dfs_iterative(start, maze_graph, visited)
    run_program()

    uniform_cost = ucs.UCS(start, goal)
    start_time = timer()
    uniform_cost.search(maze_graph)
    ucs_path = uniform_cost.find_path()
    end_time = timer()

    draw_solution(ucs_path)
    run_program()

    print("Maze ", num, "\n")
    print("Time taken to find the path: ", end_time - start_time, "secs")
    print("Length of the path: ", len(ucs_path))
    print("Number of expanded nodes: ", len(uniform_cost.expanded))
    print("-------------------")

    delete(ucs_path)


generate(1)
generate(2)
