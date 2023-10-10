'''
#1
list_odd = []
list_even = []
list_total = [list_odd,list_even]
for i in range (1,52)
    if i % 2 == 0:
        list_even.append(i)
    else:
        list_odd.append(i)
print(list_even)
print(list_odd)
'''
'''
#2
string = input("Enter a string")
list_numeric = []
list_alphabetic = []
for c in string:
    if c.isnumeric() is True:
        list_numeric.append(c)
    elif c.isalpha() is True:
        list_alphabetic.append(c)
print(list_total)
'''
'''
#3
list_input = [2,1,2,1]
list_output = []
for i in list_input:
    found = False
    for j in list_output:
        if i in j:
            j.append(i)
            found = True
    if found is False:
        list_output.append([i])
print(list_output)
''' 