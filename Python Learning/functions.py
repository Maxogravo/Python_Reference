#Function = a block of re-usable code

#functions have to be defined 
def happy_birthday():
    print("Happy Birthday")

happy_birthday()

def namess(name): #Can create temp vars 
    print(f"Hi {name}")

namess("Max") #add temp vars

def invoice(usr, amnt, due):
    print(f"{usr}, your owe £{amnt} by {due}.")

invoice("Max G", "1500.53", "2026")

def add(x, y):
    z = x + y
    print (z)

add(2, 4)