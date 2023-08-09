class Human():
    def walking(self, name):
        print(f"{self.name} is waking")

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello {self.name}")

    def __str__(self):
        return f"{self.name}"


mine = Human("Mr Sultan")
mine2 = Human("Mr Sultan")
mine.greet()
mine2.greet()
print(mine.name)
mine.walking("Esther")
