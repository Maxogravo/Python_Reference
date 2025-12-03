
class Student:

    class_year = 2024
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Max", str(13))
student2 = Student("Finn", 14)

print(student1.name + "; " + student1.age)
