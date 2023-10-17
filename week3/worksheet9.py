'''
#1
usr_input = input("Enter a value: ")
try:
    usr_input = float(usr_input)  # q1(1)
    # usr_input = int(usr_input)  # q1(2)

except ValueError:
    print("ValueError - float is expected.")  # q1(1)
    # print("ValueError - integer is expected.")  # q1(2)
'''
'''
#2
def dummy_func(data):
    try:
        if not isinstance(data, list):  # q2(1)
        # if not isinstance(data, dict):    # q2(2)
            raise TypeError
    except TypeError:
        print("TypeError - expected a list")  # q2(1)
        # print("TypeError - expected a dictionary")  # q2(2)
'''