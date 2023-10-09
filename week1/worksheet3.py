'''
#1
number = input("Enter a number between 0 and 94")
if number >= 0 and number <= 94:
    print("number in range")
else:
    print("number not in range")
'''
'''
#2
age = input("Enter age: ")
legal_age = input("Enter legal alcohol age: ")
paid_by_card = input("Has the customer paid by card (True/False): ")
age_on_id = input("What is the age on the id")
estimated_age = input("How old does the customer look: ")
sale = False
if (age == age_on_id and age > legal_age) or (paid_by_card == "True" or paid_by_card == "False") or estimated_age > 21:
    sale = True
print(sale)
'''