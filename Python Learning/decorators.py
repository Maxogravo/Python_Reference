#Adding something to a base function

def add_sprinkles(func):
    def wrapper():
        print("You add sprinkles")
        func()
    return wrapper

@add_sprinkles
def get_icecream():
    print("Here's your ice cream")

get_icecream()