import random
#1
word = ""
for i in range(1,101):
    answer = ""
    if i % 3 == 0 and i % 5 == 0 and i % 7 == 0:
        word = "fizzbuzzwoof"
    elif i % 3 == 0 and i % 7 == 0:
        word = "fizzwoof"
    elif i % 5 == 0 and i % 7 == 0:
        word = "buzzwoof"
    elif i % 3 == 0 and i % 5 == 0:
        word = "fizzbuzz"
    elif i % 3 == 0:
        word = "fizz"
    elif i % 5 == 0:
        word = "buzz"
    elif i % 7 == 0:
        word = "woof"

    if i % 2 != 0:
        if random.randint(1,5) == 1:
            print(i)
            answer = i
            if answer != word:
                print("you win")
                break
        else:
            print(i)
    else:
        answer = input("enter your answer")
        if answer != word:
                print("you lose")
                break
        