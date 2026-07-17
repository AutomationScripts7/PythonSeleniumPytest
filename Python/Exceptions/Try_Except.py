

try:
    with open('filelog.txt','r') as reader:
        reader.read()

except Exception as e:      # Without as e, you know something failed but not what. With as e, you get the exact reason — making debugging easy
    print(e)

finally:
    print("Cleaning up resources")


