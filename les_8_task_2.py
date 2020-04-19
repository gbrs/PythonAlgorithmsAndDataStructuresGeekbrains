'''
2. Доработать алгоритм Дейкстры (рассматривался на уроке),
чтобы он дополнительно возвращал список вершин, которые необходимо обойти.
'''

import collections

def dijkstra(start, finish, matrix):
    '''
    алгоритм Дейкстры, возвращающий список расстояний до всех вершин от вершины start
    и путь от start до finish
    '''

    # создаем списки: distances - расстояний от start до всех остальных,
    # parents - для каждой вершины сосед сверху, наиболее близкий к start
    # is_visited - уже пройденные алгоритмом вершины
    parents = [None] * len(matrix)
    is_visited = [False] * len(matrix)
    distances = [float('inf')] * len(matrix)
    distances[start] = 0

    # начинаем с вершины start
    min_dist = 0
    min_vertex = start

    while min_dist < float('inf'):

        # исследуем вершину min_vertex с минимальным значением дистанции;
        # отмечаем,что обошли ее
        i = min_vertex
        is_visited[i] = True

        # расчет дистанций от min_vertex до соседей снизу и
        # замена их, если найдена дистанция меньше
        for j in range(len(matrix)):
            if distances[i] + matrix[i][j] < distances[j]:
                distances[j] = distances[i] + matrix[i][j]
                parents[j] = i

        # поиск среди вершин, до которых уже определена дистанция,
        # но которые ещё не помечены обойденными,
        # вершины с самой маленькой дистанцией.
        # Следующий цикл будем исследовать её соседей
        min_dist = float('inf')
        for i in range(len(matrix)):
            if not is_visited[i] and distances[i] < min_dist:
                min_dist = distances[i]
                min_vertex = i

    # Теперь очередью описываем самый короткий путь от start до finish,
    # пользуясь тем, что parent для каждой вершины -
    # та из соседок, которая наиболее близка к start.
    # Бежим к родителю, от него к его родителю и т.д.
    # Но сначала обрабатываем случай, когда finish - несвязная вершина
    if not parents[finish]:
        return distances, 'oops'
    way_to_finish = collections.deque([finish])
    i = finish
    while parents[i] != start:
        way_to_finish.appendleft(parents[i])
        i = parents[i]
    way_to_finish.appendleft(start)

    return distances, way_to_finish


g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]

# ноликами в исходной матрице обозначены несвязанные вершины,
# заменяю их бесконечностями
for i in range(len(g)):
    for j in range(len(g)):
        if i != j and g[i][j] == 0:
            g[i][j] = float('inf')
# print(*g, sep='\n')

s = int(input('От какой вершины двигаемся? '))
f = int(input('До какой вершины двигаемся? '))

d, w = dijkstra(s, f, g)

print(f'Список расстояний от вершины {s} до всех вершин: {d}')
if w == 'oops':
    print(f'Пути из вершины {s} в вершину {f} не существует')
else:
    print(f'Путь длиной {d[f]} от вершины {s} до вершины {f}: {list(w)}')
