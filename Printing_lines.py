Python 3.6.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def new_line():
	print('.') # line that prints a dot

	
>>> def three_lines():
	#now calling new_line function
	new_line()
	new_line()
	new_line()

	
>>> def nine_lines():
	#now calling 3 lines fnc
	three_lines()
	three_lines()
	three_lines()

	
>>> def clear_screen():
	#now calling 9 lines fnc
	print("Now Calling clearScreen")
	print("printing 9lines")
	nine_lines()
	print("printing another 9lines")
	nine_lines()
	#now calling 3 lines fnc twice to make it 24
	print("printing the rest of the lines")
	three_lines()
	three_lines()
	#now calling new line to make it 25
	new_line()

	
