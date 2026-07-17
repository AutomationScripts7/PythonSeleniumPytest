#For loop

for storing in range(5):
    print(storing)


for storing in range(1,7):
    print(storing)

#sum of natural numbers 1+2+3+4+5 = 15
summation = 0

for i in range(1,6):
    summation += i
    # summation = summation + i
print(summation)

#sum of numbers but with steps of 2

for j in range(1,6,2):
    print(j)


print("******************************************************")

#while loop - it will execute until condition will be false (which means if true it will go inside loop)

loop = 10

while loop >= 7:
    print("condition is true")
    loop -=1
    # loop = loop - 1   #if we don't mention this then it will go infinite loop

else:
    print("condition is false")

print("********************************************************")

loop = 7

while loop > 3:
    if loop !=4:
        loop -=1
        print(loop)

else:
    print("condition is false")

print("********************************************************")

#break to completely break the loop
#continue to skip the iteration
#pass for nothing, to add code later

loop = 15

while loop > 1:
    if loop == 4:
        break
    print(loop)
    loop -=1


else:
    print("condition is false")

print("********************************************************")

loop = 50

while loop > 7:
    if loop == 30:
        loop -= 1
        continue
    if loop == 25:
        break
    print(loop)
    loop -=1

    # loop = loop - 1   #if we don't mention this then it will go infinite loop
else:
    print("condition is false")





