#logical operator allow us to evaluate multiple conditions

temp = 25
is_raining = False


#use or to check for different features all at once. either one could set it off
if temp > 35 or temp < 0 or is_raining == True:
    print("The outdoor event is cancelled")
else:
    print("The event is still scheduled")

is_sunny = True

#And checks that both features are true before proceeding
if temp >= 28 and is_sunny:
    print("It's too hot!!!")
# and not checks if the first feature is true but the other is false.
elif temp <= 5 and not is_sunny:
    print("It's deceptive out there!")
else:
    print("It's fine")