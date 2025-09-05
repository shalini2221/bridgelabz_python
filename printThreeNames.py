
class StringReplace:
	def ReplaceString(String args) 

		// Initializing variables
		Utility utility = new Utility()
		template = "Hi <<UserName1>>, <<UserName2>> and <<UserName3>>"

		System.out.print("Please enter three names: ")
		String userName = utility.inputString()
		
		// Method declaration for replacing String
		String outputString = utility.replaceString(userName1, userName2, userName3, template)
		System.out.println(outputString)
