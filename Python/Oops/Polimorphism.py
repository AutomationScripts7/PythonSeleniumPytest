
#same method name but different behavior

class BMW:
    def M5(self):
        print("My M5 model of BMW")

class porche:
    def M5(self):
        print("My M5 model of porche")


obj1 = BMW()
obj2 = porche()

obj1.M5()
obj2.M5()


#Method Overriding - run time polymorphism

#using inheritance and change the parent method in child class

class parent:
    def porche(self):
        pass

class child(parent):
    def porche(self):
        print("Child model of parent")  #here inherited and changed method of porche in parent

obj = child()
obj.porche()

#Method overloading - compile time polymorphism

#we can achieve via *args

class demo:
    def sum(self, a, b, c, *args):
        return a + b + c + sum(args)    #intead of adding one by one sum(args)
                                        # #multiple argument accepted without any error

obj = demo()
print(obj.sum(10, 20, 30, 40, 50))















