#object = bundle of related attributes:
#   e.g book will have title, pages, rating, price,genre
#class = (blueprint) used to design the structure and layoit of object
#   e.g open book, read book, close book

class Car:
    def __init___(self,model,year,colour,for_sale):
        self.model = model
        self.year = year
        self.colour = colour
        self.for_sale = for_sale

car1 = Car("Dodge Hellcat", 2024, "Camo", False)
print(car1.model())