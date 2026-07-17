
#Constructor __init_ is one method which is automatically called/execute when object is created ( obj = Cars() )

#Self using for current object reference

#self keyword is mandotory for calling variable names into method

class Cars:

    model = 7       #Class variable >>> cause variable declared in class level, not in method

    #Default Contructor
    def __init__(self, name1, name2):
        self.firstname = name1      #Instance variable
        self.secondname = name2

        print("I WILL EXECUTE FIRST WHATEVER METHOD IS THERE, CAUSE AM A CONTRUCTOR")

    def Summation(self):
        return self.firstname + self.secondname + self.model



obj1 = Cars(7, 10)
print(obj1.Summation())

obj2 = Cars(100, 100)
print(obj2.Summation())






