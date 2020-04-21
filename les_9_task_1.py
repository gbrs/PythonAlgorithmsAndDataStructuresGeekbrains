'''
1. Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка. Требуется вернуть количество различных
подстрок в этой строке.
'''

import hashlib

text = input('Введите вашу фразу: ')
l = len(text)
subs = set()
cnt = 0

assert l > 0, 'Молчание, конечно, - золото. Но мне бы фразу подлиннее'

# три вложенных цикла - перебираем: начальный элемент подстроки, ее длину и
# ищем ее аналоги во всех позициях строки. Запоминаем все подстроки во множество
# subs и сверяемся с ним, чтобы не считать одни и те же подстроки многократно
for start in range(l):
    for length in range(1, l-start+1):
        sub = text[start: start + length]
        if sub not in subs:
            for position in range(l-length+1):
                sample = text[position : position+length]
                if hashlib.sha1(sub.encode('utf-8')).hexdigest() == \
                    hashlib.sha1(sample.encode('utf-8')).hexdigest():
                    subs.add(sub)
                    # print(sub, position, sample, subs)
                    cnt += 1

# удаляем подстроку, совпадающую со всей строкой
subs.remove(text)
print('Множество подстрок: ', subs)
print(f'{len(subs)} различных подстрок, встречающихся {cnt - 1} раз')
