'''2. Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное
и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.
'''

import cProfile
from math import ceil

def erat(start, stop):
    for k in range(Sieve_size):  # TODO должен быть способ проще
        sieve.append(True)
    if start == 0:
        sieve[0] = sieve[1] = False
        for k in range(2, stop // 2):
            if sieve[k]:
                for j in range(2 * k, stop, k):
                    sieve[j] = False
    else:
        for k in range(2, stop // 2):
            if sieve[k]:
                for j in range(ceil(start / k) * k, stop, k):
                    sieve[j] = False


sieve = []
Sieve_size = 1000
start = 0
cnt_prime = 0

number_prime = int(input("Какое по счету простое число вы хотите найти? "))

while cnt_prime < number_prime:
    stop = start + Sieve_size
    erat(start, stop)
    # for i in range(start, stop):
    #     if sieve[i]:
    #         print(i, end=' ')
    # print()
    cnt_prime += sieve[start:stop].count(True)  # TODO [start:stop]
    start += Sieve_size

i = stop
while cnt_prime >= number_prime:
    i -= 1
    if sieve[i]:
        cnt_prime -= 1
else:
    print('\n',  i)

# cProfile.run('prime_seeker_cycle(5000)')

# 96 - 503, 1000 - 7919, 5000 - 48611


'''
-----АНАЛИЗ-----


'''

# python -m timeit -n 10 -s "import les_4_task_2a" "les_4_task_2a.prime_seeker_cycle(10)"
