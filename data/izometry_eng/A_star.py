import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(graph, start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic(start, goal)

    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor, cost in graph[current].items():
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    total_path.reverse()
    return total_path

def path_to_edges(path):
    return [(path[i], path[i + 1]) for i in range(len(path) - 1)]



# 0 - нет стен
# 1 - стена сверху
# 2 - стена слева


grid = [[(1, 2), 1, (1, 2), 1, 1, 1, 1],
        [2, 0, 2, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0],
        [2, 0, 1, 1, 1, 2, 0],
        [2, 0, 0, 0, 0, 2, 0],
        [2, 0, 0, 0, 0, 2, 0],
        [2, 0, 0, 0, 0, 1, 0]]


def create_graph(grid): #преобразование списка в граф
    graph = dict()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            graph[(row, col)] = dict()
            cell = graph[(row, col)]
            if 0 <= row < len(grid) - 1:
                if any([grid[row + 1][col] in [0, 2] and isinstance(grid[row + 1][col], int),
                        isinstance(grid[row + 1][col], tuple) and 1 not in grid[row + 1][col]]):
                    cell[(row + 1, col)] = 1
                else:
                    cell[(row + 1, col)] = 10 ** 5

            if 0 < row <= len(grid) - 1:
                if any([grid[row][col] in [0, 2] and isinstance(grid[row][col], int),
                        isinstance(grid[row][col], tuple) and 1 not in grid[row][col]]):
                    cell[(row - 1, col)] = 1
                else:
                    cell[(row - 1, col)] = 10 ** 5

            if 0 <= col < len(grid[0]) - 1:
                if any([grid[row][col + 1] in [0, 1] and isinstance(grid[row][col + 1], int) == 0,
                        isinstance(grid[row][col + 1], tuple) and 1 not in grid[row][col + 1]]):
                    cell[(row, col + 1)] = 1
                else:
                    cell[(row, col + 1)] = 10 ** 5
            if 0 < col <= len(grid[0]) - 1:
                if any([grid[row][col] in [0, 1] and isinstance(grid[row][col], int) == 0,
                        isinstance(grid[row][col], tuple) != 0 and 1 not in grid[row][col]]):
                    cell[(row, col - 1)] = 1
                else:
                    cell[(row, col - 1)] = 10 ** 5
    return graph


graph = create_graph(grid)
start = (0, 0)
goal = (2, 2)

path = a_star(graph, start, goal)
print(path)