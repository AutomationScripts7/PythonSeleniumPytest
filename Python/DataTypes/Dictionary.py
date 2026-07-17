
#dictionary - {key:value}

dict = {
    "name": "python",
    "version": 3.1
}

print(dict)

#-----------------------------------------------


#adding key  & value pairs in empty dictionary

dict = {}

dict["Starname"] = "OpenAI"     #same as update values like list (refer list concept if any doubt)
dict["Endname"] = "ChatGPT"
dict[7]= "opensource"
print(dict)

#-----------------------------------------------


#get
var = {1: "Open", 2:"AI"}
print(var.get(1))   # print value of key


#-----------------------------------------------


#keys
char = {1: "Open", 2:"AI"}
print(char.keys())    #print all keys present in dict


#-----------------------------------------------

#values
print(char.values()) #print all values present in dict


#-----------------------------------------------

#items
print(char.items()) #print all items present in dict

#-----------------------------------------------

#update new key & value pair
char.update({3:"GPT"})   #add new key value pair
print(char)

#-----------------------------------------------

#updating existing key & value pair
char.update({2:"CHATGPT"})   #updating existing key value pair
print(char)

#-----------------------------------------------

#pop - deleting existing pair
text = {1: "Open", 2:"AI"}

text.pop(1)
print(text)

#-----------------------------------------------


#clear
print(text.clear())  #clear all elements in dict


#-----------------------------------------------


#dict - access value using key but not possible to access value directly using key. we can achieve through for loop

dict = {
    "name": "python",
    "version": 3.1
}

print(dict)

print(dict["version"])

#accessing values
print(dict["python"])    #access through key not by index and also not possible


#-----------------------------------------------


#key - accessing value using key

for key, value in dict.items():
    if value == "python":
        print(key)


##############