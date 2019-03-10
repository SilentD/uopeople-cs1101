''' 
def countUp(value):
    if value == 0:
        return
		
    print(value)
    countUp(value + 1)

def countDown(value):

    if value == 0:
	    return
		
    print(value)
    countDown(value - 1)

try:
    value=int(input('Input:'))
except ValueError:
    print ("Not a number")

if (value < 0):
	countUp(value)
else:
	countDown(value)
 
def countUp(n):
    if n==0:
        print("Blastoff!")
    else:
        print(n)
        countUp(n+1)
countUp(-5)



def  area(radius):
    a=math.pi * radius**2
    return a


def area(raduis):
    return math.pi * radius**2


def absolute_value(x):
    if x < 0:
        return -x
    else:
        return  x


def two_values(value):
     
    if x > y:
        return 1
    elif x==y:
        return 0
    else:t
        x < y
        return -1

def distance(x1, y1, x2, y2):
    return 0.0

def distance(x1, y1, x2,y2):
    dx =x2 - x1
    dy =y2 - y1
    print("'dx is', dy")
    print("'dy is', dy")
    return 0.0

def is_divisible(x,y):
    if 10 % 10 == 0:
        return True
    else:
        return False

def fibonacci(n):
    if n ==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci (n-1) + fibonacci(n-2)

def is_divisible (value, divisor, time):
if (time == 1):

import math
def square_root(x):
    assert x >= 0 # precondition

    y = math.sqrt(x)

    assert y * x == x #postcondition
    return y


def is_divisible(x,y): #This function checks if the two are divisible
    if x % y ==0:
        return True
    else:
        return False


def is_power (x,y): #check the power of the numbers
    if y == 1:
        if x == 1:
            return True
        else:
            return False
        if x == y:
            return False
        if x == 1:
            return True
        else:
            return (is_devisible(x/y,y))
            return (is_power(x/y,y))

print("is_power(10, 2) returns: ", is_power(10,2))
print("is_power(27, 3) returns: ", is_power(27,3))
print("is_power(1, 1)returns:", is_power(1,1))
print("is_power(10, 1)returns:", is_power(10,1))
print("is_power(3, 3) returns:", is_power(3,3))

void write_squareroot(double)

'''


def distance(x1, y1, x2, y2):
dx = x2 - x1
dy = y2 - y1
dsquared = dx**2 + dy**2
print('dsquared is: ', dsquared)
return 0.0























