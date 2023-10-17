import random
#1
for i in range(1,101):
    answer = ""
    word = ""
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
    else:
        word = str(i)

    if i % 2 != 0:
        if random.randint(1,5) == 1:
            print(i)
            answer = str(i)
            if answer != word:
                print("you win")
                break
        else:
            print(word)
    else:
        answer = input("enter your answer")
        if answer != word:
                print("you lose")
                break
        