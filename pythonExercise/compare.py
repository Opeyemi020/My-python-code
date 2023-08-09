class Compare:

    def __init__(self, num1, num2):
        self.b = None
        self.a = None
        self.num1 = num1
        self.num2 = num2

    def __str__(self):
        return f"{self.a}{self.b}"

    def __eq__(self, other):
        return self.num1 == other.num1 and self.num2 == other.num2

    def __gt__(self, other):
        return self.a > other.a and self.b > other.b

# p1 = Point(3, 3)
# p2 = Point(1, 2)
# print(p1 < p2)
