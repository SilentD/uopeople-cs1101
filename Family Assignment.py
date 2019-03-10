print("End year examination comments for the Computer science students")

passed = int(input("Enter a number")) # if you enter the number it will give you a comment

if passed != 3:
    if failed > 3:
        print("Passed greatly")
    else:
        print("Failed, Work hard, you will do better next time")
else:
        print("Had a fair mark")
    
#print("Pass rates for the Computer Science students")

'''
Code 7 (A Symbol): 80 - 100%
Code 6 (B Symbol): 70 - 79%
Code 5 (C Symbol): 60 - 69%
Code 4 (D Symbol): 50 - 59%
Code 3 (E Symbol): 40 - 49%
Code 2 (F Symbol): 30 - 39%
Code 1 (FF Symbol): 0 - 29%
'''

print("Which is mum's favorate place in the yard")

place = 8 #this is favorate mum's place

#searching through for mum's favorate place
if place == 1:
    print("Bathroom")
elif place == 2:
    print("Bedroom")
elif place == 3:
    print("Kitchen")
elif place == 4:
    print("Office")
elif place == 5:
    print("Garden")
elif place == 6:
    print("Pantry")
elif place == 7:
    print("Garage")
else:
    print("We failed to guess") # failure to pick one of the above will print the statement



