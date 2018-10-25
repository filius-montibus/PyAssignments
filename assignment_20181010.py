# Q.1- Write a python code to find a valid email address from a text.
import re
mail=input('Enter a valid emial - ')
def isValidEmail(email):
	if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email) != None:
		return True
	else:
		return False

if isValidEmail(mail) == True :
	print("This is a valid email address")
else:
	print("This is not a valid email address")
print('-'*50)

# Q.2- Write a python program to find a valid Indian phone number from a text.(Valid Indian numbers will start with "+91-" and after that [6-9] followed by 9 digits. )
import re
ph=r'^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$'
inp=input('Enter valid Indian phone number - ')
if re.match(ph,inp):
	print(inp,'is a valid number.')
else:
	print(inp,'is invalid.')