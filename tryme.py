from math import pi, pow #import math

radius = int(input("Enter the radius: ")) #enter input

sphere_volume = 4/3 * pi* pow(radius,3) #Calculate radius

print("The volume of a sphere with radius %s is %s" %(radius, sphere_volume)) #gives you the output

def new_lines(): #dot function
    print('.')
def three_lines(): 
    new_lines()
    new_lines()
    new_lines()
def nine_lines():
    three_lines()
    three_lines()
    three_lines()
def clear_lines():
    nine_lines()
    nine_lines()
    three_lines()
    three_lines()
    new_lines  
clear_lines()     # function dot stops here

