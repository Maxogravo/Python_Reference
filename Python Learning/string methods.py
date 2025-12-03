name = input("Enter your name: ")

result = len(name) #Shows us how long the string is
print(result)

result2 = name.find("G") #Returns the first instance of any given character

print(result2)

result3 = name.capitalize() #Capitalises first word

print(result3)

result4 = name.upper() #Capitalises full word

print(result4)

result5 = name.lower() # All lowercase

print(result5)

result6 = name.isdigit() # Is this a string of numbers?

print(result6)

result7 = name.isalpha() #Contains only alphabetical characters

print(result7)

phonenumber = input("Enter number: +44")

result8 = phonenumber.count("-") #Counts how many of a specified charcater

print(result8)

result9 = phonenumber.replace("-", " ") # Replaces specified characters with other ones

print(result9)

print(help(str)) #Prints all possible commands