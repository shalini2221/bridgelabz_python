import java.util.Scanner
class Utility:
	user_input_int = int(input("Enter an integer: "))
	user_input_float = float(input("Enter a float: "))
	user_input_string = string(input("Enter a string: "))

def replaceString(userName, template): 
		userName=''
		if userName.len() <= 3:
			return "Please input string with more than 3 characters"
		else:
			output = template.replace("<<UserName>>", userName)
			return output
		
Scanner scanner = new scanner(System.in)
	

def inputBoolean():
		return scanner.nextBoolean()
	
	
def  inputLong():
		return scanner.nextLong()
		
def inputFloat():
		return scanner.nextFloat()
	
	
def inputDouble():
		return scanner.nextDouble()
	
def inputString():
		return scanner.nextLine()
def inputString1():
		return scanner.next()
	
	
def inputInteger():
		return scanner.nextInt()
	
def leapYearCheaker(int year):
	if(year>1582):
		   if year % 400 == 0 or year % 4 == 0 & year % 100 != 0:
			   
			   return True
		   
		
return False
	
	
def checkLeapYear(int year):
		if year >= 1000 & year <= 9999: 
			if year % 400 == 0 or year % 4 == 0 & year % 100 != 0:

				return "Leap Year"
		    else:
			
			return "not a Leap Year"
        else:


            return "Wrong year"
import sys

# Check if enough command-line arguments are provided
if len(sys.argv) != 3:
    print("Usage: python SpringSeason.py <month> <day>")
    sys.exit(1)

# Read command-line arguments
m = int(sys.argv[1])
d = int(sys.argv[2])

# Determine if the date is in the spring season (March 20 to June 20)
if (m == 3 and d >= 20) or (m == 4) or (m == 5) or (m == 6 and d <= 20):
    print("true")
else:
    print("false")

import random

# Generate 5 random numbers between 0 and 1
values = [random.random() for _ in range(5)]

# Calculate average, min, and max
average = sum(values) / len(values)
minimum = min(values)
maximum = max(values)

# Print the results
print("Five random values between 0 and 1:")
for i, val in enumerate(values, 1):
    print(f"Value {i}: {val}")

print(f"\nAverage: {average}")
print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")
