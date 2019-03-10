'''
def new_line():
    print('.')

def three_lines():
    new_line()
    new_line()
    new_line()


#moving to nine lines

def nine_lines():
    three_lines()
    three_lines()
    three_lines()

#beginning clear screen

def clear_screen():
    nine_lines()
    nine_lines()
    three_lines()
    three_lines()
    new_line()
    #line end

clear_screen()

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

def repeat_lyrics():
    print_lyrics()
    print_lyrics()


def main():
    print("Please enter five numbers: ")
    # Allow the user to enter in the five values.
    n1 = eval(input("Please enter number 1:"))
    n2 = eval(input("Please enter number 2:"))
    n3 = eval(input("Please enter number 3:"))
    n4 = eval(input("Please enter number 4:"))
    n5 = eval(input("Please enter number 5:"))
    print("Numbers entered:", n1, n2, n3, n4, n5)
    print("Average:",(n1 + n2 + n3 + n4 + n5)/5 )

main()

def main():
    sum = 0.0
    number_of_entries = 5
    print("Please enter", number_of_entries, "numbers: ")
    for i in range(0, number_of_entries):
        num = eval(input("Enter Number" + str(i) + ": "))
        sum += num;
    print("Average:", sum/number_of_entries)

main()
 

a = [1, 2, 5]
b = [1, 2, 3]

if a == b:
    print('True')
else:
    print ('False')
 

colors = ['blue', 'red', 'black', 'green']
def add_color(color):
    color = input('enter color: ')
    if color not in colors:
        colors.append(color)
        print(color+' '+"Added in colors list")
    else:
        print('Color already exists! sorry')
while True:
    ip=input('Enter Color:')
    ip.islower()
    add_color(ip)  
 '''   

colors = ['blue', 'red', 'black', 'green']
def add_color(color):
    
    if color not in colors:
        colors.append(color)
        print(color + " Added in colors list")
    else:
        print('Color already exists! sorry')
while True:
    color = input('enter color: ')
    color.islower()
    add_color(color)
    

































