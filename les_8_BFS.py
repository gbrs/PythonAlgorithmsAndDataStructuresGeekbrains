import collections


def breadth_first_search(graph, start, finish):
    '''
    находит кратчайший путь из start в stop.
    Поиск в ширину. От start находим первый слой ее соседок.
    Для последних находим их соседок (второй слой). И т.д.
    '''

    # список,в котором для каждой вершины записан её сосед сверху, ближайший к start;
    # список уже просмотренных вершин;
    # очередь (FIFO) вершин, которые предстоит обойти
    parents = [None for _ in range(len(graph))]
    is_visited = [False for _ in range(len(graph))]; is_visited[start] = True
    must_see = collections.deque([start])

    # В цикле while обрабатываем элементы из списка must_see.
    # Бежим по строке текущей вершины в матрице смежности,
    # находя и отмечая её соседей (в которых еще не бывали) и пополняя ими список must_see.
    # Если список must_see опустел, а мы так и не дошли до finish,
    # значит такого пути нет.
    while must_see:

        current_vertex = must_see.pop()

        if current_vertex == finish:
            break

        for i, neighbour in enumerate(graph[current_vertex]):
            if neighbour == 1 and not is_visited[i]:
                is_visited[i] = True
                parents[i] = current_vertex
                must_see.appendleft(i)
    else:
        return f'Из вершины {start} нельзя попасть в вершину {finish}'

    # Теперь очередью описываем путь с самым коротким distance,
    # пользуясь тем, что родителем для каждой вершины
    # записана та из соседок, которая наиболее близка к start.
    # Бежим к родителю, от него к родителю родителя и т.д.
    distance = 0
    way_to_finish = collections.deque([finish])
    i = finish

    while parents[i] != start:
        distance += 1
        way_to_finish.appendleft(parents[i])
        i = parents[i]

    distance += 1
    way_to_finish.appendleft(start)

    return f'Кратчайший путь {list(way_to_finish)} из {start} в {finish} длиною {distance}'


g = [
    [0, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0]
]

s = int(input('От какой вершины идти? '))
f = int(input('До какой вершины идти? '))
print(breadth_first_search(g, s, f))
