# for i in range(1,6):
#     print(i)

# num=int(input("Enter the number :"))
# for i in range(11):
#     print(str(num) + "X" + str(i) + "=" + str(i*num))

# name=["Kunal","Ravi","darshil","pritesh","jaimin"]
# for i in name:
#     if i.startswith("K"):

# Factorial----------

# num=0
# factorial=0
# for i in range(num):
#     factorail=factorial * (i+1)
# print(factorial)

# product=["Mouse","Speaker","Key Board","LED","HDD"]
# found=False

# for item in product:
#     if(item=="LED"):
#         found=True


# if found:
#     print("\nProduct Found")
# else:
#     print("\nSorry ! Product Not Found....")

 
product=["Mouse","Speaker","Key Board","LED","HDD"]

for item in product:
    if item=="Key Board":
        print("\nProduct Found")    
        break
else:
    print("\nSorry ! Product Not Found....")