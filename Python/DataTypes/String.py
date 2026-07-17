#string

#upper
variable = "Python World"
print(variable.upper())

#lower
variable = "Python World"
print(variable.lower())

#capitalize
variable = "Python World"
print(variable.capitalize())

#title
variable = "python World"
print(variable.title())

#strip(remove spaces at front and end)
variable = "  python  "
print(variable.strip())

#replace value in string
variable = "Good"
print(variable.replace("Good", "Morning"))

#split
text = "python basics string"
list_split = text.split()
print(list_split)   #split will be in list/Index only [python, basics, string]
print(list_split[1])    #acessing using index -- value is "basics"

#join - list into string with space >> syntax for better understanding : "separator".join(iterable)
variable = ["openAI", "KIRO"]
print(" ".join(variable))

#startswith and endswith - returns only true or false which means boolean only
variable = "playwright"
print(variable.startswith("p"))
print(variable.endswith("t"))

#find - use to find the position the element
variable = "playwright"
print(variable.find("i"))

#count - use to find number of elements
variable = "playwright"
print(variable.count("i"))

#slicing
variable = "playwright"
print(variable[0:3])
print(variable[-4:-1])
print(variable[-7:-1:2])


#Validating string2 values in string1 (Substring Validation)

string1 = "Hello Python"
string2  = "Python"

print(string2 in string1)


#NOTES:

#If you concatenate combination of int, float, string use format method:
#a, b, c = 5, 1.2, "Python"

# print("Integer: {}, Float: {}, String: {}".format(a, b, c))
#simply says >> {} {} .format(c)

#---------------------------------------------------------------------

#If both are string
#string = "HELLO"
#string2 = "PYTHON"
#print(string+string2)




