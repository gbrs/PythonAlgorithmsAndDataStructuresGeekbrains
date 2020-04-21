'''2. Закодируйте любую строку по алгоритму Хаффмана.'''

# text = 'алексей петренко'
# text = 'abrakadabbra'
# text = 'for sale, baby shoes, never worn'
text = input('Type your phrase: ')
print(f'В тексте длиной {len(text)} знака, {len(set(text))} разных знаков')
print()

# формируем частотный словарь: "знаки - их частотность"
dict_freq = {}
for chart in set(text):
    dict_freq[chart] = text.count(chart) / len(text)

# формируем пустой словарь-переводчик; значения в словаре - строки
dict_translator = {}
for chart in set(text):
    dict_translator[chart] = ''

print('Частотный словарь: ')
for key in dict_freq:
    print(key, ': ', dict_freq[key])
print()

# бежим по словарю частот и сливаем друг с другом самые
# маленькие элементы (пока не сольем всё в один элемент),
# запоминая при этом путь до них в словаре-переводчике
while len(dict_freq) > 1:

    # находим минимальные элементы
    Min1 = Min2 = 1
    Min1_idx = Min2_idx = None
    for key in dict_freq:
        if dict_freq[key] < Min1:
            Min2 = Min1
            Min2_idx = Min1_idx
            Min1 = dict_freq[key]
            Min1_idx = key
        elif Min1 <= dict_freq[key] < Min2:
            Min2 = dict_freq[key]
            Min2_idx = key

    # сливаем их и удаляем
    key_new = Min1_idx + Min2_idx
    freq_new = dict_freq[Min1_idx] + dict_freq[Min2_idx]
    dict_freq.update({key_new: freq_new})
    dict_freq.pop(Min1_idx)
    dict_freq.pop(Min2_idx)

    # записываем "путь до знаков" в словарь-переводчик (справа налево)
    for chart in Min1_idx:
        dict_translator[chart] = '0' + dict_translator[chart]
    for chart in Min2_idx:
        dict_translator[chart] = '1' + dict_translator[chart]

print('Словарь-переводчик нашей фразы: ')
for key in dict_translator:
    print(key, ': ', dict_translator[key])

# закодируем нашу фразу
letter = ''
for chart in text:
    letter += dict_translator[chart]
print(letter)
print(f'Письмо записано в {int(len(letter) / 8)} байт, '
      f'вместо {int(len(text))} байт')

