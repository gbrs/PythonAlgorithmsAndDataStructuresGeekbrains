'''2_3. Сформировать из введенного числа обратное по порядку входящих в него цифр
и вывести на экран. Например, если введено число 3486, надо вывести 6843
'''

'''переворот "чтением" строки задом наперёд'''

import sys

number = input("Введите натуральное число: ")

print(f'"Обратное" число: {number[::-1]}')

# ---АНАЛИЗ---

print(f'Моя система: версия Python и разрядность - {sys.version}, платформа - {sys.platform}')

print(f'строка number, принадлежащая {number.__class__}, указывает на ячейку '
      f'{id(number)} и занимает {sys.getsizeof(number)} байт')

'''Пример числа: 3141592653589793238462643383279502884197169399375105820974944
'''

'''---РЕЗУЛЬТАТЫ АНАЛИЗА---
Моя система: версия Python и разрядность - 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)], платформа - win32
строка number, принадлежащая <class 'str'>, указывает на ячейку 2265203616208 и занимает 110 байт
'''