#a collection of {key:values}

capitals = {"USA": "Washington D.C",
            "India":"New Delhi",
            "China":"Beijing",
            "Russia":"Moscow"}
print(capitals.get("USA"))

capitals.update({"Germany":"Berlin"}) #Adds new values
capitals.update({"USA":"Detroit"}) #Updates current value
capitals.popitem() #removes latest value inserted
capitals.clear() #clears the list
print(capitals.keys())#Prints the keys, in this case countries
print(capitals.values())#Prints values, in this case capital cities