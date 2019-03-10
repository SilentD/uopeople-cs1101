def is_power(a, b):
	if a/b == 1:
		return True
	if a < b: 
		return False
	if a == b:
		return True
	else:
		return is_power(a / b, b) 

print(is_power(10, 2))

print(is_power(27, 3))

print(is_power(1, 1))

print(is_power(10, 1))

print(is_power(3, 3))
