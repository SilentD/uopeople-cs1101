#This function prints one line.
def new_line():
    print('.')

#This function prints three lines using the new_line function.
def three_lines():
    new_line()
    new_line()
    new_line()

#This function calls three_lines() three times to print a total of nine lines.
def nine_lines():
    three_lines()
    three_lines()
    three_lines()

#This function calls the combination of nines_lines, three_lines and new_line to print a total of 25 lines.
def clear_screen():
    print("Running 25 lines using clear_screen")
    print("Running nine_lines")
    nine_lines()
    print("Running three_lines")
    three_lines()
    print("Running nine_lines")
    nine_lines()
    print("Running three_lines")
    three_lines()
    print("Running new_line")
    new_line()

#This is the function call for the desired output.
clear_screen()
