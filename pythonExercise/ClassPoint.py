def draw():
    print("drawing...")


class point:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def draw(self):
        return f"drawing.... from point {self.a} to {self.b})"

    def __str__(self):
        return f"({self.a}, {self.b})"

    @classmethod
    def point_from_one(cls):
        return cls(1, 1)


p1 = point(2, 3)
p2 = point(1, 1)
print(p1.point_from_one())
