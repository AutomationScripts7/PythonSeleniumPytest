#Function is a group of statement to perform specific task

def Greetings():
    print("Good Morning")

Greetings()

#-----------------------------------------------

#parameterize function

def greet(params):      #parameterization here
    print("Hi" + params)

greet("Rahul Shetty")

#-----------------------------------------------

#paramterize with intergers

def integer(a,b,c):     #parameterization here
    print(a + b / c)

integer(2,3,4)

#-----------------------------------------------

#return type function

def int(a,b):
    return a + b

print(int(2,3))

#-----------------------------------------------

#Default params

def int(a = 7):
    print(a)

int()           #here defaultly params takes because edhume kudukla params la
int(10)         #here we are giving params so taking that value

#-----------------------------------------------


#*args   - Positional Arguments , we can give multiple values if we give *args
def char(*args):
    print(args)

char(1,2,3)      #multiple argument accepted without any error

#-----------------------------------------------


#**kwargs -  Keyword Arguments
def var(**kwargs):
    print(kwargs)

var(one="open", two="AI", three="chatGPT")  #if you use **kwargs, multiple key, values pairs kuduklam. output dictionary la kudukum

#-----------------------------------------------


#lamda       -      lamba num: num * num
def lamda(a, b):
 print(a + b)

lamda(5, 5)

#-----------------------------------------------

#if we write in lamba function - to write code in one line

add = lambda num1, num2: num1 * num2
print(add(7, 7))

#-----------------------------------------------


##example for lambda for better understanding

square = lambda a, b : a / b
print(square(7, 7))








