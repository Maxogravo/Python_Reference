#allows class to inherit attributes and methods from another class

class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Cat(Animal):
    pass #inherits from animal

kitten = Cat("Mittens")

print(kitten.name)
kitten.sleep()

