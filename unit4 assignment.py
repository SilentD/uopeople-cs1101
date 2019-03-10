'''
#Creating a function to check if the two numbers are divisible
def is_divisible(x,y):
    if x % y ==0:
        return True
    else:
        return False

#creating a function to check if one number is a power to the other
def is_power (x,y):
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
'''


def is_divisible(a,b):
    if a % b ==0:
        return True
    else:
        return False

def is_power(a,b): 
    if b == 1:
            if a == 1:
                return True
            else:
                return False
            if a==b:
                return False
            if a==1:
                return True
            else:
                return (is_divisible(a/b,b))
                return (is_power(a/b,b))


print("is_power(50, 5) returns: ", is_power(50,5))
print("is_power(117, 9) returns: ", is_power(117,9))
print("is_power(1, 1)returns:", is_power(1,1))
print("is_power(11, 1)returns:", is_power(11,1))
print("is_power(7, 7) returns:", is_power(7,7))
