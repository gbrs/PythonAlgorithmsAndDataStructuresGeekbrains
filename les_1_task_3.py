'''3. Написать программу, которая генерирует в указанных пользователем границах:
a. случайное целое число,
b. случайное вещественное число,
c. случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
'''

import random
import time


print("Сгенерируем случайное целое число в указанном диапазоне")
time.sleep(1)
border_int_1, border_int_2 = map(int, input("Введите через пробел два целых числа, между которыми надо "
                                            "сгенерировать случайное целое число ").split())
# если пользователь ввёл сначала большее число, то меняем их "местами"
if border_int_1 > border_int_2:
    border_int_1, border_int_2 = border_int_2, border_int_1
print(random.randrange(border_int_1, (border_int_2 + 1)))


print("Сгенерируем случайное вещественное число в указанном диапазоне")
time.sleep(1)
border_float_1, border_float_2 = map(float, input("Введите через пробел два числа, между которыми надо "
                                                  "сгенерировать случайное вещественное число ").split())
if border_float_1 > border_float_2:
    border_float_1, border_float_2 = border_float_2, border_float_1
print(border_float_1 + (border_float_2 - border_float_1) * random.random())


print("Сгенерируем случайную букву в указанном диапазоне")
time.sleep(1)
border_chart_1, border_chart_2 = input("Введите через пробел две буквы, между которыми надо "
                                       "сгенерировать случайную букву ").lower().split()
alphabet = "abcdefghijklmnopqrstuvwxyz"
# есть ли способы простой генерации алфавита в пайтоне?
if border_chart_1 > border_chart_2:
    border_chart_1, border_chart_2 = border_chart_2, border_chart_1
print(random.choice(alphabet[alphabet.find(border_chart_1): (alphabet.find(border_chart_2) + 1)]))



'''
Тесты:
5 -6
6 6
2.7182818 -3.1415
5 -3
b b
I b
'''
