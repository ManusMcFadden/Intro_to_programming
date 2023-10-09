'''
#1
forename = input("Enter your first name: ")
surname = input("Enter your surname: ")
print("Hello {0} {1}".format(forename.capitalize(),surname.capitalize()))
'''
'''
#2
sentence = input("Enter a sentence: ")
letter = input("Enter a letter: ")
print("The sentence contains", sentence.count(letter),  "letter", letter ,"s")
'''
'''
#3
sentence = input("Enter a sentence: ").lower()
count = 0
for i in sentence:
    if i in "aeiou":
        count += 1
print("There are ", count, " vowels in the sentence")
'''
'''
#4
sentence = input("Enter a sentence: ").lower()
a_used = False
e_used = False
i_used = False
o_used = False
u_used = False
count = 0
for i in sentence:
    if i == "a":
        a_used = True
    elif i == "e":
        e_used = True
    if i == "i":
        i_used = True
    if i == "o":
        o_used = True
    if i == "u":
        u_used = True
if a_used == True:
    count += 1
if e_used == True:
    count += 1
if i_used == True:
    count += 1
if o_used == True:
    count += 1
if u_used == True:
    count += 1
print(count, "vowels in the sentence.")
'''
'''
#5
name = input("Enter your name: ")
encrypted = ""
for i in name:
    if ord(i) >= 97 and ord(i) <= 122:
        encrypted += "x"
    elif ord(i) >= 65 and ord(i) <= 90:
        encrypted += "X"
    else:
        encrypted += i
print(encrypted)
'''