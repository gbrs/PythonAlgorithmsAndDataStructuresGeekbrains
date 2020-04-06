'''2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого — цифры числа.

Например, пользователь ввёл A2 и C4F.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
'''


from collections import defaultdict, deque


def _16_10(inn, out):
    # for i, item in enumerate(inn):
    #     out[i] = hx[item]
    for i, item in enumerate(inn):
        out.append(hx[item])


'''
a = list(input('Введите первое число: '))
b = list(input('Введите второе число: '))
'''

hx = defaultdict(int)
spam = -1
for i in '0123456789ABCDEF':
    spam += 1
    hx[i] = spam
print(hx)

a16 = list('A2')
b16 = list('C4F')
print(a16, b16)

a10 = []
b10 = []
sm10 = []
mlt10 = []
_16_10(a16, a10)
_16_10(b16, b10)
print(a10, b10)

for i in range(-1, 0, max())
