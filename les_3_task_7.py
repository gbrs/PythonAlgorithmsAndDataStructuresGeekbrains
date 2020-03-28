'''7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться.
'''

from random import randrange

# a = [6, 6]  # проверка
# сгенерируем случайную последовательность
a = [randrange(0, 100) for i in range(10)]
print(a)

min1 = a[0]
min2 = a[1]

if min1 > min2:
    min1, min2 = min2, min1

for i in range(2, len(a)):
    if a[i] < min2:
        if a[i] <= min1:
            min2 = min1
            min1 = a[i]
        else:
            min2 = a[i]

print("Два минимальныхзначения в списке: ", min1, min2)
