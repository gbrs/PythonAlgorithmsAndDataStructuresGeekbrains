'''4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
'''


# рекурсивный вариант

import cProfile

def uroboros(sum_, n):
    if n < 2:
        sum_ = 1
    else:
        sum_ = uroboros(sum_, n - 1) + 1 / (-2) ** (n - 1)
    return sum_


n = 900

sum_ = 0

cProfile.run('uroboros(0, 900)')

# print(uroboros(sum_, n))



'''Стадия 1. Программа не работает: не понимаю почему...
Стадия 2. Программа работает: не понимаю почему...
'''

# python3 -m timeit -n 10 -s "import Пробы" "Пробы.uroboros(0, 10)"
# python3 -m timeit -n 100 -s "import Пробы" "Пробы.uroboros(0, 900)"
