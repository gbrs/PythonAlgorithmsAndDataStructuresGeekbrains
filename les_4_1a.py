'''2.4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
'''

import timeit

def summator(n):
    sum_ = 0
    for i in range(n):
        sum_ += 1 / (-2) ** i
    # print(sum_)

# n = int(input())
# summator(n)

# python -m timeit -n 10 -s "import les_4_1a" "les_4_1a.summator(10)"

# "les_4_1a.summator(10)"
# 10 loops, best of 5: 9.86 usec per loop

