'''
1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.
'''

from random import randint


def bubble(arr):
    '''
    Сортирует пузырьком: гонит справа налево самые большие числа. Указатель left
    ставим на 0 позицию и толкаем справа налево к leftу самое большое число.
    Запоминаем при этом место, где в последний раз пузырек сработал:
    влево от этого места все числа уже и так отсортированы. left смещаем именно сюда,
    а не просто на шаг вправо.
    '''

    left = 0

    while left < size - 1:
        right = size - 1
        last = right
        while right > left:
            if arr[right] > arr[right - 1]:
                last = right
                arr[right], arr[right - 1] = arr[right - 1], arr[right]
            # для прояснения механизма работы print(left, right, last, arr)
            right -= 1
        left = last


size = 10
# удачный пример a = [92, 69, 81, 46, 20, 42, 28, -19, -1, 60]
a = [randint(-100, 99) for i in range(size)]
print(a)

bubble(a)
print(a)
