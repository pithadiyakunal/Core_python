# class person:
#     name="Pithadiya Kunal"
#     study="Bachor of Computer Appplication"
#     collage="Khyati Foundation"

#     def sum(self):
#         a=10
#         b=30
#         c=a+b
#         print("Total is :",c)
# a=person()
# a.name="Pritesh Ghole"
# a.study="Bachor of Commerce"
# print(a.name)
# print(a.collage)
# print(a.study)
# a.sum()
# print(a)

# class car():
#     def __init__(self,name,modle,fule):
#         self.name = name
#         self.modle = modle
#         self.fule = fule

# honda=car("city honda",2015,"petrol")
# print("Car Name :",honda.name)
# print("Modle :",honda.modle)
# print("Fule :",honda.fule)
# print("------------------------------------")

# tata=car("nano",2019,"disel")
# print("Car Name :",tata.name)
# print("Modle :",tata.modle)
# print("Fule :",tata.fule)


# class Books:
# 	def __init__(self, id, name, rate):
# 		self.idno = id
# 		self.bookName = name
# 		self.price = rate
# 		self.quantity=0

# 	def printData(self):
# 		print("\nBook IdNo : " , self.idno)
# 		print("Book Name : " , self.bookName)
# 		print("Book Price : " , self.price)
# 		print("Book Quantity : " , self.quantity)
# 		print("=======================================")

# 	def buyQunatity(self, qty):
# 		self.quantity=qty
# 		amount = self.price * qty
# 		print("You Buy {0} Piece {1} Book and Payment Amount is {2}".format(qty,self.bookName,amount))

# 	def setDiscount(self, value):
# 		originalPrice=self.price

# 		self.price = self.price - (self.price * value /100)
# 		print("Original Price {0} and Discounted Price {1}".format(originalPrice, self.price))


# b1=Books(1001,"Photoshop",450)
# b1.printData()

# b2=Books(1002,"C++ Language",850)
# b2.printData()

# b1.buyQunatity(5)

# b2.setDiscount(25)
# b2.buyQunatity(10)
