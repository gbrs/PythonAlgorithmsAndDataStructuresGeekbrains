'''2_3. Сформировать из введенного числа обратное по порядку входящих в него цифр
и вывести на экран. Например, если введено число 3486, надо вывести 6843
'''

'''переворот при помощи арифметических действий'''

import sys

number = int(input("Введите натуральное число: "))
new_number = 0

while number > 0:
    new_number = new_number * 10 + number % 10
    number //= 10

print(f'"Обратное" число: {new_number}')

# ---АНАЛИЗ---

print(f'Моя система: версия Python и разрядность - {sys.version}, платформа - {sys.platform}')

catalog = number, new_number
names = 'number', 'new_number'
memory_size = 0

for i in range(len(catalog)):
    print(f'{names[i]}, принадлежащий {catalog[i].__class__}, указывает на ячейку '
          f'{id(catalog[i])} и занимает {sys.getsizeof(catalog[i])} байт')
    memory_size += sys.getsizeof(catalog[i])

print(f'Итого данные занимают {memory_size} байт')

'''Пример числа: 3141592653589793238462643383279502884197169399375105820974944
'''

'''---РЕЗУЛЬТАТЫ АНАЛИЗА---
Моя система: версия Python и разрядность - 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)], платформа - win32
number, принадлежащий <class 'int'>, указывает на ячейку 140726277464688 и занимает 24 байт
new_number, принадлежащий <class 'int'>, указывает на ячейку 2218551235504 и занимает 52 байт
Итого данные занимают 76 байт
'''
