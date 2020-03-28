'''8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее
в последнюю ячейку строки. В конце следует вывести полученную матрицу.
'''

a = [[0 for j in range(4)] for i in range(5)]

# организуем ввод
for i in range(4):
    for j in range(4):
        a[i][j] = float(input("Введите очередное число: "))
    print()

# вычисляем элементы пятой строки
for j in range(4):
    t = 0
    for i in range(4):
        t += a[i][j]
    a[4][j] = t

# распечатываем получившуюся 'матрицу'
for i in range(5):
    for j in range(4):
        print(a[i][j], end="\t")
    print()