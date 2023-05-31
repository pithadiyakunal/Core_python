# try:
# 	num1=int(input("Enter Any Number 1 : "))
# 	num2=int(input("Enter Any Number 2 : "))

# 	if num1<0:
# 		raise TypeError

# 	total=num1/num2

# 	print("Divition : " , total)
# except NameError:
# 	print("Sorry ! Undefine Variable Name. Please ! Check Your Variable Name")

# except ValueError:
# 	print("Sorry ! Invalid Number Data Input. Please ! Enter Only Numeric Value")

# except ZeroDivisionError:
# 	print("Sorry ! Input Number is Zero. Please ! Not Input Zero Value")

# except TypeError:
# 	print("Sorry ! Number 1 Value is Not Inpute Less than 0")

# finally:
# 	print("\n\nThis is Finally Block\n\n")

# for x in range(1,11):
# 	print("Number : " , x)  


class InvalidAgeError(Exception):
    def __init__(self):
        super()

try:
    age=int(input("Enter Your age:"))
    # age = "15"       # TypeError Occur...
    print("Age is " , age , " Year's")

    if(age<18):
        raise InvalidAgeError

except InvalidAgeError:
    print("Sorry ! Your Age Value is Less Than 18")
except TypeError:
    print("Sorry ! Your Age Value is Not Numeric")
else:
    print("Congratulation ! You are a Valid User")
finally:
    print("Programme Ending Code Here........")