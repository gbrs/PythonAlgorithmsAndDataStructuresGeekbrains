'''
4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
'''

border_chart_1, border_chart_2 = input("Введите через пробел две латинские буквы ").lower().split()
alphabet = "abcdefghijklmnopqrstuvwxyz"

print(f'Буква {border_chart_1} находится на позиции №{alphabet.find(border_chart_1) + 1}')
print(f'Буква {border_chart_2} находится на позиции №{alphabet.find(border_chart_2) + 1}')

distance = abs(alphabet.find(border_chart_1) - alphabet.find(border_chart_2))
if distance > 1:
    print('Количество букв между введенными вами буквами:', distance - 1)
else:
    print('Между введенными вами буквами нет других букв')

'''
тесты:
A a
b a
a B
c A
z A
d ф ошибается ставя позицию для ненайденного символа -1
'''
