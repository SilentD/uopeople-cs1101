'''
from TurtleWorld import *
world = TurtleWorld()
bob = Turtle()

def square(t):
    for i in range(4):
        fd(t, 100)
        lt(t)

square(bob)
wait_for_user()



import turtle
sayi = turtle.Turtle()
print(sayi)

sayi.fd(100)
sayi.lt(90)

sayi.fd(100)
sayi.lt(90)

sayi.fd(100)
sayi.lt(90)

sayi.fd(100)

for i in range(4):
   print('sayi')

for lee in range (0,10):
    print("We 're on time %d" %(lee))

x = 1
while True:
    print("To infinity and beyond! We're getting close, on %d now!" % (x))
    x += 1
'''

'''
# nested if-else statement
x = -10
if x < 0:
    print("The negative number ",  x, " is not valid here.")
else:
    if x > 0:
        print(x, " is a positive number")
    else:
        print(x, " is 0")



def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" %(arg1, arg2))

def print_two_again(arg1, arg2):
    print("arg1: %r" % arg1)

def print_one(arg1):
    print("arg1: %r" % arg1)

def print_none():
    print("I got nothing")

def sayi(arg1):
    print("arg1: %r" % arg1)

people = 30
cars = 40
buses = 15

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars")
else:
    print("We cant decide")

if buses > cars:
    print ("That's too many buses.")
elif buses < cars:
    print("Maybe we could take the buses.")
else:
    print("We still can't decide.")

if people > buses:
    print ("Alright, let's just take the buses.")
else:
    print("Fine, lets stay home then.")
'''

print("You enter a dark room with two doors. Do you go through door #1 or door #2?")

door = input("> ")

if door == ("1"):
    print("There's a giant bear here eating a cheese cake. What do you do?")
    print("1 Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == ("1"):
        print("The bear eats your face off. Good job!")
    elif bear == ("2"):
        print("The bear eats your legs off. Good job!")
    else:
        print("Well, doing %s is probably better. Bear runs away." % bear)



elif door == ("2"):
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == ("1") or insanity == ("2"):
        print("Your body survives powered by a mind of jello. Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck. Good job!")

else:
    print("You stumble around and fall on a knife and die. Good job!")



hour = 12

if (hour == 12):
    print("noon")
if (hour > 12):
    print("AM")
else:
    print("PM")


cost = 200
refund = 3

if (cost > 100):
    refund = 10
refund = refund * 2
print(refund)

print("This is always first")
if x > 0:
    if y > 0:
        print("x is positive, y is positive")
else:
    print("x is negative")
print("This is always last")

#nested conditionals 
a = 19

if a >= 50:
    print("Big")
else:
    if (a < 10):
        print("Small")
    else:
        print("Medium")
        

i = 11
j = 19

if i > 5:
    if j > 15:
        print("A")
else:
    if j > 15:
        print("B")
if i > 10:
    print("C")
    
#chained conditionals

i

















    
