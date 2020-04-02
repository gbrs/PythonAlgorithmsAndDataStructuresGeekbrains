'''2.4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
'''

# вариант с циклом for

import cProfile

def step_by_step(sum_, n):
    for i in range(n):
        sum_ += 1 / (-2) ** i
    return sum_

'''
n = int(input("Введите количество элементов ряда: "))

sum_ = 0

print(step_by_step(sum_, n))
'''

cProfile.run('step_by_step(0, 980)')

'''
-----АНАЛИЗ-----

"les_4_task_1b.step_by_step(0, 10)"
10 loops, best of 5: 7.75 usec per loop

"les_4_task_1b.step_by_step(0, 100)"
10 loops, best of 5: 121 usec per loop

"les_4_task_1b.step_by_step(0, 200)"
10 loops, best of 5: 301 usec per loop

"les_4_task_1b.step_by_step(0, 980)"
10 loops, best of 5: 2.64 msec per loop

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.003    0.003 <string>:1(<module>)
        1    0.003    0.003    0.003    0.003 les_4_task_1b.py:9(step_by_step)
        1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''

# python -m timeit -n 10 -s "import les_4_task_1b" "les_4_task_1b.step_by_step(0, 980)"
