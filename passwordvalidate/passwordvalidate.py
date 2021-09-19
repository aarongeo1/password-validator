c1=0
c2=0
c3=0
c4=0
def validate(password):
	if i in password in [" ","@","#"] or len(password)<7:
		return "Invalid"
	for i in password:
		if i.isupper:
			c1+=1
		if i.islower:
			c2+=1
		if type(i)==int:
			c3+=1
		for j in "!-$%&'()*+,./:;<=>?_[]^`{|}~":
			if i==j:
				c4+=1
	if c3>0 and c2>0 and c1>0 and c4>0:
		return "Secure"
	else:
		return "Insecure"
INPUT_STRING=input("Enter a password : ")
if __name__=="__main__":
	print(validate("INPUT_STRING"))




