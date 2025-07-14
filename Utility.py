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

            return "You have entered a wrong year"