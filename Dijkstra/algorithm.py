import random
from itertools import combinations


def generator(possibility: float, size, q, r: int) -> set:   #Генератор графа
    _edges = set()
    vertexes = set([v for v in range(size)])

    for combination in combinations(vertexes, 2):
        temp = random.random()
        weight = random.randint(q, r)
        if temp < possibility:
            current_edge = (combination[0], combination[1], weight)
            _edges.add(current_edge)

    return _edges


def converter(_edges: set, size: int) -> list:    #Конвертирует матрицу смежности
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    for _edge in _edges:
        matrix[_edge[0]][_edge[1]] = _edge[2]
    return matrix


def dijkstra(_adj_matrix: list, start, size: int) -> [list, list]:   #Классическая реализация алгоритма Дейкстры
    int_max = 10**10
    distance = [int_max] * size
    visited = [False] * size
    distance[start] = 0
    last_visited = [-1] * size

    for _ in range(size - 1):
        minimum, index = int_max, -1
        for current in range(size):
            if not visited[current] and distance[current] <= minimum:
                minimum, index = distance[current], current
        visited[index] = True

        for i in range(size):
            if not visited[i] and _adj_matrix[index][i] and distance[index] != int_max \
                    and (distance[index] + _adj_matrix[index][i] < distance[i]):
                distance[i] = distance[index] + _adj_matrix[index][i]
                last_visited[i] = index

    for i in range(len(distance)):
        if distance[i] == int_max:
            distance[i] = None
            last_visited[i] = None

    return distance, last_visited


def ford_bellman(_edges: set, start, size: int) -> [list, list]:   #Классическая реализация алгоритма Форда-Беллмана
    int_max = 10**10
    distance = [int_max] * size
    distance[start] = 0
    last_visited = [-1] * size
    cnt = 1
    stop = False
    while cnt < size and not stop:
        cnt += 1
        stop = True
        for _edge in _edges:
            if distance[_edge[0]] + _edge[2] < distance[_edge[1]]:
                distance[_edge[1]] = distance[_edge[0]] + _edge[2]
                stop = False
                last_visited[_edge[1]] = _edge[0]

    for i in range(len(distance)):
        if distance[i] == int_max:
            distance[i] = None
            last_visited[i] = None

    return distance, last_visited

