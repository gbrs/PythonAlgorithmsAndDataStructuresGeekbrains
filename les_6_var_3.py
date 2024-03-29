'''2_3. Сформировать из введенного числа обратное по порядку входящих в него цифр
и вывести на экран. Например, если введено число 3486, надо вывести 6843
'''

'''переворот массива, созданного на основе числа'''

import sys

number = list(input("Введите натуральное число: "))
number.reverse()

print('"Обратное" число: ', *number, sep='')

# ---АНАЛИЗ---

print(f'Моя система: версия Python и разрядность - {sys.version}, платформа - {sys.platform}')

print(f'массив number, принадлежащий {number.__class__}, указывает на ячейку '
      f'{id(number)} и занимает {sys.getsizeof(number)} байт')

'''Пример числа: 3141592653589793238462643383279502884197169399375105820974944
'''

'''---РЕЗУЛЬТАТЫ АНАЛИЗА---
Моя система: версия Python и разрядность - 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)], платформа - win32
массив number, принадлежащий <class 'list'>, указывает на ячейку 2854129022728 и занимает 656 байт
'''

'''
Решение 1 задействовало 76 байт памяти на две целочисленные переменные, решение 2 - 110 байт на строку,
решение 3 - 656 байт на массив. Лучший вариант по памяти - первый.
'''
