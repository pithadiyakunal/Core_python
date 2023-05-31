# class parents():
#     def __init__(self,firstname,lastname,mobileno):
#         self.firstname=firstname
#         self.lastname=lastname
#         self.mobileno=mobileno

#     def showdata(self):
#         print("Firstname :",self.firstname)
#         print("Lastname :",self.lastname)
#         print("Mobile Number:",self.mobileno)
#         print("-------------------------------------")
# class student(parents):
#     def __init__(self, firstname, lastname, mobileno,stander):
#         super().__init__(firstname, lastname, mobileno)
#         self.stander=stander

#     def showdata(self):
#          super().showdata()
#          print("Stander :",self.stander)
#          print("-------------------------------------")
# p1=parents("Pithadiya","Kunal",2255446699)
# p2=parents("Pritesh","Gohel",1155998822)
# s1=student("Kamlesh","Dhamecha",2255446699,5)
# p1.showdata()
# s1.showdata()
# p2.showdata()

# class Employe:
#     def __init__(self,id,name,salary):
#         self.id=id
#         self.name=name
#         self.salary=salary
#         self.hra=0
#         self.da=0
#         self.pf=0
#         self.net=0
#     def SalarySleep(self):
#         self.hra=self.salary*0.50
#         self.da=self.salary*0.17
#         self.pf=self.salary*0.10
#         self.net=self.salary+self.hra+self.da-self.pf

#         print("\nEnter the Manager Detail-----")
#         print("Enter the ID No:",self.id)
#         print("Enter the Name:",self.name)
#         print("Enter the Salary",self.salary)
#         print("HRA",self.hra)
#         print("DA",self.da)
#         print("PF declare",self.pf)
#         print("Net Salary",self.net)



# Emp1=Employe(1,"Kamlesh",25000)
# Emp1.SalarySleep()

# Emp2=Employe(2,"Jaimin",20000)
# Emp2.SalarySleep()

# class dog:                                  # class attributes are shared by all instances of the class.
#         def __init__(self,name,color):
#             self.name=name
#             self.color=color
#         def bark(self):
#             print("woof!")
# fido=dog("fido","brown")
# print(fido.name)
# fido.bark()

# class student:
#         def __init__(self,name):
#             self.name=name
#         def sayhi(self):
#             print("hi from"+self.name)
# s1=student(" amy")
# s1.sayhi()

class A():              
        def sum(self,a,b):     
            c=a+b               
            return c           
class B():
        def sub(self,a,b):
            c=a-b
            return c
class C(A,B):
        pass
c_obj=C()
print("Sum is ",c_obj.sum(12,4))
print("After subtraction ",c_obj.sub(45,5))

