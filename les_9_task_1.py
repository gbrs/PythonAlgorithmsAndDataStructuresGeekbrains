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

for start in range(l):
    for length in range(1, l-start+1):
        sub = text[start: start + length]
        if sub not in subs:
            for position in range(l-length+1):
                sample = text[position : position+length]
                # print(sub, position, sample)
                if hashlib.sha1(sub.encode('utf-8')).hexdigest() == \
                    hashlib.sha1(sample.encode('utf-8')).hexdigest():
                    subs.update(sub)
                    print(sub, position, sample, subs)
                    break

print(subs)
print(len(subs) - 1)
