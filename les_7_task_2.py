'''
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
'''

from random import randint


def merger(arr):
    arr.sort()


size = 10
a = [randint(0, 49) for i in range(size)]
print(a)

merger(a)
print(a)