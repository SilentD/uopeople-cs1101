

import turtle
bob = turtle.Turtle()
print(bob)

bob.fd(200)
bob.lt(90)

bob.fd(200)
bob.lt(90)


bob.fd(200)
bob.lt(90)

bob.fd(200)
bob.lt(90)

bob.fd(200)

for i in range(4):
    print('Hello')

for i in range(4):
    bob.fd(200)
    bob.lt(90)

for i in range(4):
    bob.fd(200)
    bob.rt(90)

for i in range(4):
    bob.bk(200)
    bob.lt(90)

for i in range(4):
    bob.bk(200)
    bob.lt(90) 

def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)
        
def countdown(n):
    if n <= 5:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)
