'''
3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
'''

from random import random


def dfs(graph, vertex, is_visited):
    '''
    рекурсивный DFS. Берем вершину, отмечаем ее пройденной.
    Бежим по списку ее соседей, выбирая только еще не обойденные,
    и рекурсивно вызываем для них функцию
    '''
    if vertex not in is_visited:
        is_visited.append(vertex)
        for nxt in graph[vertex]:
            dfs(graph, nxt, is_visited)
    return is_visited


def adjacency_maker(adjacency_dictionary, size, sparsity):
    '''случайная генерация списка смежности'''
    for i in range(size):
        adjacency_vector = []
        for j in range(size):
            if i != j and random() <= (1 / sparsity):
                adjacency_vector.append(j)
        adjacency_dictionary[i] = tuple(adjacency_vector)
    return adjacency_dictionary


g = {}
sz = int(input('Введите количество вершин дерева: '))
print('Разреженность дерева - положительное вещественное число. '
      '1 - все вершины связаны со всеми')
sp = float(input('Введите разреженность дерева: '))

g = adjacency_maker(g, sz, sp)
print(f'Список смежности: {g}')

v = int(input('Введите название вершины: '))
print(f'Список обойденных вершин: {dfs(g, v, [])}')

''' Пример из урока
g = {
    0: [1, 8],
    1: [0],
    2: [3, 4, 5, 8],
    3: [2],
    4: [2, 7],
    5: [2, 6],
    6: [5, 8],
    7: [4, 6],
    8: [0, 2, 6]
}
'''
'''Ответ [0, 1, 8, 2, 3, 4, 7, 6, 5]'''
