'''
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

def countdown(n):
    n = 12
    while n > 0:
        print(n)
        n = n - 3 
        print('Blastoff!')

        
try:
    value=int(input('Input:'))
except ValueError:
    print("Not a number")

if (value < 0):
	countUp(value)
else:
	countDown(value)


def sequence(n):
    while n != 1:
        print(n)
if n % 2 == 0: # n is even
    n = n / 2
else: # n is odd
    n = n*3 + 1

def countdown(n):
    if n <= 5:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-5)
'''
i = 0 
while i < 7: 
    print(i)
    if i == 4: 
        print("Breaking from loop")
        break
    i += 1

tabby_cat = ("\tI'm tabbed in.")
persian_cat = ("I'm split\non a line.")
backslash_cat = ("I'm \\ a \\ cat.")

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print('tabby_cat')
print('persian_cat')
print('backslash_cat')
print('fat_cat') 


while True:
    for i in (["/","- ","|","\\","|"]):
        print ("%s\r" % i,)
    break

        
hairs = ['brown','blond','red']
eyes = ['brown', 'blue', 'green']
weights= [1, 2, 3, 4]


the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quartes']

#this first kind of for- loop goes though a list

for number in the_count:
    print("This is count %d" % number)

#same as above
for fruit in fruits:
    print("A fruit of type: %s" % fruit)

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print ("I got %r" % i)

# we can also build lists, first start with an empty one
elements = []

#then use the range function to do 0 to 5 counts
#while i <= 6:
 #   print ("Adding %d to the list." % i)
# append is a function that lists understand
#elements.append(i)    

# now we can print them out too
for i in elements:
    print("Element was: %d" % i)


two_dimension = [[1, 2, 3], [4,5, 6]]

for two_dimensions in two_dimension:
    print("Review the %s" % two_dimension)


s='apple'
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

c='APPLe'
def any_lowercase2(s):
    for c in s:
        if 'c' .islower():
            return'True'
        else:
            return 'False'



c='apple'
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
        return flag

    
c='apple'
def any_lowercase4(s):
    flag = false
    for c in s:
        flag = flag or c. islower()
        return flag

c='apple'
def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True    

a = 4
x = 3
while True:
    y = (x +a/x) / 2
    if y == x:
        break
    x = y
    
'''   
my_sqrt(a) and math.sqrt=(a)
a = 1 | my_sqrt(a) = 1 | math.sqrt (a) = 1.0 | diff = 0.0
a = 2 | my_sqrt(a) = 1.41421356237 | math.sqrt(a) = 1.41421356237 | diff 2.22044604925e-16
a = 3 | my_sqrt(a) = 1.73205080757 | math.sqrt(a) =1.73205080757 | diff 0.0
a = 4 | my_sqrt(a) = 2.0 | math.sqrt (a) = 2.0 | diff = 0.0
a = 5 | my_sqrt(a) = 2.2360679775  | math.sqrt(a) =2.2360679775 | diff= 0.0
a = 6 | my_sqrt(a) = 2.44948974278 | math.sqrt(a) =2.44948974278 | diff = 0.0
a = 7 | my_sqrt(a) = 2.64575131106 | math.sqrt(a) =2.64575131106 | diff = 0.0
a = 8 | my_sqrt(a) = 2.82842712475 | math.sqrt(a) =2.82842712475 | diff = 4.4408920985e-16
a = 9 | my_sqrt(a) = 3.0 | math.sqrt (a) = 3.0 | diff = 0.0
'''

import math
def test_sqrt():
    def my_sqrt(a):
        x = 1
        while True:
            y = (x + a / x) / 2
            if y == x:
                return x
            x = y
    for a in range(1,26):
        print(a,my_sqrt(a),abs(my_sqrt(a) - math.sqrt(a)))


test_sqrt()


index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1


prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    if letter in ('O', 'Q'):
        print(letter + 'u' + suffix)
    else:
        print(letter + suffix)


tip='Eat Green To Live Health'
p=tip[9:26]
q=tip[0:9]
p+''+q


>>> tip='Eat Green To stay Health'
>>> tip.replace('Live', 'Stay')
'Eat Green To stay Health'
>>> 











