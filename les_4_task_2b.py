'''2. Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное
и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.
'''

import cProfile
from math import ceil  # округление вверх


def main(number_prime, Sieve_size, start, cnt_prime):
    '''основное тело программы, спрятанное в функцию
    '''

    # последовательно достраиваем решето Эратосфена
    # пока не найдем достаточно простых чисел
    while cnt_prime < number_prime:
        stop = start + Sieve_size
        erat(start, stop)
        cnt_prime += sieve[start:stop].count(True)
        start += Sieve_size

    # поиск нужного по счёту простого числа (от конца к началу).
    # Не нашёл нужный встроенный метод для списков
    i = stop
    while cnt_prime >= number_prime:
        i -= 1
        if sieve[i]:
            cnt_prime -= 1
    else:
        return i


def erat(start, stop):
    '''строит решето Эратосфена для элементов от start до stop
    '''

    # достраиваю к решету Sieve_size элементов True.
    # Наверняка можно было и без цикла решить, но "нешмогла"
    for k in range(Sieve_size):
        sieve.append(True)

    # заполнение Falseами первой части решета.
    # Не смог придумать как не выделять этот случай
    if start == 0:
        sieve[0] = sieve[1] = False
        for k in range(2, stop // 2):
            if sieve[k]:
                for j in range(2 * k, stop, k):
                    sieve[j] = False

    # заполнение Falseами всех остальных частей решета
    else:
        for k in range(2, stop // 2):
            if sieve[k]:
                for j in range(ceil(start / k) * k, stop, k):
                    sieve[j] = False


# Решето; размер блоков, которыми последовательно достраиваем решето;
# начало очередного блока; счетчик найденных простых чисел.
''' Как переменные делать глобальными? Пайтон ругается на неопреленность переменных внутри функции
даже после global ... Поэтому всё передал "ручками" в функцию main. А erat не ругался ни на что...
'''
sieve = []
Sieve_size = 1000
start = 0
cnt_prime = 0

''' отключенная часть программы: ввод и вывод
number_prime = int(input("Какое по счету простое число вы хотите найти? "))
print(main(number_prime, Sieve_size, start, cnt_prime))
'''

cProfile.run('main(5000, 1000, 0, 0)')

# Проверка: 96 - 503, 1000 - 7919, 5000 - 48611


'''
-----АНАЛИЗ-----
 

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.233    0.233 <string>:1(<module>)
        1    0.001    0.001    0.233    0.233 les_4_task_2b.py:11(main)
       49    0.177    0.004    0.231    0.005 les_4_task_2b.py:34(erat)
        1    0.000    0.000    0.233    0.233 {built-in method builtins.exec}
    71800    0.047    0.000    0.047    0.000 {built-in method math.ceil}
    49000    0.006    0.000    0.006    0.000 {method 'append' of 'list' objects}
       49    0.001    0.000    0.001    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        
Сложность оценить не могу. "Гугл говорит, что" сложность "эратосфена" - n*log(log n)
Данное решение намного быстрее предыдущего "переборного" решения через цикл.
'''

# python -m timeit -n 10 -s "import les_4_task_2b" "les_4_task_2b.main(10, 1000, 0, 0)"
