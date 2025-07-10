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
		
	