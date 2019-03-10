# A function which accepts two integers as arguments and tests if the first argument is divisible by the second
def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False

# Check if the first integer argument is a power of the second integer argument
def is_power(a, b):
    # First Test Case - Both arguments are equal
    if a == b:
        return True
    # Second Test Case - Second argument is equal to 1 and therefore returns true
    elif b == 1:
        return True
    # Third Test Case - Check if the first integer argument is divisble by the second integer argument by calling the is_divisible() function
    elif is_divisible(a, b):
        # Sub Test Case - Call the is_power() function recursively to test if the result of a/b is divisible by b. EX: (10 / 2 = 5), 5 -> Both numbers equal. Will now match the first test case!
        if is_power(a / b, b):
            return True
        # If the sub test case above fails, we return False
        else:
            return False
    # Alternatively  - Thie second integer argument is not a power of the first integer argument, so return False
    else:
        return False


# Call the function with a print statement
print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))