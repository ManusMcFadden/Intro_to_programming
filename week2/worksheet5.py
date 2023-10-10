'''
#1
tuple_nums = ((5, 10, 15, 20),  (2, 4, 6, 8), (57, 68, 79, 81), (1, 3, 5, 7))
list_sums = []
for i in tuple_nums:
    count = 0
    for j in i:
        count += j
    list_sums.append(count)
tuple_sums = tuple(list_sums)
print(tuple_sums)
'''