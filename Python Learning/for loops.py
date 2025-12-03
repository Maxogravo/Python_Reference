#executes block of code certain number of times
from time import sleep


for x in range(1, 11): #executes 10 times
    #sleep(1)#counts every 1 second
    print(x)
print("Happy New Year!!!")

for y in range(1,11,2): # the last two at the end of the brackets means count every two
    print(y)

credit = "1234-5678"

for x in credit: #prints every char in credit individually
    print(x)

for x in range(1, 26):
    if x == 13:
        continue # Continues with the counting but doesn't print
    elif x >= 20:
        break # Stops cycle
    else:
        print(x)