def net_price(ls, ds=0, tx=0.05): #Allows to fill in a default value
    return ls * (1 - ds) * (1+tx)

print(net_price(500)) # Only have to input once
print(net_price(500, 0.1)) #Can override the default arg if you want