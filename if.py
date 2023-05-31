#single if statement 
# ------------------------------
# a=int (input("Enter the Number :"))
# b=int (input("Enter the Number :"))
# if(a>b):
#     print("Greater is A : ",a)
# else:
#     print("Greater is B",b)


# Odd Number OR Even Number
# ------------------------------
# n1=int(input("Enter the value :"))
# if(n1%2==0):
#     print("Even Number",n1)
# else:
#     print("Odd Number",n1)


# Greater number ifnested
# ------------------------------
# a=int(input("Enter the Number A :"))
# b=int(input("Enter the Number B :"))
# c=int(input("Enter the Number C :"))

# if(a>b and a>c):
# 	print("A is Greater : ",a)
# elif(b>a and b>c):
# 	print("B is Greater : ",b)
# else:
# 	print("C is Greater : ",c)

# Greater number ifnested
# -------------------------------
# a=int(input("Enter the Number A :"))
# b=int(input("Enter the Number B :"))
# c=int(input("Enter the Number C :"))

# if(a>b and a>c):
# 	print("A is Greater : ",a)
# elif(b>a and b>c):
# 	print("B is Greater : ",b)
# else:
# 	print("C is Greater : ",c)

# Result in if Statement.
# --------------------------------
# eng=int(input("Enter the English Marks :"))
# Ss=int(input("Enter the Social Science Marks :"))
# guj=int(input("Enter the Gujarati Marks :"))
# hin=int(input("Enter the Hindi Marks :"))
# sci=int(input("Enter the Sccirnce Marks :"))
# sum=eng + Ss + guj + hin + sci
# per=sum*100/500
# print("Total is :",sum)
# print("Percentage is :",per)
# if(eng<=35 or Ss<=35 or guj<=35 or hin<=35 or sci<=35):
#     print("Youare Fail.....")
# elif(per>=80 and per>=70):
#     print("First Class")
# elif(per>=70 and per>=60):
#     print("Second Class")
# else:
#     print("Pass Class")

# Which team are win--------
# india=int(input("Enter the India Scorce :"))
# aus=int(input("Enter the Austrial Scorce :"))
# if(india>aus):
#     print("India Win ---")
# elif(aus>india):
#     print("Austrial is win---")
# else:
#     print("Match is Tie---")

# Find leap year.......
# num=int (input("Enter the one Number : "))
# if(num%4==0):
#     print("Leap Year")
# else:
#     print("It is not leap year ")

# Checkout the word is palindrom

# word=input("Enter the Value :")
# reversed = word[::-1]
# if(word == reversed):
#     print("It is palindrom")
# else:
#     print("It is not palindrom")

import datetime
now = datetime.datetime.now()
print("Current Date")
print(now.strftime("%m-%d-%y"))

#           
# from datetime import datetime

# current_time = datetime.now().time()
# print(current_time)