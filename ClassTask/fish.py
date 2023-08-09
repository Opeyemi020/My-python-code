class Animal:

    def __init__(self):
        self.age = 1

    def eat(self):
        print("Eating...")

    def walk(self):
        print("Walking...")


class Fish(Animal):
    def swim(self):
        print("Swimming...")


class Mammal(Animal):
    def __int__(self):
        super().__init__()
        self.weight = 2

    #
    # def eat(self):
    #     print("Eating...")
    def swim(self):
        print("Swimming...")


m = Mammal
m.eat()
f = Fish()
print(m.age)
