
def validate(password):
	c1=0
	c2=0
	c3=0
	c4=0
	for i in password:
		if i in [" ","@","#"] or len(password)<8:
			return "Invalid"

		if i.isalpha:
			if i.isupper:
				c1=+1
			if i.islower:
				c2=+1
		for j in "123456789":
			c3=+1

		for j in "!-$%&'()*+,./:;<=>?_[]^`{|}~":
			if i==j:
				c4=+1
	if c1>0 and c2>0 and c3>0 and c4>0:
		return "Secure"
	else:
		return "Insecure"
INPUT_STRING=input("Enter a password : ")
if __name__=="__main__":
	print(validate(INPUT_STRING))




