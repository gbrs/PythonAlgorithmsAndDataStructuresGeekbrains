'''2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого — цифры числа.
'''

from collections import defaultdict, deque


def _16_10(inn):
    '''на основе матрицы из 16-ричных чисел inn
    создает матрицу из 10-ричных чисел out
    '''
    out = []
    for i, item in enumerate(inn):
        out.append(hx[item])
    return out


def _10_16(inn):
    '''на основе матрицы из 10-ричных чисел inn
    создает матрицу из 16-ричных чисел out
    '''
    out = []
    for i in inn:
        # перебором ищем в словаре по values их keys
        for k, v in hx.items():
            if v == i:
                out.append(k)
    return out


def summator(a, b):
    '''суммирует элементы матрицы 'столбиком', начиная с последних элементов,
    не учитывая переполнение разрядов
    '''
    c = [None] * len(b)
    for i in range(-1, -len(a) - 1, -1):
        c[i] = b[i] + a[i]
    for i in range(0, len(b) - len(a)):
        c[i] = b[i]
    return c


def multiplicator(a, b):
    '''перемножает элементы матрицы 'столбиком',
    не учитывая переполнение разрядов
    '''
    c = [0] * (len(b) + len(a) - 1)
    for i in range(-1, -len(a) - 1, -1):
        for j in range(len(b)):
            c[len(a) + i + j] += a[i] * b[j]
            # print(i, j, len(a) + i + j, sep='\t')
    return c


def shifter(a):
    '''разбирается с переполненными разрядами (четрыепишемдваввуме),
    записывая результат в двустороннюю очередь
    '''
    b = deque()
    spam = 0
    for i in range(-1, -len(a) - 1, -1):
        spam += a[i]
        b.appendleft(spam % 16)
        spam //= 16
    if spam:
        b.appendleft(spam)
    return b


# сгенерируем словарик hx, который будем использовать для перевода
# из 16-ричной системы в 10-ричную (и обратно)
hx = defaultdict(int)
spam = -1
for i in '0123456789ABCDEF':
    spam += 1
    hx[i] = spam

# вводим числа, превращая их в матрицы с 16-ричными элементами
a16 = list(input('Введите первое шестнадцатиричное число: ').upper())
b16 = list(input('Введите второе шестнадцатиричное число: ').upper())
# для удобства дальнейших манипуляций более короткое число будет a16
if len(a16) > len(b16):
    a16, b16 = b16, a16
# создаем матрицы с 10-ричными элементами вместо 16-ричных
a10 = _16_10(a16)
b10 = _16_10(b16)

# производим суммирование и умножение "в столбик",
# пока не обращая внимание на переполнение разрядов
sm10 = summator(a10, b10)
mlt10 = multiplicator(a10, b10)
# разбираемся с переполнение разрядов,
# получая матрицу-ответ, но с элементами записанными в 10-ричной системе
sm_sh = shifter(sm10)
mlt_sh = shifter(mlt10)
# формируем матрицу-ответ с элементами записанными в 16-ричной системе
sm16 = _10_16(sm_sh)
mlt16 = _10_16(mlt_sh)

print('сумма', sm16, sep='\t\t\t')
print('произведение', mlt16, sep='\t')
