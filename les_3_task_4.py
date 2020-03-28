'''4. Определить, какое число в массиве встречается чаще всего.
'''


from random import randrange

# сгенерируем случайную последовательность
a = [randrange(1, 6) for i in range(10)]
print(a)

amx = -1
mx = 0

for A in set(a):
    if a.count(A) > mx:
        mx = a.count(A)
        amx = A

print(amx)
