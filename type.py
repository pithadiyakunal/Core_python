price=1000

print(type(price))
print(isinstance(price,int))
print(isinstance(price,float))
print(isinstance(price,complex))

#-------------------------------------------------------#

price=50.75

print(type(price))
print(isinstance(price,int))
print(isinstance(price,float))
print(isinstance(price,complex))

#-------------------------------------------------------#

price=50 + 6j

print(type(price))
print(isinstance(price,int))
print(isinstance(price,float))
print(isinstance(price,complex))

# Python math Module
# import math

# print(math.pi)
# print(math.cos(10))
# print(math.log(10))
# print(math.log10(10))
# print(math.factorial(5))
# print(math.sinh(10))
# print(abs(-50.75))

# Python random Module
import random

print("Random Numbers : " , random.randrange(1,6))

day=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
print(random.choice(day))

print(day)
random.shuffle(day)
print(day)

# Print random element
#------------------------------

print(random.random())