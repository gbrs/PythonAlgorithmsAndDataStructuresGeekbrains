'''2.4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
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


'''
n = int(input("Введите количество элементов ряда: "))

sum_ = 0

print(uroboros(sum_, n))
'''

cProfile.run('uroboros(0, 980)')

'''
-----АНАЛИЗ-----

"les_4_task_1a.uroboros(0, 10)"
10 loops, best of 5: 9.72 usec per loop

"les_4_task_1a.uroboros(0, 100)"
10 loops, best of 5: 143 usec per loop

"les_4_task_1a.uroboros(0, 200)"
10 loops, best of 5: 366 usec per loop

"les_4_task_1a.uroboros(0, 980)"
10 loops, best of 5: 3.05 msec per loop

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.004    0.004 <string>:1(<module>)
    980/1    0.004    0.000    0.004    0.004 les_4_task_1a.py:9(uroboros)
        1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''

# python -m timeit -n 10 -s "import les_4_task_1a" "les_4_task_1a.uroboros(0, 980)"
