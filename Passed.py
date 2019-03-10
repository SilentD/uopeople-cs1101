print("Which is mum's favourite place in the yard")

place = int(input('Mums favourite place in the yard is the: ')) #this is favourite mum's place

#searching through for mum's favourite place
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
elif place >= 8:
    print("Oops invalid input")
else:
    print("Failed to guess") 

# Nested Condition

print("End year examination comments for the Computer science students") #Description

x = int(input('Enter your marks: ')) #Input the mark

for marks in range(101, 0, -1):
#country = "US"
country = "AU"
if country == "US":
    if total <= 50:
        print("Shipping Cost is  $50")
elif total <= 100:
        print("Shipping Cost is $25")
elif total <= 150:
	    print("Shipping Costs $5")
else:
        print("FREE")
if country == "AU": 
	  if total <= 50:
	    print("Shipping Cost is  $100")
else:
	    print("FREE")



#Logical operator

print("End year examination comments for the Computer science students") #Description

x = int(input('Enter your marks: ')) #Input the mark

#The marks and comments of the grades between 0 - 100 %
if x >= 80 and x <= 100 :
    print('Passed  greatly') 
elif x >=60 and  x <= 80:
    print('You passed so well!')
elif x >= 40 and x <= 60:
    print('Fair mark')
elif x >= 20 and x <= 40:
    print ('Need to improve!')
elif x >= 0 and x <= 20:
    print ('Work Hard!')
elif x < 0 or x > 100:
    print ('You entered wrong results!')
else:
    print ('Oops! Your selection is invalid.')



#Nested conditional
print("End year examination comments for the Computer science students")

passed = int(input("Enter a number")) # if you enter the number it will give you a comment

if passed == 3:
    print("Had a fair mark: ")
    if passed > 3:
        print("Passed greatly")
    else:
        print("Failed, Work hard, you will do better next time")
else:
        print("Had a fair mark")
    

#chained Condition
passed = int(input("Enter a number: ")) # if you enter the number it will give you a comment

if passed == 3:
    print("Had a fair mark: ")
if passed == 3:
        print("Passed greatly")
else:
    print("Failed, Work hard, you will do better next time")



