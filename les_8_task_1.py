'''
1. На улице встретились N друзей.
Каждый пожал руку всем остальным друзьям (по одному разу).
Сколько рукопожатий было?
'''

def handshake_cnt(graph):
    '''
    Подсчитываем количество рукопожатий пробегаясь по всей матрице смежности.
    Не включаем в подсчёт тех, чьи рукопожатия мы уже считали
    '''

    is_shake = [False for _ in range(len(graph))]
    cnt = 0

    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] == 1 and not is_shake[j]:
                cnt += 1
        is_shake[i] = True

    return cnt


N = int(input('Введите количество друзей: '))

# формируем матрицу смежности: все со всеми. Кроме самих себя
g = [[1 for i in range(N)] for j in range(N)]
for i in range(N):
    g[i][i] = 0
# print(*g, sep='\n')

print(handshake_cnt(g))
