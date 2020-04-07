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


def summator(a, b):
    c = [None] * len(b)
    for i in range(-1, -len(a)-1, -1):
        c[i] = b[i] + a[i]
    for i in range(0, len(b)-len(a)):
        c[i] = b[i]
    return c


def multiplicator(a, b):
    c = [0] * (len(b) + len(a) - 1)
    for i in range(-1, -len(a)-1, -1):
        for j in range(len(b)):
            c[len(a) + i + j] += a[i] * b[j]
            # print(i, j, len(a) + i + j, sep='\t')
    return c


def shifter(a):
    b = deque()
    spam = 0
    for i in range(-1, -len(a)-1, -1):
        spam += a[i]
        b.appendleft(spam % 16)
        spam //= 16
    if spam:
        b.appendleft(spam)
    return b


hx = defaultdict(int)
spam = -1
for i in '0123456789ABCDEF':
    spam += 1
    hx[i] = spam
# print(hx)

'''
a = list(input('Введите первое число: '))
b = list(input('Введите второе число: '))
'''

a16 = list('C4F')
b16 = list('A21')
a16 = list('FFF')
b16 = list('FFF')
print(a16, b16)

if len(a16) > len(b16):
    a16, b16 = b16, a16

a10 = []
b10 = []
_16_10(a16, a10)
_16_10(b16, b10)
print(a10, b10)

sm10 = summator(a10, b10)
mlt10 = multiplicator(a10, b10)
sm_sh = shifter(sm10)
mlt_sh = shifter(mlt10)

print('сумма', sm10)
print('сумма', sm_sh)
print('произведение', mlt10)
print('произведение', mlt_sh)