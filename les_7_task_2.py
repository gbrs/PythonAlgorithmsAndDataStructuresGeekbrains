'''
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
'''

from random import randint


def merger(arr):
    '''
    Сортировка слиянием. Разделение ~пополам производится "срезами"
    до матриц с одним элементом. Слияние производится с использованием методов массивов
    pop, append и extend
    '''
    # print('/', arr)  # для контроля процесса разделения
    if len(arr) < 2:
        return arr

    # разделяем
    left = merger(arr[0 : len(arr)//2])
    right = merger(arr[len(arr)//2 : len(arr)])

    # сливаем
    total = []
    while len(left) > 0 and len(right) > 0:
        total.append(left.pop(0) if left[0] < right[0] else right.pop(0))
        # print('*', total)  # для контроля процесса слияния
    else:
        if len(left) != 0:
            total.extend(left)
        else:
            total.extend(right)
    # print('*', total)  # для контроля процесса слияния
    return total


size = 10
a = [randint(0, 49) for i in range(size)]
print(a)

a = merger(a)
print(a)
