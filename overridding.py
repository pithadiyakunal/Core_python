# class employe:
#     def show(self):
#         print("Welcome to my sites")
# class manager(employe):
#     def show(self):
#         print("Welome our My Web Page")
# obj=manager()
# obj.show()

class A:
    def result(self,a,b):
        print("Addition is:",a+b)

class B(A):
    def result(self,a,b):
        super().result(20,20)
        print("Divided:",a/b)
obj=B()
obj.result(50,5)




