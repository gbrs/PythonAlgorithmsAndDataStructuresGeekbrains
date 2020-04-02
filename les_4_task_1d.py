'''2.4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
'''

# преднамерено усложненный рекурсивный вариант

import cProfile
import functools

def adder(sum_, n):
    if n < 2:
        sum_ += 1
    else:
        sum_ = adder(sum_, n - 1) + divider(n)
    return sum_

@functools.lru_cache()
def divider(n):
    if n < 2:
        mosq = 1
    else:
        mosq = divider(n - 1) / -2
    return mosq

'''
n = int(input("Введите количество элементов ряда: "))
sum_ = 0
print(adder(sum_, n))
'''

cProfile.run('adder(0, 980)')


'''
-----АНАЛИЗ-----

"les_4_task_1d.adder(0, 10)"
10 loops, best of 5: 4.16 usec per loop

"les_4_task_1d.adder(0, 100)"
10 loops, best of 5: 44.2 usec per loop

"les_4_task_1d.adder(0, 200)"
10 loops, best of 5: 206 usec per loop

"les_4_task_1d.adder(0, 980)"
10 loops, best of 5: 1.08 msec per loop

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.003    0.003 <string>:1(<module>)
    980/1    0.003    0.000    0.003    0.003 les_4_task_1d.py:10(adder)
  980/979    0.000    0.000    0.000    0.000 les_4_task_1d.py:17(divider)
        1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

'''

# python -m timeit -n 10 -s "import les_4_task_1d" "les_4_task_1d.adder(0, 980)"