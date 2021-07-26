import random
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WINDOW_HEIGHT = 601
WINDOW_WIDTH = 601
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
SCREEN.fill(BLACK)
pygame.display.set_caption("Maze")

maze_size = 30
cell_width = WINDOW_WIDTH // maze_size
maze = [[0 for j in range(maze_size)] for i in range(maze_size)]

start = (0, 0)      # maze[0][0]
goal = (maze_size - 1, maze_size - 1)
visited = []

neighbor_dict = {}
maze_graph = {}     # dead-ends not added


def neighbors(x, y):
    return [(r, c) for r in range(x - 1, x + 2) for c in range(y - 1, y + 2)
            if (-1 < r < maze_size and -1 < c < maze_size) and ((r == x - 1 and c == y) or
                                                                (r == x + 1 and c == y) or (r == x and c == y - 1)
                                                                or (r == x and c == y + 1)) and (r, c) not in visited]


def direction(current, next_node):

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


def dfs(vertex, step):          # generate maze with randomized depth first search

    if vertex in visited:
        return
    else:
        visited.append(vertex)                      # mark as visited
        maze[vertex[0]][vertex[1]] = step
        neighs = neighbors(vertex[0], vertex[1])
        neighbor_dict[vertex] = neighbors(vertex[0], vertex[1])

        while len(neighs) != 0:

            idx = random.randint(0, len(neighs) - 1)    # index of random neighbor
            next_vertex = neighs[idx]                   # pick one
            dfs(next_vertex, step+1)
            neighs.remove(next_vertex)

        return


def draw_map():

    w = cell_width

    for x in range(0, maze_size+2):
        for y in range(0, maze_size+2):
            pygame.draw.line(SCREEN, WHITE, [x, y*w], [WINDOW_WIDTH, y*w])          # top of cell
            pygame.draw.line(SCREEN, WHITE, [x * w, y], [x * w, WINDOW_HEIGHT])     # right of

    pygame.display.update()


def remove_walls(cell, next_cell):

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


def remove(idx, num):

    if idx + 1 == len(neighbor_dict):
        return
    else:
        cell = dict_keys[idx]

        for j in range(len(dict_values[idx])):
            if maze[dict_values[idx][j][0]][dict_values[idx][j][1]] == num + 1:
                nxt = dict_values[idx][j]

                if cell not in maze_graph.keys():
                    maze_graph[cell] = [nxt]
                else:
                    maze_graph[cell] = [*maze_graph.get(cell), nxt]

                remove_walls(cell, nxt)
                remove(dict_keys.index(nxt), num+1)


def run_program():

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


pygame.init()
draw_map()
dfs(start, 1)

dict_keys = [k for k, v in neighbor_dict.items()]
dict_values = [v for k, v in neighbor_dict.items()]

remove(0, 1)
run_program()
