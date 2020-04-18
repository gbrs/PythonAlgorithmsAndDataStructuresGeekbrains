import collections


def breadth_first_search(graph, start, finish):
    '''находит кратчайший путь из start в stop'''

    parents = [None for _ in range(len(graph))]
    is_visited = [False for _ in range(len(graph))]
    is_visited[start] = True

    deq = collections.deque([start])

    while deq:  # пока не пустой

        curent_vertex = deq.pop()

        if curent_vertex == finish:
            # return parents
            break

        for i, neighbour in enumerate(graph[curent_vertex]):
            if neighbour == 1 and not is_visited[i]:
                is_visited[i] = True
                parents[i] = curent_vertex
                deq.appendleft(i)
    else:
        return f'Из вершины {start} нельзя попасть в вершину {finish}'

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
