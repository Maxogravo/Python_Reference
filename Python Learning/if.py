age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old")
elif age >= 18:
    print("You are eligible!")
elif age < 0:
    print("You haven't even been born yet")
else:
    print("You must be 18+")