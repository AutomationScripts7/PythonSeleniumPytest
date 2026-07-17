
import os
#Open file with path
text_File = open(os.path.join(os.path.dirname(__file__),"Text.txt"))

#To read all contents of file
print(text_File.read())

#To read n number of characters
print(text_File.read(7))

#Note: The file maintains a cursor position — after read(7), the cursor is at position 7, so the next read() picks up from there

#To read line by line using readline method
print(text_File.readline())
print(text_File.readline())

#-----------------------------------------------------

#Read all lines using readline method with while loop
line = text_File.readline()

while line != "":
    print(line)
    line = text_File.readline()

#-----------------------------------------------------

#Readlines -- Reads all lines and return list   [a, b, c]
listoflines = (text_File.readlines())
print(listoflines[5])

#Print line by line using for loop
for line in listoflines:
    print(line)


text_File.close()

