'''2. Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное
и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.
'''

import cProfile

def prime_seeker_cycle(number_prime):
    '''определение простоты числа путём последовательного деления
    на предыдущие числа
    '''

    cnt_prime = 1
    date = 2
    while cnt_prime < number_prime:
        date += 1
        for i in range(2, date // 2 + 1):
            if date % i == 0:
                break
        else:
            cnt_prime += 1
    return date


''' отключенный ввод-вывод программы
number_prime = int(input("Какое по счету простое число вы хотите найти? "))
print(prime_seeker_cycle(number_prime))
'''

cProfile.run('prime_seeker_cycle(5000)')

# Проверка: 96 - 503, 1000 - 7919, 5000 - 48611


'''
-----АНАЛИЗ-----

"les_4_task_2a.prime_seeker_cycle(10)"
10 loops, best of 5: 24.8 usec per loop

"les_4_task_2a.prime_seeker_cycle(100)"
10 loops, best of 5: 1.49 msec per loop

"les_4_task_2a.prime_seeker_cycle(1000)"
10 loops, best of 5: 234 msec per loop

"les_4_task_2a.prime_seeker_cycle(5000)"
10 loops, best of 5: 7.69 sec per loop

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    7.490    7.490 <string>:1(<module>)
        1    7.490    7.490    7.490    7.490 les_4_task_2a.py:9(prime_seeker_cycle)
        1    0.000    0.000    7.490    7.490 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        
Сложность алгоритма, видимо, O(n^2)
'''


# python -m timeit -n 10 -s "import les_4_task_2a" "les_4_task_2a.prime_seeker_cycle(10)"