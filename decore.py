def smartDivide(function):
    def innerFunction(x,y):
        print("I am going to Divide " , x , " and " , y)
        if(y==0):
            print("Sorry ! Cannot Divide by 0......")
            return
        else:
            return function(x,y)
    
    return innerFunction

@smartDivide
def divide(x, y):
    print(x/y)

divide(6,3)