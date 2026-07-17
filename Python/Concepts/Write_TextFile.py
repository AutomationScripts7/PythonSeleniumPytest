import os
#Open file with path
# text_File = open(os.path.join(os.path.dirname(__file__),"Text.txt"))


#Scenario - Read the file and reverse it back to file

#Another to open file, need not to add close action separately
file_path = os.path.join(os.path.dirname(__file__), "Text.txt")

with open(file_path, "r") as reader:    #reader is like object/variable name only
    content = reader.readlines()        #Read all lines in the file
with open(file_path, "w") as writer:
    for line in reversed(content):      #Content reversed in the file
        writer.write(line)              #Writing content back to file
        print(line, end="")



