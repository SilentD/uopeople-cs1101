# first function that print one blank line
def new_line():
   print()
# second function that print three blank lines using new_line function
def three_lines():
   new_line()# new_line function call
   new_line()# new_line function call
   new_line()# new_line function call

# third function that print nine blank lines using three_lines function
def nine_lines ():
    three_lines()# three_lines function call
    three_lines()# three_lines function call
    three_lines()# three_lines function call

# forth function that print twenty-five blank lines using nine_lines function
def clear_screen():
    nine_lines()# nine_lines function call
    print('now printing 9 lines')# placeholder
    nine_lines()# nine_lines function call
    print('now printing 9 lines')# placeholder
    three_lines()# nine_lines function call
    print('now printing 3 lines')# placeholder
    three_lines()# nine_lines function call
    print('now printing 9 lines')# placeholder
    new_line()# nine_lines function call
    print('now printing 25 lines')# placeholder


clear_screen()