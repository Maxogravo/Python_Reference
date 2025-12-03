#lists, sets and tuples
#List = [] ordered and changable. Duplicates OK
#Sets = {} unordered and immutable
#Tuples = () ordered and unchangable

fruits = ["apple", "orange", "banana", "pear", "mango", "coconut"]
print(fruits)
print(fruits[0]) #Only prints the first entry
print(fruits[0:3]) #Prints entries 0, 4
print(fruits[::2]) #Prints every second entry

for fruits in fruits:
    print(fruits, end="  ")

print("apple" in fruits)

fruits[0] = "pineapple" #chnage value
fruits.remove("pineapple") #removes item from list