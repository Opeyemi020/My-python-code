

class Person:
    def greet(self):
        print("Person greeting")


class Admin(Employee, Person):
    pass




admin1 = Admin()