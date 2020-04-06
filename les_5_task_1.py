''' 1. Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за четыре квартала для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и
отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
'''

from collections import namedtuple

# соберем все данные по каждому предприятию в namedtuple
# и сложим их в список lst
factory = namedtuple('factory', 'name, I, II, III, IV, Y')
lst = []
n = 3

n = int(input('Введите количество предприятий: '))

'''# проверка программы без этапа ввода данных
lst.append(factory('b', 3, 5, 4, 2, 14))
lst.append(factory('a', 1, 2, 3, 4, 10))
lst.append(factory('c', 11, 12.4, 13.6, -16, 21))

for i in range(n):
    print(lst[i])
'''

for i in range(n):
    name = input(f'Введите название предприятия №{i+1} ')
    I = float(input(f'Введите прибыль в первом квартале предприятия №{i+1} '))
    II = float(input(f'Введите прибыль во втором квартале предприятия №{i+1} '))
    III = float(input(f'Введите прибыль в третьем квартале предприятия №{i+1} '))
    IV = float(input(f'Введите прибыль в четвертом квартале предприятия №{i+1} '))
    Y = I + II + III + IV  # прибыль за год
    lst.append(factory(name, I, II, III, IV, Y))

# найдем среднюю прибыль предприятий
s = 0
for i in range(n):
    s += lst[i].Y
avr = s / n

# составим два списка предприятий с прибылью выше и ниже средней
downer = []
upper = []
for i in range(n):
    if lst[i].Y < avr:
        downer.append(lst[i].name)
    elif lst[i].Y > avr:
        upper.append(lst[i].name)

# вывод списков
print('Предприятия с прибылью выше средней: ', end='')
print(*upper, sep=', ')
print('Предприятия с прибылью ниже средней: ', end='')
print(*downer, sep=', ')
