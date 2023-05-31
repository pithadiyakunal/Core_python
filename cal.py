def Addition(x,y):
	print("Addition Operation")
	return (x+y)
	
def Subtraction(x,y):
	print("Subtraction Operation")
	return (x-y)
	
def Multiplication(x,y):
	print("Multiplication Operation")
	return (x*y)
	
def Divition(x,y):
	print("Divition Operation")
	return (x/y)
	
def Menu():
	print("Main Menu")
	print("[1] Addition Operation")
	print("[2] Subtraction Operation")
	print("[3] Multiplication Operation")
	print("[4] Divition Operation")

	num=int(input("Please ! Enter Your Choice Number : "))
	return num


def Calulation():
	choice=Menu()
	n1=int(input("Please ! Enter Number 1 : "))
	n2=int(input("Please ! Enter Number 2 : "))

	if choice==1:
		result=Addition(n1,n2)
	elif choice==2:
		result=Subtraction(n1,n2)
	elif choice==3:
		result=Multiplication(n1,n2)
	elif choice==4:
		result=Divition(n1,n2)
	
	print("Your Result : " , result)

# ----------------------------------------------------

Calulation()