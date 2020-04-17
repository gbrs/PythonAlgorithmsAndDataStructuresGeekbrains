'''
3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану.
'''

from random import shuffle


m = 5
# удачный пример работы a = [32, 42, 20, 10, 0, 19, 85, 54, 27]
a = list(range(2*m + 1))
shuffle(a)
print(a)
# print(sorted(a))  # для визуального нахождения медианы для контроля

left = -101
right = 101

# перебираем все элементы массива, сравнивая сколько есть чисел больше и меньше него,
# пока не найдем число, у которого чисел больше и меньше него одинаковое количество.
# Учитываем, что если, например, у числа 32 чисел больше него больше, чем меньших чисел,
# то все числа меньше 33 смысла рассматривать уже нет
# (исследуем только элементы в диапазоне left < a[i] < right)
for i in range(2*m + 1):
    if left < a[i] < right:
        top = down = 0  # счетчики
        for j in range(2*m + 1):
            if a[i] < a[j]:
                top += 1
            elif a[i] > a[j]:
                down += 1
        if top == down:
            print(f'Медиана - {a[i]}')
            break
        elif top > down and a[i] > left:
            left = a[i]
        elif top < down and a[i] < right:
            right = a[i]
        # print(left, right)  # для пояснения механизма работы

# программа не доработана: не учитывает случай, когда в списке несколько медианных значений left != right
