import random

low = 1
high = 100

options = ("rock","paper","scisscors")

print(random.randint(1,6)) #random integer 1 to 6
print(random.randint(low,high)) #random can also use vars as a range
print(random.random())
print(random.choice(options)) #can also put rsandom strings
