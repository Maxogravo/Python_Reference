#while loop passes function when codition is matched

name = input("what is your name: ")
sigma = ""

while name == "":
    print("You did not enter your name!")
    name = input("what is your name: ")
print(f"Hi {name}!" ) 

food = input("Enter a food you like (q to quit): ")

while not food == "q": #Continues until a certain action has happened
    print(f"You like {food}")
    food = input("Don't be shy, tell me another. (q to quit): ")
print("AAHAHAHHAHAHHA")