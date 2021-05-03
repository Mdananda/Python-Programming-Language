print()
#Start Program

class Aanada:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printName(self):
        print(self.name, self.age)

class Student(Aanada):
    def __init__(self, name, age):
        Aanada.__init__(self, name,age)

p = Student("Ananda", 20)
p.printName()
