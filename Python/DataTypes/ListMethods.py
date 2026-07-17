#Lis[]  >>>  Methods - Mutable – can be changed after creation (update, remove possible)


#insert

var = ["hi", "python"]
var.insert(0, "HELLO")
print(var)

#Update / replace values

variable = ["hi", "python"]
variable[0] = "WORLD"
print(variable)

#append - add value in last

text = [1, 2, 7, "Python"]
text.append("world")
print(text)

#Delete - from index

char = [1, 2, 7, "Python"]

del char[1]
print("Delete is: ", char)

#pop
char = [1, 2, 7, "Python"]

char.pop()      #Delete last value
print(char)

char.pop(1)     #Delete by index
print("pop is: ", char)

#remove
TEXT = [1, 2, 7, "Python"]

TEXT.remove("Python")   #Remove value
print(TEXT)

#sort / ascending
TEXT = [1, 7, 2, "Python"]

TEXT.sort()
TEXT.sort(key=str) # if collection all datatypes like int,string. (This uses key=str so all elements are compared as strings during sorting)

#sort / descending
TEXT = [1, 7, 2, 4]

TEXT.sort(reverse=True)
print(TEXT)





