'''
#1
dict1 = {'sc0011': 'Ali Bin Ahmad', 'sc0012': 'Wong Fei Hung', 'sc0013': 'James Purple', 'sc0014': 'Salimah Wahid'}
dict2 = {'it1011': 'Abdus Salam', 'it1012': 'Alex Chung', 'it1013': 'Anastasia Zeus', 'it1014': 'Vihaan Arjun'}
dict3 = {'ai2011': 'Charles Lewin', 'ai2012': 'Apollo Leto', 'ai2013': 'Ciarra Vega', 'ai2014': 'Lara Gould'}
dict4 = {}
for i in (dict1,dict2,dict3):
    dict4.update(i)
print(dict4)
'''
'''
#2
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3 = {}
for i, j in d1.items():
    for k, l in d2.items():
        if i == k:
            d3.update({i:j+l})
print(d3)
'''
'''
#3
dict_num = {'even': [], 'odd': []}
for i in range (1,52):
    if i % 2 == 0:
        dict_num['even'].append(i)
    else:
        dict_num['odd'].append(i)
print(dict_num)
'''
'''
#4
import math
dict_my = {'a': 500, 'b': 200, 'c': 1500, 'd': 20, 'x': 1550, 'v': 260}
maximum = 0
minimum = math.inf
for i,j in dict_my.items():
    if j > maximum:
        maximum = j
    if j < minimum:
        minimum = j
print(minimum)
print(maximum)
'''