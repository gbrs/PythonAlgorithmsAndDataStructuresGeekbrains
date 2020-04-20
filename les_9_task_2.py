import collections

# str = 'шебуршавший мезокайнозойский зоопланктон'
str = 'for sale, baby shoes, never worn'
dict_freq = collections.Counter(str)
# for chart in set(str):
#     dict_freq[chart] = str.count(chart)
print(len(set(str)), len(str))
print(dict_freq)
