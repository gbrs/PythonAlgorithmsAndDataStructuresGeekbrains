'''2. Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
второй массив надо заполнить значениями 0, 3, 4, 5
(помните, что индексация начинается с нуля),
т. к. именно в этих позициях первого массива стоят четные числа.
'''


from random import randrange

# сгенерируем случайную последовательность
a = [randrange(0, 10) for i in range(10)]
print(a)

b = []

for i in range(len(a)):
    if a[i] % 2 == 0:
        b += [i]

print(b)