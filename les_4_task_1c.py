'''2.4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
'''

# преднамерено усложненный рекурсивный вариант

import cProfile

def adder(sum_, n):
    if n < 2:
        sum_ += 1
    else:
        sum_ = adder(sum_, n - 1) + divider(n)
    return sum_

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

"les_4_task_1c.adder(0, 10)"
10 loops, best of 5: 18.3 usec per loop

"les_4_task_1c.adder(0, 100)"
10 loops, best of 5: 1.57 msec per loop

"les_4_task_1c.adder(0, 200)"
10 loops, best of 5: 6.38 msec per loop

"les_4_task_1c.adder(0, 980)"
10 loops, best of 5: 188 msec per loop

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.344    0.344 <string>:1(<module>)
480689/979    0.340    0.000    0.340    0.000 les_4_task_1c.py:16(divider)
    980/1    0.004    0.000    0.344    0.344 les_4_task_1c.py:9(adder)
        1    0.000    0.000    0.344    0.344 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''

# python -m timeit -n 10 -s "import les_4_task_1c" "les_4_task_1c.adder(0, 980)"
