'''
#1
capacity = int(input("Enter capacity of tank in litres: "))
kilometers_per_litre = int(input("Enter the number of kilometres the car can travel per litre: "))
kilometers = capacity * kilometers_per_litre
print("The car will travel {0} kilometers.".format(kilometers))
'''
'''
#2
import math
radius = int(input("Enter radius of cylinder: "))
height = int(input("Enter height of cylinder: "))
volume = math.pi * radius ** 2 * height
print("The cylinder has a volume of {0}.".format(volume))
'''
'''
#3
farenheight = int(input("Enter temperature in farenheight: "))
celsius = ((farenheight - 32) * 5) / 9
print("The temperature is {0} celsius".format(celsius))
'''