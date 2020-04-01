''' 3.9. Найти максимальный элемент среди минимальных элементов столбцов матрицы
'''


from random import randrange

# сгенерирую случайную матрицу 5 строк на 10 столбцов
a = [[randrange(0, 100) for j in range(10)] for i in range(5)]

# Распечатываю получившуюся 'матрицу'
for i in range(5):
    for j in range(10):
        print(a[i][j], end="\t")
    print()

# вложенные циклы: поиск максимума(поиск минимума)
for j in range(len(a[0])):
    for i in range(len(a)):
        if i == 0 or a[i][j] < mn:
            mn = a[i][j]
    print(mn, end="\t")  # DELETE
    if j == 0 or mn > mx:
        mx = mn

print(mx)
