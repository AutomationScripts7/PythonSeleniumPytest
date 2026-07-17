
#Acquiring properties of parent class

from Python.Oops.Constructor import Cars

class inheritance(Cars):

    num = 100

    def __init__(self):
        Cars.__init__(self, 7, 10)       # calls parent's __init__
        print("This is constructor of child class")

    def get_fromChild(self):
        return self.num + self.model

    def super_keyword(self):
        super().Summation()         #super keyword for calling function directly from another file
        print("sup")


obj = inheritance()

print(obj.get_fromChild())
obj.super_keyword()

#Types

#Single inheritance         - A > B
#Multiple inheritance       - A + B > C
#Multilevel inheritance     - A > B > C
#Hierarchical inheritance   - A > B + C
#Hybrid inheritance         - A > B + C > D


#When you define __init__ in the child class, it overrides the parent's __init__.
# So the parent's constructor never runs — that's why you only see the child's behavior.

# If you want both parent and child constructors to run, use super()
#class inheritance(Cars):

    #def __init__(self):
        #super().__init__(7, 10)        # calls parent's __init__
        #print("This is constructor of child class")



