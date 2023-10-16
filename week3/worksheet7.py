'''
#1
num1 = int(input("Enter a number"))
num2 = int(input("Enter a bigger number"))
sum = 0
for i in range (num1,num2 + 1):
    sum += i
print(f"The sum of the numbers between {num1} and {num2} is {sum}")
'''
'''
#2
list_main = []
for i in range(5):
    list_main.append([])
    for j in range (5):
        list_main[i].append(i * 5 + j)
print(list_main)
'''
'''
#3
sum = 0
for i in range(10):
    sum += int(input("enter a number"))
print(f"The sum of the numbers is {sum} and the mean is {sum / 10}")
'''
'''
#4
import copy
list_nested = [[1, 4, 0, 1, 3, 1], [2, 2, 4, 2, 2, 3], [1, 0, 1, 0, 1, 0]]
list_rounded_to_integer = copy.deepcopy(list_nested)
for i in range(3):
    for j in range(6):
        if i != 0:
            list_rounded_to_integer[i][j] += list_nested[i - 1][j]
        if i != 2:
            list_rounded_to_integer[i][j] += list_nested[i + 1][j]
        if j != 0:
            list_rounded_to_integer[i][j] += list_nested[i][j - 1]
        if j != 5:
            list_rounded_to_integer[i][j] += list_nested[i][j + 1]

for i in range(3):
    for j in range(6):
        if i == 0 or i == 2:
            if j == 0 or j == 5:
                list_rounded_to_integer[i][j] = list_rounded_to_integer[i][j]/3
            else:
                list_rounded_to_integer[i][j] = list_rounded_to_integer[i][j]/4
        elif j == 0 or j == 5:
            if i != 0 or i != 2:
                list_rounded_to_integer[i][j] = list_rounded_to_integer[i][j]/4
        else:
             list_rounded_to_integer[i][j] = list_rounded_to_integer[i][j]/5

for i in range(3):
    for j in range(6):
        list_rounded_to_integer[i][j] = round(list_rounded_to_integer[i][j])

print(list_rounded_to_integer)           
'''


    
    
