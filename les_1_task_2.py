x1, y1 = map(float, input("Введите координаты x и y первой точки через пробел ").split())
x2, y2 = map(float, input("Введите координаты x и y первой точки через пробел ").split())

if x2 < x1:
    x1, y1, x2, y2 = x2, y2, x1, y1

k = (y2 - y1) / (x2 - x1)
b = y1 - k * x1

if b < 0:
    print(f'y = {k}x - {abs(b)}')
elif b == 0:
    print(f'y = {k}x')
else:
    print(f'y = {k}x + {b}')
